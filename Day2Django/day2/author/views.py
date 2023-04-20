from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def list(r):
    #get all authors
    authors=Author.objects.all()
    #render list.html
    return render(r,'author/list.html',{'auth':authors})
def addauthor(r):
    if(r.method=='GET'):
        return render(r,'author/add.html')
    else:
        #create object author
        #auth1=Author(name=r.POST['authorname'])
        #auth1.save()
        Author.objects.create(name=r.POST['authorname'])
        #redirect author
        return redirect('/Author/')