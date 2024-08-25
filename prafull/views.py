# i am create this file
import string

from django .http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps= request.GET.get('fullcaps', 'off')

    if removepunc=="on":
        punctuation=string.punctuation
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                 analyzed=analyzed+char
        params={'purpose':'removed punctuations','analyzed_text':analyzed}
        return render(request, 'login.html',params)
    elif(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        return render(request, 'login.html', params)


    else:
        return HttpResponse("<h1>Please on the removepuc<h1>")