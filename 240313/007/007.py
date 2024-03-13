class Secret:
    def __init__(self, t):
        code, point, time = t
        self._code = code
        self._point = point
        self._time = time
    def __str__(self):
        # print('secret code : ', self._code)
        # print('meeting point : ', self._point)
        # print('time : ', self._time)
        return f'secret code : {self._code}\nmeeting point : {self._point}\ntime : {self._time}'

secret = Secret(tuple(input().split()))

print(secret)