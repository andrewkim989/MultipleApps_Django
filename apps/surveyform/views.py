from django.shortcuts import render, redirect

def home(request):
    if "count" not in request.session:
        request.session['count'] = 0
    return render(request, "form.html")

def process(request, methods = ['POST']):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['count'] = int(request.session['count']) + 1

    return redirect('/survey/result')

def result(request):
    info = {
        "n": request.session['name'],
        "lo": request.session['location'],
        "la": request.session['language'],
        "c": request.session['comment'],
        "count": request.session['count']
    }

    return render(request, "results.html", info)

def delete(request):
    request.session['count'] = 0
    return redirect('/survey')
