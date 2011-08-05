from fun_randnum import *
import random
from fun_modulus import *
from fun_euclid import *
from fun_powmod import *
from fun_numarr import *
def coprimenumgen(p,n):
    flag=True
    tp=getnum(p)
    while(flag):
        a=['+',randnumgen(n)]
        ta=getnum(a)
        if(extended_euclid(getarr(tp),getarr(ta))[0][1]==[1]):
            flag=False
        a=getarr(ta)
    return a
def fermattest(p):
    flag=True
    temp1=getnum(p)
    p=getarr(temp1)
    i=0
    while((flag==True) and (i<1)):
        temp=[[2],[4],[5],[7],[11],[13]]
        a=['+',temp[i]]
        temp2=getnum(a)
        i=i+1
        if(pow_mod(getarr(temp2),getarr(temp1),subtractnum(getarr(temp1),['+',[1]]))==['+',[1]]):
            flag=True
        else:
            flag=False
        return flag
#def ismultof2(p):
    #temp=getnum(p)
    #p=getarr(temp)
    #if((getval(getarr(temp))[0])%2==0):
        #return True
    #else:
        #return False
def ismultof3(p):
    temp=getnum(p)
    if(temp!=3):
        p=getarr(temp)
        q=getval(getarr(temp))
        tmsum=0
        while(len(q)>0):
            tmsum=(tmsum+q[0])%3
            q[0:1]=[]
        if(tmsum==0):
            return True
        else:
            return False
    else:
        p=getarr(temp)
        return False
#def ismultof5(p):
    #temp=getnum(p)
    #p=getarr(temp)
    #if(((getval(getarr(temp))[0])==0) or ((getval(getarr(temp))[0])==0)):
        #return True
    #else:
        #return False
def ismultof7(p):
    temp=getnum(p)
    if(temp!=7):
        if(modulus(getval(getarr(temp)),[7])==[]):
            return True
        else:
            return False
    else:
        return False
def ismultof11(p):
    temp=getnum(p)
    if(temp!=11):
        if(modulus(getval(getarr(temp)),[11])==[]):
            return True
        else:
            return False
    else:
        return False
def ismultof13(p):
    temp=getnum(p)
    if(temp!=13):
        if(modulus(getval(getarr(temp)),[13])==[]):
            return True
        else:
            return False
    else:
        return False
def ismultof17(p):
    temp=getnum(p)
    if(temp!=17):
        if(modulus(getval(getarr(temp)),[17])==[]):
            return True
        else:
            return False
    else:
        return False
def ismultof19(p):
    temp=getnum(p)
    if(temp!=19):
        if(modulus(getval(getarr(temp)),[19])==[]):
            return True
        else:
            return False
    else:
        return False
def ismultof23(p):
    temp=getnum(p)
    if(temp!=23):
        if(modulus(getval(getarr(temp)),[23])==[]):
            return True
        else:
            return False
    else:
        return False
