# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import strftime

def index(request):
    
    context = {
        "title": "The current time and date:",
        "date": strftime("%A %B %d"),
        "time": strftime("%-I:%M %p %Z")
        }

    return render(request, "time_display/time.html", context)