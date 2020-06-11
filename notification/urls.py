from django.urls import path
from notification import views

urlpatterns = [
    path('notifications/<int:id>/', views.notifications),
    path('altnotificationsview/<int:id>/', views.NotificationsView.as_view()),



]