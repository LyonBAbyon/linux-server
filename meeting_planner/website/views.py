from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from meetings.models import Meeting

@login_required
def index(request):
    meetings = Meeting.objects.filter(user=request.user).order_by('date', 'start_time')
    return render(request, "website/index.html", {"meetings": meetings})

def about(request):
    return HttpResponse("My names is Eevert I'm from Finalnd")

def profile(request):
    return render(request, "website/profile.html", {"user": request.user, "now": datetime.now()})

def meetings(request):
    meetings = Meeting.objects.filter(user=request.user).order_by('date', 'start_time')
    return render(request, "website/meetings.html", {"meetings": meetings})

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('email','username', 'first_name', 'last_name',)

@login_required
def change_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'website/change_profile.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def contact(request):
    return render(request, "website/contact.html")