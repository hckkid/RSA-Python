import time
from fun_nums import *
from fun_compare import *
from fun_numarr import *
def powmoditer(t,xseq,p,b):
    if(b>0):
        if(b%2==1):
            r=powmoditer((((t%p)*xseq)%p),((xseq*xseq)%p),p,b/2)
        else:
            r=powmoditer(((t%p)%p),((xseq*xseq)%p),p,b/2)
    else:
        r=t
    return r
def pow_mod(a,p,b):
    x=powmoditer(1,a,p,b)
    return x
