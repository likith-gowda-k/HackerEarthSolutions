word = list(input())
rev = word[::-1]
wordlen = int(len(word))
vow = ['a','e','i','o','u']
c = 0
for i in range(wordlen):
    if(word[i]==rev[i] and word[i]in vow):
        c=c+1
print(c)
