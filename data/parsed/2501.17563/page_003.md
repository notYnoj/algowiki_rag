5. Cost versus Value: we only use _cost_ when we discuss the cost of an STT, and use _value_ when we consider the value of a feasible point of the LP with respect to an objective function.

**Problem 1** (Static STT)**.** Let _U_ be a tree topology, and let _f_ be a vector of frequencies. Determine an STT _T_ over _U_ such that _cost(T,f_) is minimized.

## 1.1 The Linear Program

The work of \[9\] defines a linear program (LP) formulation to find a 2-approximation for an optimal solution. The LP uses the following reasoning: Given topology _U_ and the STT _T_ over it, for every pair of nodes, one must be an ancestor of the other, or there is an intermediate node between them that was queried first and acts as their LCA (least common ancestor) in the STT. We define an _ancestry variable X<sub>ij</sub>_ for each pair of nodes \(i,j\in U\) which should take the value 1 if _i_ is an ancestor of _j_ in _T_, and another variable _Z<sub>kij</sub>_ which should be 1 if _k_ is the LCA of _i_ and _j_ in _T_. We only define _Z<sub>kij</sub>_ for nodes \(k\in U\) that are on the path between _i_ and _j_, i.e., \(k\in(i\unknown j)\). Ideally, one would hope to write _Z<sub>kij</sub>_=min(_X<sub>ki</sub>,X<sub>kj</sub>_) but in an LP formulation we cannot do this, so we are content with writing the inequalities \(Z_{kij}\le X_{ki}\) and \(Z_{kij}\le X_{kj}\).<sup>1</sup> We can also define the depth variable \(D_i=\sum_{(i\neq j)\in U}X_{ji}\). The depth represents the cost of search, off by one, such that one aims to minimizes \(\sum_{i\in U}f_i\cdot D_i\). Ideally we would also require that all of _X_ and _Z_ are either 0 or 1, and this would define an integer LP (ILP). However, to be able to rely on LP machinery, we relax this definition and let the variables have non-negative real values.<sup>2</sup> To conclude this exposition, the final LP is as follows:

**Definition 1.2** (STT LP)**.** A complete description of the LP is as follows:

1. Variables: _X,Z,D_:<tbc>

(a) (Depths) \(\forall i\in U:D_i\).<tbc>

(b) (Ancestry) \(\forall i,j\in U,i\neq j:X_{ij}\).<tbc>

(c) (LCAs) \(\forall i,j\in U,i\neq j:\forall k\in(i\unknown j):Z_{kij}\). Note that _Z<sub>kij</sub>_ and _Z<sub>kji</sub>_ are considered as the same variable. (Rather than defining both and equating _Z<sub>kij</sub>=Z<sub>kji</sub>_.)<tbc>

<sup>1</sup>The LP we define soon does not capture additional STT properties, see further discussion in Section 5.1. <sup>2</sup>Allowing values larger than 1 is not a problem, because any quantity above 1 can only hurt the minimization. Bounding each variable only introduces new constraints, so we prefer to "let the LP do its job" without it.

1
2
3
4
5
6
7

3
6
6
1
4
1
7
7
2
5
4
2
5
3

(a) Underlying tree _U_

(b) STT _T_<sub>1</sub>

(c) STT _T_<sub>2</sub>

Figure 1: We show two STTs _T_<sub>1</sub> and _T_<sub>2</sub> over the same topology _U_, as described in Definition 1.1. Note that while while both _U_ and _T<sub>i</sub>_ are trees on the same set of nodes, their edges may connect the nodes very differently.

