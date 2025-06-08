from django.urls import path
from . import views

urlpatterns = [
    path("api/users/", views.create_user),
    path("api/chat/", views.create_chat),
    path("api/get_users", views.get_users),
    path("api/messages/<chat_id>", views.chat_messages)
]