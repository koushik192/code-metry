# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isprime(n):
    count =0 
    for i in range(1,(n+1)):
        if n%i==0:
            count=count+1
    if (count==2):
        return 1
    else:
        return 0 
def nthcircularprime(n):
    digit=0
    i=0
    rem=0
    sum=0
    num=int(n)
    while(i<num):
        rem=int(num%10)
        num=int(num/10)
        num=int((rem*(10**(n-1))+num))
        digit=isprime(n)
        sum=sum+digit
        i=i+1
    if (sum==n):
        print(n)
    else:
        print('fail')

nthcircularprime(29)