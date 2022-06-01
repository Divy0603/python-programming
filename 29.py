try:
   p= open("testfile", "w")
   p.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   p.close()
