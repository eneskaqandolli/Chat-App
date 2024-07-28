from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import ChatRoom, ChatMessage
from django.contrib.auth.decorators import login_required
from users.models import Profile


# Create your views here.

def index(request):
    rooms = ChatRoom.objects.all()
    return render(request, "chatapp/index.html", {"rooms": rooms})

@login_required
def chatroom(request, slug):
    profile = Profile.objects.all()
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)

    if request.method == "POST":
        message_content = request.POST.get('message')
        if message_content:
            ChatMessage.objects.create(user=request.user, room=chatroom, message_content=message_content)
            return redirect(reverse('chatapp:chatroom', args=[slug]))

    return render(request, 'chatapp/chatroom.html', {'chatroom': chatroom, 'messages': messages, "profile": profile})

@login_required
def delete_message(request, id):
    message = get_object_or_404(ChatMessage, id=id)
    chatroom_slug = message.room.slug
    message.delete()
    return redirect(reverse('chatapp:chatroom', args=[chatroom_slug]))
