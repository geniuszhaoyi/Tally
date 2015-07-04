import User
import ModelRecord

class Record:
    def __init__(self,user,change,timestamp,note):
        if type(user)!=User.User or (type(change)!=int and type(change)!=float) or type(timestamp)!=int or type(note)!=str:
            raise KeyError()
        
        self.__added=0
    
    def add():
        if self.__added==1:
            raise ValueError()
        
        if user.islogedin()==1 and user.isrole('users')==True:
            ModelRecord.add(user,change,timestamp,note)
        
        self.__added=1
    
    


