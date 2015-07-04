import User,Record
import ModelErrors,ModelSQL
import util

def addRecord(op,tally,change,balance,note):
    sql="INSERT INTO RECORDS (rcd_op, rcd_tally, rcd_change, rcd_balance, rcd_note) VALUES ('"+op+"','"+tally+"',"+str(change)+","+str(balance)+",'"+util.asciiEncode(note)+"');"
    data=ModelSQL.execute(sql)
    for d in data:
        print d
    data=ModelSQL.execute("UPDATE TALLYS SET tallys_balance="+str(balance)+" WHERE tallys_name='"+tally+"';")
    for d in data:
        print d

def checkUserPswd(name,pswd,roles):
#    if type(name)!=str or type(pswd)!=str:
#        raise KeyError()
    
    data=ModelSQL.execute("SELECT count(users_name) FROM USERS WHERE users_name='"+name+"' and users_pswd='"+pswd+"'; ")
    x=int(data[0][0])
    if x!=1: return False
    roles=[]
    
    return True
    
def checkTallyAccess(owner,tally,rp='11'):
    if len(rp)!=2:
        raise ValueError()

    data=ModelSQL.execute("SELECT tallys_owner, tallys_permission FROM TALLYS WHERE tallys_name='"+tally+"'; ")
    if data[0][0]==owner:
        return True
    else:
        for i in range(len(rp)):
            if rp[i]=='1' and data[0][1][i]=='0': return False
        return True

def tallyGetOwner(tally):
    if type(tally)!=str:
        raise KeyError()
    
    sql="SELECT tallys_owner FROM TALLYS WHERE tallys_name='"+tally+"';"
    data=ModelSQL.execute(sql)
    if len(data)==1: return data[0][0]

def getBalance(tally):
    sql="SELECT tallys_balance FROM TALLYS WHERE tallys_name='"+tally+"'; "
    data=ModelSQL.execute(sql)
    
    return data[0][0]
    #x=data[0][0].split('.')
    #return int(x[0])*100+int(x[1])
    
def getRecord(tally, lower=None, upper=None, op=None):
    sql="SELECT rcd_timestamp,rcd_op,rcd_tally,rcd_change,rcd_balance,rcd_note FROM RECORDS WHERE 1=1   "
    if lower!=None: sql+=" and rcd_timestamp>="+str(lower)
    if upper!=None: sql+=" and rcd_timestamp<="+str(upper)
    if tally!=None: sql+=" and rcd_tally='"+str(tally)+"'"
    if op!=None: sql+=" and rcd_op='"+str(op)+"'"
    data=ModelSQL.execute(sql)
    ans=[]
    for d in data:
        record=Record.Record(d[3],util.asciiDecode(d[5]))
        record.timestamp=d[0]
        record.op=d[1]
        record.tally=d[2]
        record.balance=d[4]
        ans.append(record)
    
    return ans


