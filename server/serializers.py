from rest_framework import serializers
from . import models


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chat
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class UserWithChatsSerializer(serializers.ModelSerializer):
    chats = ChatSerializer(many=True, read_only=True)

    class Meta:
        model = models.User
        fields = ['user_id', 'user_name','chats']