# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
    count =0  
    s=abs(n)
    k=0
    m=[]
    while(n!=0):
        k=n%10
        n//=10
        m.append(k)
    for q in m:
        if(q==n):
            count=count+1
            if(count==2):
                print(True)
            else:
                print(False)

hasconsecutivedigits(123)
