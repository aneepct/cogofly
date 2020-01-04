from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _

from .forms import LoginForm, RegisterForm

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    else:
        context = {'login_form': LoginForm(), 'register_form': RegisterForm()}
        return render(request, 'landing.html', context)


def social_api_callback(request):
    # return JsonResponse(request.user.email, safe=False)
    return HttpResponseRedirect('/')


def login_view(request):
    context = {'login_form': LoginForm()}
    return render(request, 'login.html', context)


def register_view(request):
    context = {'register_form': RegisterForm()}
    return render(request, 'register.html', context)


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    else:
        # Create a form instance with the submitted data
        form = LoginForm(request.POST)  # 2
        # Validate the form
        if form.is_valid():  # 3
            email = request.POST['email']
            try:
                u = User.objects.get(username=email.replace('@', '_at_'))
                user = authenticate(username = email.replace('@', '_at_'), password=request.POST['password'])
                # return redirect('/home')
                if user:
                    auth_login(request, user)
                    return HttpResponseRedirect('/home')
                else:
                    messages.error(request, 'Invalid username or password.!')
                    return HttpResponseRedirect('/login_view')
            except User.DoesNotExist:
                messages.error(request, 'User not found.!')
                return HttpResponseRedirect('/login_view')
        else:
            messages.error(request, 'Invalid username or password.!')
            return HttpResponseRedirect('/login_view')


def register(request):
    email = request.POST['email']
    username = email.replace('@', '_at_')
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    if password != confirm_password:
        err = _('Passwords do not match.!')
        messages.error(request, err)
        return HttpResponseRedirect('/register_view')

    # Si username déjà utilisé, erreur :
    if len(User.objects.filter(username__exact=username)):
        err = _('User already registered.!')
        messages.error(request, err)
        return HttpResponseRedirect('/register_view')
    # Si email déjà utilisé, erreur :
    if len(User.objects.filter(email__exact=email)):
        err = _('This email is already used.!')
        messages.error(request, err)
        return HttpResponseRedirect('/register_view')

    # Création de l'utilisateur :
    try:
        user = User.objects.create_user(
            username=username, email=email, password=password,
            first_name=firstname, last_name=lastname)
    except IntegrityError:
        err = _('Username already registered.!')
        messages.error(request, err)
        return HttpResponseRedirect('/register_view')

    user.is_active = True
    user.save()

    return HttpResponseRedirect('/register_view')


@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/')
def home(request):
    return render(request, 'auth/home.html')
