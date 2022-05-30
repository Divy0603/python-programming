x=int(input())
sp=x-1
next=0
spa=0
nex=x-1
for i in range(1,x+1):
    print(" "*sp+"*"*i+"*"*next)
    sp-=1
    next+=1
for j in range(x,0,-1):
    print(" "*spa+"*"*j+"*"*nex)
    nex-=1
    spa+=1
