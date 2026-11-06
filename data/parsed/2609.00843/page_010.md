We next give an example of local CDFs and tile offsets. Let the input array be _A_=(3,1,2,1,3,0,1), the range size be _R_=4, and the tile width be _T_=2. Tile 0 handles values 0 and 1, whereas tile 1 handles values 2 and 3. The histogram, local CDF, and tile offset of each tile are shown in  1. For tile 0, the local CDF is (1,4), so value 0 is written at within-tile position _p_=0 and value 1 at positions _p_=1,2,3. For tile 1, the offset is 4 and the local CDF is (1,3), so value 2 is written at global position 4 and value 3 at positions 5 and 6. The resulting output is therefore (0,1,1,1,2,3,3). As this example illustrates, the proposed algorithm does not compute the rank of every input element; it determines the output interval of each value from a local CDF and writes values through parallel processing over output positions.

## 3.2 Correctness and Complexity Analysis

Correctness follows from the facts that a local CDF correctly represents output intervals within a tile, tile offsets correctly position the tiles relative to one another, and output generation uniquely selects the value corresponding to each output position. Let _c<sub>v</sub>_ be the number of occurrences of value _v_. For tile _t_, let _b<sub>t</sub>_ be its starting value, _w<sub>t</sub>_ its width, and _C<sub>t</sub>_\[0_..w<sub>t</sub>_-1\] its local CDF. For convenience, define _C<sub>t</sub>_\[-1\]=0.

**Lemma 1** (Correctness of the local CDF)**.** _After local-CDF construction, for every tile t and every_ \(x\in[0,w_t)\),

\(C_t[x]=\sum_{j=0}^xc_{b_t+j}.\)

_Proof._ During histogram construction, one is added to bin _x_ of the tile histogram if and only if an input value _A<sub>i</sub>_ belongs to tile _t_, that is, if there exists an _x_ such that _A<sub>i</sub>=b<sub>t</sub>+x_. Therefore, before the prefix- sum computation, entry _x_ of the tile histogram is _c_<sub>_b<sub>t</sub>+x_</sub>. The prefix-sum computation that constructs the local CDF consequently makes entry _x_ equal to the sum of the occurrence counts from entry 0 through entry _x_. The lemma follows.

**Lemma 2** (Correctness of tile offsets)**.** _The value O_\[_t_\] _obtained by Algorithm 6 is equal to the number of input elements whose values are smaller than the range handled by tile t; that is,_<tbc>

\(O[t]=\sum_{u=0}^{b_t-1}c_u.\)

<tbc>_Proof._ Let _N<sub>s</sub>_ be the number of elements in tile _s_. By Lemma 1, _N<sub>s</sub>=C<sub>s</sub>_\[_w<sub>s</sub>_-1\]. Algorithm 6 computes _O_\[_t_\] as the prefix sum of _N<sub>s</sub>_ over tiles 0 through _t_-1. Because the tiles handle disjoint intervals in<tbc>

\begin{tabular}{ccccc}
Tile & Values & Histogram & Local CDF & Offset \\
0 & 0,1 & (1,3) & (1,4) & 0 \\
1 & 2,3 & (1,2) & (1,3) & 4 \\
\end{tabular}

1: Example of local CDFs and tile offsets

