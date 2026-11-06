The new idea (Section 2.4) is to visit only the leaves of the recursion tree that the wanted entries from _W_ need. A priori, it is not clear that this reduces the number of leaves by much, or that the encoding and decoding phases stay cheap. Both nonetheless turn out to hold, for two reasons.

First, we observe that the additions in the encoding phase that prepare the leaves depend on _X_ alone or on _Y_ alone (as is the case in all tensor rank decompositions). Since each _X_ block is multiplied with every _Y_ block, we only need to compute these additions once for each _X_ block and may share them among many calls to our algorithm (and similarly for _Y_ ). One reason for the requirement \(N\ge D^{18}\) is to ensure that this total cost will be negligible (Section 2.4.1).

Second, we prune the recursion tree, and make a recursive call only when one of its outputs is wanted by _W_. This way, the running time is governed by the union of the sets of leaves that the wanted entries need. Most of the analysis goes into bounding this union (Section 2.4.3). We will see that every output entry has a private leaf that no other entry needs, but that all its other leaves are shared by many entries. We will characterize each leaf by how often one needs to pick each of the two matrix products from Schönhage’s identity to get to it in the recursion tree, and find a trade-off: choosing one of the matrix products leads to a relatively small number of leaves, while choosing the other increases how many output entries share each leaf. Balancing the two, we will find that a set of \(N^2/\sqrt{D}\) wanted entries only needs about _N_<sup>2</sup>_/D_<sup>1/18</sup> leaves in all, and paying _O_(log<sup>2</sup>_D_) operations per leaf gives Theorem 5.

## 2.1 Strassen’s recursive algorithm

We use the recursive approach for multiplying matrices introduced by Strassen \[Str69\]. We begin by recalling his algorithm for intuition. The key behind his algorithm is an identity that shows how to multiply two \(2\times 2\) matrices _A_ and _B_ using only seven multiplications instead of eight. It forms seven products, each of a linear combination of the entries of _A_ with a linear combination of the entries of _B_, and then obtains each entry of _AB_ as a linear combination of those seven products. Recall that, writing _A_=(_a<sub>ij</sub>_) and _B_=(_b<sub>ij</sub>_), the seven products are<tbc>

\(S_1=(a_{11}+a_{22})(b_{11}+b_{22}),S_5=(a_{11}+a_{12})b_{22},S_2=(a_{21}+a_{22})b_{11},S_6=(a_{21}-a_{11})(b_{11}+b_{12}),S_3=a_{11}(b_{12}-b_{22}),S_7=(a_{12}-a_{22})(b_{21}+b_{22}),S_4=a_{22}(b_{21}-b_{11}),\text{(1)}\)

<tbc>and the product is

\(AB=\left(\begin{array}{ c c }
S_1+S_4-S_5+S_7 & S_3+S_5 \\
S_2+S_4 & S_1-S_2+S_3+S_6
\end{array}\right).\)

To use this identity to multiply \(N\times N\) matrices _A,B_ for larger _N_, we interpret _A_ and _B_ as \(2\times 2\) block matrices (whose entries are \(N/2\times N/2\) matrices), then multiply them as in the identity, i.e., we form seven pairs of linear combinations of the blocks of _A_ and of _B_, recursively multiply each pair, and then assemble the four blocks of _AB_ from the seven results. When _N_=2_<sup>L</sup>_, the recursion tree (Figure 2) has _L_ levels, and 7_<sup>L</sup>_ leaves, one for each choice of one of the seven products at each level. The multiplications take place at the leaves, meaning there are 7_<sup>L</sup>=N_<sup>log<sub>2</sub>7</sup>_\<N_<sup>2.81</sup> multiplications in total. We call the additions on the way down, which prepare the leaves and are computed from _A_ alone and from _B_ alone, the **_encoding_**, and those on the way up, which assemble the product, the **_decoding_**.

