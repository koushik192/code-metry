# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def fun_nth_tidynumber(n):
    k=[]
    prev =10000
    for i in range(n):
        while(n!=0):
            rem=(n%10)
            n=(n/10)
            if (rem>prev):
                return False
            prev = rem
        k.append(n)
        print(k)
    for i in k:
        print(i) 

fun_nth_tidynumber(0)