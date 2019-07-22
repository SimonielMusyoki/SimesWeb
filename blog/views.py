from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm

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
    template_name = 'blog/list.html'
    qs2 = BlogPost.objects.filter(title__icontains='some_text')
    qs = BlogPost.objects.all()
    context = {"object_list":qs}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    template_name = "blog/detail.html"
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj, "title":"Post Detail"}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    template_name = "blog/update.html"
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj, "title":"Post Update"}
    return render(request, template_name, context)

def blog_post_create_view(request):
    # Create objects
    # ? User forms
    # form = BlogPostForm(request.POST or None)
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data)
        # obj = BlogPost.objects.create(**form.cleaned_data)
        # obj.save()
        form.save()
        return redirect('home')
        

    template_name = "blog/create.html"
    context = {"form": form,"title":"Post Create"}
    return render(request, template_name, context)

def blog_post_delete_view(request,slug):
    template_name = "blog/delete.html"
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj, "title":"Post Delete"}
    return render(request, template_name, context)