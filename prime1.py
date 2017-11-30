list=[1,3, 9 ,27]
for i in list:
    prime=True
    for j in range(2,int(i**(1/2))+1):
        if i%j==0:
            prime=False
            break
    if prime is True:
        print(i, "is a prime number")
        
