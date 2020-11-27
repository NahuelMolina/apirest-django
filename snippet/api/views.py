from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User

from snippet.models import mymodel, Customer
from .serializers import UserSerializer, mymodel_serializer
from .serializers import CustomerSerializer

# Here is where the models serializers and the objects created on terms of this models, 
# are connected

class CustomerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    # we can use the next method instead of queryset
    # def get_queryset(self):
        # return self.request.user.accounts.all()


class SomethingViewSet(viewsets.ModelViewSet):
	queryset = mymodel.objects.all()
	serializer_class = mymodel_serializer

