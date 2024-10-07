from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='')
    created_date = models.DateTimeField()
    match_date = models.DateField()
    match_time = models.TimeField(default='00:00')
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    participants = models.ManyToManyField(User, related_name='matches_participating')

    def __str__(self) -> str:
        return self.title
