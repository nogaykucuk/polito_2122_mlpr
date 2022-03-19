# Laboratory 1
# Exercise 3 (adapted from Computer Sciences exam 14/02/2020)
from sys import argv


def main():
    class Person:
        def __init__(self, name, surname, birthplace, birthdate):
            self.name = name
            self.surname = surname
            self.birthplace = birthplace
            self.birthdate = birthdate

    h_months = {
        "01": 'January',
        "02": 'February',
        "03": 'March',
        "04": 'April',
        "05": 'May',
        "06": 'June',
        "07": 'July',
        "08": 'August',
        "09": 'September',
        "10": 'October',
        "11": 'November',
        "12": 'December'}

    f_name = argv[1]
    l = []
    with open(f_name) as f:
        for line in f:
            name, surname, birthplace, lin = line.split()
            birthdate = ("%s/%s" % (lin[3:5], lin[0:2]))
            person = Person(name, surname, birthplace, birthdate)
            l.append(person)

    birth_by_city = sorted(l, key=lambda i: i.birthplace)
    initial = True
    print("Births per city:")
    for i in birth_by_city:
        if initial:
            city = i.birthplace
            birth_num = 1
            city_num = 1
            initial = False
        else:
            if i.birthplace != city:
                city_num += 1
                print("  %s: %d" % (city, birth_num))
                city = i.birthplace
                birth_num = 1

            else:
                birth_num += 1
    print("  %s: %d" % (city, birth_num))

    birth_by_month = sorted(l, key=lambda i: i.birthdate)
    initial = True
    print("Births per month:")
    for i in birth_by_month:
        if initial:
            month = i.birthdate[0:2]
            birth_num = 1
            total_num = birth_num
            initial = False
        else:
            if i.birthdate[0:2] != month:
                print("  %s: %d" % (h_months[month], birth_num))
                month = i.birthdate[0:2]
                total_num += birth_num
                birth_num = 1
            else:
                birth_num += 1
    print("  %s: %d" % (h_months[month], birth_num))

    avg_birth = total_num / city_num
    print("Average number of births: %.2f" % avg_birth)


if __name__ == "__main__":
    main()
