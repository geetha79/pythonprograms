divisorList=[1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200]
for j in divisorList:
    if j>1:
        for i in range(2,j):
            if (j%i)==0:
                break
            else:
                print(j)
        
