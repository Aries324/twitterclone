from django.urls import path
from twitteruser import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('althomepageview/', views.HomepageView.as_view(), name='homepage'),
    path('follow/<int:id>/', views.follow_view, name='homepage'),
    path('altfollowview/<int:id>/', views.FollowView.as_view(), name='homepage'),
    path('unfollow/<int:id>/', views.unfollow_view, name='homepage'),
    path('altunfollowview/<int:id>/', views.UnfollowView.as_view(), name='homepage'),
    path('profileview/<int:id>/', views.profile_view),
    path('altprofileview/<int:id>/', views.ProfileView.as_view())

]
