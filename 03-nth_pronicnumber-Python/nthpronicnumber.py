# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
import math
def ispronic(x):
    i=1
    while(i<=(int)(math.sqrt(x))):
        if(x==i*(i+1)):
            return True
        i=i+1
    return False
	
    
def nthpronicnumber(n):
    i=1
    c=0
    while(c<n):
        if ispronic(i):
            c=c+1
        i=i+1
    print(i-1)

nthpronicnumber(1)