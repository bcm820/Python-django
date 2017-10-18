from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
from .models import *


def list(request):
    courses = { "courses": Course.objects.all() }
    return render(request, 'courses/list.html', courses)

def show(request, id):
    course = {
        "course": Course.objects.get(id=id),
        "reviews": Course.objects.get(id=id).reviews.all()
    }
    return render(request, 'courses/show.html', course)

def confirm(request, id):
    course = { "course": Course.objects.get(id=id) }
    return render(request, 'courses/confirm.html', course)

def create(request):

    errors = Course.objects.validate(request.POST)

    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
    
    else:
        Course.objects.create(
            title = request.POST['title'],
            description = request.POST['description'])

    return redirect('/courses/')

def review(request, id):

    errors = Review.objects.validate(request.POST)

    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)

    else:
        Review.objects.create(
            review = request.POST['review'],
            course = (Course.objects.get(id=id)))

    return redirect('/courses/' + str(id))

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/courses/')