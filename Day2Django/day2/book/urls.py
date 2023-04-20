from django.urls import path,include
from .views import *
urlpatterns=[
path('insert',insert,name='bookadd'),
path('',list,name='booklist'),
path('del/<int:id>',deleteview,name='bookdel'),
path('edit/<int:id>',editview,name='bookedit'),
]