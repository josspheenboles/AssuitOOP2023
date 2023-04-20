from django.shortcuts import render
def home(r):
    context={}
    context['id']=1
    context['authors']=[
        {
            'id':10,
            'name':'hi\nos'
        }
    ,    {
            'id':20
        }
    ]
    return render(r,'author/list.html',context)