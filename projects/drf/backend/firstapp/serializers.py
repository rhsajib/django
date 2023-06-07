from rest_framework import serializers
from firstapp.models import Contact
from rest_framework.validators import UniqueValidator

class ContactSerializers(serializers.ModelSerializer):

    # uniqueness validation of name field for ensuring data integrity 
    # and preventing duplicate entries.
    name = serializers.CharField(
        max_length=100, 
        validators=[UniqueValidator(queryset=Contact.objects.all())])
    
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['name', 'email', 'phone', 'subject', 'details']



class ContactSerializerOne(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=200)
    subject = serializers.CharField(max_length=200)
    details = serializers.CharField(max_length=200)



    def create(self, validated_data):
        """
        Create and return a new `Contact` instance, given the validated data.
        """
        return Contact(**validated_data)    # or, return Contact.objects.create(**validated_data)
    


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.details = validated_data.get('details', instance.details)

        instance.save()

        return instance
    