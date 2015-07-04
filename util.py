
def asciiEncode(string):
    if type(string)!=str: raise ValueError
    
    ans=''
    for c in string:
        ans=ans+str(ord(c))+'.'
        
    return ans
    
def asciiDecode(string):
#    print '|'+string+'|'
    xs=string.split('.')
    
    ans=''
    for x in xs[:-1]:
#        print x
        ans=ans+chr(int(x))
    
    return ans
    


