x=int(input("enter no of terms"))
dict={}
for i in range(1,x+1):
    a=input("enter key")
    b=input("enter value")
    dict.update({a:b})
print(dict)
