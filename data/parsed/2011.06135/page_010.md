_Proof._ First, notice that _A_<sub>0</sub>-_B_<sub>0</sub>=L<sup>{0,1}</sup>. It follows that _A_<sub>0</sub>-_B_<sub>1</sub>=L<sup>{0,1}</sup>\\_A_<sub>0</sub> since \(B_1=B_0\backslash\{\vec{0}\}\) and \(\mathcal{B}=\mathcal{B}_1\cup\mathcal{B}_2\) is a basis. Similarly, _A_<sub>1</sub>-_B_<sub>0</sub>=L<sup>{0,1}</sup>\\_B_<sub>0</sub>. Hence,

\((A_0-B_1)\cup(A_1-B_0)=(\mathcal{L}^{\{0,1\}}\backslash A_0)\cup(\mathcal{L}^{\{0,1\}}\backslash B_0)\)<br>
\(=\mathcal{L}^{\{0,1\}}\backslash(A_0\cap B_0)\)<br>
\(=\mathcal{L}^{\{0,1\}}\backslash\{\vec{0}\}.\)

From Claim 3.3, we know that if there exists a vector in _A_<sub>0</sub>-_B_<sub>1</sub> or _A_<sub>1</sub>-_B_<sub>0</sub> with \(\ell_p\)-norm less than _r_, then there exists a vector in L<sup>{0,1}</sup> with \(\ell_p\)-norm less than _r_. If all vectors in \((A_0-B_1)\cup(A_1-B_0)\) have \(\ell_p\)-norm greater than \(\gamma r\), then all non-zero vectors in L<sup>{0,1}</sup> must have \(\ell_p\)-norm greater than \(\gamma r\) which concludes our proof.

**Remark 3.4.** _A similar reduction can be shown for_ \(\gamma\)-\(\mathsf{CVP}_p^{\{0,1\}}\)_, which is the_ CVP _analogue of_ \(\gamma\)-\(\mathsf{SVP}_p^{\{0,1\}}\)_. To see this, take_ \(\mathcal{B}'_0=\mathcal{B}_0+t\) _in the proof of Lemma 3.2, where_ \(t\in\mathbb{R}^d\) _is a target point which is guaranteed to be close to a_ {0,1}_-coefficient lattice vector. Then, run the Bichromatic Closest Pair algorithm on the input_ \((\mathcal{A}_0,\mathcal{B}'_0)\).

Combining Lemma 3.1 and Lemma 3.2, we obtain our main theorem which connects hardness of \(\gamma\)-SVP<sup>{0,1}</sup> and hardness of \(\gamma\)-ANN.

**Theorem 3.5.** _For any_ \(\delta>0\) _and C\>_1_, if there is an algorithm for_ \(\gamma\)_-ANN under the_ \(\ell_p\) _norm with N<sup>C</sup> preprocessing time and_ \(N^{1-\delta}\) _query time, then there is a_ \(2^{(1-\Omega(\frac{\delta}{C-1}))n}\)_-time algorithm for_ \(\gamma\)-\(\mathsf{SVP}_p^{\{0,1\}}\) _with the same ambient dimension, where n denotes the rank of the input lattice._

_Proof._ By Lemma 3.1, we get a \(N^{2-\delta^\prime}\)-time algorithm for \(\gamma\)-approximate Bichromatic Closest Pair where \(\delta'=\Omega\left(\frac{\delta}{C-1}\right)\) from the algorithm for \(\gamma\)-ANN. By Lemma 3.2, this in turn gives a \(2^{(1-\frac{\delta}{2})n}\)-time algorithm for \(\gamma\)-\(\mathsf{SVP}_p^{\{0,1\}}\).

Note that the SETH-hard instance of \(\gamma\)-\(\mathsf{SVP}_\infty^{\{0,1\}}\) in Theorem 2.8 has ambient dimension _d=O(n_) by the Sparsification Lemma \[IPZ01\]. Hence, we obtain the following lower bound for \(\gamma\)-ANN under \(\ell_\infty\).

**Corollary 3.6.** _Assuming SETH, for any_ \(\delta>0\) _and C\>_1_, there exists a constant_ \(\gamma=\gamma(\delta,C)\in(1,2)\) _such that_ \(\gamma\)_-ANN under_ \(\ell_\infty\) _(where d=O_(log_N)) cannot be solved with N<sup>C</sup> preprocessing and_ \(N^{1-\delta}\) _query time._

## 3.3 Bichromatic Subset Query Hardness implies Hardness of ANN under \(\ell_\infty\)

In this section, we show that solving \(\gamma\)-ANN for \(\gamma<3\) with polynomial preprocessing time requires nearly linear query time unless SETH is false. We first modify Indyk’s reduction \[Ind01\] from Subset Query to ANN to show that \(\gamma\)-approximate Bichromatic Closest Pair under \(\ell_\infty\) is as hard as Bichromatic Subset Query for any \(\gamma<3\).

**Lemma 3.7.** _For any_ \(\gamma<3\)_, if there exists a f(N)-time algorithm for_ \(\gamma\)_-approximate Bichromatic Closest Pair under the_ \(\ell_\infty\) _norm, then there exists a f(N_)+_O(dN)-time algorithm for Bichromatic Subset Query._

