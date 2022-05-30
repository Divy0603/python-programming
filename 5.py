x=int(input("enter the number"))
d={}
for i in range(x):
  a=int(input())
  b=int(input())
  d.update({a:b})
print(d)
d.clear()
print(d)
