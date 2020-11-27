from django.shortcuts import render
from rest_framework import viewsets, mixins
from django.contrib.auth.models import User

from snippet.models import mymodel
from .serializers import UserSerializer, mymodel_serializer


# Here is where the models serializers and the objects created on terms of this models, 
# are connected

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    # we can use the next method instead of queryset
    # def get_queryset(self):
        # return self.request.user.accounts.all()


class SomethingViewSet(viewsets.ModelViewSet):
	queryset = mymodel.objects.all()
	serializer_class = mymodel_serializer

