from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.http import Http404


from .models import Articles
from random import randint

# Create your views here.

# def articles_home(request):
#     obj_query_set = Articles.objects.all()
#     string1 = '<h1> I am from articles articles_home view</h1>'
#     return HttpResponse(string1)

def articles_home(request):
    # get set of all objects of Articles class
    obj_query_set = Articles.objects.all()

    # get all objects id queryset
    all_ids = Articles.objects.values_list('id', flat = True)  # it is an iterable set
    all_ids_list = list(all_ids) # it's a list of ids

    # let's create random id
    random_id = randint(1, len(all_ids))
    random_obj = Articles.objects.get(id=random_id)

    # creating context
    context = {
        'all_obj' : Articles.objects.all(),
        'rand_obj' : random_obj
    }
    return render(request, 'articles/articles_home.html', context)


def article_detail(request, id):
    all_ids = Articles.objects.values_list('id', flat = True)  # it is an iterable set
    object = Articles.objects.get(id = id) if id in all_ids else None
    return render(request, 'articles/detail.html', {'obj' : object})


# Raising a 404 error
def article_random_detail(request, id):
    try:
        object = Articles.objects.get(pk=id)  # this is same as Articles.objects.get(id = id)
    except Articles.DoesNotExist:
        raise Http404('Article does not exist')
    
    # A shortcut: get_object_or_404()
    # we can use it instead of try except statement
    # from django.shortcuts import render, get_object_or_404
    # object = get_object_or_404(Articles, pk=id)

    return render(request, 'articles/detail.html', {'obj' : object})


# view for search id
def article_search_detail(request):
    # print(dir(request))
    print(request.GET) # look at terminal to see the output of print function

    # extracting data from the request using get method
    query_dict = request.GET       
    # query_dict is a dictionary
    # but it is not possible to get data writing like request.GET ['q] or query_dict['q]
    # we sould grab data using 'get' function

    query = query_dict.get('q')   # <input type="text"  name="q">
    # or, query = rquest.GET.get('q)
    
    # get data fffrom database
    object = get_object_or_404(Articles, pk=query)
    return render(request, 'articles/search.html', {'obj' : object})
    # we could use detail page instead of search page like below
    # return render(request, 'articles/detail.html', {'obj' : object})
    # it would be good for us as we don't need to create extra search.html page


def article_create(request):
    print(request.GET)
    print(request.POST)
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(title, content)
    object = Articles.objects.create(title = title, content = content)
    context = {
        'obj' : object,
        'created' : True     # this value indicates that for is created
    }

    # sometimes GET and POST methods are called simultaneously
    # on that time, GET request will show 'None, None' value in terminal
    # so to avoid this we should use the following code 

    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(title, content)
        Articles.objects.create(title = title, content = content)
        
    """
    title = request.POST.get('title')
    content = request.POST.get('content')
    print(title, content)
    object = Articles.objects.create(title = title, content = content)
    context = {
        'obj' : object,
        'created' : True     # this value indicates that for is created
    }
    """
    return render(request, 'articles/create.html', context = context)





# see: https://docs.djangoproject.com/en/4.2/intro/tutorial03/
# def detail(request, id):
#     try:
#         article = Articles.objects.get(pk=id)
#     except Articles.DoesNotExist:
#         raise Http404("Articles does not exist")
#     return render(request, "articles/detail.html", {"article": article})

# def detail(request, id):
#     article = get_object_or_404(Articles, pk=id)
#     return render(request, "articles/detail.html", {"article": article})