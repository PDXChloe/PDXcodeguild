import random
import datetime

class RainDataRow:

    def __init__(self, date, daily_total):
        self.date = date
        self.daily_total = daily_total

    def __str__(self):
        return str(self.date) + ' ' + str(self.daily_total)



data = []
with open('sauvies_island.rain.txt', 'r') as file:
    lines = file.read().split('\n')
    for i in range(4, len(lines)):
        data_str = lines[i].split()
        if len(data_str) < 1 or data_str[1] == '-':
            continue

        date = datetime.datetime.strptime(data_str[0], '%d-%b-%Y')
        daily_total = int(data_str[1])
        rain_data_row = RainDataRow(date, daily_total)
        data.append(rain_data_row)


for data_row in data:
    print(data_row)


def average(data):
    total = 0
    for x in data:
        total += x.daily_total
    av = total / len(data)
    return av


def variance(data, av):
    total = 0
    for x in data:
        diff = x.daily_total - av
        total += diff * diff
    var = total / len(data)
    return var


av = average(data)
print(av)
print(variance(data, av))