from django.urls import path
from . import views

app_name = 'chatapp'

urlpatterns = [
    path('', views.chat_page, name='chat_page'),
    path('api/send/', views.send_message, name='send_message'),
    path('api/history/', views.get_history, name='get_history'),
    path('api/start-session/', views.start_session, name='start_session'),
    path('new/', views.new_chat, name='new_chat'),           # new chat
    path('sessions/', views.list_sessions, name='list_sessions'),  # sidebar
]
