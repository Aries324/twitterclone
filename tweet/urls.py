from django.urls import path
from tweet import views

urlpatterns = [
    path('tweetadd/', views.tweetadd),
    path('tweetdetail/<int:pk>/', views.tweet_detail)
]