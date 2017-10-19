from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
from .models import *
import bcrypt

def index(request):
    return render(request, 'login_registration/index.html')

def success(request):
    if not 'user' in request.session:
        error(request, "You must login to view your information.")
        return redirect('/login_registration/')

    user = {
        "user": User.objects.get(email_address=request.session['user'])
    }
    
    return render(request, 'login_registration/success.html', user)

def login(request):

    errors = User.objects.validate(request.POST)

    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/login_registration/')

    else:
        request.session['user'] = email_address=request.POST["login_email"]

        return redirect('/login_registration/success/')

def register(request):

    errors = User.objects.validate(request.POST)

    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/login_registration/')

    else:
        User.objects.create(
            first_name = request.POST["first_name"],
            last_name = request.POST["last_name"],
            email_address = request.POST["email_address"],
            password = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
        )

        request.session['user'] = request.POST["email_address"]

        return redirect('/login_registration/success/')

def logout(request):
    request.session.flush()
    error(request, "You have successfully ended your session. Thank you!")
    return redirect('/login_registration/')