x=int(input("enter the number: "))
old=x
sum=0
while(x!=0):
    rem=x%10
    sum=sum+rem
    x=x//10
if(sum*sum==old):
    print("neon number")
