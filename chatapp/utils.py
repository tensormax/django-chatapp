import requests
from django.conf import settings

def call_llm(conversation, user=None):
    api_key = settings.OPENROUTER_API_KEY

    if not api_key:
        raise Exception("OPENROUTER_API_KEY missing in .env or environment.")

    url = "https://openrouter.ai/api/v1/chat/completions"

    payload = {
        "model": "amazon/nova-2-lite-v1:free",
        "messages": conversation,
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"OpenRouter API Error: {response.text}")

    data = response.json()
    return data["choices"][0]["message"]["content"].strip()
