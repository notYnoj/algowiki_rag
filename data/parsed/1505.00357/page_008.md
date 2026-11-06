<tbc>particular, represent each key-interval _I_ by its two endpoints. For each key- interval _I_ and integer \(h\le n\), precompute \(\omega(\mathcal{S}(I,h))\), and top(_I,h_), and the _h_’th largest key in _I_. Given these _O(n_<sup>3</sup>) values (computed in _O(n_<sup>3</sup>log_n_) time), the recurrence for opt(S(_I,h_)) can be evaluated in _O(n_) time. In particular, for line (ii), one can enumerate all _O(n_) pairs \((k,h_k^\prec)\) in _O(n_) time total, and, for each, compute \(I_k^\prec\) and \(I\backslash I_k^\prec\) in _O_(1) time. Each base case can be recognized and handled (by a cost-0 leaf) in _O_(1) time, giving total time _O(n_<sup>4</sup>). This proves Thm. 1 when all probabilities in \(\beta\) are distinct; Sec. 3.1 finishes the proof.

## 3.1 Perturbation argument; proofs of Theorems 1 and 3<sup>7</sup>

Here we show that, without loss of generality, in looking for an optimal search tree, one can assume that the key probabilities (the \(\beta_i\)’s) are all distinct. Given any instance \(\mathcal{I}=(\mathcal{K},\mathcal{Q},\mathcal{C},\alpha,\beta)\), construct instance \(\mathcal{I}'=(\mathcal{K},\mathcal{Q},\mathcal{C},\alpha,\beta')\), where \(\beta'_j=\beta_j+j\varepsilon\) and \(\varepsilon\) is a positive infinitesimal (or \(\varepsilon\) can be understood as a sufficiently small positive rational). To compute (and compare) costs of trees with respect to \(\mathcal{I}'\), maintain the infinitesimal part of each value separately and extend linear arithmetic component-wise in the natural way:

1. Compute \(z\times(x_1+x_2\varepsilon)\) as \((zx_1)+(zx_2)\varepsilon\), where _z,x_<sub>1</sub>_,x_<sub>2</sub> are any rationals,<tbc>

2. compute \((x_1+\varepsilon x_2)+(y_1+\varepsilon y_2)\) as \((x_1+x_2)+(y_1+y_2)\varepsilon\),<tbc>

**Lemma 7.** _In the instance_ \(\mathcal{I}'\)_, all key probabilities_ \(\beta'_i\) _are distinct. If a tree T is optimal w.r.t._ \(\mathcal{I}'\)_, then it is also optimal with respect to_ I.

_Proof._ Let _A_ be a tree that is optimal w.r.t. \(\mathcal{I}'\). Let _B_ be any other tree, and let the costs of _A_ and _B_ under \(\mathcal{I}'\) be, respectively, \(a_1+a_2\varepsilon\) and \(b_1+b_2\varepsilon\). Then their respective costs under I are _a_<sub>1</sub> and _b_<sub>1</sub>. Since _A_ has minimum cost under \(\mathcal{I}'\), \(a_1+a_2\varepsilon\le b_1+b_2\varepsilon\). That is, either _a_<sub>1</sub>_\<b_<sub>1</sub>, or _a_<sub>1</sub>=_b_<sub>1</sub> (and \(a_2\le b_2\)). Hence \(a_1\le b_1\): that is, _A_ costs no more than _B_ w.r.t. I. Hence _A_ is optimal w.r.t. I. \(\square\)

Doing arithmetic this way increases running time by a constant factor.<sup>6</sup> This completes the proof of Thm. 1. The reduction can also be used to avoid the significant effort that Anderson et al. \[1\] devote to non-distinct key probabilities.

For computing optimal _binary split trees_ for unrestricted queries, the fastest known time is _O(n_<sup>5</sup>), due to \[9\]. But \[9\] also gives an _O(n_<sup>4</sup>)-time algorithm for the case of distinct key probabilities. With the above reduction, the latter algorithm gives _O(n_<sup>4</sup>) time for the general case, proving Thm. 3. <sup>7</sup>

<sup>6</sup> For an algorithm that works with linear (or _O_(1)-degree polynomial) functions of \(\beta\). <sup>7</sup> ERRATUM (MARCH 2021): This reasoning is incorrect for binary split trees, because perturbing the key probabilities can change which key is the maximum- likelihood key, changing the space of valid search trees.

