import random
from fun_nums import *
def randnumgen(n):
    i=0
    p=[]
    while(i<n-1):
        p.append(random.randint(0,999999))
        i=i+1
    p.append(random.randint(1,999999))
    return p
