
x=int(input("enter the number: "))
old=x
sum=0
while(x>0):
    k=x%10
    sum=sum+(k*k*k)
    x=x//10
if(sum==old):
    print("armstrong")
else:
    print("not armstrong")
