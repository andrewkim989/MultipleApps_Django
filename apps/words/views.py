from django.shortcuts import render, redirect
import datetime

def entry(request):
    if "word" not in request.session:
        request.session['word'] = ['']
    info = {
        "words": request.session['word']
    }
    return render(request, "sessionwords.html", info)

def enter(request, methods = ['POST']):
    if request.method == 'POST':
        now = datetime.datetime.now()
        color = request.POST['color']
        newword = request.POST['newword']
        wordlist = request.session['word']
        
        if 'big' in request.POST:
            wordlist.append(f"<p style='color: {color}; font-size: 25px;'>{newword} - added on {str(now)}</p>")
        else:
            wordlist.append(f"<p style='color: {color}'>{newword} - added on {str(now)}</p>")  
        
        request.session['word'] = wordlist
        return redirect("/words")

def reset(request, methods = ['POST']):
    request.session.clear()
    return redirect("/words")