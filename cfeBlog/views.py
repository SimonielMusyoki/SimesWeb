from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>Hello CFE Blog</h1>")

def about(request):
    title=" About Us"
    return render(request, 'about.html', {"title":title})

def contact(request):
    title = " Contact Us"
    return render(request, 'contact.html', {"title":title})

class HomeTemplateView(TemplateView):
    title = "Home"
    template_name="home.html" 