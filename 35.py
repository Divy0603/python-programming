import numpy as np
r=int(input("Enter no. of rows:"))
c=int(input("Enter no. of cols:"))
print("Enter the values in a  single line:)
entries=list(map(int,input().split()))
m=np.array(entries).reshape(r,c)
a=m.diagonal()
print(a)
