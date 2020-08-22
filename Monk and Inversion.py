




#This problem invles 4 loops to since we have to check condition of inversion 
test = int(input())
#Fetching Input for number of test cases 
for _ in range(test):#looping on number of test cases
    n = int(input())
    matrix = []#creating matrix
    for i in range(n):#looping over inputs and appending them to matrix 
      a = list(map(int,input().split()))
      matrix.append(a)

    c=0#Creating temp variable
#looping over each position of matrix with condition ro find number of inversion
    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if i<=p and j<=q:
                        if matrix[i][j]>matrix[p][q]:
                            c+=1
    print(c)
