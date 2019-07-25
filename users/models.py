from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    position = models.CharField(max_length=120, default="Anonymous")
    technologies = models.CharField(max_length=120,blank=True, null=True)
    github = models.URLField(max_length=120,blank=True, null=True)
    facebook = models.URLField(max_length=120,blank=True, null=True)
    twitter = models.URLField(max_length=120, blank=True, null=True)
    linkedin = models.URLField(max_length=120,blank=True, null=True)
    bitbucket = models.URLField(max_length=120, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.png', upload_to='profile_pics')
#     username = models.CharField(max_length=120, default="Anonymous")
#     position = models.CharField(max_length=120, default="Anonymous")
#     technologies = models.CharField(max_length=120,blank=True, null=True)
#     github = models.URLField(max_length=120,blank=True, null=True)
#     facebook = models.URLField(max_length=120,blank=True, null=True)
#     twitter = models.URLField(max_length=120, blank=True, null=True)
#     linkedin = models.URLField(max_length=120,blank=True, null=True)
#     bitbucket = models.URLField(max_length=120, blank=True, null=True)

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self):
#         super().save()

#         img = Image.open(self.image.path)
#         if img.height > 300 or img.width > 300:
#             output_size = (300,300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)
