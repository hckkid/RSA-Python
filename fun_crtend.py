from fun_randnum import *
from fun_primegen import *
from fun_numarr import *
from fun_euclid import *
def create_e_n_d(m):
    temp=getnum(m)
    e=['+',[random.randint(11,99)]]
    while(not(isprime(e[1][0]))):
        e=['+',[random.randint(11,99)]]
    te=getnum(e)
    while(not(getval(extended_euclid(getarr(te),getarr(temp))[0])==[1])):
        e=['+',[random.randint(11,99)]]
        while(not(isprime(e[1][0]))):
            e=['+',[random.randint(11,99)]]
        te=getnum(e)
    d=multiplicative_inverse(getarr(te),getarr(temp))
    return [getarr(te),d]
