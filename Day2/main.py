x=4
y=5
x=y
x=56
print(x,y)
"""
front={
    '1':'react',
    '20':'ang'
}
back={
    '1':'python',
    '2':'java',
    '3':'c'
}

#print(front+back)
#print(front*2)
back.update(front)
#front.update(back)
print(front)
print(back)

trainee=    {
    'id':1,
    'name':'aya ali',
    'track':'os',
    'course':['python','c','c++'],
    'grade':(100,100,50),
    'cgrade':{
        'python':90,
        'c':100,
        'c++':50
    },


}
for x in trainee.keys():
    print(x,trainee[x])
print( trainee.keys())
print(trainee.values())
print(trainee.items())

l=[1,2.1,'one']
for x in l:
    print(x,type(x))

print(trainee['grade'])
trainee['id']=10
trainee['grade']=''
trainee['plpal']='plplap'
print(trainee['cgrade']['python'])
print(trainee['course'][0])
print(trainee,type(trainee))
d=trainee.copy()
d['id']=1000
print(d)
print(trainee)

x,*y=1,2,3
print(x,y)

t=(1,'one')
x,y=t
x=2
print(x,y)

front='react','ang.'
back='python','java','php'
print(front+back)
print(front*2)

number=1
number='one'
t=1,2,3,5
t=1

#tuple
t=1,1.1,True,'one',[3,4],(5,6),{}
print(t,type(t))
t=1,
print(t,type(t))

#t[0]='plpalpa'
t[4][0]='ssdsd'
print(t)

front=['react','ang']
back=front.copy()
back[0]='plpa'
back.clear()
print(back)

#list collection of values different datatypes
front=['react','ang']
back=front.copy()
print(front,back)
back.clear()
back.append('plplpl')
print(front,back)

back=(front+back)
print(front*2)
#back.extend(front)
print(back)
print(front)


techi=[]

techi.extend(back)
print(techi.count('java'))
print(techi)
l=['',1.1,True,'']
l.append(['one',3])
l.insert(0,1)
#l.pop(1)
l.remove('')
print(l)

l[0]='one'
l[0]=''
#l[3]='plplp'

print(l)

print(l[-1])
print(l[1:2])

print(type(l),l)
print(l[3])
print(len(l))
"""