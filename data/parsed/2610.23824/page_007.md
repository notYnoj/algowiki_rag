\(\sigma:\{1,\dots,n\}\rightarrow\{1,\dots,n\}\) _is a permutation that is selected uniformly at random from n! possibilities, each with probability_ \(\frac{1}{n!}\).

**Definition 6** (First-Fit)**.** _First-Fit is an algorithm for online coloring that assigns each new vertex the smallest available color._

We use the following notation. Given a graph _G_=(_V,E_), we denote the set of vertices adjacent to \(v\in V\) as _N(v_), and the set of vertices adjacent to at least one vertex in \(S\subseteq V\) as _N(S_). For a vertex set \(X\subseteq V\) , we denote \(N_X(v):=N(v)\cap X\) and \(N_X(S):=N(S)\cap X\). We denote the subgraph induced by \(S\subseteq V\) as _G_\[_S_\]. We denote the chromatic number of _G_ as \(\chi(G)\). We denote the set of all independent sets as I(_G_). In _O_-, \(\Omega\)-, and \(\Theta\)-notation, we write \(\widetilde{O}(f(n))\), \(\widetilde{\Omega}(f(n))\), and \(\widetilde{\Theta}(f(n))\) to hide polylogarithmic factors in _f(n_).

## 3 Hardcore Model

In this section, we discuss the properties of randomly sampled independent sets. We sample independent sets using the _hardcore model_ \[DK25; Wei06\].

**Definition 7** (Hardcore Model)**.** _Given a graph G_=(_V,E), the hardcore model_ \(\mathsf{IS}_\lambda(G)\) _with parameter_ \(\lambda>0\) _is a probability distribution that chooses an independent set_ \(I\in\mathcal{I}(G)\) _with probability proportional to_ \(\lambda^{|I|}\)_. More precisely, define_

\(Z_\lambda(G):=\sum_{I\in\mathcal{I}(G)}\lambda^{|I|}.\)

_Then, an independent set_ \(I\in\mathcal{I}(G)\) _is chosen with probability_ \(\frac{\lambda^{|I|}}{Z_\lambda(G)}\)_. See Figure 4 for an example._

### 3.1 Basic Properties

First, we present some properties of the hardcore model that are used in the subsequent proofs.

**Proposition 8.** _Let_ \(\lambda>0\)_, and let G_=(_V,E_) _be a k-colorable graph. Then,_

\((1+\lambda)^{|V|/k}\le Z_\lambda(G)\le(1+\lambda)^{|V|}.\)

Probability
1
λ
λ
λ
λ
λ2
λ2
222 + 4A + 1
222 + 4A + 1
222 + 4A + 1
222 + 4A + 1
222 + 4A + 1
222 + 4A + 1
222 + 4A + 1
222 + 4A + 1
222 + 4A + 1

**Figure 4:** An example of the hardcore model, with the probability of selecting each independent set.

