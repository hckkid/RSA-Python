def add(l1,l2):
    carry=0
    q=[]
    n1=len(l1)
    n2=len(l2)
    i=0
    if(n1<n2):
        q=add(l2,l1)
    else:
        #INV: 0 <= i <= n1
        while(i<n1):
            if(i<n2):
                if(l1[i]+l2[i]+carry>999999):
                    q.append(l1[i]+l2[i]+carry-1000000)
                    carry=1
                    i=i+1
                else:
                    q.append(l1[i]+l2[i]+carry)
                    carry=0
                    i=i+1
            else:
                if(l1[i]+carry>999999):
                    q.append(l1[i]+carry-1000000)
                    carry=1
                    i=i+1
                else:
                    q.append(l1[i]+carry)
                    carry=0
                    i=i+1
        if(carry==1):
            q.append(1)
    return q
