class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class AccessDeniedError(Exception):
    def __init__(self, value='Access Denied'):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
class AuthDeniedError(Exception):
    def __init__(self, value='Auth Denied'):
        self.value = value
    def __str__(self):
        return repr(self.value)
    

if __name__=='__main__':
    try:
        raise MyError(2*2)
    except MyError as e:
        print 'My exception occurred, value:', e.value
        
        
