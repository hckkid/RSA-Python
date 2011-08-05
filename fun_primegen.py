from fun_randnum import *
from fun_numarr import *
from fun_tests import *
import time
def print_timing(func):
	def wrapper(*arg):
		t1 = time.clock()
		res = func(*arg)
		t2 = time.clock()
		print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
		return res
	return wrapper
def numgen(n):
    p=[]
    t=random.randint(1,999999)
    if(n>0):
        while((t%5==0) or (t%2==0)):
            t=random.randint(1,999999)
        p.append(t)
        i=1
        while(i<n-1):
            p.append(random.randint(0,999999))
            i=i+1
        if(n>1):
            p.append(random.randint(1,999999))
    return p
def isprime(p):
    if(ismultof3(getarr(p))):
        flag=False
    elif(ismultof7(getarr(p))):
        flag=False
    elif(ismultof11(getarr(p))):
        flag=False
    elif(ismultof13(getarr(p))):
        flag=False
    elif(ismultof17(getarr(p))):
        flag=False
    elif(ismultof19(getarr(p))):
         flag=False
    elif(ismultof23(getarr(p))):
         flag=False
    elif(fermattest(getarr(p))):
        flag=True
    else:
        flag=False
    return flag
def nprimenumgen(n):
    p=['+',numgen(n)]
    temp=getnum(p)
    if(isprime(temp)):
        return getarr(temp)
    else:
        return nprimenumgen(n)
