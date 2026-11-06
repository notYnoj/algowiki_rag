<tbc>listing \[98\], as well as approximate \[2, 37\] and dynamic problems \[6, 98\], even in planar graphs \[3\]. In fact, many such problems have been shown not merely to be APSP-hard, but APSP-equivalent.

The two secondary hypotheses we consider can both be seen as strengthenings of the APSP hypothesis concerning graphs with _small_ weights and _no_ weights. (In fact, the restriction to small-weight instances is a common secondary pattern, see e.g. the Strong 3SUM \[10\], Strong Zero Triangle \[2\] and Strong Min-Plus Convolution \[33\] Hypotheses.) Specifically, the fastest-known algorithm for graphs with weights in {0_,...,u_} runs in time \(\tilde{O}(n^\omega u)\) \[9\], where \(2\le\omega<2.372\) is the matrix multiplication exponent \[8\]. Thus, for a universe of size \(u=n^{3-\omega}\) the fastest-known algorithms take cubic time _n_<sup>3-_o_(1)</sup>, and it is plausible to hypothesize that this is best-possible. Chan, Vassilevska W., and Xu \[35\] first proposed this as the following hardness assumption, which has become the basis for several conditional lower bounds \[35, 66\]:

**Hypothesis 1.2** (Strong APSP)**.** _For every constant_ \(\epsilon>0\)_, APSP on graphs with weights in_ \(\{0,\dots,n^{3-\omega}\}\) _cannot be solved in time_ \(O(n^{3-\epsilon})\).

Conversely, APSP on graphs with weights smaller than \(n^{3-\omega}\) and therefore also _unweighted_ directed graphs is known to be in subcubic time. The fastest-known algorithm for this problem is due to Zwick \[104\] and runs in time \(\tilde{O}(n^{2+\mu})=\tilde{O}(n^{2.528})\). This running time depends on a rectangular matrix multiplication constant\(^40.5\le\mu\le 0.528\) and becomes \(\tilde{O}(n^{2.5})\) if \(\omega=2\). This time bound has not been challenged for more than 20 years, which recently led Chan, Vassilevska W., and Xu \[33\] to hypothesize that Zwick’s algorithm is best-possible.

**Hypothesis 1.3** (Directed Unweighted APSP)**.** _For every constant_ \(\epsilon>0\)_, APSP on directed unweighted graphs cannot be solved in time_ \(O(n^{2+\mu-\epsilon})\).

This hypothesis turns out to be surprisingly powerful--it is equivalent to various \(\tilde{O}(n^{2+\mu})\)-time problems \[33\], and conditionally resolves the complexity of many well-studied graph problems with "intermediate" complexity; see the discussion below in Section 1.3.

### Min-Plus Product.

To relate these three hypotheses, it is helpful to introduce some more background. The _min-plus product_ of two matrices _A_ and _B_ of size \(n_1\times n_2\) and \(n_2\times n_3\), respectively, is the matrix _A∗B_ of size \(n_1\times n_3\) defined by (_A∗B_)\[_i,j_\]=min_<sub>k</sub>(A_\[_i,k_\]+_B_\[_k,j_\]). We refer to the problem of computing _A∗B_ as the _Min-Plus Product_ problem, and we denote its complexity by MinPlus(_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>). We sometimes annotate bounds on the maximum entry _u_ in the three matrices by MinPlus(_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>|_u_). It is a long- known fact that the complexity of APSP is _exactly_ MinPlus(_n,n,n_) (up to _n_<sup>_o_(1)</sup> factors). Via two elegant reductions \[90, 36\] one can similarly give equivalent characterizations of the Strong and Directed Unweighted APSP Hypotheses in terms of some Min-Plus Product problems:

**Hypothesis 1.4** (APSP)**.** \(\mathrm{MinPlus}(n,n,n)=n^{3\pm o(1)}\).

**Hypothesis 1.5** (Strong APSP \[90\])**.** \(\mathrm{MinPlus}(n,n,n|u\le n^{3-\omega})=n^{3\pm o(1)}\).

**Hypothesis 1.6** (Directed Unweighted APSP \[33\])**.** \(\mathrm{MinPlus}(n,n^\mu,n|u\le n^{1-\mu})=n^{2+\mu\pm o(1)}\).

From these characterizations it is easy to read off that, when \(\omega=2\), the Directed Unweighted APSP Hypothesis implies the Strong APSP Hypothesis.<sup>5</sup> In summary, the three assumptions get _increasingly stronger_--i.e., the Directed Unweighted APSP Hypothesis implies the Strong APSP Hypothesis (if \(\omega=2\)) which in turn implies the APSP Hypothesis.

<sup>4</sup>Namely, the constant \(\mu\) satisfying that \(\omega(1,\mu,1)=1+2\mu\), where \(\omega(\cdot,\cdot,\cdot)\) is the rectangular matrix multiplication exponent. <sup>5</sup>Note that \(\mathrm{MinPlus}(n,\sqrt{n},n|u\le\sqrt{n})=O(n\cdot\mathrm{MinPlus}(\sqrt{n},\sqrt{n},\sqrt{n}|u\le\sqrt{n}))\). Thus, \(\mathrm{MinPlus}(n,n,n|u\le n)=O(n^{3-\epsilon})\) implies that \(\mathrm{MinPlus}(n,\sqrt{n},n|u\le\sqrt{n})=O(n^{2.5-\epsilon/2})\).

