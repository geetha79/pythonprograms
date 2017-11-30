import random
print("its ur turn press y or n")
a=input("enter y to roll")
if a=='y':
	r=(random.randint(1,6))
	print(r)
if (r==6):
	print("congratulations you got 6!!!!!")
elif r=2:
	count=count+r
	print(count)