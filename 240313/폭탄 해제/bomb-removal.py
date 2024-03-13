class Bomb:
    def __init__(self, t):
        # code, color, sec = t
        self._code, self._color, self._sec = t
    def __str__(self):
        return f'code : {self._code}\ncolor : {self._color}\nsecond : {self._sec}'

bomb = Bomb(input().split())
print(bomb)