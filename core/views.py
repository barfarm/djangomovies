from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def hello(request):
#     return HttpResponse("Hello world!")
from django.shortcuts import  render
from core.models import Movie

def hello(request):
    return render(
        request,
        template_name="hello.html",
        context= {'adjectives':["beautiful","cruel","wonderful"]},
    )