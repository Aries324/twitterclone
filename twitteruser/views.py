from django.shortcuts import render, reverse, HttpResponseRedirect
from twitterclone import settings
from twitteruser.models import MyUser
from tweet.models import Tweet


# Create your views here.
def index(request):
    auth_value = settings.AUTH_USER_MODEL
    return render(request, 'index.html', {'auth_value': auth_value})


def follow_view(request, id):
    current_user = request.user
    follow_user = MyUser.objects.get(id=id)
    current_user.following.add(follow_user)
    current_user.save()
    return HttpResponseRedirect(reverse('homepage'))


def unfollow_view(request, id):
    current_user = request.user
    follow_user = MyUser.objects.get(id=id)
    current_user.following.remove(follow_user)
    current_user.save()
    return HttpResponseRedirect(reverse('homepage'))


def profile_view (request, id):
    html = 'twitteruser/userprofile.html'
    current_user = MyUser.objects.filter(id=id).first()
    tweets = Tweet.objects.filter(user=current_user).order_by('-time')
    return render(request, 'twitteruser/profile.html', {
        'tweets': tweets, 'current_user': current_user})




