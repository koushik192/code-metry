# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

def isevenpositiveint(x):
        if(x%2==0) & (x>0):
            return True
        elif(isinstance(x,int)==True):
            return True
        elif(isinstance(x,list)==True):
            return False
        elif(isinstance(x,tuple)==True):
            return False
        else:
            return False
