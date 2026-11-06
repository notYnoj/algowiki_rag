## Appendix A. Proofs of structural properties

In this section, we prove Lemma 3.13.

The first condition of nice hypergraphs, i.e., \(H_\Phi\) is in \(\mathcal{H}_{\le k}\) and has density \(\alpha\), is trivial. Then Property 3.4 follows from a classical result \[RS98, Theorem 1\].

**Lemma A.1.** _With probability_ 1-_o_(1_/n_) _over the random formula_ \(\Phi=\Phi(k,n,m)\) _with density_ \(\alpha\), \(H_\Phi\) _satisfies Property 3.4, namely, the maximum degree of variables is at most_ \(4k\alpha+6logn\).

Similar to this lemma, the following proposition, which bounds the number of high-degree vertices in \(H_\Phi\), also follows from the classical result of the balls-and-bins model.

**Proposition A.2.** _Assume_ \(k\ge 2\), \(q\ge 2\) _and_ \(\alpha\le q^k\) _are constants. Let p_<sub>1</sub> _be a parameter satisfying_ \(p_1\ge 4k\)_. Then with probability_ 1-_o_(1_/n_) _over the random formula_ \(\Phi\)_, for_ \(H_\Phi=(V,\mathcal{E})\)_, we have_

\(|\{v\in V|deg(v)>p_1\alpha\}|\le\mathrm{e}^{-k}\alpha^{-2}n,\)

_i.e.,_ \(|\mathrm{HD}(V)|\le\mathrm{e}^{-k}\alpha^{-2}n\).

_Proof._ The degrees of the variables in \(\Phi\) distribute as a balls-and-bins experiment with _km_ balls and _n_ bins. Let \(D_1,\dots,D_n\sim\mathrm{Pois}(k\alpha)\) be _n_ independent Poisson random variables with parameter \(k\alpha\). Then the degrees of the variables in \(\Phi\) has the same distribution as {_D_<sub>1</sub>_,...,D<sub>n</sub>_} conditioned on the event E_<sub>n,m</sub>_ that \(\sum_{i=1}^nD_i=km\) \[MU17, Chapter 5.4\]. Note that \(\sum_{i=1}^nD_i\) is a Poisson random variable with parameter \(k\alpha n=km\). Thus<tbc>

\(\mathbf{Pr}\left[\mathcal{E}_{n,m}\right]=\mathrm{e}^{-km}\cdot\frac{(km)^{km}}{(km)!}\ge\frac{1}{\sqrt{2\pi km}}=\frac{1}{\sqrt{2\pi k\alpha n}}.\)

<tbc>For any fixed \(i\in[n]\), we have<tbc>

\(\mathbf{Pr}\left[D_i\ge p_1\alpha\right]=\mathbf{Pr}\left[\mathrm{Pois}(k\alpha)\ge p_1\alpha\right]\le\frac{\mathrm{e}^{-k\alpha}(\mathrm{e}k\alpha)^{p_1\alpha}}{(p_1\alpha)^{p_1\alpha}}\le\mathrm{e}^{-k\alpha}(\mathrm{e}/4)^{4k\alpha}\le\mathrm{e}^{-k\alpha} 2^{-2k\alpha}\le 2^{-3k\alpha}.\)

<tbc>Define \(U=\{i\in[n]|D_i\ge p_1\alpha\}\). Then by Chernoff-Hoeffding bound, we obtain that<tbc>

\(\mathbf{Pr}\left[|U|>\mathrm{e}^{-k}\alpha^{-2}n\right]\le\mathbf{Pr}\left[|U|-\mathbf{E}[|U|]>\mathrm{e}^{-k+1}\alpha^{-2}n\right]<\mathrm{e}^{-2\mathrm{e}^{-2k+2}\alpha^{-4}n}=o(1/n^2),\)

<tbc>which further gives that

\(\mathbf{Pr}\left[|\{v\in V(H_\Phi)|deg(v)>p_1\alpha\}|\ge\mathrm{e}^{-k}\alpha^{-2}n\right]\)<br>
\(=\mathbf{Pr}\left[|U|\ge\mathrm{e}^{-k}\alpha^{-2}n|\mathcal{E}_{n,m}\right]\)<br>
\(\le\sqrt{2\pi k\alpha n}\cdot o(1/n^2)=o(1/n).\) □

