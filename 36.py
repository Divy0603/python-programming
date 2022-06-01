def revsrse(str1):
  rstr1=' '
  index=len(str1)
  while index>0:
    rstr1+=str1[index-1]
    index=index-1
  return rstr1
print(reverse('1234abcd'))
