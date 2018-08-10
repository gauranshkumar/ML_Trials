import time
from data_algo import lst
start_time = time.clock()

def peak_finder(list):
    n = list[1]

    if n < list[n-1] and n >list[n+1]:
        return n

    if n < list[len(list)-2]:
        return n
    else:
        return peak_finder(n+1)

















##    max_num = int(list[0])
##    for i in range(len(list)-1):
##        if max_num <= list[i]:
##            max_num = list[i]
##
##    return max_num











##def peak_finder_optimized(list):
##    mid = (len(list)-1)//2
##    max_num = int(list[0])
##    if max_num < list[mid]:
##        temp = list[::mid]
##        return peak_finder_optimized(temp)
##    elif max_num > list[mid]:
##        temp = list[mid::]
##        return peak_finder_optimized(temp)
##    else:
##        return list[mid]
##

print(peak_finder(lst))

end_time = time.clock()
print(end_time - start_time)
