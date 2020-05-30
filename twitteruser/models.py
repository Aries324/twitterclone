from django.db import models
from django.contrib.auth.models import AbstractUser

"""
Will need to be a custom user
display name
following
"""

# Create your models here.
class MyUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True, blank=True)
    # https: // stackoverflow.com / questions / 16613013 / model - self - dependency - one - to - many - field - implementation / 16614136  # 16614136
    following = models.ManyToManyField("self", symmetrical=False)



