
users_path='./Database/users'
roles_path='./Database/roles'

def check(name,pswd,roles):
    f=open(users_path)
    ls=f.readlines()
    f.close()
    
    for l in ls:
        x=l.split(':')
        if x[0]==name and x[1]==pswd:
            roles=x[2].split('-')
            return True
            
    return False
    

