sol = ['0','1','2','3','4','5','6','7','8','9']
for _ in range(int(input())):
    flag = 'YES'
    num = list(input())
    if(int(len(num))!=10):
        flag = 'NO'
    else:
        for i in range(int(len(num))):
            if(num[i] not in sol or num[0]=='0'):
                flag = 'NO'
    print(flag)
