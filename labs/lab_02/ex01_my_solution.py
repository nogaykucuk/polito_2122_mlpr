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


def plot_hist(attr, label):
    set = attr[:, label == 0]
    ver = attr[:, label == 1]
    vir = attr[:, label == 2]
    hAttr = {
        0: "Sepal length",
        1: "Sepal width",
        2: "Petal length",
        3: "Petal width"
    }
    for row in range(4):
        plt.figure()
        plt.xlabel(hAttr[row])
        plt.hist(set[row, :], bins=10, density=True, alpha=0.4, label='Setosa')
        plt.hist(ver[row, :], bins=10, density=True,
                 alpha=0.4, label='Versicolor')
        plt.hist(vir[row, :], bins=10, density=True,
                 alpha=0.4, label='Virginica')
        plt.legend()
    plt.show()


def plot_scatter(attr, label):
    set = attr[:, label == 0]
    ver = attr[:, label == 1]
    vir = attr[:, label == 2]
    hAttr = {
        0: "Sepal length",
        1: "Sepal width",
        2: "Petal length",
        3: "Petal width"
    }
    for row_i in range(4):
        for row_j in range(4):
            if row_i == row_j:
                continue
            plt.figure()
            plt.xlabel(hAttr[row_i])
            plt.ylabel(hAttr[row_j])
            plt.scatter(set[row_i, :], set[row_j, :], label='Setosa')
            plt.scatter(ver[row_i, :], ver[row_j, :], label='Versicolor')
            plt.scatter(vir[row_i, :], vir[row_j, :], label='Virginica')
            plt.legend()
        plt.show()


def main():
    filename = argv[1]
    attr, c_label = load(filename)
    plot_hist(attr, c_label)
    plot_scatter(attr, c_label)


if __name__ == "__main__":
    main()
