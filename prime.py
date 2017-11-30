for n in range(1,10):
    for i in range(2,n-1):
        if(n%i==0):
           break
        else:
            print(n)
            break
