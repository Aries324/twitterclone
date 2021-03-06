from django.shortcuts import render, reverse, HttpResponseRedirect,get_object_or_404
from tweet.models import Tweet
from tweet.forms import TweetAddForm
from notification.models import Notification
from twitteruser.models import MyUser
import re




def tweetadd(request):
    html = 'genericform.html'

    if request.method == "POST":
        form = TweetAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            make_tweet = Tweet.objects.create(
                body=data['body'],
                # time=data['time'],
                author=request.user

            )
            find_users = re.findall(r'@(\w+)', data['body'])
            if '@' in data['body']:
                for users in find_users:
                        Notification.objects.create(
                            current_user=MyUser.objects.get(username=users),
                            tweet=Tweet.object.filter(body=make_tweet).first()
                        )

            return HttpResponseRedirect(reverse('homepage'))

    form = TweetAddForm()

    return render(request, html, {'form': form})


def tweet_detail(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    return render(request, 'tweet_detail.html', {'tweet': tweet})
