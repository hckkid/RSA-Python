from fun_nums import *
from fun_numarr import *
from fun_compare import *
from fun_randnum import *
def powmoditer(t,xseq,tp,tb):
    r=['+',[]]
    txseq=getnum(xseq)
    ttp=getnum(tp)
    ttb=getnum(tb)
    tt=getnum(t)
    if(getarr(tt)[1]==[]):
        r=getarr(tt)
    elif(getarr(txseq)[1]==[1]):
        r=getarr(tt)
    elif(len(getval(getarr(ttb)))>0):
        if(modulusnum(getarr(ttb),['+',[2]])==['+',[1]]):
            r=powmoditer(modulusnum(multiplynum(modulusnum(getarr(tt),getarr(ttp)),getarr(txseq)),getarr(ttp)),modulusnum(multiplynum(getarr(txseq),getarr(txseq)),getarr(ttp)),getarr(ttp),divisionnum(getarr(ttb),['+',[2]]))
        else:
            r=powmoditer(getarr(tt),modulusnum(multiplynum(getarr(txseq),getarr(txseq)),getarr(ttp)),getarr(ttp),divisionnum(getarr(ttb),['+',[2]]))
    else:
        r=getarr(tt)
    return r
def pow_mod(a,p,b):
    ta=getnum(a)
    tp=getnum(p)
    tb=getnum(b)
    return powmoditer(['+',[1]],getarr(ta),getarr(tp),getarr(tb))
