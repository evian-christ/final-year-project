from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.contrib import messages
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.urls import reverse

from .models import Match
from .forms import MatchForm
from notifc.models import Notification

def index(request):
    return HttpResponse("hey")

def detail(request, match_id):
    try:
        match = Match.objects.get(pk=match_id)
    except Match.DoesNotExist:
        raise Http404("Match Does Not Exist!")
    return render(request, 'match/detail.html', {'match': match})

def create(request):
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            match = form.save(commit=False)
            match.created_date = timezone.now()
            match.holder = request.user
            match.save()
            match.participants.add(request.user)
            return redirect('match:detail', match_id=match.id)
    else:
        form = MatchForm()
    return render(request, 'match/create.html', {'form':form})

def join(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    if request.user in match.participants.all():
        messages.warning(request, "You're already a participant in this match!")
        return redirect('match:detail', match_id=match_id)
    else:
        match.participants.add(request.user)
        channel_layer = get_channel_layer()
        message = {
            'type': 'match_join',
            'message': '<a href="' + reverse("account:profile", args=[request.user.username]) + '">' + request.user.username + '</a> has joined the match <a href="' + reverse("match:detail", args=[match.id]) + '">' + match.title + '</a>',
            'match_id': match.id,
            'user_id': match.holder.id,
            'timestamp': timezone.now().isoformat(),
        }
        try:
            async_to_sync(channel_layer.group_send)('notifications', message)
            temp = Notification.objects.create(
                message=message['message'],
                user_id=message['user_id'],
                timestamp=message['timestamp'],
            )
            messages.success(request, "You've successfully joined the match!")
        except Exception as e:
            messages.error(request, "Failed to send notification message. Please try again later.")
            match.participants.remove(request.user)
            return redirect('match:detail', match_id=match_id)
    return redirect('match:detail', match_id=match_id)

def leave(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    if not request.user in match.participants.all():
        messages.warning(request, "You're not a participant in this match!")
        return redirect('match:detail', match_id=match_id)
    else:
        match.participants.remove(request.user)
        channel_layer = get_channel_layer()
        message = {
            'type': 'match_leave',
            'message': '<a href="' + reverse("account:profile", args=[request.user.username]) + '">' + request.user.username + '</a> has left the match <a href="' + reverse("match:detail", args=[match.id]) + '">' + match.title + '</a>',
            'match_id': match.id,
            'user_id': match.holder.id,
            'timestamp': timezone.now().isoformat(),
        }
        try:
            async_to_sync(channel_layer.group_send)('notifications', message)
            temp = Notification.objects.create(
                message=message['message'],
                user_id=message['user_id'],
                timestamp=message['timestamp'],
            )
            messages.success(request, "You've successfully left the match.")
        except Exception as e:
            messages.error(request, "Failed to send notification message. Please try again later.")
            match.participants.add(request.user)
            return redirect('match:detail', match_id=match_id)
    return redirect('match:detail', match_id=match_id)