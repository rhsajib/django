from typing import Iterable, Optional
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from PIL import Image
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User




class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Class_in(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=17)
    content = models.TextField()

    def __str__(self):
        return self.name
    
class Post(models.Model):
    CATAGORY = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )

    OPTIONS = (
        ('bangla', 'Bangla'),
        ('english', 'English'),
        ('arabic', 'Arabic'),
        ('hindi', 'Hindi'),
        ('urdu', 'Urdu'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    email = models.EmailField()
    salary = models.FloatField()
    detail = models.TextField()
    available = models.BooleanField()
    catagory = models.CharField(max_length=100, choices=CATAGORY, default='Student')
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='tution/images')
    medium = MultiSelectField(max_length=100 ,choices=OPTIONS, max_choices=3, default='bangla')
    subject = models.ManyToManyField(Subject, related_name='subject_set')
    class_in = models.ManyToManyField(Class_in, related_name='class_set')


    def save(self, *args, **kwargs):
        # slugify slug field
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        # convert image to desired size
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            converted_size = (300, 300)
            img.thumbnail(converted_size)
            img.save(self.image.path)


    def __str__(self):
        return self.title