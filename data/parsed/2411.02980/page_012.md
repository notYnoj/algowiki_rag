<tbc>for sufficiently large _n_. Thus, it follows that

\(\mathbf{Pr}_{\Phi\sim\Phi(k,n,m)}[H_\Phi\notin\mathbb{P}]\)<br>
\(\ge\mathbf{Pr}_{\Phi\sim\Phi(k,n,m)}[H_\Phi\notin\mathbb{P}|\mathcal{E}_{k,n,m}]\cdot\mathbf{Pr}_{\Phi\sim\Phi(k,n,m)}[\mathcal{E}_{k,n,m}]\)<br>
\(\ge\frac{1}{2}\mathrm{e}^{-k^2\alpha}\cdot\mathbf{Pr}_{H\sim H(k,n,m)}[H\notin\mathbb{P}].\)

Since \(\mathbf{Pr}_{\Phi\sim\Phi(k,n,m)}[H_\Phi\notin\mathbb{P}]=o(1/n)\), we conclude that \(\mathbf{Pr}_{H\sim H(k,n,m)}[H\notin\mathbb{P}]=o(1/n)\). □

As a corollary, we have the following lemma immediately.

**Lemma 3.15.** _For any fixed parameters_ \(k,\alpha,\eta,\rho,\varepsilon_1,p_1,\varepsilon_2,p_2\) _where_ \(\eta k\ge 4\), \(\mathrm{e}(\rho k\alpha)^\eta\le 1\), \(\varepsilon_1=2\eta\), \(6k^5\le p_1\le\mathrm{e}^{k-2}\alpha\), \(\varepsilon_2=12k^5/((1-\eta)\eta p_1)\) _and p_<sub>2</sub>=e_k_<sup>2</sup>_, with probability_ 1-_o_(1_/n_) _over the choice of all k-uniform hypergraphs with n vertices and density_ \(\alpha\)_, a random k-uniform hypergraph H is_ \((k,\alpha,\varepsilon_1,\varepsilon_2,\eta,\rho,p_1,p_2)\)_-nice._

We conclude this section by noting that Theorem 3.3 is simply a combination of Lemmas 3.13 and 3.15. Here, we do not need the lower bound on _k_ in the conditions of Theorems 1.2 and 1.4 as the case of small _k_ can be handled by taking a sufficiently large _c_.

## 4. Recursive coupling of random CSPs

In this section, we establish the following theorem regarding the decay of correlations for CSP instances that satisfy the structural properties introduced in the previous section. We note that Theorem 1.7 from introduction is an immediate consequence of Theorems 3.3 and 4.1.

**Theorem 4.1.** _Let_ \(\Phi=(V,[q],\mathcal{C})\) _be an satisfiable atomic CSP formula satisfying Condition 3.1. Let_ \(c_0\in\mathcal{C}\) _be an arbitrary constraint. There exists a coupling_ (_X,Y_) _of_ \(\mu_\mathcal{C}\) _and_ \(\mu_{\mathcal{C}\backslash\{c_0\}}\) _such that for any integer_ \(\mathrm{log}n\le M\le\rho m\)_, it holds that_

\(\mathbf{Pr}\left[d_\mathrm{Ham}(X,Y)\ge k\cdot M\right]\le 2^{-M}.\)

Theorem 4.1 asserts that for CSP instances satisfying the specified structural properties, the discrepancy between uniform satisfying assignments induced by any particular constraint decays exponentially.

### 4.1. The coupling procedure.

The coupling in Theorem 4.1 is the constraint-wise recursive coupling introduced in \[WY24\]. This coupling procedure, denoted as \(\mathrm{Couple}(\mathcal{E},\mathcal{F},\sigma,\tau)\), is formally described in Algorithm 2. The procedure takes as inputs:

\(\bullet\) a pair of collections of pinned atomic constraints \(\mathcal{E},\mathcal{F}\subseteq\mathcal{C}^*\), corresponding to two formulas;<tbc>

\(\bullet\) a pair of partial assignments \(\sigma,\tau\in[q]^\Lambda\), specified on the same subset \(\Lambda\subseteq V\) of variables.

It is assumed that both pinned formulas \(\mathcal{E}^\sigma\) and \(\mathcal{F}^\tau\) are satisfiable. The objective of the procedure is to generate a pair of random assignments \((X,Y)\in[q]^V\times[q]^V\), such that marginally \(X\sim\mu_\mathcal{E}^\sigma\) and \(Y\sim\mu_\mathcal{F}^\tau\), while minimizing the discrepancy between _X_ and _Y_.

The validity of this coupling is ensured by the following proposition. A similar correctness result was proven under a stronger local lemma condition in \[WY24, Lemma 3.3\].

**Proposition 4.2.** _Assume that the atomic CSP formula_ \(\Phi=(V,[q],\mathcal{C})\) _is satisfiable. For any constraint_ \(c_0\in\mathcal{C}\)_, the procedure_ \(\mathrm{Couple}(\mathcal{C}\backslash\{c_0\},\mathcal{C},\emptyset,\emptyset)\) _terminates with probability 1 and returns a pair of random assignments_ \((X,Y)\in[q]^V\times[q]^V\) _such that marginally_ \(X\sim\mu_{\mathcal{C}\backslash\{c_0\}}\) _and_ \(Y\sim\mu_\mathcal{C}\).

_Proof sketch._ The proof follows the same inductive framework as the proof of \[WY24, Lemma 3.3\]. We provide a brief outline here.

First, by applying structural induction in the top-down order of recursion, one can verify the following induction hypothesis for each recursive call \(\mathrm{Couple}(\mathcal{E},\mathcal{F},\sigma,\tau)\):

\(\Lambda(\sigma)=\Lambda(\tau),\mathcal{P}[\mathcal{E}\wedge\sigma]>0,\text{and}\mathcal{P}[\mathcal{F}\wedge\tau]>0.\)

This induction holds as long as the initial formula with constraints C is satisfiable, and it ensures that the coupling procedure remains well-defined throughout the recursion.

