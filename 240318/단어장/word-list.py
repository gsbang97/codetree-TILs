n = int(input())
words = dict()
for _ in range(n):
    word = input()
    if word in words.keys():
        words[word] += 1
    else:
        words[word] = 1

words_keys = sorted(list(words.keys()))

for key in words_keys:
    print(key,words[key])