from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, SomethingViewSet
from .views import CustomerViewSet

router = routers.DefaultRouter()

router.register(r'thats_users_data', UserViewSet)
router.register(r'data_prove', SomethingViewSet)
router.register(r'customer_db_prove',CustomerViewSet)

urlpatterns = [
	path('', include(router.urls))
]
