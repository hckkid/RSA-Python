from fun_keycrtr import *
from fun_numarr import *
from fun_powmod import *
import time
def print_timing(func):
	def wrapper(*arg):
		t1 = time.clock()
		res = func(*arg)
		t2 = time.clock()
		print '%s took %0.3fms' % (func.func_name, (t2-t1)*1000.0)
		return res
	return wrapper
def encrypter(msg,pub):
    [e,n]=pub
    tn=getnum(n)
    te=getnum(e)
    pub=[getarr(te),getarr(tn)]
    return pow_mod(getarr(msg),getarr(tn),getarr(te))
def decrypter(cht,pri):
    [d,n]=pri
    tn=getnum(n)
    td=getnum(d)
    pri=[getarr(td),getarr(tn)]
    return pow_mod(getarr(cht),getarr(tn),getarr(td))
