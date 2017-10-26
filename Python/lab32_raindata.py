import random
import datetime
import matplotlib.pyplot as plt

class RainDataRow: #made a class but.....didn't really have to

    def __init__(self, date, daily_total):
        self.date = date
        self.daily_total = daily_total

    def __str__(self):
        return str(self.date) + ' ' + str(self.daily_total)


data = []
with open('sauvies_island.rain.txt', 'r') as file:
    lines = file.read().split('\n')
    for i in range(4, len(lines)): #scrubing some data, taking out the top four lines
        data_str = lines[i].split()
        if len(data_str) < 1 or data_str[1] == '-': #getting rid of all the dashes
            continue

        date = datetime.datetime.strptime(data_str[0], '%d-%b-%Y') #using datetime module to get usable dates
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
        total += (diff * diff)
    var = total / (len(data))
    return var

#graph your data
av = average(data)
print(av)
print(variance(data, av))

x_values = []
y_values = []

for data_row in data: #graph it by the year
    if data_row.date.year == 2012:
        x_values.append(data_row.date)
        y_values.append(data_row.daily_total)


plt.plot(x_values, y_values, 'ro') #using matplotlib module


plt.show() #calling it1