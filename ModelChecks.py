import ModelErrors

def checkTallyAccess(user,tally,ty='11'):
    ty_len=2

    if type(user)!=User.User or type(tally)!=Tally.Tally:
        raise KeyError()
    if len(ty)!=ty_len:
        raise ValueError()

    tallys_path='./Database/tallys'
    f=open(tallys_path)
    ls.f.readlines()
    f.close()
    
    for l in ls:
        x=l.split(":")
        if x[0]==tally:
            if x[1]==user.getName():
                # user is owner of tally
                return True
            else:
                # user is not the owner
                for i in range(len(ty)):
                    if ty[i]==1 and x[2][i]!=1:
                        return False
                return True
                
    return False
    
