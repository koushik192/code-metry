# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def Lychrel(n):
    n=0
    for i in range(20):
        n=n+reverse(n)
        if (ispalindrome(n)):
            return False
    return True

def ispalindrome(n):
    return n==reverse(n)

def reverse(n):
    reverse=0
    while(n>0):
        rem=n%10
        reverse=(reverse*10)+rem
        n=int(n/10)
    return reverse
def nthlychrelnumbers(n):
	# your code goes here
    i=1
    c=0
    while c<n:
        if Lychrel(i):
            c=c+1
        i=i+1
    return(i-1)
    pass