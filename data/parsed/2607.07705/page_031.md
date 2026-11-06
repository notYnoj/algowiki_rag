Now suppose that \(|C|\ge\mathbf{w}(A)+k\). We first show that \(|\mathrm{Inv}(I)\cap\mathrm{Inv}(C)|\ge|C|\). Assume the contrary. We order the elements of _C_ arbitrarily, and then for each \(e\in\mathrm{Inv}(I)\cap\mathrm{Inv}(C)\) we mark the first element \(c\in C\) in this order such that \(e\in\mathrm{Inv}(c)\). Since \(|\mathrm{Inv}(I)\cap\mathrm{Inv}(C)|<|C|\), at least one \(c\in C\) remains unmarked. Define \(C'\) as _C_\\{_c_}. Because \(|C'|<|C|\), from the minimality of _C_ it follows that there exists \(b\in B'\) such that \(b\notin\mathrm{Inv}(C')\). On the other hand, \(b\in\mathrm{Inv}(C)\). Hence _c_ is the only element in _C_ with \(b\in\mathrm{Inv}(c)\). Recall that every element of \(B'\) is inverse to at least two edges in _S_. Consequently, there must be \(i\in I\) with \(b\in\mathrm{Inv}(i)\), and therefore \(b\in\mathrm{Inv}(I)\cap\mathrm{Inv}(C)\). But then _c_ would have been marked when processing _b_, because no other element of _C_ contains _b_ in its inverse set. This contradicts the choice of _c_. Therefore, \(|\mathrm{Inv}(I)\cap\mathrm{Inv}(C)|\ge|C|\).

Since _X_ is a feasible solution of I, we have \(\mathbf{w}(X)\ge\mathbf{w}(T)+k\). Additionally, recall that \(\mathbf{w}(X)\le\mathbf{w}(T)+\mathbf{p}(S)+\mathbf{w}(A)\), and therefore \(\mathbf{p}(S)\ge k-\mathbf{w}(A)\). On the other hand, observe that

\(\mathbf{p}(S)=\mathbf{w}(\mathrm{Inv}(S))-\mathbf{w}(S)\)<br>
\(=(\mathbf{w}(\mathrm{Inv}(C))-\mathbf{w}(C))+(\mathbf{w}(\mathrm{Inv}(I)\backslash\mathrm{Inv}(C))-\mathbf{w}(I))\)<br>
\(=\mathbf{p}(C)+(\mathbf{w}(\mathrm{Inv}(I))-\mathbf{w}(I))-\mathbf{w}(\mathrm{Inv}(I)\cap\mathrm{Inv}(C))\)<br>
\(=\mathbf{p}(C)+\mathbf{p}(I)-\mathbf{w}(\mathrm{Inv}(I)\cap\mathrm{Inv}(C))\)

Since \(|\mathrm{Inv}(I)\cap\mathrm{Inv}(C)|\ge|C|\ge\mathbf{w}(A)+k\) and all weights are at least one, we have

\(\mathbf{p}(C)+\mathbf{p}(I)=\mathbf{p}(S)+\mathbf{w}(\mathrm{Inv}(I)\cap\mathrm{Inv}(C))\ge(k-\mathbf{w}(A))+(\mathbf{w}(A)+k)=2k\)

This implies that at least one subgraph of _T-C_+Inv(_C_) and _T-I_+Inv(_I_) is a solution of I. Indeed, Lemma 1 guarantees that both of them are acyclic. Moreover, \(\mathrm{max}\{\mathbf{p}(C),\mathbf{p}(I)\}\ge 2k/2=k\). This again contradicts the choice of _X_, since \(1\le|C|<|S|\) implies that both _C_ and _I_ are strictly smaller than _S_.

In both cases, we derive a contradiction. Consequently, \(\mathbf{w}(B')\le(\mathbf{w}(A)+k)^2\). This completes the proof.

In combination, Lemma 7 and Lemma 8 supply us with a powerful tool. For example, an instance (_G,_**w**_,k_) with \(A=\emptyset\) can now be solved in time _n_<sup>O(_k_<sup>2</sup>)</sup> as follows. Enumerate all \(B'\subseteq B\) of weight at most (**w**(_A_)+_k_)<sup>2</sup>=_k_<sup>2</sup>. For each \(B'\), consider all sets _R_ formed by picking, for every \(b\in B'\), one tree edge that breaks the cycle in _T+b_. For every such pair \((B',R)\), apply the algorithm from Lemma 7 with the given \(B'\), _R_, and \(F=\emptyset\), and obtain a maximum-profit set _S_ under these restrictions. If a solution exists, some such _S_ will yield \(\mathbf{p}(S)\ge k\).

## 5.2 Dealing with allowed edges

When allowed edges come into play, we encounter a further complication: the structure of acyclic subgraphs no longer admits the same clean characterization as before. Given a set of removed tree edges _S_, the blocked edges of any acyclic subgraph are still confined to Inv(_S_). However, once the subgraph includes allowed edges, we lose the guarantee that the whole Inv(_S_) can be taken without producing cycles. In this section, we unravel this difficulty.

Our approach, however, will differ significantly from the one used in the integral case, so let us first compare two versions of the problem (integral- and rational-weighted) in the context of allowed edges and discuss why the methods we developed for our FPT-algorithm for integral weights cannot be directly applied to rational weights.

