# Laboratory 1 Extra
# Exercise 1 (adapted from Computer Sciences exam 04/02/2013)
from sys import argv


def main():
    hMonthNames = {
        "1": 'January',
        "2": 'February',
        "3": 'March',
        "4": 'April',
        "5": 'May',
        "6": 'June',
        "7": 'July',
        "8": 'August',
        "9": 'September',
        "10": 'October',
        "11": 'November',
        "12": 'December'}
    hMonth = {}
    hSell = {}
    hBuy = {}
    hTotalBuy = {}
    hTotalSell = {}
    fname = argv[1]
    with open(fname) as f:
        for line in f:
            isbn, t_type, date, copy_no, price_per_copy = line.split()
            copy_no = int(copy_no)
            price_per_copy = float(price_per_copy)
            month = date[3:5]
            year = date[6:10]
            if isbn not in hSell:
                hSell[isbn] = 0
            if isbn not in hBuy:
                hBuy[isbn] = 0
            if isbn not in hTotalBuy:
                hTotalBuy[isbn] = 0
            if isbn not in hTotalSell:
                hTotalSell[isbn] = 0
            if t_type == "B":
                hBuy[isbn] = hBuy[isbn] + copy_no
                hTotalBuy[isbn] = hTotalBuy[isbn] + (copy_no * price_per_copy)
            elif t_type == "S":
                hSell[isbn] = hSell[isbn] + copy_no
                hTotalSell[isbn] = hTotalSell[isbn] + \
                    (copy_no * price_per_copy)
                if month not in hMonth:
                    hMonth[month] = 0
                hMonth[month] = hMonth[month] + copy_no

        print("Available Copies:")
        for i in hBuy:
            print("\t%s: %d" % (i, (hBuy[i]-hSell[i])))
        print("Sold books per month:")
        for i in hMonth:
            print("\t%s, %s: %d" % (hMonthNames[i], year, hMonth[i]))
        print("Gain per book:")
        for i in hBuy:
            average_buy = hTotalBuy[i]/hBuy[i]
            gain = hTotalSell[i]-(average_buy*hSell[i])
            avg = gain/hSell[i]
            print("\t%s: %.1f (%.1f, sold %d)" % (i, gain, avg, hSell[i]))


if __name__ == "__main__":
    main()
