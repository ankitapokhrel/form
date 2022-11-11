# from django.contrib import admin
# from django.urls import path
# from app import views
# from .views import *

# urlpatterns = [
#     path('', views.index, name="index"),
#     path('form/', form, name="form"),
# ]
    

from django.urls import path, include
from rest_framework import routers
from .views import FormViewSet

router = routers.DefaultRouter()
router.register('form', FormViewSet)

urlpatterns = [
    path('', include(router.urls)),
]