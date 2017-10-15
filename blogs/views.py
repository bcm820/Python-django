# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

# '/'
def index(request): # HTTP req passed into method
    response = "display list of blogs" # var set inside method
    return HttpResponse(response) # var passed in as res to req

# '/new'
def new(request):
    
    # Dictionary data can be called within renders via their keys
    # No need to call by variable, just add {{title}}, {{name}}, etc.
    # This is a much nicer way to oragnize all your data!
    context = {
        "title" : "Create a New Blog",
        "name" : "Brian"
    }

    # Render will look in templates dir, but you specify <app>/<file>.html
    return render(request, "blogs/new.html", context)

# '/create'
def create(request):

    # In Django, we specify request methods inside the function. Functions can take both POST and GET request methods via IFs.
    # But we should still isolate request methods for maintainability
    
    # request.method returns a string with request type ('POST' or 'GET')
    if request.method == "POST":

        # request.POST is a dictionary of data from the POST request
        print request.POST
        print request.POST['title'] # title is key
        print request.POST['desc'] # desc is key

        # request.session is also a dictionary, as per usual
        # to call within renders, use dot notation {{request.session.title}}
        request.session['title'] = request.POST['title'] # store posts
        request.session['counter'] = 100 # store any key and value

        # it's VERY important to delete session keys since otherwise they will be stored in Django's session dict permanently!
        del request.session['counter'] # delete session key if it exists
        
        # if no session key exists, there will be a keyError
        # better to use a try and except to avoid the error
        try:
            del request.session['whatever']
        except:
            pass

        # or you can ask if key exists, and delete if so
        if 'whatever' in request.session: # returns a boolean
            del request.session['whatever']

        return redirect('/blogs/')

    else: # i.e. else if request.method == "GET"
        return redirect('/blogs/')

# '/<num>'
def show(request, num):
    response = "address for blog #"
    return HttpResponse(response + num)

# '/<num>/edit'
def edit(request, num):
    response = "address to edit blog #"
    return HttpResponse(response + num)

# '/<num>/delete'
def destroy(request, num):
    return redirect('/blogs/')