from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):

    if request.method == 'GET':

        # for page refresh while in session
        if 'random' in request.session:
            context = {
                "counter": "(attempt #{})".format(request.session['counter']),
                "word": request.session['random']
                }
            return render(request, "random_word/random.html", context)
        
        # for first visits or resets
        else:
            return render(request, "random_word/random.html")
    
    else: # if POST method

        try: # increment if counter in session
            request.session['counter'] += 1
        except: # create counter if not exists
            request.session['counter'] = 1

        request.session['random'] = get_random_string(length=14)

        context = {
        "counter": "(attempt #{})".format(request.session['counter']),
        "word": request.session['random']
        }

        return render(request, "random_word/random.html", context)

def reset(request):

    try: # reset if keys in session
        del request.session['counter']
        del request.session['random']
        return redirect('/random_word/')

    except: # redirect if user tries to del non-existing keys
        return redirect('/random_word/')