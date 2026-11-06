**Definition 6.7.** _Given a directed graph G, an_ \(\ell\)_-cover is a collection of_ \(\ell\) _(not necessarily disjoint) paths in G,_ \(\mathcal{P}=\{P_1,\dots,P_\ell\}\) _satisfying:_

1. _(Size Bound)_ \(\sum_{P\in\mathcal{P}}|P|\le min(\ell,diam(G))\cdot n\).<tbc>

_2._ _(Longest Path Bound)_ \(LP(G')\le 2n/\ell\) _where_ \(G'=TC(G)[U]\) _and U=V_\\_V_(P).

**Definition 6.8.** _Given a directed graph G, a chain is a path in_ TC(_G)._

Given a vertex _v_ and a chain _C_, let _w_:=_w(v,C_) denote the first vertex in _C_ such that \((v,w)\in TC(G)\), if such a vertex exists. We are now ready to state the algorithm of \[KP22a\].

The above algorithm returns a _D_-shortcut-set of size \(\widetilde{O}\left(n^2/D^3+n\right)\) (see Theorem 1.4 of \[KP22a\]). It suffices for us to analyze the running time. Step 1 requires time \(\widetilde{O}\left(m+n^{3/2}\right)\) by Theorem 1.3 of \[KP22a\]. Step 2 requires time \(\widetilde{O}\left(m+n^{3/2}+n\cdot min(diam(G),\ell)\right)\) by Theorem 2.3 of \[KP22a\]. Step 3 requires time \(\widetilde{O}\left(\sum_{P\in\mathcal{P}}|P|\right)\) by Lemma 1.15 of \[KP22a\]. Step 4 requires time \(\widetilde{O}\left(\sum_{C\in\mathcal{C}}|C|\right)\) by Lemma 1.10 of \[KP22a\]. Step 5 requires time _O(n_+|C|). Step 7 requires time \(\widetilde{O}\left(n\right)\) by the size of the shortcut set. In total, all steps (excluding step 6) require time \(\widetilde{O}\left(n^2\right)\).

It thus suffices to analyze the running time of step 6, for which we propose a new algorithm. First, we need a simple bound on \(|V'|,|\mathcal{C}'|\).

**Claim 6.9.** _With high probability,_ \(|V'|=O\left(nlogn/D\right)\) _and_ \(|\mathcal{C}'|=O\left(nlogn/D^2\right)\).

_Proof._ Note that \(|V'|\) is a sum of independent Bernoulli variables with mean _O(n_log_n/D_). A Chernoff bound shows that \(Pr(|V'|>10\mu)<exp(-\mu)\checkmark n^{-10}\). A similar bound holds for \(|\mathcal{C}'|\), a sum of independent Bernoulli variables with mean \(\widetilde{O}\left(nlogn/D^2\right)\).

Next, we argue that we can assume that the length of each chain is at most twice the average.

**Claim 6.10.** _Given a collection of vertex disjoint chains_ C<sub>0</sub> _of size_ \(\ell\)_, there is a collection of vertex disjoint chains_ C _of size_ \(\ell\) _satisfying (1) V_(C)=_V_(C<sub>0</sub>) _and (2) each_ \(C\in\mathcal{C}\) _satisfies_ \(|C|\le 2n/\ell\)_. Furthermore,_ C _can be computed in O(n_) _time._

_Proof._ For every chain \(C\in\mathcal{C}_0\) of length \(|C|>n/\ell\), we split _C_ into \(|C|\ell/n\) chains of length at most \(2n/\ell\). Let C be the union of all the split chains. Note that C is vertex disjoint and _V_(C)=_V_(C<sub>0</sub>). Furthermore, every \(C\in\mathcal{C}\) satisfies \(|C|\le 2n/\ell\). We bound the size of C as

\(\sum_{C\in\mathcal{C}_0}|C|\ell/n\le\frac{\ell}{n}\sum_{C\in\mathcal{C}_0}|C|\le\ell\)

where we use the fact that C<sub>0</sub> are vertex disjoint so \(\sum_{C\in\mathcal{C}_0}|C|\le n\). It is clear that C can be computed in _O(n_) time.

\begin{tabular}{cc}
1. & Compute _H_<sub>0</sub>, a shortcut set of diameter \(D_0=O(\sqrt{n})\) of size \(\widetilde{O}\left(n\right)\). \\
2. & Compute an \(\ell\)-cover P of \(G\cup H_0\) where \(\ell=16n/D\). \\
3. & Compute C, a collection of vertex disjoint chains in _G_ satisfying (i) \(|\mathcal{C}|\le|\mathcal{P}|\) and (ii) _V_(C)=_V(P_). \\
4. & For every \(C\in\mathcal{C}\), compute _H(C_): a 2-shortcut-set for _C_. \\
5. & Let \(V'\subset V,\mathcal{C}'\subset\mathcal{C}\) be random subsets where each vertex (resp. chain) is sampled with probability \(p=\Theta(logn/D)\). \\
6. & Compute \(\hat{H}=\{(v,w(v,C))\text{s.t.}v\in V',C\in\mathcal{C}'\text{if}w(v,C)\text{exists}\}\). \\
7. & Return \(H_0\cup\left(\bigcup_{C\in\mathcal{C}}H(C)\right)\cup\hat{H}\). \\
\end{tabular}

