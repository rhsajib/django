To pass the error message from `UniqueValidator` to `message.error` method, we can catch the `ValidationError` raised by the serializer's validation process and extract the error message from it. Here's an example of how we can achieve this:

```python
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib import messages

class ContactSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def validate(self, data):
        # Validate uniqueness of username and email
        username = data.get('username')
        email = data.get('email')

        if username and User.objects.filter(username=username).exists():
            error_message = "Username already exists."
            raise serializers.ValidationError(error_message)

        if email and User.objects.filter(email=email).exists():
            error_message = "Email already exists."
            raise serializers.ValidationError(error_message)

        return data

    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'username', 'password1', 'password2']

    def create(self, validated_data):
        # Create the user object
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )

        # Set is_active to False for email verification
        user.is_active = False
        user.save()

        return user
```

In your view or API endpoint, after calling the serializer's `is_valid()` method, we can check if there are any validation errors and then use `messages.error()` to display the error message to the user:

```python
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Send email with activation link
            # ...
            messages.success(request, 'Registration successful. Please check your email for activation.')
            return redirect('index:index')
        else:
            for field, errors in serializer.errors.items():
                for error in errors:
                    messages.error(request, error)
            return redirect('index:index')
```

In the example above, the error messages from `UniqueValidator` are extracted in the `validate` method of the serializer and raised as `ValidationError`. Then, in the view, the error messages are retrieved from the serializer's `errors` attribute and passed to `messages.error()` for displaying to the user.