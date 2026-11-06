## 4.3 The data structure, in terms of the parameters

In this subsection, we assemble the boxes into our data structure and bound its costs in terms of the parameters _m_, _L_, and _t_. We will then choose settings for the parameters in Section 4.4. We begin by recalling two notions from Section 2 that the data structure builds on.

The _tiling_ of Section 2.3.4 cuts the product _XY_ into _tiles_. A row block is _N_<sub>0</sub> consecutive rows of _X_, a column block is _N_<sub>0</sub> consecutive columns of _Y_ , and a tile is a band of \(K_0=\lfloor\sqrt{K}\rfloor\) consecutive row blocks together with a band of _K_<sub>0</sub> consecutive column blocks. One run of the recursion computes all \(K_0^2\) block products of a tile at once, each as the product _X<sub>Q</sub>Y<sub>Q</sub>_ for its own subset _Q_. The _encodings_ of Section 2.4.1 are the arrays of the 10_<sup>L</sup>_ numbers \(\Phi_\tau(a)\), one for each leaf \(\tau\), computed from the input array _a_ of a row band, and similarly the numbers \(\Psi_\tau(b)\) computed from the input array _b_ of a column band. We compute an encoding once per band and share it among all the tiles that use that band, and the product at a leaf of a tile is the product of its two encoded numbers.

Our data structure consists of three components:

• the list of the \(K_0^2\) subsets _Q_ assigned to the block products of a tile (recall that this list is the same for every tile),<tbc>

• the encodings of all row bands and all column bands, and<tbc>

• for every tile, the values of all its boxes (the boxes are the same strings in every tile, but their values depend on the input arrays of the tile).

To answer a query for an entry (_XY_)\[_I,J_\], the data structure performs the following three steps:

(1) Find the tile that contains (_I,J_), the subset _Q_ of its block product, and the output string _w_ of (_I,J_).<tbc>

(2) Add up the products at the leaves of order below _t_ contributing to _w_, by reading the two factors of each product from the encodings of the tile.<tbc>

(3) Add to this the values of the \(\alpha_t\) boxes of _w_, which are stored for the tile.

By Lemma 28, the result is (_X<sub>Q</sub>Y<sub>Q</sub>_)\[_w_\]=(_XY_)\[_I,J_\]. We will give the details of the query, as well as the preprocessing, in the proof of Theorem 30 below.

The encodings are indexed by the leaves (Section 2.4.1), and for each tile we store its boxes, with their values, in a standard trie on their strings of _L_ symbols. Thus reading the product at a leaf, or looking up or inserting a box, takes _O(L_) operations.

We will next show that there are at most _m_+1 times as many boxes as there are leaves of order at least _t_, and that the dynamic program described in the technique overview computes their values (a box with _e_ stars being the sum of ten boxes with _e_-1 stars).

**Lemma 29.** _There are at most_ \((m+1)\sum_{d=t}^m\beta_d\) _boxes. Given the two encodings of a tile, we can compute the values of all these boxes, and store them in the trie for that tile, in O(L_) _time and space per box._

_Proof. The count._ A box in which _f_ of the symbols are _P_<sub>0</sub> or stars is obtained from a leaf of order _m-f_ (namely the leaf we get by replacing its stars with _P_<sub>0</sub>) by turning the _e_ lowest symbols _P_<sub>0</sub> of that leaf into stars, for some \(e\le f\). Thus, such a box can be specified by choosing the _f_ levels of these symbols, the number _e_, and a term other than _P_<sub>0</sub> at each of the other _L-f_ levels. There are hence \((f+1)\genfrac(){pt}{2}{L}{f}9^{L-f}=(f+1)\beta_{m-f}\) such boxes, and summing over \(f\le m-t\) gives the upper bound on the number of boxes.

_The values._ We compute the values of the boxes in increasing order of their number of stars. The boxes without stars are the leaves with at most _m-t_ symbols _P_<sub>0</sub>, and the value of each of them is the product of its two numbers in the encodings.

