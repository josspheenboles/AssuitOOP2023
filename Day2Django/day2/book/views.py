from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from author.models import Author
# Create your views here.
def deleteview(r,id):
   Book.objects.filter(id=id).delete()
   context = {}
   context['books'] = Book.objects.all()
   return render(r, 'book/list.html', context)
def editview(r,id):
   if(r.method=='GET'):
      b1=Book.object.get(id=id)
      context={'book':b1}
      return render(r, 'book/add.html')
   else:
      Book.objects.filter(id=id).update(name=r.POST['bookname'])
def list(r):
   context={}
   context['books']=Book.objects.all()
   return render(r,'book/list.html',context)
def insert(r):
   #book1=Book(name='book1',authorobj=Author.objects.get(id=1))
   #book1.save()
   #Book.objects.create(name='book2',authorobj=Author.objects.get(id=2))
   if(r.method=="GET"):
      authors=Author.objects.all()
      return render(r,'book/add.html',{'authors':authors})
   else:
      Book.objects.create(
         name=r.POST['bookname'],
         authorobj=Author.objects.get(id=r.POST['authorid'])
      )
      return redirect('/Book/')