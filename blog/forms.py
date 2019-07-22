from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','content','slug']
    
    def clean_slug(self, *args, **kwargs):
        slug = self.cleaned_data.get('slug')
        qs = BlogPost.objects.filter(slug=slug)
        if qs.exists():
            raise forms.ValidationError("Slug is already taken")
        return slug
