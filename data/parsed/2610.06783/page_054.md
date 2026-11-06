<tbc>into \(n^{1-\mu}\) blocks of \(n^\mu\) consecutive columns. The (min,+)-product then consists of \(n^{2-2\mu}\) products of two \(n^\mu\times n^\mu\) matrices, one for each pair of blocks. Their entries have absolute value \(\tilde{O}(n^{1-\mu})\le\tilde{O}(n^\mu)\), because \(\mu\ge\frac{1}{2}\), so Theorem 22 computes each of them in \(\tilde{O}((n^\mu)^{3-\varepsilon^\prime/3})\) time, and all of them in \(\tilde{O}(n^{2+\mu-\mu\varepsilon^\prime/3})\) time. This is \(O(n^{2+\mu-\varepsilon_1})\) for any constant \(\varepsilon_1<\mu\varepsilon'/3\), so \[CVX21, Theorem 3.1\] applies, in the deterministic form of Theorem 33, since the algorithm of Theorem 22 is deterministic.

## 5.2 3SUM, APSP, and Exact Triangle with real inputs

**Theorem 35** (Real inputs)**.** _In the real RAM in which the only operations allowed on real numbers are comparisons, additions, and subtractions, Las Vegas algorithms solve the following problems on real inputs:_ 3_SUM on n numbers in O(n_<sup>1.998</sup>) _expected time, and the_ (min,+)_-product of two_ \(n\times n\) _matrices, APSP with no negative cycles, and Exact Triangle in O(n_<sup>2.998</sup>) _expected time. The bounds also hold with probability_ 1-_n_<sup>-_c_</sup> _for any constant c._

The reductions are by Chan, Vassilevska Williams, and Xu \[CVX22\], who reduce the real- valued problems to the counting version of All-Edges Sparse Triangle on graphs with _m_ edges (and real APSP also to the Boolean version). Our version of All-Edges Sparse Triangle in Corollary 16 needs lopsided sparse graphs. To deal with this slight change, we follow the reductions of \[CVX22\] down to the point where the All-Edges Sparse Triangle oracle is called, and change the call. At that point, the reductions only need the oracle to compute _comparison counts_, which we define next. These come from Fredman’s trick \[Fre76\]: \(a'+b'<a+b\) if and only if \(a'-a<b-b'\). This turns a comparison of two sums into a comparison of a number that depends only on the row against a number that depends only on the column.

We first define comparison counts, then restate the reductions of \[CVX22\] as reductions to comparison counts (Lemma 36), and then solve the comparison counts problem: following \[CVX22\], Lemma 37 reduces it to the wanted entries of one thin matrix product using Matoušek’s technique for the dominance product \[Mat91\], and Corollary 38 applies Corollary 26 to that product. The proof of Theorem 35 then adds up the running times. The only randomized steps are in the reductions of \[CVX22\], and the algorithms never output a wrong answer, so they are Las Vegas.

### Comparison counts.

We are given _n row lists_: for every \(r\in[n]\), a list R_<sub>r</sub>_ of at most _d_ real numbers _x_, where each \(x\in\mathcal{R}_r\) has a _color_ \(\chi(x)\in[d]\) associated with it.

Similarly, we are given _n column lists_: for every \(c\in[n]\), a list C_<sub>c</sub>_ of at most _d_ real numbers _y_, each \(y\in\mathcal{C}_c\) again with a color \(\chi(y)\in[d]\) associated with it.

Given a set \(P\subseteq[n]^2\) of (row, column) pairs, we want, for every \((r,c)\in P\), the number

\(\gamma(r,c):=\big|\{(x,y):x\in\mathcal{R}_r,y\in\mathcal{C}_c,\chi(x)=\chi(y),x<y\}\big|.\)

### The reductions.

We follow the reductions of \[CVX22\] down to their two counting problems \[CVX22, Problems 4.1 and 4.5\], which we define in the proof of Lemma 36 below, and turn every call of a counting problem into comparison counts, in place of the triangle-counting instances of \[CVX22, Lemmas 4.3 and 4.7\]. Throughout, \(d\in[n]\) is a parameter, which the proof of Theorem 35 chooses.

**Lemma 36** (after Chan, Vassilevska Williams, and Xu \[CVX22\])**.** _Let_ \(1\le d\le n\).

