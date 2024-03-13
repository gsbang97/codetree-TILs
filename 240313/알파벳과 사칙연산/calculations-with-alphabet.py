import sys
strings = '+'+input()
alpha = {
    'a' : None,
    'b' : None,
    'c' : None,
    'd' : None,
    'e' : None,
    'f' : None,
    'g' : None
}
max_value = -sys.maxsize
def calc(value,s):
    global max_value
    if len(s) == 0:
        max_value = max(max_value, value)
        return
    operator = s[0]
    right = s[1]
    if alpha[right] == None:
        for i in range(1,5):
            alpha[right] = i
            if operator == '+':
                calc(value+i,s[2:])
            if operator == '-':
                calc(value-i,s[2:])
            if operator == '*':
                calc(value*i,s[2:])
            alpha[right] = None
    else:
        i = alpha[right]
        if operator == '+':
            calc(value+i,s[2:])
        if operator == '-':
            calc(value-i,s[2:])
        if operator == '*':
            calc(value*i,s[2:])
    

if len(strings) == 1:
    print(4)
else:
    calc(0,strings)
    print(max_value)