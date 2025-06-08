from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, ChatSerializer, UserWithChatsSerializer, MessageSerializer
from rest_framework import status
from .models import User, Chat

@api_view(["POST"])
def create_user(request):

    user_id = request.data.get('user_id')

    if User.objects.filter(user_id = user_id).exists():
        return Response({"message" : "User already exists"}, status=status.HTTP_200_OK)

    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_chat(request):
    serializer = ChatSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def chat_messages(request, chat_id): 
    user_id = request.GET.get("user_id") or request.data.get("user_id")

    try:
        chat = Chat.objects.get(chat_id=chat_id, user__user_id=user_id)
    except Chat.DoesNotExist:
        return Response({"error": "Invalid chat_id or unauthorized."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        messages = chat.messages.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(chat=chat)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_users(request):
    users = User.objects.prefetch_related('chats')
    serializer = UserWithChatsSerializer(users, many=True)
    return Response(serializer.data)