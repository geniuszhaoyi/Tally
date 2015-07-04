import User
import ModelErrors

records_path='./Database/records'
tally_path='./Database/tallys'

def getBalance(user,tally):
    if type(user)!=User.User or type(tally)!=Tally.Tally:
        raise KeyError()
    if user.islogedin()!=1:
        raise AuthDeniedError
    
    f=open(tally_path)
    ls=f.readlines()
    f.close()
    
    name=user.getName()
    
    for l in ls:
        x=l.split(':')
        if tally==x[0]:
            return float(x[2])
    
    # error
    

def checkTally():
    # 检查账单是否有错帐
