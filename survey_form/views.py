from django.shortcuts import render, redirect, HttpResponse

def form(request):
    return render(request, 'survey_form/form.html')

def process(request):
    
    request.session['name'] = request.POST['name']
    request.session['dojo'] = request.POST['dojo']
    request.session['stack'] = request.POST['stack']
    request.session['comment'] = request.POST['comment']

    try:
        request.session['counter'] += 1
    except:
        request.session['counter'] = 1

    return redirect('/survey_form/result/')

def result(request):
    return render(request, 'survey_form/result.html')