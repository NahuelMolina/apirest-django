from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from .models import mymodel
from .serializers import UserSerializer, mymodel_serializer


# Here is where the models serializers and the objects created on terms of this models, 
# are connected

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class SomethingViewSet(viewsets.ModelViewSet):
	queryset = mymodel.objects.all()
	serializer_class = mymodel_serializer