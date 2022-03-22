from sys import argv
import numpy
import matplotlib
import matplotlib.pyplot as plt


def load(fname):
    l_a = []  # list that will hold the attributes
    l_c = []  # list that will hold the class labels
    with open(fname) as f:
        for line in f:
            s_len, s_wid, p_len, p_wid, label = line.split(",")
            l_a.append(float(s_len))
            l_a.append(float(s_wid))
            l_a.append(float(p_len))
            l_a.append(float(p_wid))
            if label == "Iris-setosa\n":
                label = 0
            if label == "Iris-versicolor\n":
                label = 1
            if label == "Iris-virginica\n":
                label = 2
            l_c.append(label)
    attr = numpy.array(l_a).reshape(150, 4)
    attr = attr.T
    c_label = numpy.array(l_c)
    return attr, c_label


def plot_hist(D, L):
    D0 = D[:, L == 0]
    D1 = D[:, L == 1]
    D2 = D[:, L == 2]
    hAttr = {
        0: "Sepal length",
        1: "Sepal width",
        2: "Petal length",
        3: "Petal width"
    }
    for row in range(4):
        plt.figure()
        plt.xlabel(hAttr[row])
        plt.hist(D0[row, :], bins=10, density=True, alpha=0.4, label='Setosa')
        plt.hist(D1[row, :], bins=10, density=True,
                 alpha=0.4, label='Versicolor')
        plt.hist(D2[row, :], bins=10, density=True,
                 alpha=0.4, label='Virginica')
        plt.legend()
    plt.show()


def plot_scatter(D, L):
    pass


def main():
    filename = argv[1]
    attr, c_label = load(filename)
    plot_hist(attr, c_label)
    plot_scatter(attr, c_label)


if __name__ == "__main__":
    main()
