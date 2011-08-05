def getarr(num):
    q=[]
    if(num<0):
        sign='-'
        num=abs(num)
    else:
        sign='+'
    while(num>0):
        q.append(num%1000000)
        num=num/1000000
    return [sign,q]
def getnum(arr):
    [sign,val]=arr
    num=0
    while(len(val)>0):
        num=num*1000000+val[len(val)-1]
        val[len(val)-1:]=[]
    if(sign=='-'):
        num=0-num
    return num
