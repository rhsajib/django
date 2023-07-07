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





"""Class based API view without serializer"""

from rest_framework.views import APIView
from .models import Contact

class ContactAPIView2(APIView):   
    permission_classes = [AllowAny,]
    def post(self, request, format=None):
        data = request.data

        name = data['name']
        email = data['email']
        subject = data['subject']
        phone = data['phone']
        details = data['details']

        if Contact.objects.filter(name=name).exists():
            return Response({'error': 'This name already exists'})

        contact = Contact(
            name = name,
            email = email,
            subject = subject,
            phone = phone,
            details = details
        )
        contact.save()       
        return Response({'succeess': 'Successfully saved!!'})
    
    def get(self, request, format=None):
        return Response({'success': 'Successfully saved!! from get'})
    

"""Class based API view with Modelserializer"""

from rest_framework.views import APIView
from .models import Contact
from .serializers import ContactSerializers

class ContactAPIView(APIView):   
    permission_classes = [AllowAny,]
    def post(self, request, format=None):
        # load request data
        data = request.data

        # create instance
        serializer = ContactSerializers(data=data)

        # check validity
        if serializer.is_valid():
            serializer.save()
            return Response({'succeess': 'Successfully saved!!'})
            # return Response(serializer.data) # it will return serializer data        
        else:
            return Response({'error': 'Name already exists'})


    def get(self, request, format=None):
        # get all data of the class
        query_set = Contact.objects.all()
        serializer = ContactSerializers(query_set, many=True) 
        # many=True is added as query_set holds multiple objects

        return Response(serializer.data)   # response will be a list of dictionaries


        """
        
        #  get data of an id
        # request get with only id

        data = request.data  
        id = data.get('id')
        # id = data['id']

        query_set = Contact.objects.get(pk=id)
        serializer = ContactSerializers(query_set, many=False) 
        # many=False is added as query_set holds only one object

        return Response(serializer.data)    # response will be a dictionary not a list of dictionaries.
        

        """
       

"""Class based API view with only serializer"""

from rest_framework.views import APIView
from .models import Contact
from .serializers import ContactSerializerOne

class ContactAPIViewOne(APIView):   
    permission_classes = [AllowAny,]
    def post(self, request, format=None):
        # load request data
        data = request.data

        # create an instance
        serializer = ContactSerializerOne(data=data)

        # check validity
        if serializer.is_valid():
            serializer.save()
            # return Response({'succeess': 'Successfully saved!!',})
            return Response(serializer.data) # it will return serializer data        
        else:
            return Response({'error': 'Name already exists'})


    def get(self, request, format=None):
        # get all data of the class
        query_set = Contact.objects.all()
        serializer = ContactSerializerOne(query_set, many=True) 
        # many=True is added as query_set holds multiple objects

        return Response(serializer.data)   # response will be a list of dictionaries


        """
        
        #  get data of an id
        # request get with only id

        data = request.data  
        id = data.get('id')
        # id = data['id']

        query_set = Contact.objects.get(pk=id)
        serializer = ContactSerializerOne(query_set, many=False) 
        # many=False is added as query_set holds only one object

        return Response(serializer.data)    # response will be a dictionary not a list of dictionaries.
        

        """