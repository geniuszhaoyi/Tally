import MySQLdb

__MYSQL_USERNAME__ = 'root'
__MYSQL_PASSWORD__ = 'zy19930108'
__MYSQL_DATABASE__ = 'tally'

def execute(string):
    #print string
    conn = MySQLdb.connect('localhost','root','zy19930108','tally',charset='utf8')
    conn.autocommit(1)
    cur = conn.cursor()
    cur.execute(string)
    data=cur.fetchall()
    cur.close()
    conn.close()
    return data

if __name__=='__main__':
    conn = MySQLdb.connect('localhost','root','zy19930108','tally',charset='utf8')
    cur = conn.cursor()
    cur.execute('SELECT * FROM user')
    data=cur.fetchall()
    for i in data:
        print i
    cur.close()
    conn.close()
    
