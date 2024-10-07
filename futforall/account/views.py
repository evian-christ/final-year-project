from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import Http404

from account.forms import UserForm
from .models import Friend


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})

def profile(request, username):
    try:
        u = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404("User Does Not Exist!")
    return render(request, 'account/profile.html', {'usr': u})

def add_friend(request, friend_id):
    current_user = request.user
    friend = User.objects.get(id=friend_id)
    Friend.objects.create(current_user=current_user, friend=friend)
    return redirect('account:profile', username=friend.username)