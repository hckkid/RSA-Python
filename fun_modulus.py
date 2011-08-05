from fun_division import *
def modulus(p,q):
    if(len(division(p,q))>0):
        r=trnctr(subtract(p,trnctr(multiply(division(p,q),q))))
    else:
        r=p
    return r
