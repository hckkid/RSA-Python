import fun_add
import fun_subtract
import fun_partition
from fun_truncator import *
partition=fun_partition.partition
add=fun_add.add
subtract=fun_subtract.subtract
#def normalize(p):
#    i=0
#    while(i<len(p)-1):
#        if(p[i]<0):
#            p[i]=p[i]+1000000
#            p[i+1]=p[i+1]-1
#        i=i+1
#    return trnctr(p)
def nmultiply(p,q):
    r=[]
    m=len(p)/2
    n=len(q)/2
    if(len(p)==0 or len(q)==0):
        r=[]
    elif(m>0 and n>0):
        k=min(n,m)
        [p1,p2]=partition(p,k)
        [q1,q2]=partition(q,k)
        l1=multiply(add(p2,p1),add(q2,q1))
        l2=multiply(p2,q2)
        l3=multiply(p1,q1)
        tl1=l1[:]
        tl2=l2[:]
        tl3=l3[:]
        t1=subtract(l1,l2)
        t2=subtract(t1,l3)
        l4=t2
        while(len(l2)<k):
            l2.append(0)
        while(len(l3)<k):
            l3.append(0)
        while(len(l4)<k):
            l4.append(0)
        if(len(l3)>k):
            carry1=l3[k:]
            l3=l3[0:k]
            l4=add(l4,carry1)
            if(len(l4)>k):
                carry2=l4[k:]
                l4=l4[0:k]
                l2=add(l2,carry2)
        elif(len(l4)>k):
            carry2=l4[k:]
            l4=l4[0:k]
            l2=add(l2,carry2)
        r[0:0]=l2
        r[0:0]=l4
        r[0:0]=l3
    elif(m==0 and n>0):
        [q1,q2]=partition(q,n)
        l1=multiply(p,q1)
        l2=multiply(p,q2)
        if(len(l1)>n):
            carry1=l1[n:]
            l1=l1[0:n]
            l2=add(l2,carry1)
        r[0:0]=l2
        r[0:0]=l1
    elif(m>0 and n==0):
        [p1,p2]=partition(p,m)
        l1=multiply(p1,q)
        l2=multiply(p2,q)
        if(len(l1)>m):
            carry1=l1[m:]
            l1=l1[0:m]
            l2=add(l2,carry1)
        r[0:0]=l2
        r[0:0]=l1
    else:
        x=q[0]*p[0]
        if(x>999999):
            r[0:0]=[(x%1000000),(x/1000000)]
        else:
            r[0:0]=[x]
    while(len(r)<len(p)+len(q)-1):
        r.append(0)
    return r
def multiply(a,b):
    t1=a[:]
    t2=b[:]
    n1=len(t1)
    n2=len(t2)
    i=0
    carry=0
    temp3=[]
    while(i<n1):
        temp4=[]
        j=0
        k=0
        while(k<i):
            temp4.append(0)
            k=k+1
        while(j<n2):
            temp4.append((t1[i]*t2[j]+carry)%1000000)
            carry=(t1[i]*t2[j]+carry)/1000000
            j=j+1
        if(carry>0):
            temp4.append(carry)
            carry=0
        temp3=add(temp3,temp4)
        i=i+1
    return temp3
