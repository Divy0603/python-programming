def calculator(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    p=a,b,c,d
    return p
x=int(input())
y=int(input())
print(calculator(x,y))
