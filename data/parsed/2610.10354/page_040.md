**Lemma 5.8** (Large-Universe Reduction for Min-Plus Convolution)**.** _Assume Hypothesis 1.7. If Min-Plus Convolution over the universe_ \[_n_\] _can be solved in time_ \(O(n^{2-\epsilon})\) _for some constant_ \(\epsilon>0\)_, then Min-Plus Convolution over the universe_ \[_u_\] _can be solved in time_ \(O(n^{2-\epsilon^\prime}(\mathrm{log}u)^{O(1)})\) _for some constant_ \(\epsilon'>0\).

In other words, Lemma 5.8 states that the Strong Min-Plus Convolution Hypothesis implies the Min-Plus Convolution Hypothesis assuming Hypothesis 1.7. This proves Theorem 1.8.

For the proof we will also rely on the following simple covering lemma, which essentially constitutes an instance of the classic greedy algorithm for Set Cover. For a proof see, e.g., \[Fis26, Lemma 5.11\].

**Lemma 5.9** (Greedy Covering)**.** _There is a deterministic algorithm that, given sets_ \(X,Y\subseteq[-u,u]\)_, computes a set_ \(S\subseteq[-2u,2u]\) _of size at most_ \(|Y-X|/|Y|\cdot\mathrm{ln}|X|\) _such that_ \(X\subseteq Y+S\)_. It runs in time_ \(|Y-X||S|\cdot(\mathrm{log}u)^{O(1)}\).

**Proof of Lemma 5.8.** Let \(\rho,\epsilon>0\) be two constants to be determined. We apply Lemma 5.3 to reduce any given Min-Plus Convolution instance over the universe \[_u_\] to \(O(n^\epsilon)\) instances of Min-Plus Convolution Listing with listing threshold \(t=O(n^{2\rho})\). Each such instance \((A',B')\) is equipped with a \((K=O(n^\epsilon),N=O(n^{2-2\rho}))\)-container _H_ for the joint index set \(\mathcal{I}(A')\cup\mathcal{I}(B')\). Focus on one such instance \((A',B')\) for now.

Let \(\phi:\mathbb{Z}^2\rightarrow\mathbb{Z}\) be the map defined by \(\phi(i,a)=i\cdot 10M+a\), where _M_ is an upper bound on the largest entry in _H_. Recall that \(H\subseteq[2n]\times\mathbb{Z}\), and that _H_ has doubling at most _K_. It follows easily that \(\phi\), restricted to _H+H_, is an isomorphism, and thus \(\phi(H)\) also has doubling at most _K_. Thus, we may apply Hypothesis 1.7 on the integer set \(\phi(H)\). This yields a subset \(Y\subseteq\phi(H)\) of size at least<tbc>

\(|Y|\ge\Omega\big(\frac{|H|}{K^c}\big),\)

<tbc>and a sum-order-preserving hash function \(h:Y\rightarrow\{0,\dots,N\}\), where _c_ is the constant from Hypothesis 1.7. Next, apply Lemma 5.9 to compute a set of shifts _S_ such that \(\phi(H)\subseteq Y+S\) and such that

\(|S|\le\frac{|Y-\phi(H)|}{|Y|}\cdot\mathrm{ln}|H|=O\big(K^c\cdot\frac{|\phi(H)-\phi(H)|}{|H|}\cdot\mathrm{log}|H|\big)=O(K^{c+2}\mathrm{log}|H|),\)

where the last step is due to the Plünnecke-Ruzsa inequality (Lemma 2.1).

Next, we apply Lemma 2.14 to reduce the Min-Plus Convolution Listing instance \((A',B')\) with listing threshold \(t=O(n^{2\rho})\) to \(\widetilde{O}(n^{2\rho})\) plain Min-Plus Convolution subinstances (i.e., for which we do not have to list multiple witnesses). In what follows, fix any such instance, denoted (_A,B_); we argue that it reduces to few instances of Monotone Min-Plus Convolution over the universe \[_n_<sup>2</sup>\]. By Lemma 5.6, any such instance further reduces to (non-Monotone) Min-Plus Convolution over the universe \[_n_\]. Let _C_ be the output sequence, initialized to \(\perp\). We will only update _C_ by updates of the form \(C[k]\leftarrow\mathrm{min}\{C[k],A[i]+B[k-i]\}\), guaranteeing that no output is underestimated.

