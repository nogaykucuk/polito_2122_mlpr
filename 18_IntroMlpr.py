# Machine Learning: A computer program is said to learn from experience
# E with respect to some class of tasks T and performance measure P, if
# its performance at tasks in T, as measured by P, improves with
# experience E.

# Pattern Recognition: Automatic discovery of regularities in data
# through the use of computer algorithms (...) to take actions such as
# classifying the data into different categories.

# Define models that are able to capture the regularities in our data
# and allow performing inference about the properties we are interested
# in. The models should not simply specify a set of human–defined rules,
# but should be able to learn from data. The learning stage should
# leverage observed data to improve the quality of the inference.

# Example: Classification. Given a set of objects, assign them to
# discrete categories. Find a mapping from the space of input vectors
# representing the objects to a discrete set of labels (output values).
# Possible applications include image and face recognition and speaker
# identification.

# Example: Regression (which we will not cover in this course). Similar
# to classification, but output values are single or multiple continuous
# variables. Possible applications include modeling of physical
# phenomena or prediction of continuous–valued functions (e.g. stock
# market prediction).

# Example: Density Estimation (we won't deal with this in this course,
# at least explicitly. In reality, we will be working on them).
# Estimation of the distribution of input vectors. Often used to explore
# data characteristics and to build inference models.

# Depending on the task, we identify two main branches: "Supervised
# learning" and "Unsupervised Learning".

# Supervised learning: Along with the "input" data the system is also
# provided with "output" data (e.g. class labels, function values, ...).
# The goal is estimating a mapping between input and output data. Common
# supervised tasks are:
#   Classification
#   Regression

# Unsupervised learning: No feedback is provided to the system, whose
# goal is to identify some (useful) structure of the data. Examples of
# unsupervised tasks:
#   Clustering
#   Density estimation
#   Dimensionality reduction

# Unsupervised methods are often used as pre–processing steps for
# supervised learning tasks (e.g. unsupervised dimensionality
# reduction). Furthermore, some techniques are common to both supervised
# and unsupervised tasks (e.g. density estimation for generative
# classification models). In this course we will focus on classification
# and density estimation tasks.

# "This course, dealing with classical machine learning, is essentially
# an applied statistics and applied math course, rather than pure
# engineering".
