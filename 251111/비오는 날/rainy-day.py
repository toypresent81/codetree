n = int(input())
date = []
day = []
weather = []

class Data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

datas = []
for _ in range(n):
    d, dy, w = input().split()
    data = Data(d, dy, w)
    datas.append(data)

rain_datas = [data for data in datas if data.weather == "Rain"]

if rain_datas:
    fast_data = rain_datas[0]
    for data in rain_datas:
        if data.date < fast_data.date: 
            fast_data = data
    
    print(f"{fast_data.date} {fast_data.day} {fast_data.weather}")