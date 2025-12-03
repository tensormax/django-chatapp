from django.conf import settings
from django.db import models

from django.db import models
from django.contrib.auth.models import User

class ChatSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # optional: sort by last activity

    def save(self, *args, **kwargs):
        # Optional: automatically set title from first_message attribute
        if not self.title and hasattr(self, 'first_message'):
            self.title = self.first_message[:50]  # first 50 chars
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or f"Session {self.id}"


class ChatMessage(models.Model):
    """
    Messages stored for the session. role: 'user' or 'assistant' or 'system'
    """
    ROLE_CHOICES = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
        ('system', 'System'),
    ]

    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f"[{self.role}] {self.content[:60]}"
