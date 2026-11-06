\(\mathrm{cost}(x,I)\ge\rho\cdot\mathrm{OPT}(I)\) to holds for a given \(\rho\le 1\). We say that \((\Pi,\mathrm{sol},\mathrm{cost},\mathrm{goal})\) is _polynomial-time approximable_ to a factor of \(\rho\) if it admits a factor-\(\rho\) approximation algorithm that runs in polynomial time.

We say that \((\Pi,\mathrm{sol},\mathrm{cost},\mathrm{goal})\) admits a _polynomial-time approximation scheme_ (PTAS) if for every approximation error \(\varepsilon>0\), it is polynomial-time approximable to a factor of \(1+\varepsilon\) (for minimization) and \(1-\varepsilon\) (for maximization).

**Definition 2** (Fixed-parameter approximation algorithms)**.** Let \((\Pi,\mathrm{sol},\mathrm{cost},\mathrm{goal})\) be an optimization problem and _I_ an instance of \(\Pi\). We say that \((\Pi,\mathrm{sol},\mathrm{cost},\mathrm{goal})\) is FPT_-approximable to factor_ \(\rho\) with respect to a parameter _k_ if it admits a factor-\(\rho\) approximation algorithm that runs in time \(f(\rho,k)\cdot n^{O(1)}\), where _f_ is a computable function on _k_ and \(\rho\).

Consequently, we say that \((\Pi,\mathrm{sol},\mathrm{cost},\mathrm{goal})\) admits an FPT_-approximation scheme_ (FPT-AS) with respect to a parameter _k_ if for every \(\varepsilon>0\) it is FPT-approximable to factor \((1+\varepsilon)\) (for minimization) and \((1-\varepsilon)\) (for maximization) with respect to _k_.

To show that no FPT-approximation scheme exists, we need a specific reduction, called _gap-producing parameterized reduction_ \[10\]. The idea is to provide a parameterized reduction to a gap version of an optimization problem. Below, we only define the reduction for minimization problems. The one for maximization problems is analogous.

**Definition 3** (gap-producing parameterized reduction)**.** Let \(X=(\Pi,\mathrm{sol},\mathrm{cost},\mathrm{goal})\) be a minimization problem and let _k_ be the natural parameter of _X_ to turn it into a decision problem. Let \(\alpha:\mathbb{N}\rightarrow\mathbb{N}\) be a computable function.

A reduction _R_ from a parameterized problem \(\hat{\Pi}\) with parameter _h_ to our optimization problem _X_ parameterized by _k_ is called an \(\alpha\)_-gap producing parameterized reduction_ if for every instance \(\hat{I}\) of \(\hat{\Pi}\) with parameter _h_, _R_ produces in \(f(h)\cdot|\hat{I}|^{O(1)}\) time an instance _I_ of \(\Pi\) with parameter _k_ such that

(i) _k_ is bounded by a function of _h_,<tbc>

(ii) if \((\hat{I},h)\) is a yes-instance, then _I_ admits a solution _x_ with \(\mathrm{cost}(x,I)\le k\);<tbc>

(iii) if \((\hat{I},h)\) is a no-instance, then every solution _x_ of _I_ has \(\mathrm{cost}(x,I)>\alpha(k)\cdot k\).

The existence of an \(\alpha\)-gap-producing parameterized reduction from a parameterized intractable (e.g., W\[1\]-hard) problem shows that a factor-\(\alpha\) FPT approximation algorithm is unlikely, unless FPT=W\[1\].

## 3 FPT Inapproximability of Min-BP-SMI and Min-BP-SRI

In this section, we show that Min-BP-SMI and Min-BP-SRI remain parameterized inapproximable with respect to \(\beta\), where \(\beta\) denotes the number of blocking pairs in the natural parameterization variant of the problems. The idea is to present a gap producing reduction from the Clique problem that is W\[1\]-hard with respect to the size _h_ of clique.

Clique

**Input:** A directed graph _G_=(_V,E_) and a non-negative number _h_.

**Question:** Does _G_ admit a _clique_ \(K\subseteq V\) of size at least _h_, , i.e., _G_\[_K_\] is a complete subgraph (aka. _clique_) of size at least _h_?

We remark that the reduction presented here is a modified version of Theorem 1 by Gupta et al. \[12\]. In their reduction, the vertex gadget is connected to the edge gadget by an edge. However, we add \([(h+\genfrac(){pt}{2}{h}{2})\cdot F(h+\genfrac(){pt}{2}{h}{2})+1]\) cycles of length four to connect a vertex gadget with an "incident" edge gadget instead to boost the gap.

**Theorem 1.** _Let_ \(F:\mathbb{N}\rightarrow\mathbb{N}\) _be an arbitrary computable function. Given an instance_ \((\mathcal{P},k,\beta)\) _of_ Min-BP- SMI-dec _it is_ W\[1\]_-hard to distinguish between the following two cases:_

(_i)_ P _admits a size-k matching with at most_ \(\beta\) _blocking pairs._<tbc>

_(ii)_ _Every size-at-least k matching of_ P _has at least_ \(F(\beta)\cdot\beta\) _blocking pairs._

_Proof._ We reduce from Clique, parameterized by the clique size _h_. Let (_G_=(_V,E),h_) be an instance of Clique with \(V=\{v_1,\dots v_\hat{n}\}\) and \(E=\{e_1,\dots,e_{\hat{m}}\}\). We construct an instance (_I,k_) of Min-BP-SMI as follows; the construction is illustrated in Figure 1. For brevity’s sake, define \(L:=(h+\genfrac(){pt}{2}{h}{2})\cdot F(h+\genfrac(){pt}{2}{h}{2})+1\).

