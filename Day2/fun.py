from mathoperation import *

"""
import mathoperation
print(mathoperation.pi)
mathoperation.sum(1,3)

l=[]
for x in range(1,13):
    if(x%2==0):
        l.append(x)
print(l)
print([x for x in range(1,13) if(x%2==0)])
print([ch for ch in 'aya'])

for index,value in enumerate('aya ali'):
    print(index,value)


import sys
try:
    n1=float(z('enter num1'))
    n2=float(input('enter num2'))
    res=(n1+n2)
    print(n1/n2)
except ValueError:
    print('number must be digi')
#except ZeroDivisionError:
#    print('cannt divid by zero')
except:
    print('call admin')
    print(sys.exc_info()[1])
else:
    print('else block')
    print('result=',res)
finally:
    print('thnx for using')

n1=input('enter num1')
n2=input('enter num2')
print(n1+n2)

name='global'
l=[]
def fun():
    print ('hi')

fun()
print(l)
print(name)

name='global'
def outer():
    name='outer'
    print(name)#1
    def mid():
        name='mid'
        def inner():
            nonlocal name
            print(name)#2
            name = 'inner'
        inner()
    mid()
    print('')
outer()
print(name)#3


#x=1
y=2

def mysum():
    #x=5
    def internal ():
        print(x,y)
    print(x+y)#5+2
    internal()

mysum()

def mysum():
    print(1+2)
print(mysum)
mysum()
def mysum(x,y):
    print(x+y)
print(mysum)



#'{name} sdsldj'.formate(name='aya')
def mysum(**var):
    print(var,type(var))
    res=0
    for x in var:
        res+=var[x]
    print(res)
mysum(x=1,y=100)
mysum({'x':1,'y':100})


#min(ar1g....)
def mysum(*var):
    print(var,type(var))
    res=0
    for x in var:
        res+=x
    print(res)

#mysum((1,2))
mysum(1,2.3,5,7,334)
x,y,*z=1,2,3,46,7
print(z,type(z))
#range([start=0],end,[step=1])
def mysum(y,x=1,z=10):
    print(x+y+z)
mysum(2)
mysum(1,2)
mysum(1,2,3)

#def funname(arg1,arg2):
name=2
def mysum(x,y):
    return (x+y)
#calling
mysum(1,2)
"""