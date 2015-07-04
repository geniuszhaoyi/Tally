import os,sys
import User
import ModelErrors

if __name__=='__main__':
    raise ModelErrors.MyError(5)
    
    name=sys.argv[1]
    pswd=sys.argv[2]
    user=User.User(name,pswd)
    print user.islogedin()
    user.login()
    print user.islogedin()
    user.logout()
    print user.islogedin()
    

