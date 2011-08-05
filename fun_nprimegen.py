from fun_randnum import *
import gmpy
from fun_numarr import *
def primenumgen(n):
    p=['+',randnumgen(n)]
    temp=getnum(p)
    if(gmpy.is_prime(gmpy.mpz(temp))>0):
        return getarr(temp)
    else:
        return primenumgen(n)
