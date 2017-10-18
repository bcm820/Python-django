from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import User


def index(request):
    users = { "users": User.objects.all() }
    return render(request, 'users/index.html', users)

def new(request):
    users = { "users": User.objects.all() }
    return render(request, 'users/new.html', users)

def show(request, id):
    user = { "user": User.objects.get(id=id) }
    return render(request, 'users/show.html', user)

def edit(request, id):
    user = { "user": User.objects.get(id=id) }
    return render(request, 'users/edit.html', user)

def create(request):

    User.objects.create(
        name = request.POST['name'],
        email = request.POST['email'])

    id = User.objects.last().id

    return redirect('/users/' + str(id))

def update(request, id):

    user = User.objects.get(id=id)
    user.name = request.POST['name']
    user.email = request.POST['email']

    return redirect('/users/' + str(id))

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users/')