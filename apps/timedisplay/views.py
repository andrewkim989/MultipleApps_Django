from django.shortcuts import render
from time import localtime, strftime

def index(request):
    context = {
        "mdy": strftime("%B %d, %Y", localtime()),
        "time": strftime("%I:%M:%S %p", localtime())
    }
    return render(request, 'time.html', context)