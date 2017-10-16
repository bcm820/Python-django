from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

def index(request):
    
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = ""
    
    # Create ninja gold options to display on page
    request.session['locations'] = [
        {'id': 'farm', 'name': 'Farm', 'actions': 'earns 10-20'},
        {'id': 'cave', 'name': 'Cave', 'actions': 'earns 5-10'},
        {'id': 'house', 'name': 'House', 'actions': 'earns 2-5'},
        {'id': 'casino', 'name': 'Casino', 'actions': 'earns/takes 0-50'}
    ]

    return render(request, "ninja_gold/index.html")

def process(request, place):

    if place == 'farm':
        find = random.randrange(10, 21)
        request.session['gold'] += find
        request.session['activities'] += "Earned {} gold from the farm! {}\n".format(find, datetime.now().strftime("%d/%m/%y %H:%M"))

    if place == 'cave':
        find = random.randrange(5, 11)
        request.session['gold'] += find
        request.session['activities'] += "Earned {} gold from the cave! {}\n".format(find, datetime.now().strftime("%d/%m/%y %H:%M"))

    if place == 'house':
        find = random.randrange(2, 6)
        request.session['gold'] += find
        request.session['activities'] += "Earned {} gold from the house! {}\n".format(find, datetime.now().strftime("%d/%m/%y %H:%M"))

    if place == 'casino':
        find = random.randrange(0, 51)
        gamble = random.randrange(0,2)

        if gamble == 0:
            request.session['gold'] += find
            request.session['activities'] += "Earned a casino and lost {} gold. Ouch! {}\n".format(find, datetime.now().strftime("%d/%m/%y %H:%M"))
        else:
            request.session['gold'] += find
            request.session['activities'] += "Entered a casino and won {} gold! Yesss! {}\n".format(find, datetime.now().strftime("%d/%m/%y %H:%M"))

    return redirect('/ninja_gold/')