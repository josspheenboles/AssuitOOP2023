from human import  Human
class Employee(Human):
    def __init__(self,id,name,salary,position):
        super(Employee,self).__init__(id, name)
        #self._name='asd'
        self.salary=salary
        self.position=position
    def speek(self):
        print('my position',self.position)

    def __str__(self):
        return ('myname '+self.Name+' salar'+str(self.salary))