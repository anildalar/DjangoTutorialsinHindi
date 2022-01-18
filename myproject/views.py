


from django.http.response import HttpResponse
from django.shortcuts import render

def myHomeViewFunction(request):
    #The role of any function is to return something
    #return HttpResponse('Hello From HOme route')
    return render(request,'index.html')

def myAboutUsViewFunction(request):
    return render(request,'about-us.html')

def myContactUsViewFunction(request):
    return HttpResponse('Hello from Contactus route')


def category(request,category=None):
    x = request.GET.get('name')
    return HttpResponse(f'Hello {x} from Category  {category}')


def cart(request):
    return render(request, 'shopping-cart.html')

def detail(request):
    return render(request, 'single-product.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')