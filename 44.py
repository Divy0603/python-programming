from math import factorial


x=int(input("enter the number: "))
old=x
sum=0
while(x>0):
    rem=x%10
    sum=sum+factorial(rem)
    x=x//10
if(sum==old):
    print("strong number")
else:
    print("no")
