from django.db import models
from django.utils.timezone import now
from twitteruser.models import MyUser


class Tweet(models.Model):
    body = models.CharField(max_length=140)
    time = models.DateTimeField(default=now)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

