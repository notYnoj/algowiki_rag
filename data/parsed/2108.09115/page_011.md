**Corollary 5.** _For all_ \(i\in S\), \(\ell\in[0,\mathrm{log}s+1]\) _and_ \(d\in[-k,k]\) _if_ \(H_A[\ell][i]=H_B^d[\ell][i]\) _then_ \(a_ia_{i+1}\dots,a_{i+2^\ell}\) _and_ \(b_{i+d}b_{i+1+d}\dots b_{i+d+2^\ell}\) _have less than_ \(\frac{k}{\mathrm{log}n}\) _mistatches._

_Proof._ Take any _i_ and _d_. Since _Bad(i,d_) did not happen, if \(a_ia_{i+1}\dots,a_{i+2^\ell}\) and \(b_{i+d}b_{i+1+d}\dots b_{i+d+2^\ell}\) had at least \(\frac{k}{\mathrm{log}n}\) mismatches, we would have \(H_A[\ell][i]\neq H_B^d[\ell][i]\)

Using the above corollary, we can now show that _Approx-Equal(i,d_) is a good approximation of _Equal(i,d_).

**Lemma 6.** _If Approx-Equal(i,d_)=_q then a<sub>i</sub>a_<sub>_i_+1</sub>_...a<sub>q</sub> and b_<sub>_i+d_</sub>_b_<sub>_i+d_+1</sub>_...b_<sub>_q+d_</sub> _have strictly less than_ 2_k mismatches._

_Proof._ Since the sampling probability is \(\frac{\mathrm{log}^2n}{k}\), \((n(i)-i)\le\frac{k}{\mathrm{log}n}\) with high probability (we assume \(k\ge\mathrm{polylog}n\)).

Now _A_\[_n(i),q_\] can be decomposed into at most \(\mathrm{log}s+1\le\mathrm{log}n+1\) intervals each of length that is a power of two. Moreover for each of these intervals the computed hashes _H<sub>A</sub>_ and \(H_B^d\) must match. Therefore, each of these at most log_n_+1 intervals can have at most \(\frac{k}{\mathrm{log}n}\) mismatches from Corollary 5. Thus the total number of mismatches is strictly less than \((n(i)-i)+(\mathrm{log}n+1)\frac{k}{\mathrm{log}n}=k+\frac{2k}{\mathrm{log}n}\le 2k\).

In order to complete our analysis, we now compare the _h_-waves computed by the exact algorithm from Section 3 and approximate _h_-waves computed by using _Approx-Equal(i,d_).

**Lemma 7** (Completeness)**.** \(\forall h\in[0,k]\) _and_ \(d\in[-k,k]\), \(\hat{L}^h(d)\ge L^h(d)\)_. Therefore, if_ \(\mathrm{ED}(A,B)\le k\)_, then the algorithm will return YES._

_Proof._ The proof follows simply by induction since \(\text{\textit{Approx-Equal}}(i,d)\ge\text{\textit{Equal}}(i,d)\).

**Lemma 8** (Soundness)**.** \(\forall h\in[0,k]\) _and_ \(d\in[-k,k]\), \(\hat{L}^h(d)\le L^{2k(h+1)}(d)\)_. Therefore, if_ ED(_A,B)\>_2_k_<sup>2</sup>+2_k, then the algorithm will return NO._

_Proof._ The proof is again by induction. Observe that \(\hat{L}^0(0)=\text{\textit{Approx-Equal}}(0,0)\). From Lemma 6, \(B[0,\hat{L}^0(0)]\) and \(B[0,\hat{L}^0(0)]\) can have at most 2_k_ mismatches. Therefore, \(L^{2k}(0)\ge\hat{L}^0(0)\). Suppose the result is true for 0,1_,...,h_-1 for all diagonals \(\in[-k,k]\) and upto diagonal _d_-1 for _h_. Let us consider \(\hat{L}^h(d)\). Recall the definition of \(\hat{L}^h(d)\).

\(\hat{L}^h(d)=\mathrm{max}\left\{\begin{array}{ c c }
\text{\textit{Approx-Equal}}(\hat{L}^{h-1}(d)+1,d) & \text{if}h-1\ge 0; \\
\text{\textit{Approx-Equal}}(\hat{L}^{h-1}(d-1),d) & \text{if}d-1\ge-k,h-1\ge 0; \\
\text{\textit{Approx-Equal}}(\hat{L}^{h-1}(d+1)+1,d) & \text{if}d+1,h+1\le k.
\end{array}\right.\)

Let us consider the first expression, \(\text{\textit{Approx-Equal}}(\hat{L}^{h-1}(d)+1,d)\). By the induction hypothesis, \(\hat{L}^{h-1}(d)\le L^{2kh}(d)\). There must be a mismatch at row \(\hat{L}^{h-1}(d)+1\). The number of mismatches in \(\text{\textit{Approx-Equal}}(\hat{L}^{h-1}(d)+1,d)\) is at most 2_k_-1 mismatches. Therefore, \(L^{2k(h+1)}(d)\ge\text{\textit{Approx-Equal}}(\hat{L}^{h-1}(d)+1,d)\). Similarly, for the other two expressions.

Therefore, if ED(_A,B)\>_2_k_<sup>2</sup>+2_k_, then _L_<sup>2_k_<sup>2</sup>+2_k_</sup>(0)_\<n_. Then \(\hat{L}^k(0)\le L^{2k^2+2k}(0)<n\), the algorithm aborts and declares NO.

Hence, we get the following theorem.

**Theorem 9** (Small-EDIT-Single-Preprocessing)**.** _Given two strings A=a_<sub>1</sub>_a_<sub>2</sub>_..a<sub>n</sub> and, B=b_<sub>1</sub>_b_<sub>2</sub>_..b<sub>n</sub> of length n over alphabet_ \(\Sigma\)_, we can answer if_ \(\mathrm{ED}(A,B)\le k\) _or_ ED(_X,Y)\>_3_k_<sup>2</sup> _with probability at least_ \(1-\frac{1}{n}\) _by preprocessing only a single string in_ \(\tilde{O}(n)\)_-time and with a query time of_ \(\tilde{O}(\frac{n}{k}+k^2)\).

