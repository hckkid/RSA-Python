def trnctr(q):
    temp=len(q)
    while(temp>0):
        if(q[temp-1]==0):
            q[temp-1:]=[]
            temp=len(q)
        else:
            break
    return q
