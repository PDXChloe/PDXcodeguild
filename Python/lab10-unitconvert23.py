#Version 2 + 3

print("")   #I just need whitespace
print("")


meter_dic = {"ft":0.3048, "mi":1609.34, "m":1, "km":1000, "yd":0.9144, "in":0.0254} #made a dictionary with key:value pairs of "units to convert":amount in meters

distance = input("What is the distance? \n")
final_unit = input("What are the units (ft, mi, m, km, yd, in)?\n")
units = meter_dic.get(final_unit)


meters = int(distance) * units

print(str(distance) + final_unit + " is " + str(meters)+" meters.")
