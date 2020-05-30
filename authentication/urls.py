from django.urls import path
from authentication import views


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logged_out/', views.logged_outview, name='logged_out'),



]
