import random
print("Generating 4 random integer number between 100 and 500 divisible by 4")
for num in range(4):
print(random.randrange(100,500, 4), end=', ')
