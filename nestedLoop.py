for i in range(2):
    print("i = ",i)
    for j in range(3):
        print("j = ",j)
    print()

print("==============")    

for i in range(3):
    for j in range(3):
        #print("i ={}, j = {}".format(i,j) , end=" ")
        if i == 0 and j == 0:
            print("x", end=" ")
        if i == 1 and j == 0:
            print("x", end=" ")
        if i == 2 and j == 0:
            print("x", end=" ")            
        if i == 2 and j == 1:
            print("x", end=" ")
        if i == 2 and j == 2:
            print("x", end=" ")                          
    print()

print("==============")        

data = [[1,2],[3,4],[3,2]]    
for i in data:
    for j in i:
        print(j)