from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>Hello CFE Blog</h1>")

def about(request):
    return HttpResponse("<h1>About CFE Blog</h1>")

def contact(request):
    return HttpResponse("<h1>Contact CFE Blog</h1>")

class HomeTemplateView(TemplateView):
    template_name="home.html"