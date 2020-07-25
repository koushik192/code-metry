# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46
def istidy(n):
    if (n<10):
        return True
    else:

        while(n!=0):
            rem=(n%10)
            n=(n/10)
            prev=n%10
            if (rem>prev):
                return False
            prev = rem
        return True

def fun_nth_tidynumber(n):
    c=0
    i=1
    while(True):
        if istidy(i):
            if (c==n):
                break
            c=c+1
        i=i+1
    return(i)

fun_nth_tidynumber(0)