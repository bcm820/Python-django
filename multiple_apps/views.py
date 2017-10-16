from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/multiple_apps/')

def show(request, num):
    response = "placeholder to display blog #"
    return HttpResponse(response + num)

def edit(request, num):
    response = "placeholder to edit blog #"
    return HttpResponse(response + num)

def destroy(request, num):
    return redirect('/multiple_apps/')

def surveys(request):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)

def new_survey(request):
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)

def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)

def users(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)