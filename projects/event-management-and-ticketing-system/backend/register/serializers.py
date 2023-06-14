
from .models import Contact

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.validators import MinLengthValidator, RegexValidator


from rest_framework import serializers
from rest_framework.validators import UniqueValidator



class ContactSerializer(serializers.ModelSerializer):

    # # uniqueness validation of username and email fields 
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=Contact.objects.all(), message='Email already exists.')]
        )
    
    username = serializers.CharField(
        max_length = 100,
        validators = [UniqueValidator(queryset=Contact.objects.all(), message='Username already exists.')]
        )
    
    
    password1 = serializers.CharField(
        write_only=True,
        validators=[
            MinLengthValidator(8, message='Password must be at least 8 characters.'),
            RegexValidator(
                regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d$@$!%*?&].*$',
                message='Password must contain at least one uppercase letter, one lowercase letter, and one digit.'
            )
        ]
    )


    password2 = serializers.CharField()
    
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'username', 'password1', 'password2']
        extrta_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True},
            # By providing extra_kwargs in this manner, we are explicitly specifying that 
            # password1 and password2 fields should be treated as write-only, 
            # meaning they will not be included in the serialized representation of the object. 
            # This ensures that the password fields are used for deserialization only, 
            # such as during user creation or update, 
            # but are not exposed in the API response or any serialized output.


            
            # 'email': {'validators': []}
            # To bypass the UniqueValidator for update operations
            # By setting an empty list ([]) as the validators for the email field, 
            # we are effectively removing any validators for that field, including the UniqueValidator. 
            # This allows updates to the email field without triggering uniqueness checks.
            
        }


  
    # validating password1 and password2
    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')

        if password1 != password2:
            raise serializers.ValidationError({'password2': 'Passwords do not match.'})
            # the above validation error will return a message

        return attrs



    # creating a new user with the given validated data 
    def create(self, validated_data):
        
        password1 = validated_data.pop('password1')
        password2 = validated_data.pop('password2')
       
        validated_data['password'] = make_password(password1)

        # Create the user object
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        user.is_active = False
        user.save()

        """
        # alternative way to create the user object
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        """        

        # welcome email
        subject = 'Welcome to EMTS'
        message = 'Hello ' + validated_data['name'] + '!! \n'  \
                    + 'Welcome to EMTS. \n'  \
                    + 'thanks for visiting our website.'
        
        from_email = settings.EMAIL_HOST_USER
        to_email_list = [user.email]

        send_mail(subject, message, from_email, to_email_list, fail_silently=False)
        # fail_silently=True means if the app fails to send email to user it will not crash

        """

        # Generate activation token
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)

        # Generate activation link
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_link = f'{settings.ACTIVATION_BASE_URL}/{uid}/{token}/'

        # Send the email
        subject = 'Activate your account'
        message = f'Please click the following link to activate your account: {activation_link}'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email_list = [user.email]

        send_mail(subject, message, from_email, to_email_list, fail_silently=True)
        # fail_silently=True means if the app fails to send email to user it will not crash

        """


        # Create the YourModel object
        new_contact = Contact.objects.create(**validated_data)


        return new_contact
    
  
