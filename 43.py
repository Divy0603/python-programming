x=int(input("enter the number: "))
old=x
sum=0
while(x>0):
    rem=x%10
    sum=sum*10+rem
    x=x//10
    
print(sum)
if(sum==old):
    print("palindrome")
