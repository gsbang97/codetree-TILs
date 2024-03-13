n = int(input())
words = [input() for _ in range(n)]
words.sort()
for word in words:
    print(word)