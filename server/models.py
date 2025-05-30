from django.db import models
import uuid

class User(models.Model):
    user_id=models.CharField(max_length=500, primary_key=True)
    user_name=models.CharField(max_length=150)

    def __str__(self):
        return self.user_name
    
class Chat(models.Model):
    chat_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    chat_name = models.CharField(max_length=225, blank=True, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='chats')

    def __str__(self):
        return self.chat_name or f"Chat {self.chat_id}"


class Message(models.Model):
    message_id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False, unique=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    user_query = models.TextField()
    ai_response = models.TextField()
    file = models.URLField(blank=True, null=True)   

    def __str__(self):
        return f"Message {self.message_id} in Chat {self.chat.chat_id}"