from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime

def index(request):
    return render(request, 'session_words/index.html')

def add(request):
    
    if len(request.POST['word']) == 0:
        return redirect('/session_words/')
    elif len(request.POST['color']) == 0:
        return redirect('/session_words/')

    else:
        
        if 'words' not in request.session:
            request.session['words'] = []
        
        # checkboxes optionally included in req.POST
        if 'big' in request.POST:
            size = 'big'
        else:
            size = 'normal'
        
        # can't append to list in session dict, so...
        # pull list out, append, and restore!
        temp = request.session['words']
        temp.append(
            {
                "word": request.POST['word'],
                "color": request.POST['color'],
                "size": size,
                "datetime": datetime.now().strftime("%H:%M %p, %B %d, %Y")
            }
        )
        request.session['words'] = temp

        # CD solution used .iteritems() to create {}
        # for key, value in request.POST.iteritems():
        #     if key != "csrfmiddlewaretoken" and key != "big":
        #         word[key] = value
        #     if key == 'big':
        #         word['big'] = 'big'
        #     else:
        #         word['big'] = ""

        return redirect('/session_words/')

def clear(request):
    if 'words' in request.session:
        del request.session['words']
    return redirect('/session_words/')