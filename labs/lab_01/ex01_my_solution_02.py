# Laboratory 1
# Exercise 1 (adapted from Computer Sciences exam 03/09/2012)
# Alternative solution, better solution!

import sys


def main():
    # defining a class to hold to data for each competitor
    # name,surname,nation will be a string
    # scores will a list of strings
    # self.result will hold the the final records (the highest and
    # lowest evaluations are ignored and the score is determined by the
    # sum of the remaining 3 values) in float type.
    class Competitor:
        def __init__(self, name, surname, nation, scores):
            self.name = name
            self.surname = surname
            self.nation = nation
            self.scores = scores
            self.result = 0

    # getting the file name from the command line
    i = 1
    for arg in sys.argv:
        if i == 1:
            file_name = arg

    # opening the file
    with open(file_name) as data:

        # creating an empty dictionary to store objects that will hold
        # the data of the competitors
        dict = {}
        i = 0
        for line in data:
            l = list(line.split())
            name = l[0]
            surname = l[1]
            nation = l[2]
            # scores will be a list of strings, we will convert it later
            scores = list(l[3:])
            dict[i] = Competitor(name, surname, nation, scores)
            i = i+1
        size_competitors = i

        # finding the sum of scores (without the max min values) for
        # each competitor and them assigning this sum to the "result"
        # method of each competitor
        for i in dict:
            max = -1
            min = 11
            sum = 0
            for j in dict[i].scores:
                score = float(j)
                if score > max:
                    max = score
                if score < min:
                    min = score
                sum = sum+score
            sum = sum-max-min
            dict[i].result = sum

        # finding and printing the greatest three value(and competitors)
        first = 0   # first greatest value
        second = 0  # second greatest value
        third = 0   # third greatest value
        fi = 0  # key of first in the dictionary
        si = 0  # key of second in the dictionary
        ti = 0  # key of third in the dictionary
        for i in range(0, size_competitors):
            if dict[i].result > third:
                if dict[i].result > second:
                    if dict[i].result > first:
                        third = second
                        second = first
                        first = dict[i].result
                        ti = si
                        si = fi
                        fi = i
                    else:
                        third = second
                        second = dict[i].result
                        ti = si
                        si = i
                else:
                    third = dict[i].result
                    ti = i
        print("final ranking:")
        print("1: %s %s -- Score: %.1f" %
              (dict[fi].name, dict[fi].surname, dict[fi].result))
        print("2: %s %s -- Score: %.1f" %
              (dict[si].name, dict[si].surname, dict[si].result))
        print("3: %s %s -- Score: %.1f" %
              (dict[ti].name, dict[ti].surname, dict[ti].result))
        print("\n")

        l = []
        max = 0
        for i in range(0, size_competitors):
            # meaning a new country, this if statement ensures us to
            # check every country only once
            if dict[i].nation not in l:
                # adds the name of the new country to the list
                l.append(dict[i].nation)
                sum = 0
                # for the given country we iterate the dictionary value
                # of results and calculate the greatest value and store
                # the nation with the maximum result
                for j in range(0, size_competitors):
                    if (dict[j].nation) == (dict[i].nation):
                        sum = sum+(dict[j].result)
                if sum > max:
                    max = sum
                    nation = dict[i].nation

        print("Best Country:")
        print("%s Total Score: %.1f" % (nation, max))
        print("\n")


if __name__ == "__main__":
    main()
