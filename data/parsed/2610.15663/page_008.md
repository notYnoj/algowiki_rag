_Proof._ Partition _X_ into blocks _X<sub>i,t</sub>_, with \(i\in[R]\) and \(t\in\{1,2\}\), each of size \((N/R)\times(D/2)\). Partition _Y_ into blocks _Y<sub>t,j</sub>_, with \(j\in[S]\), each of size \((D/2)\times(M/S)\). The (_i,j_) block of the output is

\((XY)_{i,j}=X_{i,1}Y_{1,j}+X_{i,2}Y_{2,j}.\)

This is the same \(R\times 2\) by \(2\times S\) multiplication as in Theorem 2.3, with matrices in place of scalars. The lemma still applies: its formulas use only linear combinations and products of a left input by a right input, always in that order. It expresses each output block as six shared products minus one private product. Each such product multiplies a linear combination of the _X_ blocks by a linear combination of the _Y_ blocks, giving the stated dimensions.

To request an entry of _XY_ , locate its output block (_i,j_) and its position within that block. Request that same position in the six shared products and the one private product used by this block. The seven returned values recover the original entry with five additions and one subtraction.

Each child maintains a set of requested positions, so repeated requests are computed only once. Each output block has its own private product, so the _w_ distinct original requests give exactly _w_ distinct private requests. The original requests also generate 6_w_ shared requests, so the shared children have at most 6_w_ distinct requests in total.

## The bounds after t steps.

For fixed _k_, iterating the rule _t_ times gives the basic dimensions \(R^t\times 2^t\) and \(2^t\times S^t\). We also allow multiples of the outer dimensions, so that arbitrary inputs can be handled by padding. We iterate the input preparation and output reconstruction steps shown in Figure 3.

**Lemma 2.6** (Iterated multiplication rule)**.** _Fix_ \(k\ge 81\)_, with R,S as above. For integers_ \(t\ge 0\) _and_ \(a,b\ge 1\)_, write_<tbc>

\(N=aR^t,D=2^t,M=bS^t.\)

<tbc>_For_ \(0\le j\le t\)_, define the capped request count_

\(B_j=\sum_{s=0}^j\genfrac(){pt}{2}{j}{s}6^smin\left\{w,\frac{NM}{k^s}\right\}.\) (6)

_Given matrices_ \(U\in\mathbb{Z}^{N\times D}\) _and_ \(V\in\mathbb{Z}^{D\times M}\)_, any_ \(w\ge 1\) _distinct specified entries of UV can be computed with the following operation bounds:_

1. **_Input preparation:_** _D_<sup>3_k_</sup>(_N+M_) _additions and subtractions to prepare linear forms separately in U and in V._<tbc>

2. **_Scalar multiplication:_** _B<sub>t</sub> multiplications of a prepared form in U by one in V._<tbc>

_3._ **_Output reconstruction:_** _O(tB<sub>t</sub>_) _additions and subtractions to recover the requested entries._

_The algorithm generates O(tB<sub>t</sub>_) _request records._

_Proof._ Apply Theorem 2.5 recursively for _t_ steps. Each step has _T=RS_+6_<sup>k</sup>_=(_k_+6)6<sup>_k_-1</sup> child products, so the full recursion has _T<sup>t</sup>_ leaves, each an \(a\times 1\) by \(1\times b\) outer product. We compute the _a_ left input values and _b_ right input values at every leaf, whether or not that leaf receives requests. We then multiply only the pairs needed for requested leaf entries and reconstruct the requested outputs up the recursion tree.

**Input preparation.** By Theorem 2.3, each entry of a child’s left input matrix is a sum of at most 6_k_ signed entries of its parent’s left input matrix. The same holds for the right input matrices. Substituting these expressions through all _t_ levels writes each left input value at a leaf as a sum of<tbc>

