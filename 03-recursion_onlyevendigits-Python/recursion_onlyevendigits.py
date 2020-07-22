# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l): 
    return even(L,[],0)

def even(L,a,i):
    if len(L)==0:
        return a
    else:
        li=list(str(L[i]))
        li=list(map(int,li))
        l2=[]
        for j in li:
            if j%2==0:
                l2.append(j)
        l2=list(map(str,l2))
        l2="".join(l2)
        if(len(l2)==0):
            a.append(0)
        elif(int(l2)%2==0):
            a.append(int(l2))
        i=i+1
        return even(L,a,i)


