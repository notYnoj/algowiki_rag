If each of the partition classes _X<sub>i</sub>_ has size at most _k_, then each of the connected components of \(S(\Pi,\rho)\) has size \(n_j\le k\), irrespective of \(\rho\). The maximum value that \(\prod_j(n_j!)\) can take under the constraints \(\sum_jn_j=n\) and \(n_j\le k\) is no more than (_k_!)<sup>_n/k_</sup>. By the Connectivity Lemma, we conclude that \(\mathrm{D}(\Pi)\ge n!/(k!)^{n/k}\), and that the query complexity is at least log<sub>2</sub>(_n_!)-_O(n_log(_k_)).

We can do better by observing that, for a random ranking \(\rho\), the number of adjacent-rank transpositions \(\tau\) that do not jump from one partition class to another is not much larger than the average size of the partition classes.

**Lemma 49 (lower bound for problems with the partition property).** _Let_ \(\Pi\) _be a computational problem in the comparison-query model on a set of size n. If_ \(\Pi\) _satisfies the partition property with class size at most k, then then_ \(\mathrm{D}(\Pi)\ge n!/(2(k!)^2)\).

_Proof._ For any rank \(r\in[n-1]\), the probability that \(\rho^{-1}(r)\) and \(\rho^{-1}(r+1)\) belong to the same partition class equals \(\sum_i\frac{|X_i|}{n}\frac{|X_i|-1}{n-1}\) , which is at most \(\frac{k-1}{n-1}\) provided each partition class _X<sub>i</sub>_ has size at most _k_. It follows that the expected number of adjacent-rank transpositions \(\tau\) that do not change partition class, is at most _k_-1, so for a fraction at least half of the rankings \(\rho\) the number is at most 2(_k_-1).

The number of adjacent-rank transpositions \(\tau\) that do not change partition class for a given ranking \(\rho\) equals the number of edges in the successor graph \(S(\Pi,\rho)\). In terms of the sizes _n<sub>j</sub>_, the number equals \(\sum_j(n_j-1)\). We are considering rankings \(\rho\) for which the sum is at most 2(_k_-1). The maximum of \(\prod_j(n_j!)\) under the constraints that \(\sum_j(n_j-1)\le 2(k-1)\) and that each individual \(n_j\le k\), is reached when two of the _n<sub>j</sub>_’s equal _k_ and the rest are 1. Thus, if each of the partition classes _X<sub>i</sub>_ are of size at most _k_, for a fraction at least half of the rankings \(\rho\), the size of the connected component of \(\rho\) in \(G(\Pi)\) is at most (_k_!)<sup>2</sup>. It follows that the number of connected components of \(G(\Pi)\) is at least _n_!/(2(_k_!)<sup>2</sup>). The Connectivity Lemma then yields the claimed lower bound on \(\mathrm{D}(\Pi)\).

Lemma 49 yields a lower bound of log(_n_!)-_O(k_log(_k_)) on the query complexity of \(\Pi\) whenever \(\Pi\) satisfies the partition property with class size at most _k_.

Next we turn to sufficient conditions on the tree _T_ that guarantee the partition property for \(\Pi_T\). For didactic reasons we first develop the conditions for binary trees, and then generalize them to arbitrary trees.

## 8.2 Binary trees

In the case of binary trees _T_, the sensitivity analysis of Section 5.1 leads to a simple sufficient condition for the partition property to hold for \(\Pi_T\). Recall that we are assuming without loss of generality that _T_ has no internal nodes of degree 1, which in the case of binary trees is equivalent to saying that the tree is full: Every internal node has the maximum degree of 2.

Consider criterion 8 in Proposition 31. The right-hand side is always -1. As for the left-hand side, we know the following.

**Fact 50.** _For all disjoint sets_ \(A,B\subseteq X\) _and any ranking_ \(\rho\) _of X,_ \(\mathrm{DInv}_\rho(A,B)=|A|\cdot|B|\mathrm{mod}2\).

_Proof._ As every pair in \(A\times B\) constitutes a cross-inversion for either _A_ to _B_, or _B_ to _A_, we have<tbc>

