from fun_nums import *
from fun_truncator import *
def calc_n(p,q):
    return trnctr(multiplynum(p,q))
def calc_m(p,q):
    temp1=subtractnum(p,['+',[1]])
    temp2=subtractnum(q,['+',[1]])
    return trnctr(multiplynum(temp1,temp2))
