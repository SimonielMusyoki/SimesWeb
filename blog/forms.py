from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','image','content','slug']
    
    def clean_slug(self, *args, **kwargs):
        instance = self.instance
        slug = self.cleaned_data.get('slug')
        qs = BlogPost.objects.filter(slug__iexact=slug)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("Slug is already taken")
        return slug



