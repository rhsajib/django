from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
# DRF has also a login() function.
# thats why we imported the login() function in Django's authentication module as auth_login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny

from.serializers import ContactSerializer
from .models import Contact

# Create your views here.

def create_user_account(request):
    return render(request, 'register/register.html')


def login(request):
    return render(request, 'register/login.html')


# creating user api view
class UserAPIView(APIView):
    permission_classes = [AllowAny,]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # success message for creating account
            messages.success(request, 'Your account has been successfully created.')

            return redirect('register:login')


        else:
            print( serializer.errors.items())          
            for fields, errors in serializer.errors.items():
                print(fields, errors)
                for error in errors:
                    messages.error(request, error)
            
            return redirect('register:create_user_account')
        


"""
# In Django, we can use the login function from django.contrib.auth to authenticate the user 
# and log them in after the account creation process. Here's an example of how we can achieve this:


class UserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the new user account
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Authenticate the user
            auth_user = authenticate(request, username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)  # Log in the authenticated user
                return Response(serializer.data, status=201)
            else:
                return Response({'detail': 'Unable to log in the user.'}, status=400)
        
        return Response(serializer.errors, status=400)


# In the code snippet above, after the user account is successfully created and saved, 
# the authenticate function is called to verify the user's credentials. 
# If the authentication is successful, 
# the login function is used to log in the user by creating a session for them.


Please note that to use the login function, 
we need to have the session middleware and 
authentication backends properly configured in our Django project.


By authenticating the user and logging them in after account creation, 
we can provide a seamless experience where the user is immediately authenticated 
and can access protected resources or perform authenticated actions on subsequent requests.


Remember to handle error cases appropriately, 
such as when the authentication fails, and provide meaningful responses to the client.

"""





# user login using django.contrib.auth module
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')       # or, username = request.POST['username']
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        # print('user: ', user)

        if user is not None:
            auth_login(request, user)

            # Get the Contact object associated with the username
            contact = Contact.objects.get(username=username)
           
            # print('name:', contact.name)
            # print('email:', contact.email)
            # print('phone:', contact.phone)
            # print('username:', contact.username)          

            return render(request, 'index/index.html', {'contact': contact})
        
        else:
            messages.error(request, 'Incorrect Username or Password')
            return redirect('register:login')
        

def user_logout(request):
    logout(request)
    return render(request, 'register/logout.html')



# user login using DRF module
class UserLoginAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')  
        password = request.data.get('password')

        print(username, password)

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        print(user)
        print(type(user))
        
        if user is not None:
            auth_login(request, user)              # Log in the authenticated user
            object_query_set = Contact.objects.filter(username=username)
            return Response({'user': object_query_set}, template_name='index/index.html')

        else:
            return Response({'detail': 'Invalid username or password.'}, status=401)




