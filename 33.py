f=open("king.txt","r")
text=f.read()
a=b=0
for i in text:
  if i.islower():
    a+=1
  elif i.upper():
    b+=1
print("no. of lower case :",a)
print("no. of upper case:",b)
f.close()
