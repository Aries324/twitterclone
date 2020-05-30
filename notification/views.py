from django.shortcuts import render
from notification.models import Notification
from twitteruser.models import MyUser

# Create your views here.
"""
class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    recipent = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
"""



def notifications(request):
    html = 'notification.html'
    current_user = MyUser.objects.filter(id=id)
    data = Notification.objects.filter(current_user=current_user)
    for notification in data:
        notification.delete()
    return render(request, html, {'data': data})

