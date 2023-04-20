from django.urls import path,include
from .views import *
urlpatterns=[
    path('insert',addauthor,name='addauthorname'),
    path('',list,name='listauthorname')
]