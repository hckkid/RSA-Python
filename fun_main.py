from fun_keycrtr import *
from fun_ende import *
flag=True
file_pub="pub_key.txt"
file_pri="pri_key.txt"
file_msg="msg.txt"
file_cht="cht.txt"
file_dmsg="dmsg.txt"
def getchoice():
    ch=raw_input("Wanna do again .(y/n)")
    if(ch=='y'):
        return True
    else:
        return False
def write_pub(pub):
    temp1=getnum(pub[0])
    temp2=getnum(pub[1])
    pub=[getarr(temp1),getarr(temp2)]
    fout=open(file_pub,"w")
    fout.write(str(temp1))
    fout.write(",")
    fout.write(str(temp2))
    fout.close()
def write_pri(pri):
    temp1=getnum(pri[0])
    temp2=getnum(pri[1])
    pri=[getarr(temp1),getarr(temp2)]
    fout=open(file_pri,"w")
    fout.write(str(temp1))
    fout.write(",")
    fout.write(str(temp2))
    fout.close()
def read_pub():
    fin=open(file_pub,"r")
    str1=fin.read()
    fin.close()
    str2=""
    i=0
    while(str1[i]!=',' and i<len(str1)):
        i=i+1
    str2=str1[:i]
    n1=long(str2)
    i=i+1
    str3=""
    str3=str1[i:]
    n2=long(str3)
    pub=[getarr(n1),getarr(n2)]
    return pub
def read_pri():
    fin=open(file_pri,"r")
    str1=fin.read()
    str2=""
    i=0
    while(str1[i]!=',' and i<len(str1)):
        i=i+1
    str2=str1[:i]
    n1=long(str2)
    i=i+1
    str3=""
    str3=str1[i:]
    n2=long(str3)
    pri=[getarr(n1),getarr(n2)]
    fin.close()
    return pri
def read_msg():
    fin=open(file_msg,"r")
    tmstr=fin.read()
    fin.close()
    return tmstr
def write_cht(code):
    fout=open(file_cht,"w")
    i=0
    n=len(code)
    while(i<n-1):
        fout.write(code[i])
        fout.write(",")
        i=i+1
    fout.write(code[i])
    fout.close()
def read_cht():
    fin=open(file_cht,"r")
    str1=fin.read()
    str2=[]
    i=0
    j=0
    ini=0
    while(i<len(str1)):
        if(str1[i]==","):
            str2[j:j]=[long(str1[ini:i])]
            i=i+1
            ini=i
            j=j+1
        else:
            i=i+1
    str2.append(int(str1[ini:i]))
    fin.close()
    return str2
def write_dmsg(dmsg):
    fout=open(file_dmsg,"w")
    sz_dmsg=len(dmsg)
    i=0
    while(i<sz_dmsg):
        fout.write(chr(dmsg[i]))
        i=i+1
    fout.close()
while(flag):
    flag=False
    print "1. Generate new keys "
    print "2. Encrypt a message "
    print "3. Decrypt a coded message "
    choice=input()
    if(choice==1):
        t1=time.clock()
        [x,y]=createkeys()
        pub=x
        pri=y
        e=pub[0]
        n=pub[1]
        tn=getnum(n)
        d=pri[0]
        write_pub([e,getarr(tn)])
        write_pri([d,getarr(tn)])
        t2=time.clock()
        print "time taken is "
        print (t2-t1)*1000
        flag=getchoice()
    elif(choice==2):
        t1=time.clock()
        pub=read_pub()
        te=getnum(pub[0])
        tn=getnum(pub[1])
        msg=read_msg()
        msgtc=map(ord,msg)
        cdmsg=[]
        i=0
        sz_msg=len(msgtc)
        while(i<sz_msg):
            pub=[getarr(te),getarr(tn)]
            cdmsg.append(str(getnum(encrypter(msgtc[i],pub))))
            i=i+1
        write_cht(cdmsg)
        t2=time.clock()
        print "time taken is "
        print (t2-t1)*1000
        flag=getchoice()
    elif(choice==3):
        t1=time.clock()
        pri=read_pri()
        td=getnum(pri[0])
        tn=getnum(pri[1])
        cdmsg=read_cht()
        sz_cdmsg=len(cdmsg)
        dmsg=[]
        i=0
        while(i<sz_cdmsg):
            pri=[getarr(td),getarr(tn)]
            dmsg.append(int(getnum(decrypter(cdmsg[i],pri))))
            i=i+1
        write_dmsg(dmsg)
        t2=time.clock()
        print "time taken is "
        print (t2-t1)*1000
        flag=getchoice()
    else:
        print "Wrong choice Enter again"
        flag=True
