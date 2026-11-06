**Theorem 1.4** (counting and sampling random _k_-uniform hypergraph _q_-colorings)**.** _There exists a universal constant_ \(c\ge 1\) _such that the following holds with high probability over the choice of the random hypergraph_ \(H=(V,\mathcal{E})\sim H(k,n,\lfloor\alpha n\rfloor)\) _where_ \(\alpha\le q^k/(qk)^c\).

_For any_ \(\varepsilon>0\)_, there exist the following algorithms, both with running time_ \((n/\varepsilon)^{poly(logq,k,\alpha)}\):

\(\bullet\) _(Counting) A deterministic algorithm that outputs_ \(\hat{Z}\) _which is an_ \(\varepsilon\)_-approximation of the number of proper q-colorings Z(H,q_) _of H, i.e.,_ \((1-\varepsilon)Z(H,q)\le\hat{Z}\le(1+\varepsilon)Z(H,q)\);<tbc>

\(\bullet\) _(Sampling) An algorithm that outputs a random assignment_ \(X\in[q]^V\) _that is_ \(\varepsilon\)_-close in total variation distance to_ \(\mu_H\)_, the uniform distribution over all proper q-colorings of H._

An analog of Theorem 1.4 holds for random _regular_ hypergraph colorings as well.

**Remark 1.5** (Comparison with worst-case bounded-degree CSPs)**.** It is helpful to review the literature on counting and sampling for worst-case bounded-degree CSPs. A random _k_-SAT formula with density \(\alpha\) has an average degree of \(k\alpha\), making it comparable to a _k_-SAT formula with maximum degree \(d=k\alpha\). For bounded-degree CSPs, while a solution exists and can be efficiently found when \(d\lesssim 2^k\) \[EL75, MT10\] via the celebrated (algorithmic) Lovász local lemma, the problem of sampling and counting solutions becomes intractable when \(d\unknown 2^{k/2}\) \[BGG<sup>+</sup>19\]. A similar separation occurs for _k_-uniform hypergraph _q_-colorings: while the existence/searching problem can be solved when \(d\lesssim q^k\), the sampling/counting problem becomes intractable at \(d\unknown q^{k/2}\) \[GGW22\]. This demonstrates that the sampling and counting problems are computationally much harder than searching for worst-case bounded-degree CSPs. In contrast, our findings demonstrate that for random CSPs, the sampling and counting problems are not significantly computationally harder than their satisfiability and algorithmic counterparts.

**Remark 1.6.** As mentioned, our main results Theorems 1.2 and 1.4 in fact apply to a broad family of random CSPs (see Theorem 3.2 for a formal statement). One may wonder if the counting/sampling threshold would always be close to or even match the searching threshold for general random CSPs. The answer is probably no in general. A very recent paper \[EG24\] by El Alaoui and Gamarnik shows that for the symmetric binary perceptron model, another important example of random CSPs, sampling a solution is intractable at _any_ constant density (for two common classes of algorithms) while there are known algorithms for finding solutions at sufficiently low density.

We note that the random CSPs considered in this paper are _sparse_, in the sense that both the size of constraints and the (average) degree of variables are constant. Meanwhile, the symmetric binary perceptron model is _dense_ as the constraint size and variable degrees are both linear. This leads to a huge difference in the geometry of the solution space: For the symmetric binary perceptron model at any constant density, most solutions are isolated with linear distance from each other. Therefore, it is still possible that the counting/sampling threshold is equivalent to the searching threshold, or at least somewhere near it, for general sparse random CSPs as considered in this paper.

## 1.2. Constraint-wise coupling and replica symmetry.

Given the extensive focus in the literature, we primarily present our results for random _k_-SAT in this subsection; however, the results and proofs are equally applicable to random hypergraph colorings or other random atomic CSPs.

The central tool for our algorithmic results is a constraint-wise coupling developed in \[WY24\]. Let \(\Phi=(V,C)\sim\Phi(k,n,\lfloor\alpha n\rfloor)\) be a _k_-SAT instance at density \(\alpha>0\), and let \(c_0\in C\) be an arbitrary clause. We define \(\mu_\Phi\) as the uniform distribution over all solutions to \(\Phi\), and \(\mu_{\Phi\backslash c_0}\) as the uniform distribution over solutions to \(\Phi\backslash c_0:=(V,C\backslash\{c_0\})\) with the clause _c_<sub>0</sub> removed from \(\Phi\). We establish the following result concerning the 1-Wasserstein distance between the two distributions \(\mu_\Phi\) and \(\mu_{\Phi\backslash c_0}\).

**Theorem 1.7.** _There exists a universal constant_ \(c\ge 1\) _such that the following holds with high probability over the choice of the random k-SAT formula_ \(\Phi=(V,C)\sim\Phi(k,n,\lfloor\alpha n\rfloor)\) _where_ \(0<\alpha\le 2^k/k^c\).

_For any_ \(c_0\in C\)_, it holds that_

\(W_1\left(\mu_\Phi,\mu_{\Phi\backslash c_0}\right)=O(logn),\)

_where_ \(W_1(\cdot,\cdot)\) _denotes the_ 1_-Wasserstein distance with respect to the Hamming metric. That is, there exists a coupling_ (_X,Y_) _of_ \(\mu_\Phi\) _and_ \(\mu_{\Phi\backslash c_0}\) _such that_ \(\mathbb{E}[d_\mathrm{Ham}(X,Y)]=O(logn)\).

