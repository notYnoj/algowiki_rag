_Proof of theorem 1.1._ For _K_<sub>1</sub> there is a single maximal independent set. For _K_<sub>2</sub> the first of the two vertices is accepted and blocks the other, so the two singleton maximal independent sets each have probability 1/2.

Now let \(|V(T)|\ge 3\). If _T_ has diameter 2, then it is a star with at least two leaves and theorem 4.3 applies. If the diameter is at least 3, use theorem 4.2. When the support vertex _y_ has at least two leaf neighbours, theorem 4.3 gives nonuniformity; when it has exactly one leaf neighbour, theorem 4.4 gives two maximal independent sets with unequal permutation-fibre sizes. Thus no tree on at least three vertices has uniform greedy terminal law.

## 5 Mixed spiders and exact output probabilities

Fix \(k\ge 0\) and \(l\ge 1\). The mixed spider _T<sub>k,l</sub>_ has centre _c_, length-two arms _c-u<sub>i</sub>-v<sub>i</sub>_ for \(1\le i\le k\), and direct leaves _w_<sub>1</sub>_,...,w<sub>l</sub>_ adjacent to _c_.

A maximal independent set containing _c_ is forced to contain every outer endpoint _v<sub>i</sub>_, and contains no _u<sub>i</sub>_ or direct leaf. Thus there is exactly one centre-containing maximal independent set. If _c_ is absent, every direct leaf must be present and each arm contributes exactly one of _u<sub>i</sub>,v<sub>i</sub>_. Hence there are 2_<sup>k</sup>_ non-centre maximal independent sets and

\(|\mathcal{M}(T_{k,l})|=2^k+1.\)

Put _N_=2_<sup>k</sup>_. Temporarily ignore _c_. On each arm the earlier of _u<sub>i</sub>_ and _v<sub>i</sub>_ is selected, and the relative orders on the _k_ disjoint pairs are equiprobable. Thus any prescribed arm pattern has probability 1_/N_.

Fix a non-centre pattern containing exactly _j_ inner vertices _u<sub>i</sub>_. Conditional on the required pair orientations, reinserting _c_ destroys that pattern precisely when _c_ is selected. This happens exactly when _c_ precedes every direct leaf and, on each of the _j_ inner-selected arms, precedes the corresponding _u<sub>i</sub>_. Under the conditioning \(u_i\prec v_i\), this is equivalent to _c_ being first among the _l_+2_j_+1 vertices consisting of _c_, all _l_ direct leaves, and both endpoints of those _j_ arms. Therefore<tbc>

\(\mathbb{P}(c\text{is selected}|\text{prescribed arm pattern})=\frac{1}{l+2j+1}.\)

<tbc>It follows that each particular type-_j_ non-centre maximal independent set has probability<tbc>

\(q_j=\frac{1}{N}\left(1-\frac{1}{l+2j+1}\right)=\frac{l+2j}{N(l+2j+1)}.\) (2)

<tbc>There are \(\genfrac(){pt}{2}{k}{j}\) such patterns. Summing the complementary centre-selected contributions over all arm patterns gives

\(p_c=\frac{1}{N}\sum_{j=0}^k\genfrac(){pt}{2}{k}{j}\frac{1}{l+2j+1}.\) (3)

This proves the counting and exact-probability parts of theorem 1.2.

## 6 The tuned bias and its asymptotics

Now assume \(k\ge 1\). Set _N_=2_<sup>k</sup>_, choose

\(l=N-k,\)

and put _A=N_+1. Since \(k\ge 1\), the elementary inequality _k\<_2_<sup>k</sup>_ shows that _l\>_0. Let _J_∼Bin(_k,_1/2) and _W_=2_J-k_. The uniform mass on each maximal independent set is 1_/A_.

