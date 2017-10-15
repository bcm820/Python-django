# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
import datetime

def index(request):
    
    context = {
        "title": "The current time and date:",
        "datetime": datetime.datetime.now()
        }

    return render(request, "time_display/time.html", context)