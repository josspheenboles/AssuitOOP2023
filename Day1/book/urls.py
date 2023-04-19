from django.urls import path
from .views import *
urlpatterns=[
    path('home1', home),
    path('', jsonres),
    path('Login/', login),
    path('<int:id>/',getbook),



]