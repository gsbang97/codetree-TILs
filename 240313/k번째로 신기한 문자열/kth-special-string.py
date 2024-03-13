n,k,T = input().split()
T = list(T)
length = len(T)
n,k = int(n), int(k)
words = []
for i in range(n):
    word = list(input())
    isSame = True
    for j in range(length):
        if word[j] != T[j]:
            isSame = False
            break
    if isSame:
        words.append(word)
words.sort()
print(''.join(words[k-1]))