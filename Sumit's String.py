t = int(input())
for _ in range(t):
    s = input()
    string = True
    for i in range(len(s)-1):
        if(abs(ord(s[i])-ord(s[i+1]))!=1 and abs(ord(s[i])-ord(s[i+1]))<=24):
            string = False
            break
    if string:
        print('YES')
    else:
        print('NO')
