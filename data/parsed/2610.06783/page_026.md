problematic, since it is more than the _D_ multiplications that computing that output entry directly, as an inner product, would take. Because of this, it is important that we do not simply count the leaves of each output string of _U_ separately. Instead, we will find that most leaves contributing to an output string also contribute to many other output strings, and there are few such leaves in total.

Let us begin by classifying leaves by how many levels they choose _P_<sub>0</sub> at (as opposed to one of the _P<sub>ij</sub>_s). As we mentioned above, the leaves contributing to an output string with inner set _Q_ are the 10_<sup>m</sup>_ leaves that choose any term at each of the _m_ levels of _Q_, but _P<sub>ij</sub>_ at every level outside _Q_ where the output string has _z<sub>ij</sub>_. We call the one that chooses _P_<sub>0</sub> at every level of _Q_ the **_private leaf_** of the output string. The private leaf contributes to no other output string, since an output string with a different inner set requires a term other than _P_<sub>0</sub> at some level of _Q_, and an output string with the same inner set but a different outer part (a different _z<sub>ij</sub>_ at some level outside _Q_) requires a different term there.

To describe how close a leaf is to being a private leaf, we define the **_order_** of a leaf as _m_ minus the number of levels at which it chooses _P_<sub>0</sub>. A leaf contributing to an output string chooses _P_<sub>0</sub> only at levels of the output string’s inner set, so its order is at least 0. Since _P_<sub>0</sub> is the only term that serves the inner product alone, this is the classification described in the technique overview: the order of a leaf contributing to an output string is the number of levels of the string’s inner set at which the leaf takes one of the terms _P<sub>ij</sub>_ shared with the outer product. The only leaf of order 0 contributing to an output string is its private leaf. Beyond this, exactly

\(\alpha_d:=\genfrac(){pt}{2}{m}{d}9^d\)

leaves of order _d_ contribute to an output string, namely its private leaf with _P_<sub>0</sub> replaced by one of the nine other terms at _d_ of the levels of _Q_ (Figure 6).

The total number of leaves of order _d_ in the entire recursion tree is<tbc>

\(\beta_d:=\genfrac(){pt}{2}{L}{m-d}9^{L-m+d}\)

<tbc>since we can choose the _m-d_ levels with _P_<sub>0</sub> and one of the nine other terms at every other level. In particular, \(\beta_0=\genfrac(){pt}{2}{L}{m}9^{L-m}=M\) since the leaves of order 0 are exactly the private leaves, and there is one per output string. A leaf of order _d_ contributes to \(\genfrac(){pt}{2}{L-m+d}{d}\) output strings, one for each inner set of size _m_ that contains the _m-d_ levels at which it chooses _P_<sub>0</sub>. Indeed, \(M\alpha_d=\beta_d\genfrac(){pt}{2}{L-m+d}{d}\), as both sides count the pairs of an output string and a leaf of order _d_ contributing to it. Finally, if _L_=19_m_, then for \(1\le d\le m\) we have

\(\frac{\beta_d}{\beta_{d-1}}=\frac{9(m-d+1)}{L-m+d}\le\frac{9m}{18m+1}<\frac{1}{2},\text{so}\beta_d\le 2^{-d}M.\) (5)

As in the technique overview, leaves of higher order are more numerous per output string, but each of them is shared by more output strings, and by (5) there are fewer of them in all. Below, we count all the leaves of order _d\>m/_9, whether or not they contribute to a string of _U_, and this count will be small enough since the \(\beta_d\) decrease geometrically. By the ratio in (5), this requires _m_ to be well below _L/_10: at _m≈L/_10, the choice that computes the whole product cheaply (Section 2.3.4), the ratio would be close to 1 for small _d_, so the \(\beta_d\) would stay about _M_ instead of decreasing, and the count would give no saving. A small _m_ also makes _D_=4_<sup>m</sup>_ small compared with _N_<sub>0</sub>=3<sup>18_m_</sup> (about \(N_0^{0.07}\)), and since a tile must fit into the product, _N_ must be a<tbc>

