from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import teams

# Create your views here.

def demo (request):
    obj = place.objects.all()
    abc = teams.objects.all()
    return render(request,'index.html',{'res':obj,'team':abc})

# def math(request):
#     return render(request,'html2.html')
# def ans(request):
#     num1=int(request.GET['num1'])
#     num2=int(request.GET['num2'])
#     ad=num1+num2
#     su=num1-num2
#     mu=num1*num2
#     di=num1/num2
#     return render(request,'html3.html',{'add':ad,'sub':su,'mul':mu,'div':di})

# def demo(request):
#     name='INDIA'
#     return render(request,'html1.html',{'obj':name})
#     # return HttpResponse('hello')
# def hello(request):
#     return HttpResponse("hy")