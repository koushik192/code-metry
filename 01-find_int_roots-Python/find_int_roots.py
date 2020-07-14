# Write the function bonusFindIntRoots(a,b,c) that takes 
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that 
# the roots are all integers. Your function should return these 2 int roots 
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

import math
def fun_find_int_roots(a, b, c):
        d=(b**2)-(4*a*c)
        s1=((-b-math.sqrt(d))/(2*a))
        s2=((-b+math.sqrt(d))/(2*a))
        if(s1>s2):
            return int(s1),int(s2)
        else:
            temp = s1
            s1=s2
            s2=temp
	return s1,s2

print (fun_find_int_roots(1,-5,6))


