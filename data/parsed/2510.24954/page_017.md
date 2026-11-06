as otherwise, we obtain a contradiction to the assumption that all paths are supported by at most _s_ edges. Rearranging the above yields that that whenever \(\eta>\frac{\sqrt{s}}{2\sqrt{rk}}\), there is some layer on which all critical paths connecting _A_ to _B_ are supported by at least _s_ edges.

With the above, \((k\ell\sigma log(n))^\frac{3}{2}\) critical paths between _A_ and _B_ yield a support size of at least \(k\ell\sigma log(n)\). Using that each edge is deleted independently with probability \(p=1/(k\ell)\) then implies that, for every such set, at least one critical path fails.

**Lemma 3.10.** _Consider any_ \(G\in G_k\) _and let i,j be such that_ \(|i-j|\ge 4rk\)_. Let_ \(A\subseteq L_i,B\subseteq L_j\) _and define_ \(\sigma:=max\{|A|,|B|\}\)_. Then with probability_ 1-1/poly(_n), for all such i,j,A,B in_ \(\widetilde{G}\) _with at least_ \((100\sigma log(n)\ell k)^{3/2}\) _critical paths connecting a vertex in A to a vertex in B, there is at least one such critical path that fails when passing from G to the noised version_ \(\widetilde{G}\).

_Proof._ Let \(\gamma:=100logn\). We show that for every choice of \(A\subseteq L_i,B\subseteq L_j\) with more than \((\gamma\sigma k\ell)^{3/2}\) critical paths, at least one path will fail after applying noise. Invoking Lemma 3.9, the support size of these paths between layers _L<sub>i</sub>_ and _L<sub>j</sub>_ is at least \(\gamma\sigma k\ell\). Furthermore, the number of all _A,B_ with \(max\{|A|,|B|\}=\sigma\) is at most \(n^{2\sigma}\), and the probability that for fixed sets _A,B_ no critical path connecting _A_ to _B_ fails is at most

\((1-p)^{\gamma\sigma k\ell}=\left(1-\frac{1}{k\ell}\right)^{\gamma\sigma k\ell}\le exp(-\gamma\sigma).\)

because we have chosen \(p=\frac{1}{k\ell}\). Applying a union bound yields that the probability that there is some \(A\subseteq L_i,B\subseteq L_j\) with \(|i-j|\ge 4rk\) and at least \((\gamma\sigma k\ell)^{3/2}\) critical paths connecting _A_ and _B_ is at most

\(\sum_{\sigma=1}^\infty(\ell k)^2n^{2\sigma}\left(1-\frac{1}{\ell k}\right)^{\gamma\sigma k\ell}\le(\ell k)^2\sum_{\sigma=1}^\infty exp\left(2\sigma log(n)-\gamma\sigma\right)\)<br>
\(\le(\ell k)^2\sum_{\sigma=1}^\infty exp\left(2\sigma log(n)-100\sigma log(n)\right)\)<br>
\(\le(\ell k)^2\sum_{\sigma=1}^\infty n^{-98\sigma}\le n^2n^{-97}\le n^{-95}.\)

This concludes that with probability 1-1/poly(_n_), there is no pair of sets \(A\subseteq L_i,B\subseteq L_j\) such that \(|i-j|\ge 4rk\) and such that there are more than \((100slog(n)\ell k)^{3/2}\) critical paths connecting _A_ and _B_.

_Proof of Theorem 3.3._ We show that there is no Steiner shortcut with diameter \(m^{\epsilon^2/k}\) while using at most \(m^{1+\epsilon^2/k}\) edges and using thickness _t_ such that \(1.01t\le\frac{8}{7}k\). Here, \(\epsilon>0\) is a sufficiently small constant fixed later.

To this end, we suppose that there is a Steiner shortcut \(E'\) with the desired properties and then deduce a contradiction. We consider the family of random graphs \(\widetilde{\mathcal{G}}_k\) and set \(p=1/(\ell k)\), and _c_=3 such that \(\ell=r^3\). Now, using that _k=O(r_), the number of critical pairs is<tbc>

\(\Theta\left(\frac{N\Delta^kr^{dk}}{(r+1)^{dk}}\right)=\Theta(N\Delta)\cdot\Delta^{k-1}=\Theta(m/(k\ell))\cdot\Delta^{k-1}.\)

