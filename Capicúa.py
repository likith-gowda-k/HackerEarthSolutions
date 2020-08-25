t=int(input())
for i in range(t):
    num = list(input())
    rev = num[::-1]
    if (num==rev):
        print("YES")
    else:
        print("NO")
