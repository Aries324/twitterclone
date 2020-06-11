from django.urls import path
from tweet import views

urlpatterns = [
    path('tweetadd/', views.tweetadd),
    path('alttweetadd/', views.TweetAddFormView.as_view()),
    path('tweetdetail/<int:pk>/', views.tweet_detail),
    path('alttweetdetail/<int:pk>/', views.TweetDetail.as_view())
]