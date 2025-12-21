import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import ChatSession, ChatMessage
from .utils import call_llm  # utility to call external model

@login_required
@ensure_csrf_cookie
def chat_page(request):
    # Ensure there's at least one session for the user
    session, _ = ChatSession.objects.get_or_create(user=request.user, title='Default')
    context = {'session_id': session.id}
    return render(request, 'chatapp/chat.html', context)


@login_required
@require_POST
def start_session(request):
    """
    Start a new chat session (POST optional title).
    """
    data = json.loads(request.body.decode() or "{}")
    title = data.get('title', '')
    session = ChatSession.objects.create(user=request.user, title=title)
    return JsonResponse({'session_id': session.id, 'title': session.title})


@login_required
@require_POST
def send_message(request):
    """
    Receive a user message (JSON: {session_id, message}) and return assistant reply.
    This saves both user and assistant messages into DB.
    """
    try:
        payload = json.loads(request.body.decode())
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")

    session_id = payload.get('session_id')
    message_text = payload.get('message')

    if not session_id or message_text is None:
        return HttpResponseBadRequest("Missing session_id or message")

    session = get_object_or_404(ChatSession, id=session_id)

    if session.user != request.user:
        return HttpResponseForbidden("Not your session")

    # Save user message
    user_msg = ChatMessage.objects.create(session=session, role='user', content=message_text)

    # Build conversation history to send to LLM (basic strategy)
    history_qs = session.messages.all()
    # Convert to model-expected format (list of dicts)
    conversation = []
    for m in history_qs:
        conversation.append({'role': m.role, 'content': m.content})

    # Call LLM (this function should handle provider details + errors)
    try:
        assistant_text = call_llm(conversation, user=request.user)
    except Exception as e:
        # Log in production; return an error to frontend
        return JsonResponse({'error': 'llm_call_failed', 'detail': str(e)}, status=500)

    # Save assistant message
    assistant_msg = ChatMessage.objects.create(session=session, role='assistant', content=assistant_text)

    return JsonResponse({
        'assistant': assistant_text,
        'user_message_id': user_msg.id,
        'assistant_message_id': assistant_msg.id,
    })


@login_required
def get_history(request):
    """
    Return JSON history for a session. GET params: ?session_id=<id>&limit=...
    """
    session_id = request.GET.get('session_id')
    if not session_id:
        return HttpResponseBadRequest("Missing session_id")

    session = get_object_or_404(ChatSession, id=session_id)

    if session.user != request.user:
        return HttpResponseForbidden("Not your session")

    limit = request.GET.get('limit')
    qs = session.messages.all()
    if limit:
        try:
            limit = int(limit)
            qs = qs[:limit]
        except ValueError:
            pass

    messages = [{'role': m.role, 'content': m.content, 'created_at': m.created_at.isoformat()} for m in qs]
    return JsonResponse({'messages': messages})


@login_required
@require_POST
def new_chat(request):
    """
    Create a new ChatSession and return its ID
    """
    session = ChatSession.objects.create(user=request.user, title="")
    return JsonResponse({'session_id': session.id})


@login_required
def list_sessions(request):
    """
    Return all sessions for current user
    """
    sessions = ChatSession.objects.filter(user=request.user).order_by('-updated_at')
    data = [
        {'id': s.id, 'title': s.title or 'Untitled', 'created_at': s.created_at.isoformat()}
        for s in sessions
    ]
    return JsonResponse({'sessions': data})
