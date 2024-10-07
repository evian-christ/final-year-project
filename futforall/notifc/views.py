from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def index(request):
    # Update all the notifications to be unread
    Notification.objects.filter(user=request.user, read=0).update(read=1)

    notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'notifc/index.html', {'notifications': notifications})