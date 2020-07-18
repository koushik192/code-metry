# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    try:
        res=[]
        for i in range(len(m1)):
            l=[]
            for j in range(len(m1[0])):
                l.append(m1[i][j]+m2[i][j])
            res.append(l)
        return res
    except:
        return None




