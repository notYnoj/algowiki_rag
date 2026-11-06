**Lemma 3** (Prescribed labeled subgraph)**.** _There is_ \(\xi_n=n^{-\Omega(1)}\mathrm{log}n\) _such that every specified admissibly port-labelled simple graph J on specified vertices, with_ \(w\le n/4\) _edges, satisfies_

\(\mathrm{Pr}(J\subseteq G_n,\mathcal{A}_n)\le\frac{e^{\xi_nw}}{(n-2w)^w}.\) (121)

_Consequently, uniformly for_ \(w\le K_0\mathrm{log}n\)_, for any fixed K_<sub>0</sub>,

\(\mathrm{Pr}(J\subseteq G_n,\mathcal{A}_n)\le(1+o(1))n^{-w}.\) (122)

_A connected unlabelled w-edge graph has at most D(D_-1)<sup>_w_-1</sup> _admissible port-labellings._

_Proof._ The prescribed Hamilton arcs either are impossible or form vertex-disjoint directed paths. If their number is _b\<n_, contracting them gives probability

\(\frac{(n-b-1)!}{(n-1)!}\le(n-b)^{-b}.\) (123)

In each matching round the prescribed edges form a matching, or the probability is zero. Apply Lemma 2 successively, conditional on the preceding rounds. Each denominator in \(\Phi_s(n)\) is at least _n_-2_w_, and the sum of all prescribed edge counts is _w_. This proves (121). The stated rate for \(\xi_n\) gives (122).

For the last assertion, order the edges so that each edge after the first meets a preceding one. The first edge has _D_ possible symbols. Each subsequent edge has at least one forbidden port at a previously encountered vertex, and therefore at most _D_-1 choices.

## A.2 Recovery with the full alphabet dependence

For recovery, each coordinate may have its own conditional nonzero-error distribution \(\theta_e\), with the same corruption probability _p_. Let \(\Theta\in(0,1]\) be a fixed upper bound on \(\mathrm{max}_{e,a\neq 0}\theta_e(a)\) along the graph-size sequence. The common channel in (58) has \(\Theta=\theta_\mathrm{max}\). Evenness is not needed for the recovery criterion or its one-coordinate extension. A nonzero flow \(f\in C^\perp\) is _Hamming-favorable_ if \(|E-f|\le|E|\). If a Hamming-favorable flow is disconnected, at least one connected component of its support is Hamming-favorable. It is therefore enough to consider connected supports. We prove recovery by minimum Hamming weight, which also bounds the error probability of the optimal ML decoder.

### A.2.1 Pairwise comparison and a budget on the support excess

Write<tbc>

\(B_\Theta(p)=2\sqrt{(1-p)p\Theta}+p(1-\Theta).\) (124)

<tbc>For a common even distribution \(\theta\) and \(0\le p\le 1/2\), Cauchy-Schwarz on the terms with \(z\notin\{0,a\}\) in (70) gives

\(2\sqrt{(1-p)p\theta_\mathrm{max}}\le Z_\theta(p)\le B_{\theta_\mathrm{max}}(p)\le Z_\theta(p)+p.\) (125)

Indeed, the remainder for a shift _a_ is at most \(p(1-\theta(a))\), and \(2\sqrt{(1-p)px}+p(1-x)\) is nondecreasing for \(0\le x\le 1\) when \(p\le 1/2\).

