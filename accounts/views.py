from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Users, AmbulanceHub, Ambulance, Token, AccountType
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage


def create_user(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.POST['email']):
            return render(request, 'user_signup.html', {'message': 1, 'username': request.POST['username'], 'password': request.POST['password'], 'email': request.POST['email'], 'address': request.POST['address'], 'phone': request.POST['phone']})
        elif User.objects.filter(username=request.POST['username']):
            return render(request, 'user_signup.html', {'message': 2, 'username': request.POST['username'], 'password': request.POST['password'], 'email': request.POST['email'], 'address': request.POST['address'], 'phone': request.POST['phone']})
        else:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
            user.is_active = False
            user.save()
            Users.objects.create(user=user, address=request.POST['address'], phone=request.POST['phone'])
            token = Token.objects.create(user=user, purpose='user_activation').token
            domain = get_current_site(request).domain
            mail_subject = 'Activate your account'
            mail_body = 'Please click on the link below to activate your account.\n{}://{}/accounts/useractivation/{}'.format(request.scheme, domain, token)
            EmailMessage(mail_subject, mail_body, to=[request.POST['email']]).send()
            return render(request, 'user_acc_activation.html')
    else:
        return render(request, 'user_signup.html')


def user_activation(request, token):
    if request.method == 'GET':
        try:
            t = Token.objects.get(token=token)
            if t.purpose != 'user_activation':
                return render(request, 'bad_request.html')
            else:
                user = t.user
                user.is_active = True
                user.save()
                t.delete()
                login(request, user)
                return redirect('home')
        except:
            return render(request, 'invalid_link.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'GET':
            return render(request, 'login.html')
        elif request.method == 'POST':
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                try:
                    return HttpResponseRedirect(request.GET['next'])
                except:
                    return redirect('home')
            else:
                return render(request, 'login.html', {'message': 'Invalid Credentials'})

def user_logout(request):
    logout(request)
    return redirect('home')
