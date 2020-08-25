for _ in range(int(input())):
    st ,m ,n = input().split()
    m = int(m)
    n = int(n)
    st = list(st)
    todo = st[m:n+1]
    todo.sort(reverse=True)
    ans = (st[:m]+todo+st[n+1:])
    listtostr = ' '.join(map(str, ans))
    print(listtostr.replace(" ",""))
