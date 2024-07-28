from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm
from .models import Profile

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
        form = RegisterForm()    
    return render(request, "users/register.html", {"form":form})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    
    def get_success_url(self):
        return reverse_lazy('chatapp:index')
    
@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('chatapp:index')  # or any other page you want to redirect to
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'users/profile.html', {'form': form, "profile": profile})
