class User:
    def __init__(self, id_, level):
        self._id = id_
        self._level = level
    def __str__(self):
        return f'user {self._id} lv {self._level}'
    def setData(self, Data):
        self._id, self._level = Data

user = User('codetree', 10)
print(user)
user.setData(tuple(input().split()))
print(user)