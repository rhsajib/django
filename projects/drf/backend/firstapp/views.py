from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny




from django.contrib.auth.models import User

@api_view(['POST'])
def registrationAPI(request):
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1 = request.data['password1']
        password2 = request.data['password2']

        if User.objects.filter(username=username).exists():
            return Response({'error': 'The username already exists'})
        if password1 != password2:
            return Response({'error': 'Two passwords didn\'t match'})
        
        # if the above conditions ok
        # we will create an user from User class
        user = User()

        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True

        # we will not save our raw password
        # django will save the password with encryption

        user.set_password(raw_password=password1)
        user.save()
        
        return Response({'success': 'User registered successfully.'})




"""Function based API view"""

@api_view(['GET', 'POST'])
# @permission_classes([AllowAny,])
@permission_classes([IsAuthenticated,])
def firstAPI(request):
    if request.method == 'POST':
        name = request.data['name']
        age = request.data['age']
        print(name, age)
        
        return Response({'name': name, 'age': age})
    
    context = {
        'name': 'Sajib',
        'university': 'BUET'
    }
    return Response(context)





"""Class based API view"""

from rest_framework.views import APIView

class Contact(APIView)
