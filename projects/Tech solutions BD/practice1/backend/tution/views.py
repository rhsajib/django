from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views import View
from django.http import HttpResponse
from django.views.generic import FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from .models import Contact, Post, Subject, Class_in
from .forms import ContactForm, ContactModelForm, PostForm







def search(request):
    query = request.POST.get('search')
    
    if query:
        queryset = (Q(title__icontains=query)) | (Q(detail__icontains=query)) | (Q(email__icontains=query)) | (Q(medium__icontains=query)) | (Q(catagory__icontains=query)) | (Q(user__username__icontains=query))

        results = Post.objects.filter(queryset).distinct()
        results_count = results.count()


    else:
        results = []
        results_count = 0

    context = {
        'results' : results,
        'results_count' : results_count,
        'query' : query,

        }

    return render(request, 'tution/search.html', context)


def post_filter(request):
    sub_query = request.POST.get('subject')
    class_query = request.POST.get('class_in')
    salary_from = request.POST.get('salary_from')
    salary_to = request.POST.get('salary_to')
    available = request.POST.get('available')

    nofilter = results = Post.objects.all()

    if sub_query != 'Choose...':
        queryset = (Q(subject__name__icontains=sub_query))
        results = results.filter(queryset).distinct()

    if class_query != 'Choose...':
        queryset = (Q(class_in__name__icontains=class_query))
        results = results.filter(queryset).distinct()

    if available:
        results = results.filter(available=True)
    
    if salary_from:
        results = results.filter(salary__gte=salary_from)

    if salary_to and (salary_to > salary_from):
        results = results.filter(salary__lte=salary_to)
  
    if nofilter == results:
        results = []

    context = {
        'results' : results,
        'results_count' : len(results),
        }

    return render(request, 'tution/postfilter.html', context)



class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'tution/postcreate.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):        
        form.instance.user = self.request.user 
        
        # self.object = form.save(commit=False)
        # self.object.user = self.request.user
        # self.object.save() 

        # subject = form.cleaned_data['subject']
        # self.object.subject.set(subject)

        # class_in = form.cleaned_data['class_in']
        # self.object.class_in.set(class_in)

        # print(form.instance.subject.all())
        # print(form.instance.class_in.all())
        messages.success(self.request, 'Post created successfully !!')  
        return super().form_valid(form)
    

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()

        # optionally we can access form data with form.cleaned_data['first_name']
        sub = form.cleaned_data['subject']
        for i in sub:
            obj.subject.add(i)
            obj.save()
            
        class_in = form.cleaned_data['class_in']
        for i in class_in:
            obj.class_in.add(i)
            obj.save()

        messages.success(request, 'Post created successfully !!') 
        return redirect('home')

    return render(request, 'tution/postcreate.html', {'form': form})
    

        
    
class PostListView(ListView):
    # model = Post
    template_name = 'tution/postlist.html'
    # queryset = Post.objects.filter(user=1)
    queryset = Post.objects.all().order_by('-id')

    # pass extra data to template
    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        posts = context.get('object_list')
        context['posts'] = posts
        context['total_posts'] = len(posts)
        context['subjects'] = Subject.objects.all()
        context['class_in'] = Class_in.objects.all()
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
        messages.success(self.request, 'Contact successfully submitted !!')
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

    initials = {
        'phone': '+880',
        'content': 'My content is'
    }

    if request.method == 'POST':
        form = ContactForm(request.POST, initial=initials)
       

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            content = form.cleaned_data['content']

            obj = Contact(name=name, phone=phone, content=content)
            obj.save()
    
    else:
        form = ContactForm(initial=initials)
               
    return render(request, 'contact.html', {'form': form})