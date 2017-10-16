# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import arrow

def index(request):
    
    context = {
        "title": "The current time and date:",
        "time": arrow.now('US/Eastern').format('hh:mm A'),
        "date": arrow.now('US/Eastern').format('dddd MMMM D, YYYY')
        }

    return render(request, "time_display/time.html", context)