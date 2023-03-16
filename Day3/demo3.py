i=input('enter list')
i=i.replace('[','').replace(']','').replace('"','').replace("'",'').split(',')
print(i)
"""
l='aya ali'

for index,value in enumerate(l):
    print(index,'==',value)

number=int(input('enter num'))
#[[1],[2,4]....]
for tablenumber in range(1,number+1):
    for x in range(1,tablenumber+1):
        print(x*tablenumber)
print([[x*tablenumber for x in range(1,tablenumber+1)] for tablenumber in range(1,number+1)])

x=lambda y:y+3
l=[1,2,3]
for u in l:
    print(x(u))
z=map(lambda y:y+3,l)
print(z)

def gen():

    for x in range(5):
      yield x
i=iter(gen())
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

def test(x):
    print(x+1)
z=lambda x,y:x+y
print(z(1,2))

f=open('asd.txt','r+')
#print(f.read(2))
#print('==',f.read(),'===')
f.seek(0)
f.write('$$')
print(f.readline())
print(f.readlines())

f.close()

f=open('asd.txt','w')
f.write('line3\n')
f.writelines(['line1\n','line'])
f.close()

from human import Human
from employee import Employee


aya=Human(1,'aya')
aya.Name='aya ali'
print(aya.Name)
print(aya)
emp1=Employee(1,'amrk',18000,'python developer')
print(emp1)
print(len(aya))


aya.setname('aya ali')
print(aya.getname())

emp1=Employee(1,'amrk',18000,'python developer')
emp1.speek()

#emp1.speek('fic')
Employee.makefault+=2
Human.makefault+=1

print(aya.makefault)
print(Human.makefault)
print(emp1.makefault)
print(Employee.makefault)


print(aya)
mark=Human(12,'mark')
aya.speek('arts')
mark.speek('FCI')
#Human.speek()
Human.makefaults()
Human.makefaults()
aya.mesuretem()
Human.mesuretem()
print(aya.makefault)
print(mark.makefault)
print(Human.makefault)

print(mark)
mark.id=1
mark.track='os'
aya.id=100
Human.count=1000

print(mark.count)
mark.count=5
print(mark.count)
print(aya.count)
print(Human.count)


def sum():
    print('s')

def sum(x,y):
    print('s2')

#external
#1-install
import mysql.connector
host='localhost'
user='root'
password=''
#connect
connection=mysql.connector.connect(host=host,password=password,username=user,database='test',port=3306)
#qruery
query='select * from users'
#execuate query
mycurser=connection.cursor()
res=mycurser.execute(query)
for x in res.fetchall():
    print(x)

#close
connection.close()

import re
statment='asd@yahoo.com assas asd@gmail.com'
pattern=r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
print(re.match(pattern,statment))
print(re.fullmatch(pattern,statment))
print(re.findall(pattern,statment))
print(re.search(pattern,statment))
"""