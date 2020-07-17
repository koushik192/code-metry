# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


def fun_nth_happy_number(n):
    c=[]
    happy=[]
    while(n<0):
        n=sum(int(i)**2 for i in str(n))
        if n in c:
            return False
        c.append(n)
    return True
    for i in range(n):
        if fun_nth_happy_number(i):
            happy.append(i)
        print(happy)

fun_nth_happy_number(1)
        