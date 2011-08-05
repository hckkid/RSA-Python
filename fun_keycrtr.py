from fun_primegen import *
from fun_calcnm import *
from fun_crtend import *
from fun_nums import *
import time
def print_timing(func):
	def wrapper(*arg):
		t1 = time.clock()
		res = func(*arg)
		t2 = time.clock()
		print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
		return res
	return wrapper
@print_timing
def createkeys():
    p=nprimenumgen(1)
    q=nprimenumgen(1)
    while(q==p):
        q=nprimenumgen(1)
    temp1=getnum(p)
    temp2=getnum(q)
    n=calc_n(getarr(temp1),getarr(temp2))
    m=calc_m(getarr(temp1),getarr(temp2))
    [e,d]=create_e_n_d(m)
    return [[e,n],[d,n]]
