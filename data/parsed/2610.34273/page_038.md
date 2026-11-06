**Lemma 5.6** (soundness of the rules)**.** _For every integer_ \(n\ge 3\) _and all_ \(X,Y\in\mathcal{F}_n\)_, the relation_ \(X\unknown_{\mathrm{poly},n}Y\) _implies_ \(\mathrm{ev}(X)\triangle\mathrm{ev}(Y)\).

_Proof._ The full algebraic identities follow from the coordinate pairings for \(\oplus_K\) and \(\otimes_K\). Reordering a partial sum only reorders the matched sectors on its two unshared legs. Distributing a product of partial sums pairs the two block labels; the shared coordinates are the same paired coordinates on both sides. For an edge product, pairing indices identifies the two conditions _u+v=q_-1 and \(u'+v'=t-1\) with

\((tu+u')+(tv+v')=qt-1.\)

This proves the edge identity. In the repeated-block identity, the edge index becomes the common block label; reversing it on one unshared leg changes the anti-diagonal representative of the edge atom to the diagonal one. Hence all identities in rule (ii) are valid local isomorphisms.

Block deletion is coordinate projection. The restriction from a full sum to a partial sum maps each shared coordinate in either full-sum sector to the corresponding shared coordinate, and leaves the two unshared sectors separate. For polynomial truncation, put \(D'=1+\sum_{i=1}^{n-1}(b_i-1)\). Keep input indices _u<sub>i</sub>\<b<sub>i</sub>_ and keep output indices \(D-D',\dots,D-1\), relabeling the latter by subtracting \(D-D'\). The support equation \(\sum_{i=1}^nu_i=D-1\) becomes the one with right-hand side \(D'-1\) for C_<sub>n</sub>_(**b**). Interpolation follows from Lemma 4.2, after reversing the output coordinate. For the star restriction, a term in the edge product has input indices _u<sub>i</sub>_ and, at leg _n_, indices _v<sub>i</sub>=a<sub>i</sub>_-1-_u<sub>i</sub>_. Send the coordinate (_v_<sub>1</sub>_,...,v_<sub>_n_-1</sub>) at leg _n_ to \(e_{v_1+\cdots+v_{n-1}}^{(D)}\). This gives precisely the reflected polynomial support and coefficient one for each input tuple.

The construction in Lemma 4.8 acts identically on every shared leg. Converting its source and target blocks to reflected atoms only changes the unshared output coordinates. It therefore proves the concavity rule, including the rule with a common partial summand: on its unshared coordinate sectors, extend the local maps by the identity.

For tripling, write _c=h+S_. In the source atom C_<sub>n</sub>_(**a**,3_h+S_), let \(s=\sum_{i=1}^{n-2}u_i\). The last two indices satisfy<tbc>

\(s+y+z=3h+2S-1,0\le y<3h+S,0\le z<3h+2S.\)

<tbc>Partition the _y_ coordinates into the integer intervals<tbc>

\([0,h-1],[h,2h+S-1],[2h+S,3h+S-1],\)

<tbc>and pair them, in this order, with the _z_ intervals

\([2h+S,3h+2S-1],[h+S,2h+S-1],[0,h+S-1].\)

Give weight 1 to the middle _y_ interval, weight -1 to the middle _z_ interval, and weight zero elsewhere. If _y\<h_, then \(z\ge 2h+S\); if \(y\ge 2h+S\), then _z\<h+S_. Thus a middle _z_ coordinate requires a middle _y_ coordinate. Every supported term has nonnegative weight, and weight zero retains just the three paired sectors.

In the first sector subtract 2_h+S=h+c_ from _z_; in the middle sector subtract _h_ from _y_ and _c_ from _z_; in the last sector subtract _h+c_ from _y_. In every case the support equation becomes

\(s+y'+z'=c-1.\)

The last two dimensions are respectively (_h,c_), (_c,h_), and (_h,c_). These are exactly the three atoms on the left of the tripling rule, with all shared coordinates unchanged. Reordering the<tbc>

