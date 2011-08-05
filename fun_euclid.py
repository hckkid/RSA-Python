from fun_nums import *
from fun_numarr import *
def extended_euclid(p,q):
    if(getval(q)==[]):
        return [p,['+',[1]],q]
    else:
        temp=getnum(q)
        temp2=getnum(p)
        m=divisionnum(getarr(temp2),getarr(temp))
        n=modulusnum(getarr(temp2),getarr(temp))
        [g,u,v]=extended_euclid(getarr(temp),n)
        temp3=getnum(v)
        return [g,getarr(temp3),subtractnum(getarr(getnum(u)),multiplynum(getarr(getnum(m)),getarr(temp3)))]
def multiplicative_inverse(e,m):
    tm=getnum(m)
    [g,x,y]=extended_euclid(e,getarr(tm))
    if(not(getval(g)==[1])):
        return ['+',[]]
    else:
        return modulusnum(x,getarr(tm))
