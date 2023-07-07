from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    excerpt = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
 
    def get_absolute_url(self):
        return reverse("firstapp:single", kwargs={'slug': self.slug})

    
    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
    