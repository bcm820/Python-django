# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

# '/'
def index(request):
    response = "placeholder to later display all list of blogs"
    return HttpResponse(response)

# '/new'
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

# '/create'
def create(request):
    return redirect('/')

# '/<number>'
def show(request, number):
    response = "placeholder to display blog "
    return HttpResponse(response + number)

# '/<number>/edit'
def edit(request, number):
    response = "placeholder to edit blog "
    return HttpResponse(response + number)

# '/<number>/delete'
def destroy(request, number):
    return redirect('/')