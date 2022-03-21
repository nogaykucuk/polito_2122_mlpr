# In many cases it will be useful to plot functions, data points and so
# on. Several libraries are available, we will use "matplotlib". The
# library has a huge number of functionalities, we won’t go into details
# much. The main module we will consider is "pyplot". Plotting values
# can be achieved through the "plot" function:
import numpy
import matplotlib.pyplot as plt
x = numpy.linspace(0, 5, 1000)
plt.plot(x, numpy.sin(x))
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

# We can specify color, line style (solid, dashed, points, ...), style
# attributes (e.g. line width) and so on
y = numpy.linspace(0, 5, 20)
plt.plot(y, numpy.sin(y), color="r", linestyle="--")
plt.plot(y, numpy.sin(y), "bo", markersize=5)
plt.show()

# We can visualize 2-D data using scatter plots:
D = numpy.random.random((2, 100))
plt.scatter(D[0], D[1])
plt.show()

# We can also do it using plot:
D = numpy.random.random((2, 100))
plt.plot(D[0], D[1], linestyle="", marker=".",
         markersize=10)
plt.show()

# Visualizing data distributions through histograms:
D = numpy.random.normal(size=1000)
plt.hist(D, bins=20, density=True, ec="black", color="#800000")
plt.show()

# We can add multiple plots to the same figure. "show" is used to show a
# picture after all elements have been added:
D = numpy.random.normal(size=1000)
plt.hist(D, bins=20, density=True, ec="black", color="#800000", alpha=0.5)
x = numpy.linspace(-4, 4, 1000)
y = 1.0/(2*numpy.pi)**0.5 * numpy.exp(-0.5 * x**2)
plt.plot(x, y, color=(0.0, 0.2, 0.8), linewidth=4)
plt.show()

# We will discuss additional functionalities as needed.
