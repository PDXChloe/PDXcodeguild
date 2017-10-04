#Version 4

meter_dic = {"ft":0.3048, "mi":1609.34, "m":1, "km":1000, "yd":0.9144, "in":0.0254}

distance = input("What is the distance?")
in_unit_type = input("What type of input unit (ft, mi, m, km)?")
out_unit_type = input("What type of output unit (ft, mi, m, km)?")

final_distance = (meter_dic.get(in_unit_type) * int(distance))/meter_dic.get(out_unit_type)

print(str(distance) + in_unit_type + " is " + str(final_distance) + out_unit_type)