from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, SomethingViewSet

router = routers.DefaultRouter()
router.register(r'thats_users_data', UserViewSet)
router.register(r'data_prove', SomethingViewSet)

urlpatterns = [
	path('', include(router.urls))
]
