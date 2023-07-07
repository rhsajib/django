from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def Home(request):
    text = {'name' : 'Rashed Sajib',
            'age' : '29',
            'phone' : '+8801675916784',
            'email' : 'sajib.mmebuet@gmail.com',
            'friends_name' : ['Piash', 'Akash', 'Bokor', 'Arif']
    }
    return render(request, 'home/home.html', text)