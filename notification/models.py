from django.db import models
from tweet.models import Tweet
from twitteruser.models import MyUser

# Create your models here.

class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    recipent = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

