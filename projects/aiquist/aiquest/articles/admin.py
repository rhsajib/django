from django.contrib import admin


# Register your models here.
from .models import Articles

# from lecture 21 CodingEntrepreneurs
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'content']



admin.site.register(Articles, ArticlesAdmin)