## A Reducing 0-1 Knapsack to Min-Plus Convolution

In the _all-capacities_ version of the _0-1 knapsack problem_, we are given _n_ items where the _j_-th item has positive integer weight _w<sub>j</sub>_ and positive real profit _p<sub>j</sub>_, and we are given a number _t_. For each \(i\in[t]\), we want to compute \(f[i]=max\left\{\sum_{j\in J}p_j:\sum_{j\in J}w_j=i,J\subseteq\{1,\dots,n\}\right\}\).

0-1 knapsack may be viewed as a two-dimensional variant of subset sum. More precisely, we map each item to a point (_w<sub>j</sub>,p<sub>j</sub>_) in two dimensions. For a set of two-dimensional points \(A\subseteq[t]\times\mathbb{R}^+\), define the<tbc>

