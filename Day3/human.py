class Human:
    #class variable
    #count=0
    makefault=0
    '''
    def __init__(self,id,name):
        print('iam const111.')
    '''
    def __init__(self,id,name):
        self.id=id
        self.__name=name
        print('iam constr.')
    def speek(self,faculty):
        print('iam '+self.name+' graduated from '+faculty)
    @classmethod
    def makefaults(s):
        s.makefault+=1
    #@staticmethod
    def mesuretem(self,temp):
        print('etst')
    def setname(self,newname):
        self.__name=newname
    def getname(self):
        return self.__name
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,newname):
        self.__name=newname
    def __str__(self):
        return 'my name:'+self.__name
    def __len__(self):
        return len(self.__name)