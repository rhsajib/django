from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q

# Create your views here.

def student_list(request):
    # posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')
    posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q(surname__startswith='baldwin') | Q(surname__startswith='avery'))

    print(posts)
    print(connection.queries)
    print(posts.query)
    
    context = {
        'post': posts,
    }

    return render(request, 'output.html', context=context)



def student_list_(request):
    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)
    
    context = {
        'post': posts,
    }

    return render(request, 'output.html', context=context)

def student_detail(request, student_id):
    
    detail_dict = Student.objects.get(pk=student_id).__dict__
    # __dict__ is used to get dictionary of all attributes with values of the object 
    # output:
    # {'_state': <django.db.models.base.ModelState object at 0x103afb210>, 
    # 'id': 1, 
    # 'firstname': 'shaina', 
    # 'surname': 'austin', 
    # 'age': 20, 'classroom': 1, 
    # 'teacher': 'trellany'}

    print(detail_dict)
    context = {
       'stdetail': detail_dict
    }

    return render(request, 'output.html', context=context)