


# peaks =#has lower number on both left and right
# valleys =#number with a higher number on both left and right
# peaks_and_valleys = #complies the list of peaks and valleys together
#
#


data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]



def find_peaks(data):#find the peaks
    peaks = []
    for i in range(1, len(data)-1): #need to adjust the range in order to communicate the comparison parameters to computer.
        if data[i-1] < data[i] and data[i+1] < data[i]:
            peaks.append(i)
    #print("Data peaks indices: " + str(peaks))
    return peaks
find_peaks(data)





def find_valleys(data):#find the valleys
    valleys = []
    for i in range(1, len(data)-1):
        if data[i-1] > data[i] and data[i+1] > data[i]:
            valleys.append(i)
    #print("Data valleys indices: " + str(valleys))
    return valleys
find_valleys(data)


def peaks_and_valleys(data):
    peaks = find_peaks(data)
    valleys = find_valleys(data)
    peaks.extend(valleys) #combining the list
    peaks.sort()
    return peaks

p_and_v = peaks_and_valleys(data)
print(p_and_v)