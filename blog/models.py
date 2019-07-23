from django.db import models
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_posted','-updated','-timestamp']

    def get_absolute_url(self):
        return f"blog/{self.slug}"

    def get_update_url(self):
        return f"{self.get_absolute_url}/update"
    
    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"

    def get_detail_url(self):
        return f"{self.slug}/"
