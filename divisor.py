n=int(input("please enter a number to divide:"))
ListRange=range(1,n+1)
divisorList=[]
for i in ListRange:
    if(n%i==0):
        divisorList.append(i)
for j in divisorList:
    print(j)
print("number of divisor=",len(divisorList))
print(divisorList)

print("the prime number divisors among the list are:")
a=[]
for j in divisorList:
    prime=True
    for i in range(2,int(j**(1/2))+1):
            if(j>1):
                if (j%i)==0:
                    prime=False
                    break
    if prime is True:
        a.append(j)
print("number of prime numbers in the list",len(a))
print(a)
            
