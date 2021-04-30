denominations = [1, 2, 5]
amount = 7
solution=[0]*(amount+1)
solution[0]=1
for den in denominations:
    for i in range(den, amount + 1):
        solution[i] += solution[i - den] 
print(solution[len(solution) - 1])
    
