from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from authentication.forms import LoginForm, Signup
from twitteruser.models import MyUser

# Create your views here.
def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'genericform.html', {'form': form})

@login_required()
def logged_outview(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))


def signup_view(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            create_user = MyUser.objects.create_user(
                username=data['username'],
                password=data['password'],

            )

            create_user.save()
        return HttpResponseRedirect(reverse('login'))

    form = Signup()
    return render(request, 'signup.html', {'form': form})

