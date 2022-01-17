


from django.http.response import HttpResponse
from django.shortcuts import render

def myHomeViewFunction(request):
    #The role of any function is to return something
    #return HttpResponse('Hello From HOme route')
    return render(request,'index.html')

def myAboutUsViewFunction(request):
    return HttpResponse('Hello from Aboutus Route')

def myContactUsViewFunction(request):
    return HttpResponse('Hello from Contactus route')


def category(request,category=None):
    x = request.GET.get('name')
    return HttpResponse(f'Hello {x} from Category  {category}')