**Remark 5.14.** _As is apparent from the proof, Lemma 5.13 still holds even if the algorithm to compute Y and h in Hypothesis 1.12 is slower than_ |_X_|<sup>1+_o_(1)</sup>_K_<sup>_O_(1)</sup>_. Any algorithm in time_ |_X_|<sup>3-\(\Omega(1)K^{O(1)}\)</sup> _would suffice._

The proof of Theorem 1.13 (restated next) is now a simple combination of Lemmas 5.7 and 5.13.

**Theorem 1.13** (APSP Conditionally Implies Strong APSP)**.** _Conditioned on Hypothesis 1.12, there is a subcubic reduction from APSP to APSP over the universe_ {0_,...,n}. In particular, conditioned on Hypothesis 1.12 and on the assumption that_ \(\omega=2\)_, the APSP and Strong APSP Hypotheses are equivalent._

**Proof.** It is clear that the Strong APSP Hypothesis implies the APSP Hypothesis. For the other direction assume that \(\mathrm{MinPlus}(n,n,n|u\le n)=O(n^{3-\epsilon})\). This is in particular the case if the Strong APSP Hypothesis fails and if simultaneously \(\omega=2\). Additionally assume Hypothesis 1.12. Under these assumptions it follows that:

\(\mathrm{MinPlus}(n,n,n|u)=\left(K\cdot\mathrm{MinPlus}(n,n,n|u;D\le n;K)+\frac{n^3}{K^{1/300000}}\right)^{1+o(1)}\cdot\mathrm{log}u\text{(Lemma 5.7)}\)<br>
\(=\left(K^{c+1}\cdot\mathrm{MinPlus}(n,n,n|u\le n)+\frac{n^3}{K^{1/300000}}\right)^{1+o(1)}\cdot\mathrm{log}u\text{(Lemma 5.13)}\)<br>
\(=\left(K^{c+1}n^{3-\epsilon}+\frac{n^3}{K^{1/300000}}\right)^{1+o(1)}\cdot\mathrm{log}u,\)

where _c_ is the constant from Lemma 5.13 and _K_ is an arbitrary parameter. Setting \(K=n^{\epsilon/(2c+2)}\), the running time becomes \(n^{3-\epsilon/(600000c+600000)+o(1)}\cdot\mathrm{log}u\), which, recalling that \(u=n^{c^\prime}\) for some arbitrarily large constant \(c'\), is truly subcubic as claimed.

**Remark 5.15.** _The statement of Theorem 1.13 remains valid when assuming the weaker Hypothesis A.3 instead (stated in Appendix A). That hypothesis leads to an overhead of_ \(|X|^\epsilon\le n^\epsilon\) _for an arbitrarily small constant_ \(\epsilon>0\)_, and the constant c from before would depend on_ \(\epsilon\) _(i.e.,_ \(c=c(\epsilon)\)_)._

## 6 Lower Bounds for Intermediate Problems

In this section, we derive APSP-based lower bounds for various graph and matrix problems with intermediate complexity. The proofs in this section are mostly technically simple consequences of Corollary 5.9 or 5.10.

### 6.1 Node-Weighted APSP

Recall that node-weighted APSP can be solved in time \(\tilde{O}(n^{(3+\omega)/2})\) \[31, 102, 4\], even in directed graphs. Chan, Vassilevska W., and Xu \[36\] gave an _n_<sup>2.5-_o_(1)</sup> lower bound based on the Directed Unweighted APSP Hypothesis, even for undirected graphs. Here, we strengthen this lower bound to be based on the APSP Hypothesis.

**Theorem 1.14** (Node-Weighted APSP)**.** _APSP in undirected node-weighted graphs cannot be solved in time_ \(O(n^{2.5-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the APSP Hypothesis fails._

**Proof.** Suppose that Node-Weighted APSP is in time \(O(n^{2.5-\epsilon})\) for some \(\epsilon>0\); we show that in this case \(\mathrm{MinPlus}(n,\sqrt{n},n|D\le\sqrt{n})=O(n^{2.5-\epsilon})\) which contradicts the APSP Hypothesis by Corollary 5.10.

Let _n_ be a square number, and let \(A\in(X\cup\{\perp\})^{n\times\sqrt{n}}\) and \(B\in(X\cup\{\perp\})^{\sqrt{n}\times n}\) be the given matrices, where \(X\subseteq\mathbb{Z}\) is a set of size \(\sqrt{n}\). We construct a 4-layered undirected node-weighted graph _G_ on 4_n_ nodes as follows:

• _(Vertices)_ The vertices consist of four distinct layers: _I_=\[_n_\] (the first layer), \(K_1=[\sqrt{n}]\times X\) (the second layer), \(K_2=[\sqrt{n}]\times X\) (the third layer), and _J_=\[_n_\] (the fourth layer).<tbc>

