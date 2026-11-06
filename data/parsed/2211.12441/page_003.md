<tbc>of the samples. It takes a sequence _A_ of _a_ samples from a random variable _Y_ , a sequence _B_ of _b_ samples from another random variable _Z_, and computes the statistic \(U\doteq min(\text{XInv}(A,B),\text{XInv}(B,A))\) that is the minimum of the number XInv(_A,B_) of cross inversions from _A_ to _B_, and vice versa.

**Definition 2 (cross inversions,** \(\text{XInv}.(\cdot,\cdot)\)**).** _Let_ \(\rho\) _be a ranking of X, and_ \(A,B\subseteq X\)_. A_ cross inversion _from A to B with respect to_ \(\rho\) _is a pair_ \((x_1,x_2)\in A\times B\) _that is out of order with respect to_ \(\rho\)_, i.e., such that_ \(\rho(x_1)>\rho(x_2)\)_. The number of cross inversions is denoted by_ \(\text{XInv}_\rho(A,B)\)_. For two arrays A and B of values, a cross inversion from A to B is a cross inversion from the set of entries in A to the set of entries in B where_ \(\rho\) _denotes the ranking by value; in this setting we write_ XInv(_A,B_) _for_ \(\text{XInv}_\rho(A,B)\).

The statistic _U_ coincides with the optimum value of our optimization problem with the tree _T_ in Figure 2 as input. The leftmost _a_ leaves correspond to the samples _A_, the rightmost _b_ leaves to the samples _B_, and the ranking \(\rho\) to the value order of the combined _a+b_ samples.

We mainly study the value version of our optimization problem, which we denote by MinInv.

**Definition 3 (inversion minimization on trees,** \(\text{MinInv}(\cdot,\cdot)\)**,** \(\Pi.\)**).** _Inversion minimization on trees is the computational problem with the following specification:_

**Input:** _A rooted tree T with leaf set X of size n, and a ranking_ \(\rho\) _of X._

**Output:** \(\text{MinInv}(T,\rho)\)_, the minimum of_ \(\text{Inv}_\rho(\sigma)\) _over all possible orderings of T, where_ \(\sigma\) _denotes the left-to-right ranking of X induced by the ordering of T._

_For any fixed tree T with leaf set X, we use the short-hand_ \(\Pi_T\) _to denote the computational problem that takes as input a ranking_ \(\rho\) _of X and outputs_ \(\text{MinInv}(T,\rho)\).

Degerman \[Deg82\] observes that the ordering at each internal node can be optimized independently in a greedy fashion. In the setting of binary trees, for each node _v_, we can count the cross inversions from the leaves in the left subtree of _v_ to the leaves in the right subtree of _v_. Between the two possible orderings of the children of a node _v_, we choose the one that yields the smaller number of cross inversions. Based on his observation, Degerman presents a polynomial-time algorithm for the case of binary trees _T_. A more refined implementation and analysis yields a running time of \(O(d_\text{avg}(T)\cdot n)\), where _d_avg(_T_) denotes the average depth of a leaf in _T_. For balanced binary trees the running time becomes _O(n_log_n_). All of this can be viewed as variants of the well-known _O(n_log_n_) divide-and-conquer algorithm for counting inversions in arrays of length _n_.

For trees of degree deg(_T)\>_2, the local greedy optimization at each internal node becomes more complicated, as there are many ways to order the children of each internal node. Exhaustive<tbc>

a leaves
b leaves

Figure 2: Mann–Whitney instance

