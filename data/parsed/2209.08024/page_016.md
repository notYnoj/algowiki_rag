<tbc>_Proof._ Denote _c<sub>n</sub>_=`cost`_<sub>w<sub>n</sub></sub>(C<sub>n</sub>_) and _t<sub>n</sub>_=`cost`_<sub>w<sub>n</sub></sub>(T<sub>n</sub>_). Clearly _c_<sub>0</sub>=_t_<sub>0</sub>=1. For _n\>_0 we have<tbc>

\(c_n=\sum_{i=1}^{\Delta-1}\frac{1}{2^{i-1}}+\sum_{i=1}^{\Delta-2}\frac{1}{2^i}c_{n-1}+2\frac{1}{2^{\Delta-1}}c_{n-1}=2-\frac{4}{2^\Delta}+c_{n-1}\)

<tbc>and

\(t_n=\sum_{i=1}^{\Delta-2}\frac{1}{2^i}(t_{n-1}+1)+2\frac{1}{2^{\Delta-1}}(t_{n-1}+1)=1+t_{n-1},\)

and the lemma follows by induction.

_Proof of Theorem 1.4(ii)._ The fact that \(lim_{n\rightarrow\infty}\mathtt{OPT}(\mathcal{T}_n,w_n)=\infty\) follows from Lemma 4.4 and Theorem 1.3 (or Theorem 1.1). Using Lemma 4.4 again, we have

\(\mathtt{cost}_{w_n}(C_n)\ge\left(2-\frac{4}{2^\Delta}\right)\mathtt{OPT}(\mathcal{T}_n,w_n)-1+\frac{4}{2^\Delta}.\)

Using Lemma 2.4, for each _n_ we can add small enough perturbation to _w<sub>n</sub>_ such that _C<sub>n</sub>_ is the unique centroid tree and the claimed bound holds.

## 5 Computing centroid trees

In this section, we show how to compute centroid trees using the _top tree_ framework of Alstrup, Holm, de Lichtenberg, and Thorup \[AHLT05\]. _Top trees_ are a data structure used to maintain dynamic forests under insertion and deletion of edges. Most importantly, they expose a simple interface that allows the user to maintain information in the trees of the forest. For this, the user only needs to implement a small number of internal operations.

Alstrup et al. in particular show how to maintain the _median_ of trees in O(log_n_) per operation, see Section 2 for the definition of the median. As mentioned before, if all edge-weights are 1, then medians are precisely centroids (see Lemma 2.3).

**Theorem 5.1** (\[AHLT05, Theorem 3.6\])**.** _We can maintain a forest with positive vertex weights on n vertices under the following operations:_

• _Add an edge between two given vertices u,v that are not in the same connected component;_<tbc>

• _Remove an existing edge;_<tbc>

• _Change the weight of a vertex;_<tbc>

• _Retrieve a pointer to the tree containing a given vertex;_<tbc>

• _Find the centroid of a given tree in the forest._<tbc>

V1
V1
V2
V4-1
Cn-1
V4-2
Tn-1
Cn-1
V4-1
Tn-1
Tn-1
Tn-1
Tn-1
Tn-1
V2
V4-2
V1
V2
V4-2
Tn-1
Tn-1
Tn-1
Cn-1
Tn-1
Tn-1
Tn-1
Cn-1
Cn-1
Cn-1
Cn-1

Figure 6: An illustration of Theorem 1.4(ii). (_Left._) The underlying tree T_<sub>n</sub>_. (_Middle._) The centroid tree _C<sub>n</sub>_. (_Right._) The search tree _T<sub>n</sub>_.

