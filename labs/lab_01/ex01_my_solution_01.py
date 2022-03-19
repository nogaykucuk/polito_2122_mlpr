# Laboratory 1
# Exercise 1 (adapted from Computer Sciences exam 03/09/2012)
# importing "sys" so that we can pass arguments from the command line
import sys

# Storing the name of the file, as a string, from the command line to
# the "file_name"
i = 0
for arg in sys.argv:
    if(i == 1):
        file_name = arg
    i = i+1

# "file_name" holds the name of the file. We open this file with "read"
# options
f = open(file_name, "r")

# We define a dictionary, that will hold our data in the file.
dict_score = {}
i = 0
for line in f:
    l = list((line.split()))
    dict_score[i] = l
    i += 1
# We find the sum of all values given by the juries for each competitor.
# We also find the max and minimum values given by the juries for each
# competitor. We then subtract these max and min values from the sum to
# get the "net sum". Then we append this values to the end of each row
# of the dictionary (i.e. for each competitor).
for k in dict_score.keys():
    sum = 0
    max = 0
    min = 0
    for j in range(3, 8):
        if j == 3:
            max = float(dict_score[k][j])
            min = max
        if max < float(dict_score[k][j]):
            max = float(dict_score[k][j])
        if min > float(dict_score[k][j]):
            min = float(dict_score[k][j])
        sum = sum+float(dict_score[k][j])
    sum = sum-max-min
    sum_round = "{:.1f}".format(sum)
    sum_str = str(sum_round)
    dict_score[k].append(sum_str)

# We then define three list "l_first", "l_second", "l_third", which hold
# the values for the three maximum sums. Each time a bigger number is
# found, the value of the smaller one is passed to the lower rank, and
# then then this number will be assigned to the smaller one. For
# example: if first=7,second=5,third=4 and if we find 9 for a max sum
# value, then we put third=second, second=first, first=9.
l_first = ["", "", 0]
l_second = ["", "", 0]
l_third = ["", "", 0]
for k in dict_score.keys():
    if float(dict_score[k][8]) > l_third[2]:
        if float(dict_score[k][8]) > l_second[2]:
            l_third[0] = l_second[0]
            l_third[1] = l_second[1]
            l_third[2] = l_second[2]
            if float(dict_score[k][8]) > l_first[2]:
                l_second[0] = l_first[0]
                l_second[1] = l_first[1]
                l_second[2] = l_first[2]
                l_first[0] = dict_score[k][0]
                l_first[1] = dict_score[k][1]
                l_first[2] = float(dict_score[k][8])
            else:
                l_second[0] = dict_score[k][0]
                l_second[1] = dict_score[k][1]
                l_second[2] = float(dict_score[k][8])
        else:
            l_third[0] = dict_score[k][0]
            l_third[1] = dict_score[k][1]
            l_third[2] = float(dict_score[k][8])

print("final ranking:")
print("1: %s %s -- Score: %.1f" % (l_first[0], l_first[1], l_first[2]))
print("2: %s %s -- Score: %.1f" % (l_second[0], l_second[1], l_second[2]))
print("3: %s %s -- Score: %.1f" % (l_third[0], l_third[1], l_third[2]))

# For finding the country with the greatest value, we traverse the
# dictionary in nested for loops and add the total number of points for
# each country, then compare this total number for each country, and we
# select the country with the highest number of points.
l = [dict_score[0][2], dict_score[0][8]]
for k in dict_score.keys():
    sum = 0
    for j in dict_score.keys():
        if dict_score[k][2] == dict_score[j][2]:
            sum = sum+float(dict_score[j][8])
    if sum > float(l[1]):
        l[0] = dict_score[k][2]
        l[1] = sum
print("\n")
print("Best Country:")
print("%s Total Score: %.1f" % (l[0], l[1]))

# Closure of the function
f.close()
