'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
m = int(input())
for _ in range(n):
    numc=0
    namc=""
    for i in range(m):
        nam,num=input().split()
        c = 0
        for j in range(len(num)):
            if(num[j]==','):
                c=c+1
            if(c>=numc):
                numc=c
                namc=nam
    print(namc,numc)

