from fun_multiply import *
from fun_modulus import *
from fun_division import *
import time
def print_timing(func):
	def wrapper(*arg):
		t1 = time.clock()
		res = func(*arg)
		t2 = time.clock()
		print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
		return res
	return wrapper
def square(p):
    return multiply(p,p)
def poweriter(p,xseq,q):
    r=[]
    if(len(q)>0):
        if(modulus(q,[2])==[1]):
            r=poweriter(multiply(p,xseq),square(xseq),division(q,[2]))
        else:
            r=poweriter(p,square(xseq),division(q,[2]))
    else:
        r=p
    return r
@print_timing
def power(p,q):
    return poweriter([1],trnctr(p),trnctr(q))

