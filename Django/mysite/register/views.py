from django.shortcuts import render, redirect
from .models import AccountsCreated


def homepage(request):
    return render(request, 'register/homepage.html', {})


def signup(request):
    return render(request, 'register/signup.html', {"title": "Signup"})


def login(request):
    if request.session.get('user'):
        return render(request, 'register/welcome.html', {})
    else:
        return render(request, 'register/login.html', {})


def signupValues(request):
    acc_id = request.POST['userid']
    acc_email = request.POST['email']
    acc_pass = request.POST['psw']
    acc_cpass = request.POST['psw-repeat']
    if acc_pass == acc_cpass:
        k = AccountsCreated.objects.filter(
            acc_id=acc_id).filter(acc_email=acc_email)
        if len(k) == 1:
            return render(request, 'register/signup.html', {"msg": "user already exists!"})
        else:
            a = AccountsCreated(
                acc_id=acc_id, acc_email=acc_email, acc_pass=acc_pass)
            a.save()
            return redirect('register:login')
    else:
        return render(request, 'register/signup.html', {"title": "Signup", "msg": "Passwords does not match!Enter again.."})


def loginValues(request):
    acc_email = request.POST['email']
    acc_pass = request.POST['psw']
    K = AccountsCreated.objects.filter(acc_email=acc_email, acc_pass=acc_pass)
    if len(K) == 1:
        request.session['user'] = (K.values('acc_id')[0])["acc_id"]
        return render(request, 'register/welcome.html', {})
    else:
        return render(request, 'register/login.html', {"msg": "Incorrect user id or password!"})


def logout(request):
    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()
        return redirect('register:homepage')
    return redirect('register:homepage')
