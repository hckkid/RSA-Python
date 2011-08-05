from fun_numarr import *
from fun_division import *
from fun_reverse import *
from fun_modulus import *
from fun_compare import *
from fun_power import *
from fun_add import *
from fun_subtract import *
def getsign(num):
    [sgn,val]=num
    return sgn
def getval(num):
    [sgn,val]=num
    return val
def invertsign(num):
    [sgn,val]=num
    if(sgn=='+'):
        num=['-',val]
    else:
        num=['+',val]
    return num
def addnum(num1,num2):
    if(getsign(num1)==getsign(num2)):
        return [getsign(num1),trnctr(add(getval(num1),getval(num2)))]
    elif(isgreater(getval(num1),getval(num2))):
        return [getsign(num1),trnctr(subtract(getval(num1),getval(num2)))]
    else:
        return [getsign(num2),trnctr(subtract(getval(num2),getval(num1)))]
def subtractnum(num1,num2):
    return addnum(num1,invertsign(num2))
def multiplynum(num1,num2):
    return getarr(getnum(num1)*getnum(num2))
def divisionnum(num1,num2):
    if(getsign(num1)==getsign(num2)):
        return ['+',trnctr(division(getval(num1),getval(num2)))]
    else:
        return ['-',trnctr(division(getval(num1),getval(num2)))]
def modulusnum(num1,num2):
    if(getsign(num1)=='+'):
        return ['+',trnctr(modulus(getval(num1),getval(num2)))]
    elif(getsign(num1)=='-'):
        val=getval(num1)
        return ['+',trnctr(subtract(getval(num2),modulus(getval(num1),getval(num2))))]
def powernum(num1,num2):
    if(getsign(num2)=='-'):
        raise Exception("Negative power")
    elif(modulus(getval(num2),[2])==[1]):
        return [getsign(num1),trnctr(power(getval(num1),getval(num2)))]
    else:
        return ['+',trnctr(power(getval(num1),getval(num2)))]
