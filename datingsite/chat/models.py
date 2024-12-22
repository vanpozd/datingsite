from django.db import models
from authentication.models import CustomUser
from django.utils.timezone import now

class Chat(models.Model):
    """
    Represents a chat session between two users.
    """
    user1 = models.ForeignKey(CustomUser, related_name='chats_as_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(CustomUser, related_name='chats_as_user2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Chat between {self.user1.username} and {self.user2.username}"

    class Meta:
        unique_together = ('user1', 'user2')

class Message(models.Model):
    """
    Represents a message in a chat session.
    """
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)