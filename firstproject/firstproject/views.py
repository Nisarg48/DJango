# error
# def index(request):
#     print "Hello"

from django.http import HttpResponse
from django.shortcuts import render

def index(request): 
    # param = {'name' : 'Nisarg', 'place' : 'Maroli'}
    return render(request, 'index.html')
    # return HttpResponse("Hello")
# send data "param" in template 

def analyze(request):
    #get the text
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    djtext = request.GET.get('text', 'default')
    # print(djtext)
    # analyzed = djtext
    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params = {'purpose' : 'Remove Punctuation', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)
    
    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        params = {'purpose' : 'Change To UpperCase', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)
    
    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        
        params = {'purpose' : 'Remove NewLine', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)

    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        
        params = {'purpose' : 'Remove NewLine', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)

    elif(charcount == "on"):
        count = 0
        for char in djtext:
            if char.isalpha():
                count = count + 1

        params = {'purpose' : 'Total Number Of Character', 'analyzed_text' : count}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

# def removepunc(request):
#     #get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     return HttpResponse("removepunc")

# def capfirst(request):
#     return HttpResponse("capfirst")

# def newline(request):
#     return HttpResponse("newline")