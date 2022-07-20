from rest_framework import routers
from django.urls import path

from .views import  LoginAPIView, UserViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)

app_name = 'authentication'
urlpatterns = [

    path('users/login/', LoginAPIView.as_view()),

] + router.urls
