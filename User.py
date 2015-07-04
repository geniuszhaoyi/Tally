import Model

def check_name(string):
    valid_char='zxcvbnmlkjhgfdsaqwertyuiop1234567890_,.'
    for i in range(len(string)):
        if string[i] not in valid_char: return False
    return True

class User:
    def __init__(self,name,pswd):
        if type(name)!=str or type(pswd)!=str:
            raise KeyError()
        if check_name(name.lower())!=True or check_name(pswd.lower())!=True:
            raise ValueError()
        
        self.__name=name
        self.__pswd=pswd
        self.__checked=0
        self.__roles=[]
        # self.privilege=[]
    
    def login(self):
        if self.__checked==1: return 1
        self.__roles=[]
        if Model.checkUserPswd(self.__name,self.__pswd,self.__roles)==True:
            self.__checked=1
            return 1
        else:
            self.__checked=0
            return 0
    def logout(self):
        self.__checked=0
    def islogedin(self):
        return self.__checked
    
    #def hasprivilege(self,privilege):
    def isrole(self,role):
        for r in self.__roles:
            if r==role: return True
        return False
        
    def getName(self,t=1):
        return self.__name
    
if __name__=='__main__':
    user=User('zhaoyi','zy19930108')
    user.login()
    print user.islogedin()
    
    

