from fun_compare import isgreater,islesser,isequal
from fun_add import add
from fun_subtract import subtract
from fun_truncator import trnctr
from fun_multiply import multiply
from fun_reverse import reverse
def no_of_digits(p):
    i=0
    if(len(p)==0):
        i=6
    else:
        while(i<=6):
            if(p[len(p)-1]<pow(10,i)):
                break
            else:
                i=i+1
    return (6*(len(p)-1)+i)
def bsearch(l,r,p,q):
    temp1=p[:]
    temp2=q[:]
    m=(l+r)/2
    if(isgreater(p,multiply([r],q))):
        return [r]
    elif(isequal(p,multiply([r],q))):
        return [r]
    elif(l-r==1):
        return [l]
    elif(isequal(p,multiply([l],q))):
        return [l]
    elif(isgreater(multiply([l+1],q),p)):
        return [l]
    elif(isequal(multiply([m],q),p)):
        return [m]
    elif(isgreater(multiply([m],q),p)):
        return bsearch(l,m,p,q)
    else:
        return bsearch(m,r,p,q)
def smalldiv(p,q):
    tmp1=p[:]
    tmp2=q[:]
    diff=no_of_digits(tmp1)-no_of_digits(tmp2)
    if(diff<=0):
        return bsearch(0,9,tmp1,tmp2)
    elif(diff==6):
        return bsearch(100000,999999,tmp1,tmp2)
    else:
        return bsearch(pow(10,diff-1),pow(10,diff+1)-1,tmp1,tmp2)
def division(p,q):
    r=[]
    m=len(p)
    n=len(q)
    if(islesser(p,q)):
        r=[]
    else:
        i=m-n
        rest=p[0:i]
        temp=p[i:m]
        while(i>0):
            rest=p[0:i]
            x=smalldiv(temp,q)
            r[0:0]=x
            temp=trnctr(subtract(trnctr(temp),trnctr(multiply(x,q))))
            temp[0:0]=[rest[i-1]]
            rest[i-1:]=[]
            i=i-1
        x=smalldiv(temp,q)
        r[0:0]=x
    r=trnctr(r)
    return r
