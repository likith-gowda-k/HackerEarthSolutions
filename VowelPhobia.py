for j in range(int(input())):
    c=0
    qus = list(input())
    vow = ['a','e','i','o','u']
    for i in range(int(len(qus))):
        if(qus[i] in vow):
            c=c+1

    print(c)
