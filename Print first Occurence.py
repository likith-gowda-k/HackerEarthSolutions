for _ in range(int(input())):
    arr = list(input())
    sol = []
    for i in range(int(len(arr))):
        if(arr[i] not in sol):
            sol.append(arr[i])
    print(''.join(sol))
                
