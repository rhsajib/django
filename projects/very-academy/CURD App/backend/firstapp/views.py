from django.views.generic import ListView, DetailView
from .models import Blogs

# Create your views here.

class IndexListView(ListView):
    model = Blogs
    template_name = 'firstapp/index.html'

class SingleDetailView(DetailView):
    model = Blogs
    template_name = 'firstapp/single.html'
    context_object_name = 'post'
