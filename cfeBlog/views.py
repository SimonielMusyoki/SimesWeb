from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>Hello CFE Blog</h1>")

def about(request):
    context = {"title":"About Us"}
    template_name = 'about.html'
    return render(request, template_name, context)

def contact(request):
    context = {"title":"Contact Us"}
    template_name = 'contact.html'
    return render(request, template_name, context)

class HomeTemplateView(TemplateView):
    title = "Home"
    template_name="home.html" 