class Data:
    def __init__(self,t):
        date, day, wheather = t
        self._date = date
        self._day = day
        self._wheather = wheather
    def __str__(self):
        return f'{self._date} {self._day} {self._wheather}'
    def isRain(self):
        return self._wheather == 'Rain'
    def getDate(self):
        return self._date 
# n : 데이터 수
n = int(input())
# 날짜, 요일, 날씨 순
Datas = [
    Data(input().split()) for _ in range(n)
]
Datas.sort(key = lambda data : data.getDate())
for data in Datas:
    if data.isRain():
        print(data)
        break