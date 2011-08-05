def isgreater(p,q):
    flag=False
    if(len(p)>0):
        if(len(p)>len(q)):
            flag=True
        elif(len(p)<len(q)):
            flag=False
        elif(p[len(p)-1]>q[len(q)-1]):
            flag=True
        elif(p[len(p)-1]<q[len(q)-1]):
            flag=False
        else:
            flag=isgreater(p[0:len(p)-1],q[0:len(q)-1])
    return flag
def islesser(p,q):
    flag=False
    if(len(p)>0):
        if(len(p)>len(q)):
            flag=False
        elif(len(p)<len(q)):
            flag=True
        elif(p[len(p)-1]>q[len(q)-1]):
            flag=False
        elif(p[len(p)-1]<q[len(q)-1]):
            flag=True
        else:
            flag=islesser(p[0:len(p)-1],q[0:len(q)-1])
    return flag
def isequal(p,q):
    if(p==q):
        return True
    else:
        return False
