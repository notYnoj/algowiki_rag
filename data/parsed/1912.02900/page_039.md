## 5 Extensions of Wilber Bound

In this section we define two extensions of the strong Wilber bound and extend our negative results to one of these bounds. In subsection 5.1, we provide formal definitions of these bounds, and we present our negative result in subsequent subsections.

### 5.1 Definitions

Assume that we are given an input set _X_ of _n_ points, that is a permutation. Let L_<sup>V</sup>_ be the set of all vertical lines with half-integral _x_-coordinates between 1/2 and _n_-1/2, and let L_<sup>H</sup>_ be the set of all horizontal lines with half-integral _y_-coordinates between 1/2 and _n_-1/2. Recall that for every permutation \(\sigma\) of L_<sup>V</sup>_, we have defined a bound \(\mathsf{WB}_\sigma(X)\). We can similarly define a bound \(\mathsf{WB}'_{\sigma^\prime}(X)\) for every permutation \(\sigma'\) of L_<sup>H</sup>_. We also let \(\mathsf{WB}'(X)\) be the maximum, over all permutations \(\sigma'\) of L_<sup>H</sup>_, of \(\mathsf{WB}'_{\sigma^\prime}(X)\). Equivalently, let \(X'\) be an instance obtained from _X_ by rotating it by 90 degrees clockwise. Then \(\mathsf{WB}'(X)=\mathsf{WB}(X')\). We denote by _B_ a bounding box that contains all points of _X_.

#### 5.1.1 First Extension - Consistent Guillotine Bound

In this section we define the _consistent Guillotine Bound_, cGB(_X_). Let \(\sigma\) be any permutations of all lines in \(\mathcal{L}^V\cup\mathcal{L}^H\). We start from a bounding box _B_ containing all points of _X_ and maintain a partition P of the plane into rectangular regions, where initially P={_B_}. We process the lines in \(\mathcal{L}^V\cup\mathcal{L}^H\) according to their ordering in \(\sigma\). Consider an iteration when a line _L_ is processed. Let _P_<sub>1</sub>_,...,P<sub>k</sub>_ be all rectangular regions in P that intersect the line _L_. For each such region _P<sub>j</sub>_, let \(P'_j\) and \(P''_j\) be the two rectangular regions into which the line _L_ splits _P<sub>j</sub>_. We update P by replacing each region _P<sub>j</sub>_, for \(1\le j\le k\), with the regions \(P'_j\) and \(P''_j\). Once all lines in \(\mathcal{L}^V\cup\mathcal{L}^H\) are processed, we terminate the process.

This recursive partitioning procedure can be naturally associated with a partitioning tree \(T=T_\sigma\) that is defined as follows:

• Each vertex \(v\in V(T)\) is associated with a rectangular region _S(v_) of the plane. If _r_ is the root of _T_, then _S(r_)=_B_.<tbc>

• Each non-leaf vertex _v_ is associated with a line \(L(v)\in\mathcal{L}^H\cup\mathcal{L}^V\) that was used to partition _S(v_) into two sub-regions, \(S'\) and \(S''\). Vertex _v_ has two children _v_<sub>1</sub>_,v_<sub>2</sub> in _T_, with \(S(v_1)=S'\) and \(S(v_2)=S''\).<tbc>

• For each leaf node _v_, the region _S(v_) contains at most one point of _X_.

We now define the cost cost(_v_) of each node \(v\in V(T)\). If the region _S(v_) contains no points of _X_, or it contains a single point of _X_, then cost(_v_)=0. Otherwise, we define cost(_v_) in the same manner as before. Assume first that the line _L(v_) is vertical. Let _p_<sub>1</sub>_,...,p<sub>k</sub>_ be all points in \(X\cap S(v)\), indexed in the increasing order of their _y_-coordinates. A pair (_p<sub>j</sub>,p_<sub>_j_+1</sub>) of consecutive points forms a crossing of _L(v_) for _S(v_), if they lie on the opposite sides of _L(v_). We then let cost(_v_) be the number of such crossings.

