from django.urls import path
from twitteruser import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('follow/<int:id>/', views.follow_view, name='homepage'),
    path('unfollow/<int:id>/', views.unfollow_view, name='homepage'),
]
