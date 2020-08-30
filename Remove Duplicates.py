inp = list(input())
# print(inp)
ans=[]
for i in range(int(len(inp))):
    if(inp[i] not in ans):
        ans.append(inp[i])
        answer = ans
print(''.join(answer))
