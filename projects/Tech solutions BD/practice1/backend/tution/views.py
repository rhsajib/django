from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views import View
from django.http import HttpResponse
from django.views.generic import FormView, CreateView, ListView, DetailView, UpdateView, DeleteView


from .models import Contact, Post
from .forms import ContactForm, ContactModelForm, PostForm






class PostCreateView(CreateView):
    # model = Post
    form_class = PostForm
    template_name = 'tution/postcreate.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):        
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class PostListView(ListView):
    # model = Post
    template_name = 'tution/postlist.html'
    # queryset = Post.objects.filter(user=1)
    queryset = Post.objects.all()

    # pass extra data to template
    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['posts'] = context.get('object_list')
        context['message'] = 'This is post list'
        return context

class PostsDetailView(DetailView):
    model = Post 
    template_name = 'tution/postdetail.html'
    # pass extra data to template
    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['post'] = context.get('object')
        context['post_dict'] = context.get('object').__dict__
        context['message'] = 'This is post detail message'
        return context


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'tution/postcreate.html'

    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('tution:PostsDetailView', kwargs={'pk':id})

    # Optional: Change context data dict
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = 'Update'
        return context
    

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'tution/postdelete.html'
    success_url = reverse_lazy('tution:PostListView')



def postview(request):
    posts = Post.objects.all()
    return render(request, 'tution/postview.html', {'posts': posts})
    

class ContactView(FormView):
    form_class = ContactModelForm
    template_name = 'contact.html'
    # success_url = '/'                # root url
    
    def form_valid(self, form):
        form.save() 
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('home')





class ContactViewWithVewClass(View):
    form_class = ContactModelForm
    template_name = 'contact.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        
        return render(request, self.template_name, {'form': form})






def contact_with_modelform(request):
    form = ContactModelForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Submitted Successfully !')
        return redirect('tution:contact_with_modelform')

    return render(request, 'contact.html', {'form': form})
        
    


def contact_with_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        

        if form.is_valid():

            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            content = form.cleaned_data['content']

            obj = Contact(name=name, phone=phone, content=content)
            obj.save()
    
    else:
        form = ContactForm()
               
    return render(request, 'contact.html', {'form': form})