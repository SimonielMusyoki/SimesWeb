from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm

# def home(request):
#     return HttpResponse("<h1>Hello CFE Blog</h1>")

def about(request):
    context = {"title":"About SIMES"}
    template_name = 'about.html'
    return render(request, template_name, context)

def executives(request):
    context = {"title":"SIMES Executives"}
    template_name = 'executives.html'
    return render(request, template_name, context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    template_name = 'contact.html'
    context = {"title":"Contact Us", "form":form}
    return render(request, template_name, context)

class HomeTemplateView(TemplateView):
    title = "Home"
    template_name="blog/list.html" 