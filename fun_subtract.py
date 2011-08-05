from fun_truncator import *
from fun_compare import *
def subtract(l1,l2):
    borrow=0
    q=[]
    i=0
    if(islesser(l1,l2)):
        raise Exception('Subtraction Error')
    else:
        #INV: 0 <= i <= n1
        n1=len(l1)
        n2=len(l2)
        while(i<n1):
            if(i<n2):
                if(l1[i]<l2[i]+borrow):
                    q.append(1000000+l1[i]-l2[i]-borrow)
                    borrow=1
                    i=i+1
                else:
                    q.append(l1[i]-l2[i]-borrow)
                    borrow=0
                    i=i+1
            else:
                if(l1[i]<borrow):
                    q.append(1000000+l1[i]-borrow)
                    borrow=1
                    i=i+1
                else:
                    q.append(l1[i]-borrow)
                    borrow=0
                    i=i+1
        if(borrow>0):
            raise Exception('Subtraction Error')
        else:
            return q
