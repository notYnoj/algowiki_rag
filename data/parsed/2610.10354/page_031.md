By construction, \(\mathcal{C}\subseteq\mathcal{X}_1+\mathcal{X}_2\) and thus C has rank at most<tbc>

<tbc>\(r:=max\{|\mathcal{X}_1|,|\mathcal{X}_2|\}\le O(|X|\sqrt{q})\le O(pn\cdot\sqrt{q})=\widetilde{O}(n^{1-\epsilon/2}),\)<tbc>

<tbc>where \(|X|\le 2pn\) follows from Chernoff’s bound with high probability. We solve the All-Integer 3SUM instance in time

\(\widetilde{O}(3SUM(n|r\le n^{1-\epsilon/2})),\)

constituting the second term in the claimed running time. For each _k_, choose the smallest of the three items \((k,c)\in\mathcal{C}\) that is involved in a 3SUM solution, and set _C_\[_k_\]=_c_.

We argue that we thereby correctly assign _C_\[_k_\] for all popular indices _k_. By definition, a popular index has at least \(n^{1-\gamma+\epsilon}\) pseudo-witnesses _i_. Thus, with good probability _X_ contains one such pseudo-witness _i_ and simultaneously _k-i_; the probability of missing all such pairs is

\((1-p^2)^{n^{1-\gamma+\epsilon}}\le exp(-p^2n^{1-\gamma+\epsilon})\le n^{-100}.\)

In the successful event, we have \((i,A_1[i]\cdot q+a)\in\mathcal{X}_1\) and \((j,B_1[j]\cdot q+b\cdot\lceil\sqrt{q}|)\in\mathcal{X}_2\) for all \(0\le a,b<\sqrt{q}\), and thus \((k,C_1[k]\cdot q+a+b\cdot\lceil\sqrt{q}|)\in\mathcal{X}_1+\mathcal{X}_2\). For an appropriate choice of \(0\le a,b<\sqrt{q}\), this becomes exactly \((k,C_1[k]\cdot q+C_0[k])=(k,C[k])\). In this event, (_k,C_\[_k_\]) is part of the All-Integer 3SUM instance and we correctly identify _C_\[_k_\].

**Corollary 5.2** (Small-Universe Reduction for Min-Plus Convolution Listing)**.** _Let_ \(\gamma\in[0,1]\)_. Listing_ \(n^{1-\gamma}\) _witnesses in Min-Plus Convolution instances with universe_ \([n^\gamma]\) _requires n_<sup>2-_o_(1)</sup> _time, under the strong Min-Plus Convolution Hypothesis._

**Proof.** Suppose there is such an algorithm with running time \(O(n^{2-\epsilon^\prime})\). We invoke Lemma 5.1 with \(\gamma:=\gamma\) and \(\epsilon=\epsilon'/2\). Combined with Theorem 4.1, this gives us a truly subquadratic time algorithm for \(MPConv(n|u\le n)\), contradicting the strong Min-Plus Convolution Hypothesis.

Combined with the listing trick from Lemma 2.14, we directly obtain Theorem 1.6:

**Theorem 1.6** (Small-Universe Reduction)**.** _Let_ \(\gamma\in[0,1]\)_. Min-Plus Convolution for length-n input sequences over a universe of size_ \(u=n^\gamma\) _cannot be solved in time_ \(O(n^{1+\gamma-\epsilon})\) _(for any constant_ \(\epsilon>0\)_), unless the Strong Min-Plus Convolution Hypothesis fails._

## 5.2 Doubling Reduction

The purpose of this subsection is to prove the following lemma. Intuitively, it states that any Min- Plus Convolution instance (_A,B_) can be assumed to have a low-doubling container for its joint index set \(\mathcal{I}(A)\cup\mathcal{I}(B)\) (Definition 2.13). The proof is close to \[Fis26, Lemma 5.7\].

**Lemma 5.3** (Doubling Reduction)**.** _For any_ \(\epsilon>0\) _and_ \(0<\rho\le 1/2\) _there is some_ \(\delta=\delta(\rho,\epsilon)>0\) _such that the following holds. There is a randomized reduction from any Min-Plus Convolution instance_ (_A,B_) _over the universe_ \[_u_\] _to_ \(O(n^\epsilon logu)\) _Min-Plus Convolution Listing instances_ \((A',B')\) _with the same size n, over the same universe_ \[_u_\]_, and with listing threshold_ \(O(n^{2\rho})\)_, each equipped with a_ \((O(n^\epsilon),O(n^{2-2\rho}))\)_-container of the joint index set_ \(\mathcal{I}(A')\cup\mathcal{I}(B')\)_. The reduction runs in time_ \(O((n^{1+2\rho+\epsilon}+n^{2-\delta})logu)\).

