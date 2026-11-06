Pick \(q=t_\mathrm{unif}^{41}\cdot t_\mathrm{sl}^2\cdot 2^{\sqrt{\mathrm{log}n}}\), then it follows that

\(r'\le\frac{r}{2^{\Omega(\sqrt{\mathrm{log}n})}}.\)

First, this implies that each recursive call indeed makes progress and that the algorithm terminates. Second, this further implies that the recursion reaches depth at most \(O(\sqrt{\mathrm{log}n})\), and as each call of the algorithms spawns only three recursive calls the total number of recursive calls is \(3^{O(\sqrt{\mathrm{log}n})}\).

We can use this to bound the final size of (I,T). Focus on any recursive call of the algorithm. The sets we construct have size<tbc>

\(|\mathcal{T}_\mathrm{unif}|\le|\mathcal{T}_\mathrm{sl}|+|\mathcal{I}_\mathrm{sl}|\cdot\tilde{O}\big(\frac{n_1n_2n_3}{t_\mathrm{unif}}\big)\le\tilde{O}\big(\frac{n_1n_2n_3}{t_\mathrm{sl}}+\frac{n_1n_2n_3t_\mathrm{sl}^2}{t_\mathrm{unif}}\big)\)

<tbc>and

\(|\mathcal{I}_\mathrm{reg}|\le q^6\cdot|\mathcal{I}_\mathrm{unif}|\le q^6\cdot t_\mathrm{sl}^2\cdot t_\mathrm{unif}^{41}\cdot\mathrm{log}^3n\le t_\mathrm{sl}^{14}\cdot t_\mathrm{unif}^{287}\cdot 2^{O(\sqrt{\mathrm{log}n})}.\)

The total sizes |T| and |I| are worse only by a factor \(3^{O(\sqrt{\mathrm{log}n})}\). Choosing _t_<sub>sl</sub>=_t_ and _t_<sub>unif</sub>=_t_<sup>3</sup>, this is as claimed in the theorem statement.

### Running Time.

Finally, focus on the running time. Per recursive call the sum of all contributions analyzed before is, loosely bounded,

\(\tilde{O}\big(\frac{n_1n_2n_3}{t_\mathrm{sl}}+\frac{n_1n_2n_3t_\mathrm{sl}^2}{t_\mathrm{unif}}+(n_1n_2+n_2n_3+n_1n_3)r\cdot t_\mathrm{unif}^{41}\cdot t_\mathrm{sl}^2\cdot q^6\big)\)<br>
\(\le\big(\frac{n_1n_2n_3}{t}+(n_1n_2+n_2n_3+n_1n_3)rt^{875}\big)^{1+o(1)}.\)

Across all recursive calls the running time worsens only by \(3^{O(\sqrt{\mathrm{log}n})}=n^{o(1)}\).

## 4.4 Reduction from Uniform Regular to Uniform Low-Doubling Exact Triangle

The fourth and final step is to reduce to uniform (regular) low-doubling Exact Triangle. This step is again due to \[4\] and \[32\] almost without modifications--we merely extend the proof to rectangular matrices and show the slightly stronger condition that the joint set of entries of all three matrices _A,B,C_ has small doubling. The reduction crucially relies on the regularity condition established before and also on the BSG theorem from additive combinatorics \[14, 58\]. Specifically, we use the following algorithmic covering version of the BSG theorem due to Chan and Lewenstein \[32\].

**Theorem 4.11** (BSG Covering \[32\])**.** _Let_ \(X,Y,Z\subseteq\mathbb{Z}\) _be sets of size at most n, and let_ \(L\ge 1\)_. Then there are subsets_ \(X_1,\dots,X_L\subseteq X\) _and_ \(Y_1,\dots,Y_L\subseteq Y\) _satisfying the following properties:_

1. \(|X_\ell+Y_\ell|\le O(L^5n)\) _for all_ \(\ell\in[L]\),<tbc>

_2._ \(|R|\le O(n^2/L)\) _where_ \(R=\{(x,y)\in X\times Y:x+y\in Z\}\backslash\bigcup_{\ell=1}^L(X_\ell\times Y_\ell)\).

_The sets X_<sub>1</sub>_,...,X<sub>L</sub>,Y_<sub>1</sub>_,...,Y<sub>L</sub> and R can be computed in deterministic time_ \(\tilde{O}(n^\omega L)\).

The following simple lemma will also be useful.

**Lemma 4.12.** _Let_ \(X,Y\subseteq\mathbb{Z}\) _be sets with doubling_ \(|X+X|\le K|X|\) _and_ \(|Y+Y|\le K|Y|\)_. Then Z=X+Y has doubling_ \(|Z+Z|\le K^8|Z|\).

