from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from .models import User

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

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)