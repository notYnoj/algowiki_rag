## Notions from Section 2.

We keep the recursion, the tiling, and the encodings of Sections 2.3 and 2.4.1, and we use the terminology of Sections 2.3.2 and 2.4.3 as defined there: the leaves contributing to an output string, its private leaf, the order of a leaf, and the counts \(\alpha_d\) and \(\beta_d\). For convenience, we briefly recall these notions here.

• A _leaf_ \(\tau=\tau_1\cdots\tau_L\) is a string of _L_ terms of Schönhage’s identity, where \(\tau_\ell\) is the term chosen at _level_ \(\ell\) of the recursion (Section 2.3.1). Throughout this section, we compare levels by their indices: we say that level \(\ell\) is _lower_ than level \(\ell'\) if \(\ell<\ell'\), so that the lowest level is the first level of the recursion.<tbc>

• An _output string w_ with _inner set Q_ has the variable _z_<sub>0</sub> at each of the _m_ levels of _Q_, and one of the variables _z<sub>ij</sub>_ at every other level. It indexes the entry (_X<sub>Q</sub>Y<sub>Q</sub>_)\[_w_\] of the product _X<sub>Q</sub>Y<sub>Q</sub>_ (Section 2.3.3).<tbc>

• A leaf _contributes to w_ if it chooses _P<sub>ij</sub>_ at every level where _w_ has _z<sub>ij</sub>_, while it may choose any of the ten terms at the levels of _Q_, where _w_ has _z_<sub>0</sub> (Section 2.3.2).<tbc>

• The _private leaf_ of _w_ is the leaf contributing to _w_ that chooses _P_<sub>0</sub> at every level of _Q_ (Section 2.4.3).<tbc>

• The _order_ of a leaf is _m_ minus the number of levels at which it chooses _P_<sub>0</sub>. For a leaf contributing to _w_, this is the number of levels of _Q_ at which it chooses a term other than _P_<sub>0</sub> (Section 2.4.3).<tbc>

• A _tile_ consists of a _band_ of \(K_0=\lfloor\sqrt{K}\rfloor\) row blocks of _X_ together with a band of _K_<sub>0</sub> column blocks of _Y_ (Section 2.3.4), and the _encoding_ of a band is the array of the 10_<sup>L</sup>_ numbers \(\Phi_\tau(a)\), or \(\Psi_\tau(b)\), computed from its input array (Section 2.4.1). We will recall both in more detail in Section 4.3.

As in Section 2.4.3, all output strings in this section have inner sets of exactly _m_ elements, so that they index the \(M=KN_0^2\) entries of the _K_ products _X<sub>Q</sub>Y<sub>Q</sub>_ of a tile, and we will use that \(M=\beta_0\le 10^L\). For a leaf \(\tau\) of a tile with input arrays _a_ and _b_, we call \(\Phi_\tau(a)\Psi_\tau(b)\) the **_product at_** \(\tau\). We read its two factors from the encodings of the tile (Section 2.4.1), and by (2) and Lemma 9, (_X<sub>Q</sub>Y<sub>Q</sub>_)\[_w_\] is the sum of the products at the leaves contributing to _w_. The one change from Section 2 is that _L_ is now any integer with \(L\ge 10m\), and we call _c=L/m_ the **_ratio_**.

## Technique overview.

The pruned recursion of Section 2.4 needs to know _W_ in advance, since it visits exactly the leaves that the wanted entries need. When the queries arrive one at a time, we must instead prepare for every possible output entry.

Recall that our preprocessing must take less time than it takes to write down _XY_ . This means it stores fewer than one number per entry of _XY_ , so each number that it stores must be useful for many different entries. Meanwhile, a query must take far fewer than the _D_ operations that it would take to compute the entry directly as an inner product. In Section 2, the running time had three parts: the leaves of small order, the leaves of large order, and the encodings (Lemma 11 and Section 2.4.4). Our data structure will divide these parts between the queries and the preprocessing. Each output entry uses only a few of the leaves of small order, so a query may just read them one by one. By contrast, each output entry may use many leaves of large order, but there are not too many such leaves in total, and each of them is shared by many output entries. Thus, in preprocessing we will add them up in advance, in groups which can be quickly summed during queries. The preprocessing also computes the encodings, once.

The 10_<sup>m</sup>_ leaves contributing to an output string form a cube: at each level of the inner set _Q_ of the output string, they choose any of the ten terms, and at each other level, they agree with the private leaf of the output string. Every one of these leaves, other than the private leaf, also<tbc>

