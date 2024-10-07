from django.contrib.auth.models import User
from django.db import models

class Friend(models.Model):
    current_user = models.ForeignKey(User, related_name='friends_initiated', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friends_received', on_delete=models.CASCADE)

    def __str__(self):
        return self.friend.username
