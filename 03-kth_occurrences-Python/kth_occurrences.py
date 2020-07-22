# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
    s=s.strip()
    if len(s)==1:
        return s
    else:
        m=[]
        for i in s:
            if(s.count(i),i)not in m and i!='':
                m.append((s.count(i),i)) 
        m.sort(key=lambda x:x[0],reverse=True)
        try:
            return m[n-1][1]
        except:
            return m[0][1]

fun_kth_occurrences("helllo woorld",1)