name='aya ali'
for x in enumerate(name):
   if(x[0]<=3):
    print(x)
'''
name='aya ali'
print('h' in name)
print(len(name))

x=1
y='one'
temp=x
x=y
y=temp
print(x,y)
x,y=y,x
print(x,y)

#var1,var2=val1,val2
x,y=1,'one'
print(x,y)


statnment='name:{name} {track} {branch} {name}'
print(statnment.format(branch='assuit',track='os',name='merna'))
print(statnment)

statnment='name:{} {} {}'
print(statnment.format('merna','os','assuit'))
print(statnment.format('SD','ebra','assuit'))

name='aya ali sayed'
print(name.replace('a','@'))
print(name)
print(name.split('a'))
print(name.count('a'))
print(name.find('a'))

num=input('enter num')
print(num,int(num))

name='aya ali'
print(name)
print(name[6],name[-1])
print(name[0:3],'asasasasas')#[start:end:step]
print(name[:5])
print(name[1:])
print(name[::-1])

print('asd'+str(1))
print(1*1)
print('asd '*2)

if True:
    print('True')

for x in range(10):
    if(x==5):
        break
    print(x,end=' ')
else:
    print('all for done')


name='ahmed'
for x in enumerate(name):#(inde,value)
    print(x[0],x[1])

index=0
for ch in name:
    print(ch,index)
    index+=1

#range([start=0],end,[step=1])
r=range(1,5,2)#[1,3]
print(r,type(r))
for x in range(1,13):
    print(x,end=' ')
print('sta1',1,1.1,sep='&',end=' ')
print('asas')
print('aasd')

range(1,5)
range(5)#[0,1,2,3,4]

name='ali'
print(name)
#for varname in collection
for ch in name:
    print(ch)

x=2

if(x==1):
    print('one')
elif (x==2):
    
    print('two')


elif x==3:
    print('three')
else:
    print('other')

if(x==1):
    print('one')
else:
    if(x==2):
        print('two')
    elif(x==3):
        print('three')
    else:
        print('other')

#and or not
print('' and 1 and 'asd','===')
print(2==True)

print(1==True)
print('1'==True)
'''