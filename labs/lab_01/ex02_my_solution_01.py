# Laboratory 1
# Exercise 2 (adapted from Computer Sciences exam 23/06/2017)
from math import sqrt
import sys

# Function definition that computes the distance in 2D space when the
# difference between the axes are given as input


def distance(x, y):
    return sqrt((x*x)+(y*y))


# Passing the command line arguments (like file_name, flag and entry) to
# variables
i = 0
for arg in sys.argv:
    if i == 1:
        file_name = arg
    elif i == 2:
        flag = arg
    elif i == 3:
        if flag == "-b":
            busId = arg
        elif flag == "-l":
            lineId = arg
    i = i+1

# Creating a condition to raise an exception if a wrong flag occurs
if (flag != "-b") and (flag != "-l"):
    raise Exception("You've entered a wrong flag!")

# Opening the file, and saving its contents to a dictionary line by line
f = open(file_name, "r")
dict_unsorted = {}
i = 0
for line in f:
    l = list((line.split()))
    dict_unsorted[i] = l
    i += 1
# Sorting the dictionary by its values' first arguments in a list (i.e.,
# sorting the dictionary according to the busId names.)
dict_bus = dict(sorted(dict_unsorted.items(), key=lambda item: item[1][0]))

# Condition to check "the total distance travel by a given bus"
if flag == "-b":
    # Assigning the initial coordinates for the given bus
    for k in dict_bus.keys():
        if dict_bus[k][0] == busId:
            x_axis = float(dict_bus[k][2])
            y_axis = float(dict_bus[k][3])
            break

    # Finding the total distance travelled by the given bus
    dist_tot = 0
    for k in dict_bus.keys():
        if dict_bus[k][0] == busId:
            # new coordinates of the bus
            x_new = float(dict_bus[k][2])
            y_new = float(dict_bus[k][3])

            # condition to check if the bus is in another position than
            # before and finding the distance travelled
            if(x_axis != x_new) or (y_axis != y_new):
                diff_in_x = x_new - x_axis
                diff_in_y = y_new - y_axis
                dist_tot = dist_tot+distance(diff_in_x, diff_in_y)
                x_axis = x_new
                y_axis = y_new

    print("%s - Total Distance: %.1f" % (busId, dist_tot))

# Condition to check "the average speed of buses travelling on the given
# line"
else:
    new_bus = True
    total_t = 0
    total_dist = 0
    bus_name = "-1"
    for k in dict_bus.keys():
        if (dict_bus[k][1] == lineId):
            # Checking the condition to see if it is a different or the
            # initial bus on the same line. If yes, it creates initial
            # data for then new bus.
            if (dict_bus[k][0] != bus_name):
                new_bus = True
            if new_bus:
                x_first = float(dict_bus[k][2])
                y_first = float(dict_bus[k][3])
                t_first = float(dict_bus[k][4])
                bus_name = dict_bus[k][0]
                new_bus = False
                continue
            # Computing the differences between axes, and times, and
            # then finding the total distance and time
            else:
                x_last = float(dict_bus[k][2])
                y_last = float(dict_bus[k][3])
                t_last = float(dict_bus[k][4])
                diff_x = x_last - x_first
                diff_y = y_last - y_first
                diff_t = t_last - t_first
                total_dist = total_dist + distance(diff_x, diff_y)
                total_t = total_t + diff_t
                x_first = x_last
                y_first = y_last
                t_first = t_last
                bus_name = dict_bus[k][0]
    # Average Speed= Total Distance Travelled / Total Time Elapsed
    avg_speed = total_dist/total_t
    print("%s - Avg Speed: %f" % (lineId, avg_speed))

# Closure of the function
f.close()
