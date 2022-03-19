# Laboratory 1
# Exercise 2 (adapted from Computer Sciences exam 23/06/2017)
# Alternative solution, better solution!
from sys import argv
from math import sqrt

# Function definition that computes the distance in 2D space when the
# difference between the axes are given as input


def distance(x, y):
    return sqrt((x*x)+(y*y))

# Defining class to instantiate objects that will hold the data from
# each line


def main():
    class BusRecords:
        def __init__(self, id, line_no, x, y, t):
            self.id = id
            self.line_no = line_no
            self.x = x
            self.y = y
            self.t = t

    # Reading arguments from the command line and returning exception if
    # needed
    busId = None
    lineId = None
    file_name = argv[1]
    flag = argv[3:5]
    if flag == "-b":
        busId = argv[3]
    elif flag == "-l":
        lineId = argv[3]
    else:
        raise Exception("You've entered a wrong flag!")

    # Opening file and reading its content line by line, and then
    # assigning this data to the attributes of the instantiated objects.
    # Then putting these objects in a list
    records = []
    with open(file_name) as f:
        for line in f:
            id, line_no, x, y, t = line.strip()
            x = int(x)
            y = int(y)
            t = int(t)
            rec = BusRecords(id, line_no, x, y, t)
            records.append(rec)

    # Condition for flag -b
    if busId:
        tot_dist = 0
        initial = True
        for i in range(0, len(records)):
            # Assigning initial locations to the inquired bus
            if busId == records[i].id:
                if initial:
                    x_i = records[i].x
                    y_i = records[i].y
                    initial = False
                    continue
                else:
                    # Finding the difference in distance and then
                    # finding the total distance travelled.
                    x_f = records[i].x
                    y_f = records[i].y
                    x_diff = x_f - x_i
                    y_diff = y_f - y_i
                    tot_dist = tot_dist+distance(x_diff, y_diff)
                    x_i = x_f
                    y_i = y_f
        print("%s - Total Distance: %.1f" % (busId, tot_dist))

    # Condition for flag -l
    if lineId:
        records = sorted(records, key=lambda i: i.id)
        tot_dist = 0
        tot_time = 0
        bus_list = []
        for i in range(0, len(records)):
            if lineId == records[i].line_no:
                # Assigning initial data when we investigate a new bus
                if records[i].id not in bus_list:
                    bus_list.append(records[i].id)
                    x_i = records[i].x
                    y_i = records[i].y
                    t_i = records[i].t
                    bus = records[i].id
                    initial = False
                    continue
                else:
                    # Finding the difference in distance and time, then
                    # finding the total distance travelled and the total
                    # time elapsed
                    x_f = records[i].x
                    y_f = records[i].y
                    t_f = records[i].t
                    x_diff = x_f - x_i
                    y_diff = y_f - y_i
                    t_diff = t_f - t_i
                    tot_dist = tot_dist + distance(x_diff, y_diff)
                    tot_time = tot_time + t_diff
                    x_i = x_f
                    y_i = y_f
                    t_i = t_f
        avg_speed = tot_dist/tot_time
        print("%s - Avg Speed: %.16f" % (lineId, avg_speed))


if __name__ == "__main__":
    main()
