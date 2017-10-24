import random
import datetime

class RainDataRow:

    def __init__(self, date, daily_total):
        self.date = date
        self.daily_total = daily_total

    def __str__(self):
        return str(self.date) + ' ' + str(self.daily_total)

    def average(self, daily_total):
        total = 0
        for d in daily_total:
            total += d
            return total/len(daily_total)

    def variance(self, nums, average):
        total = 0
        for num in self.nums:
            diff = num - self.average
            total += diff * diff

        return total/len(nums)

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

print(rain_data_row.average(daily_total))
# nums = []
# for i in range(100):
#     nums.append(random.randint(0, 100))
#
#
# def average(nums):
#     total = 0
#     for num in nums:
#         total += num
#         return total/len(num)
#
# def variance(nums, average):
#     total = 0
#     for num in nums:
#         diff = num - average
#         total += diff*diff
#
#     return total/len(nums)
#
# av = average(nums)
# var = variance(nums, av)
# std = math.sqrt(var)