# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math
import math
def karpekar(n):
    i=1
    while(i<=n):
       i=i*10
    return n==(n*n)//i+(n*n)%i

def fun_nth_kaprekarnumber(n):
    if n==0:
       return 1
    i=3
    count=0
    while(count<n):
        if karpekar(i):
            count=count+1
        i=i+1
    return i-1
def fun_nearestkaprekarnumber(n):
    k=[]
    for i in range(21):
        k.append(fun_nth_kaprekarnumber(i))
    for i in range(len(k)-1):
        if n>k[i] and n<k[i+1]:
            if abs(n-k[1])<=abs(n-k[i+1]):
                return k[i]
            else:
                return k[i+1]
   