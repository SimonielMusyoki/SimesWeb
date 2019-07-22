from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def testView(request, slug):
    # obj = get_object_or_404(BlogPost, slug=slug)
    queryset = BlogPost.objects.filter(slug=slug)
    obj = queryset.first()
    # try:
    #     obj = BlogPost.objects.get(id=post_id)
    # except BlogPost.DoesNotExist:
    #     raise Http404
    # except ValueError:
    #     raise Http404
    context= {"object":obj}
    template_name = "test.html"
    return render(request, template_name, context)

def blog_post_list_view(request):
    #  List out objects
    # Search object
    template_name = 'blog_post_list.html'
    qs2 = BlogPost.objects.filter(title__icontains='some_text')
    qs = BlogPost.objects.all()
    context = {"object_list":qs}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    template_name = "blog_post_detail.html"
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj, "title":"Post Detail"}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    template_name = "blog_post_update.html"
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj, "title":"Post Update"}
    return render(request, template_name, context)

def blog_post_create_view(request):
    # Create objects
    # ? User forms
    template_name = "blog_post_create.html"
    form = None
    context = {"form": form,"title":"Post Create"}
    return render(request, template_name, context)

def blog_post_delete_view(request,slug):
    template_name = "blog_post_delete.html"
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj, "title":"Post Delete"}
    return render(request, template_name, context)