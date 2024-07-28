from django.urls import path
from . import views

app_name = "chatapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>", views.chatroom, name="chatroom"),
    path("delete/<int:id>", views.delete_message, name="delete"),
    
]