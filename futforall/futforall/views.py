"""
This module contains functions for rendering the home page and getting the count of unread notifications.

index::
    The index function renders the home page and passes a context dictionary containing the list of Match objects
    and the count of unread notifications.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object containing the rendered index.html template with the context dictionary.
    :rtype: HttpResponse

count_unread_notifications::
    This function returns the count of unread notifications for the authenticated user.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The count of unread notifications.
    :rtype: int
"""

from django.shortcuts import render
from match.views import Match
from notifc.models import Notification

def index(request):
    """
    View for rendering the home page.

    **Context**

    ``match_list``
        List of all matches in the database, ordered by the created date.

    ``unread_notifications_count``
        The count of unread notifications for the current user.

    **Template**

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object containing the rendered index.html template with the context dictionary.
    :rtype: HttpResponse
    """
    match_list = Match.objects.all().order_by('-created_date')
    unread_notifications_count = count_unread_notifications(request)
    context = {
        'match_list': match_list,
        'unread_notifications_count': unread_notifications_count,
    }
    return render(request, 'index.html', context=context)

def count_unread_notifications(request):
    """
    Returns the count of unread notifications for the authenticated user.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The count of unread notifications.
    :rtype: int
    """
    if request.user.is_authenticated:
        count = Notification.objects.filter(user=request.user, read=False).count()
        return count
    else:
        return 0
