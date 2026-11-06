Greedy Uniformity on Trees:<br> Exact Obstruction and Near-Uniform Spiders

**Abstract**

Choose a uniformly random ordering of the vertices of a finite tree and run the usual greedy maximal-independent-set algorithm. We compare the resulting law on maximal independent sets with the uniform law. We prove that exact uniformity occurs only for the one-vertex tree and the single edge. The proof is structural: a diameter endpoint exposes a pendant star, and the remaining one-pendant-leaf case is resolved by a strict injection between exact permutation fibres obtained by swapping the pendant leaf with its support vertex. Exact uniformity is therefore rigid, but it can be approached closely. For an explicit mixed-spider family _T<sub>k,l</sub>_ we count the maximal independent sets and compute the exact probability of every output. With _l_=2_<sup>k</sup>-k_ the total-variation bias is positive and satisfies

\(b(T_{k,2^k-k})=O\left(\frac{\sqrt{k}}{4^k}\right)=O\left(\frac{\sqrt{logn_k}}{n_k^2}\right),n_k=2^k+k+1.\)

The theorem package has also been formalised in Lean and registered with Palomar. These records document machine-checked formal verification and the checked axiom boundary; they are not peer review or a certificate of novelty.

## 1 Introduction

A random ordering followed by a greedy scan is one of the simplest ways to construct a maximal independent set. Given a finite graph, scan the vertices in uniformly random order and accept a vertex exactly when none of its previously accepted neighbours has been accepted. The output is always a maximal independent set, but different maximal independent sets can have very different numbers of generating orders. The question studied here is when, for a tree, these permutation fibres happen to have equal size.

Write M(_T_) for the maximal independent sets of a finite nonempty tree _T_, let G_<sub>T</sub>_ be the law of the greedy output, and let U_<sub>T</sub>_ be uniform on M(_T_). Our first result gives a complete obstruction to exact equality.

**Theorem 1.1** (Exact obstruction)**.** _For every finite nonempty tree T,_

\(\mathsf{G}_T=\mathsf{U}_T\Longleftrightarrow T\cong K_1\text{\textit{or}}K_2.\)

_Equivalently, if_

\(b(T)=d_\mathrm{TV}(\mathsf{G}_T,\mathsf{U}_T)=\frac{1}{2}\sum_{I\in\mathcal{M}(T)}\left|\mathsf{G}_T(I)-\frac{1}{|\mathcal{M}(T)|}\right|,\)

_then b(T_)=0 _if and only if_ \(T\cong K_1\) _or K_<sub>2</sub>.

The obstruction is qualitative, so it is natural to ask whether nontrivial connected trees can nevertheless have very small bias. They can. Let _T<sub>k,l</sub>_ be the tree with a centre _c,k_ length-two arms _c-u<sub>i</sub>-v<sub>i</sub>_, and _l_ further leaves adjacent directly to _c_.

John Fairfax-Ball

October 1, 2026

