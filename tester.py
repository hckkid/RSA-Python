from fun_powmod import *
import time
t1=time.clock()
p=multiply([121331,121233],[121323,232321])
t2=time.clock()
q=division(p,[121323,232321])
t3=time.clock()
print p
print q
print (t2-t1)*1000
print (t3-t2)*1000
