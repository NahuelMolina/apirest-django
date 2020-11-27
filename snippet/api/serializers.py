from rest_framework import serializers
from django.contrib.auth.models import User
from snippet.models import mymodel, Customer

# Here is where the models are converted with the serializer class

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
    	model = User
    	fields = ('id','username','email')

class mymodel_serializer(serializers.ModelSerializer):
    class Meta:
        model = mymodel
	fields = '__all__'

class customer_serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
