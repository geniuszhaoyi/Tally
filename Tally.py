import User, Record
import ModelErrors, ModelSQL, Model
import plugin

class Tally:
    def __init__(self,user,tally):
#        if type(user)!=User.User or type(tally)!=str:
#            raise KeyError('User.User and str REQUIRED ('+str(type(user))+', '+str(type(tally))+' GIVEN)')
        if user.islogedin()!=1:
            raise ModelErrors.AuthDeniedError()
        if Model.checkTallyAccess(user.getName(),tally)!=True:
            raise ModelErrors.AccessDeniedError()
        
        owner=Model.tallyGetOwner(tally)
        if owner==None:
            raise ValueError()
        
        self.__owner=owner
        self.__user=user
        self.__tallyName=tally
        self.__records=None
        self.__balance=Model.getBalance(self.__tallyName)
        
    def getUser(self):
        return self.__user
    def getTallyName(self):
        return self.__tallyName
        
    def resetRecord(self):
        self.__records=None
    def getRecord(self,start=None,end=None):
        self.__records=Model.getRecord(self.__tallyName,start,end)
        return self.__records
    
    def getBalance(self):
        return self.__balance
    
    def addRecord(self,record):
        self.__balance=self.__balance+record.change
        Model.addRecord(op=self.__user.getName(), tally=self.__tallyName, change=record.change, note=record.note, balance=self.__balance)
        return True

if __name__=='__main__':
    user=User.User('zhaoyi','zy19930108')
    user.login()
    tally=Tally(user,'main')
    #print 'Balance:',tally.getBalance()
    #tally.addRecord(Record.Record(0.1,'test'))
    #print 'Balance:',tally.getBalance()
    for i in tally.getRecord():
        print i.timestamp,i.op,i.change,i.balance,i.note
    plugin.getChart.do(tally.getRecord())

