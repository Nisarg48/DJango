from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'calculator.html')


def calculate(request):
    ans = ''
    try:
        if request.method=='POST':
            num1=eval(request.POST.get('num1'))
            num2=eval(request.POST.get('num2'))
            sign=request.POST.get('operation')

            if sign=='+':
                ans=num1+num2
            elif sign=='-':
                ans=num1-num2
            elif sign=='*':
                ans=num1*num2
            elif sign=='/':
                ans=num1/num2
                
    except:
        ans='Invalid...'
    
    print(ans)
    return render(request, 'calculator.html', {'ans':ans})


