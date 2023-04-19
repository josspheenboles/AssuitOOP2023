from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
# Create your views here.
#controllers
#view method input http request object
def getbook(r,id):
    return HttpResponse('<h1>'+str(id)+'<h1>')

def home(req):
    if(req.method=='GET'):
        res= HttpResponse('home view')
        res.write('<h1>Day1<h1>')
        res['content-type']='text/plain'
        res.set_cookie('id',1)
        return res
    else:
        return HttpResponse('access denied')

def login (r):
    if(r.method=='GET'):

        return render(r,'book/login.html')
    else:
        print(r.POST['username'])
        print(r.POST['pass'])
        return HttpResponseRedirect('/Book/home1')

def jsonres(req):
    return JsonResponse({'id':1,'name':'add'})