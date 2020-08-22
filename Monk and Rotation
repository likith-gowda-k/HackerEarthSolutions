#Solving involves simple logic of removing spaces in input using split() function,and using function to convert every iteriable to int and performing modulus function for inputs where number of rotation is more than number itself 
testCase  = int(input())
for _ in range(testCase):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    x = k%n
    print(*(l[n-x:]+l[:n-x]))
