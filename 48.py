x=int(input())
sp=x-1
next=0
for i in range(1,x+1):
    print(" "*sp+"*"*i+"*"*next)
    sp-=1
    next+=1
