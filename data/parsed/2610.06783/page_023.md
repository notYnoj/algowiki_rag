<tbc>each an \(N_0\times D\) by \(D\times N_0\) product, and one run of Full computes _K_ such products at once. We use each run on a \(K_0\times K_0\) grid of block products, where \(K_0:=\lfloor\sqrt{K}\rfloor\): we group the row blocks into **_bands_** of _K_<sub>0</sub> consecutive blocks, and similarly the column blocks, and we call a row band together with a column band a **_tile_** (Figure 5). Each tile is one run of Full. We fix \(K_0^2\le K\) distinct subsets of {1_,...,L_} of size _m_, one for each block product of the grid, the same in every tile. In a tile, let _X<sub>Q</sub>_ and _Y<sub>Q</sub>_ be the row block and the column block of the block product with subset _Q_, and let _X<sub>Q</sub>=Y<sub>Q</sub>_=0 for the other subsets _Q_. Then one run of Full computes all \(K_0^2\) block products of the tile (Lemma 9), and running it on every tile computes all of _XY_ .

We pair the blocks in a grid like this, rather than arbitrarily, so that the left input array of a tile depends only on its row band and the right one only on its column band. This will let us share their encodings among tiles in Section 2.4.1 below. (To make the bands fit, we first pad _N_ to a multiple of _K_<sub>0</sub>_N_<sub>0</sub> with zero rows of _X_ and zero columns of _Y_ , which at most doubles _N_ since \(N\ge K_0N_0\), as we will see in Section 2.4.4.)

Before moving on, let us compute the number of operations performed by this algorithm. Let \(M:=KN_0^2\) denote the number of output entries among all _K_ products of a tile. Since \(K_0\ge\sqrt{K}/2\), there are \((N/K_0N_0)^2\le 4N^2/M\) tiles. Thus, recalling the operation count of a single tile from Section 2.3.1, the whole product takes \(O\big(\frac{N^2}{M}L\cdot 10^L\big)\) operations, that is, \(O(L\cdot 10^L/M)\) per entry of _XY_ . One can calculate that this is _N_<sup>2</sup>poly(_L_) in total when _L_=10_m_, but about _N_<sup>2</sup>_D_<sup>0.2</sup> for our choice _L_=19_m_. We nonetheless choose _L_=19_m_, and in Section 2.4.3 below we explain why this is needed for our sparsity arguments.

## 2.4 Extracting only the desired entries

In this subsection, we present the main new idea of this paper. Our goal is now to compute only the wanted entries of _XY_ , i.e., those at the positions in _W_ , which is a set of size \(|W|\le N^2/\sqrt{D}\). We will modify the algorithm of Section 2.3 in two ways. First, we will observe that the encoding (step (2)) of each input array depends only on that array and not the other, and that each input<tbc>

Y: 6 column blocks, in 2 bands of Ko = 3
X: 6 row blocks, in 2 bands of Ko = 3
4 tiles
the tile of row band 2 and column band 1: K 2 = 9 block products XQYQ, all from one left input array (row band 2) and one right input array (column band 1)
Q1
Q2
Q3
Q4
Q5
Q6
Q7
Q8
Q9

Figure 5: The tiling, drawn for _N_=6_N_<sub>0</sub> and _K_<sub>0</sub>=3. A block product, a row block of _X_ times a column block of _Y_ , holds \(N_0^2\) entries of _XY_ . A tile, a band of _K_<sub>0</sub> row blocks together with a band of _K_<sub>0</sub> column blocks, is one run of Full, which computes its \(K_0^2\le K\) block products, each with its own subset _Q_ (_Q_<sub>1</sub>_,...,Q_<sub>9</sub> shown in the highlighted tile).

