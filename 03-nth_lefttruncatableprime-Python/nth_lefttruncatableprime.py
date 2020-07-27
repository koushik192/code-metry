# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math
def isprime(x):
    if x<=1:
        return False
    else:
        for i in range(2,(x//2)+1):
            if x%i==0:
                return False
        return True
    
def isprimeatruk(x):
    if '0' in str(x):
        return False
    while (len(str(x))>1):
        i=int(str(x)[1:])
        if isprime(x)==False:
            return False
    return True

        
def fun_nth_lefttruncatableprime(n):
    i=2
    while(n>=0):
        if (len(str(i))>=1 and isprimeatruk(i)and isprime(i)):
            n=n-1
        i=i+1
    return i-1