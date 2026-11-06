**Definition 4.1.** The (median) edit distance \(\delta_E(X_1,\dots,X_k)\) of _k_ strings _X_<sub>1</sub>_,...,X<sub>k</sub>_ is the minimum total number of edits (insertions, deletions, and substitutions) needed to make all strings _X<sub>i</sub>_ equal some string _X_<sup>∗</sup>. That is, \(\delta_E(X_1,\dots,X_k)=min_{X^*}\sum_{i=1}^k\delta_E(X_i,X^*)\).

For the (median) edit distance between _k_ strings, we show that allowing \((1+\epsilon)\)-approximation gives an algorithm circumventing the bound in Theorem 6.5:

**Theorem 4.2.** _Given k=O_(1) _straight-line programs_ **G**_<sub>X<sub>i</sub></sub> of total size n generating strings X<sub>i</sub> of total length N\>_0 _and a parameter_ \(\epsilon\in(0,1]\)_, an integer between_ \(\delta_E(X_1,\dots,X_k)\) _and_ \((1+\epsilon)\delta_E(X_1,\dots,X_k)\) _can be computed in_ \(\widetilde{O}\left(\epsilon^{-O(k)}n^{k/2}N^{k/2}\right)\) _time._

To prove the above theorem, we use a different set of techniques than in the two-string case. Most approaches for speeding up the textbook DP algorithm for two (compressible) strings, including the aforementioned results in this paper, rely on the ability to perform computations involving DIST matrices efficiently. These computations crucially depend on the fact that DIST matrices satisfy the Monge property. However, for the natural high-dimensional generalization of DIST matrices, we do not know of any analog of the Monge property they satisfy that allows us to perform similar computations even for three-string similarity problems. Indeed, most natural generalizations of the Monge property seem to not hold even in the three-string setting (see Section 9 for more details). Thus, it appears unlikely that, for example, an algorithm that partitions the DP table into boxes and computes the DP values on the boundary of each box using computations involving DIST matrices would be substantially more efficient than the textbook edit-distance algorithm, even in the three-string setting.

This motivates us to instead use the window-respecting alignment scheme that has appeared in approximation algorithms for edit distance (e.g., \[CDG<sup>+</sup>18, GRS20\]).

## 4.1 Window-Respecting Alignments

We will assume that \(\delta_E(X_1,\dots,X_k)\) lies between _D_ and 2_D_ for some known _D_ at the loss of a log_N_ factor in the runtime. We partition _X_<sub>1</sub> into \(\lceil|X_1|/\tau\rceil\) disjoint windows _W_<sub>1,1</sub> to \(W_{1,N/\tau}\) each of length \(\tau\) (without loss of generality; we could always e.g. pad each string with an equal amount of a new dummy character to ensure |_X_<sub>1</sub>| is a multiple of \(\tau\), without asymptotically affecting their size or compression size). That is, \(W_{1,j}=X_1[(j-1)\tau+1,j\tau]\).

We define for _X_<sub>2</sub>_,...,X<sub>k</sub>_ possibly overlapping windows indexed by (i) \(\Delta\), a guess for the (signed) difference between the length of _W_ and the corresponding window in _X_<sub>1</sub> and (ii) the starting position _p_ of the window. More formally, the windows are indexed by \(W_{i,\Delta,p}\). Throughout the section, let \(\sigma:=max\{\lfloor\epsilon D\tau/|X_1|\rfloor,1\}\) and _R<sub>d</sub>(x_) denote _x_ rounded down to the nearest multiple of \(\sigma\). Then \(W_{i,\Delta,p}=X_i[p\sigma+1\dots R_d(p\sigma+\tau+\Delta)]\) (or is the empty string "starting" at position \(p\sigma+1\) if \(R_d(min\{p\sigma+\tau+\Delta,|X_i|\})<p\sigma+1\)). If \(R_d(p\sigma+\tau+\Delta)>|X_1|\), \(W_{i,\Delta,p}\) is not included in our set of windows. We will define this window for:

• All \(\Delta\) in \(\{0,1,-1,\lfloor(1+\epsilon)\rfloor,-\lfloor(1+\epsilon)\rfloor,\lfloor(1+\epsilon)^2\rfloor,\dots\lfloor(1+\epsilon)^{\lceil log_{1+\epsilon} 2\tau/\epsilon^2\rceil}\rfloor\}\cup\{-\tau\}\) for which \(\tau+\Delta\ge 0\),<tbc>

• All _p_ from 0 to \(\lfloor|X_i|/\sigma\rfloor\).

It suffices to consider windows of size at most \(2\tau/\epsilon^2\) by the following lemma:

**Lemma 4.3.** _Given X_<sub>1</sub>_,X_<sub>2</sub>_,...,X<sub>k</sub> and a parameter_ \(\tau\)_, for_ \(J=|X_1|/\tau\)_, let X_<sup>∗</sup> _be the string such that_ \(\delta_E(X_1,X_2,\dots X_n)=\sum_i\delta_E(X_i,X^*)\)_. There exists a partition of each X_<sub>1</sub> _into substrings_ \(\{X_{1,j}\}_{j\in[J]}\)_, disjoint substrings of the other X<sub>i</sub>,_ \(\{X_{i,j}\}_{j\in[J]}\)_, and a partition of X_<sup>∗</sup> _into substrings_ \(\{X_j^*\}_{j\in[J]}\) _such that:_

• \(|X_{1,j}|=\tau\) _for all j._<tbc>

• _For any j and_ \(j<j'\)_, X<sub>i,j</sub> appears before_ \(X_{i,j^\prime}\) _in X<sub>i</sub>._<tbc>

• \(max_{i,j}|X_{i,j}|\le 2\tau/\epsilon^2\).<tbc>

• \(\sum_{j\in[J]}\delta_E(X_{ij},X_j^*)+|X_i|-\sum_{j\in[J]}|X_{i,j}|\le(1+3\epsilon)\delta_E(X_i,X^*),\)<tbc>

<tbc>_Which implies:_<tbc>

<tbc>\(\sum_{j\in[J]}\delta_E(X_{1,j},X_{2,j},\dots,X_{k,j})+\sum_{i>1}(|X_i|-\sum_{j\in[J]}|X_{i,j}|)\le(1+3\epsilon)\delta_E(X_1,X_2,\dots X_k).\)<tbc>

<tbc>_That is, the cost of the alignment that aligns X_<sub>1_,j_</sub> _with each X<sub>i,j</sub>, and then deletes all characters in X_<sub>2</sub> _to X<sub>k</sub> that are unaligned with some X_<sub>1_,j_</sub> _is at most_ \((1+3\epsilon)\delta_E(X_1,X_2,\dots X_k)\).

