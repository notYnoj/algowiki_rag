## 1 Overview

The result of a hierarchical cluster analysis on a set _X_ of items can be thought of as an unordered rooted tree _T_ with leaf set _X_. To visualize the tree, or to spell out the classification in text, one needs to decide for every internal node of _T_ in which order to visit its children. Figure 1a represents an example of a classification of eight body parts from the psychology literature \[Deg82\]. It is obtained by repeatedly clustering nearest neighbors where the distance between two items is given by the number of people in a survey who put the items into different classes \[Mil69\]. The ordering of the resulting binary tree in Figure 1a is the output produced by a particular implementation of the clustering algorithm.

Another ordering is given in Figure 1b; black marks the nodes whose children have been swapped from the ordering in Figure 1a. Figure 1b has the advantage over Figure 1a that the leaves now appear in an interesting global order, namely head-to-toe: ear, cheek, mouth, chest, waist, thigh, knee, toe. Indeed, Figure 1b makes apparent that the anatomical order correlates perfectly with the clustering. In general, given a tree _T_ and a ranking \(\rho\) of its leaves, one might ask "how correlated" is _T_ with \(\rho\)? Degerman \[Deg82\] suggests evaluating the orderings of _T_ in terms of the number of inversions of the left-to-right ranking \(\sigma\) of the leaves with respect to the given ranking \(\rho\), and use the minimum number over all orderings as a measure of (non)correlation.

**Definition 1 (ranking, inversion,** \(\text{Inv.}(\cdot)\)**).** _A_ ranking \(\rho\) _of a set X of n items is a bijection from X to_ \[_n_\]_. Given two rankings_ \(\sigma\) _and_ \(\rho\)_, an_ inversion _of_ \(\sigma\) _with respect to_ \(\rho\) _is a pair of items_ \(x_1,x_2\in X\) _such that_ \(\rho(x_1)<\rho(x_2)\) _but_ \(\sigma(x_1)>\sigma(x_2)\)_. The number of inversions is denoted by_ \(\text{Inv}_\rho(\sigma)\)_. An inversion in an array A of values is an inversion of_ \(\sigma\) _with respect to_ \(\rho\) _where_ \(\sigma\) _denotes the ranking by array index and_ \(\rho\) _the ranking by value; in this setting we write_ Inv(_A_) _for_ \(\text{Inv}_\rho(\sigma)\).

The minimum number of inversions can be used to compare the quality of different trees _T_ for a given ranking \(\rho\), or of different rankings \(\rho\) for a given tree _T_. This mimics the use of the number of inversions in applications like collaborative filtering in recommender systems, rank aggregation for meta searching the web, and Kendall’s test for dependencies between two random variables. In particular, the Mann-Whitney test for differences between random variables can be viewed as a special case of our optimization problem. The test is widely used because of its nonparametric nature, meaning that no assumptions need to be made about the distribution of the two variables; the distribution of the statistic in the case of the null hypothesis (both variables have the same distribution) is always the same. The test achieves this property by only considering the relative order<tbc>

ear
toe
chest
waist
cheek mouth
knee thigh
(a) Initial tree ordering

ear
cheek mouth
chest
waist
toe
 thigh
knee

(a) Initial tree ordering

(b) Optimal tree ordering

Figure 1: Classification of body parts

