barkets = input()
result = 0
for idx, first in enumerate(barkets[:-1]):
    if first == '(':
        for second in barkets[idx+1:]:
            if second == ')':
                result +=1
print(result)