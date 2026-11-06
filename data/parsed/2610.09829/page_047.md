\(=w^\text{\texttt{ovr}}(\varepsilon_1,\varepsilon_\tilde{p})+w^2(\widehat{\mathcal{C}})+w^3(\widehat{\mathcal{C}})+\sum_{i\in[\tilde{p}-1]}w(E(\widehat{\beta}_i\cap\widehat{\beta}_{i+1})\backslash E(\mathcal{P}))\) (4)

Also, from Definition 5.13 (2 and 3) we can obtain that \(w^2(\mathcal{C})=w^2(\widehat{\mathcal{C}})\) and \(w^3(\mathcal{C})=w^3(\widehat{\mathcal{C}})\). Using the above combined with Equation (2)-Equation (4), we can obtain that:

\(w(\mathcal{C}\cup\mathcal{P})-w(\widehat{\mathcal{C}}\cup\mathcal{P})\)<br>
\(\ge\big(\sum_{i\in[\tilde{p}]}\Pi_\mathcal{P}(\widetilde{\beta}_i,\widetilde{h}_i)-\sum_{i\in[\tilde{p}-1]}\zeta_{\widetilde{\beta}_i,\widetilde{\beta}_{i+1}}-w^\text{\texttt{ovr}}(\varepsilon_1^*,\varepsilon_\tilde{p}^*)\big)-\big(\sum_{i\in[\tilde{p}]}\Pi_\mathcal{P}(\widehat{\beta}_i,\widetilde{h}_i)-\sum_{i\in[\tilde{p}-1]}\zeta_{\widehat{\beta}_i,\widehat{\beta}_{i+1}}-w^\text{\texttt{ovr}}(\varepsilon_1,\varepsilon_\tilde{p})\big)\)

Moreover, as \(\{\widehat{\beta}_i|i\in[\tilde{p}]\}\) must satisfy all the requirements of Definition 5.12 (but may or may not achieve the maximum), by the choice of \((\varepsilon_1^*,\varepsilon_\tilde{p}^*)\) we can further obtain that:

\(\big(\sum_{i\in[\tilde{p}]}\Pi_\mathcal{P}(\widetilde{\beta}_i,\widetilde{h}_i)-\sum_{i\in[\tilde{p}-1]}\zeta_{\widetilde{\beta}_i,\widetilde{\beta}_{i+1}}-w^\text{\texttt{ovr}}(\varepsilon_1^*,\varepsilon_\tilde{p}^*)\big)-\big(\sum_{i\in[\tilde{p}]}\Pi_\mathcal{P}(\widehat{\beta}_i,\widetilde{h}_i)-\sum_{i\in[\tilde{p}-1]}\zeta_{\widehat{\beta}_i,\widehat{\beta}_{i+1}}-w^\text{\texttt{ovr}}(\varepsilon_1,\varepsilon_\tilde{p})\big)\ge 0\)

Thus, \(w(\mathcal{C}\cup\mathcal{P})-w(\widehat{\mathcal{C}}\cup\mathcal{P})\ge 0\).

We summarize the results obtained using the previous three results in the following corollary.

**Corollary 5.1.** _The following holds:_

1. _If_ \((\varepsilon_1^*,\varepsilon_\tilde{p}^*)=(\phi,\phi)\)_, then there is no solution for_ \(\Pi_{\mathcal{P},\alpha,h}(\gamma_i,h_i,\theta_i)_{i\in[b]}\).<tbc>

_2._ _Suppose there is an (optimal) solution_ \(\widehat{\mathcal{C}}\) _for_ \(\Pi_\mathcal{P}(\alpha,h)\)_, where for_ \(i\in[\tilde{p}]\)_, we have_ \(\widehat{\mathcal{C}}_i=\widehat{\mathcal{C}}\cap V(\mathcal{T}_{\widetilde{\gamma}_i})\)_. Then there is an (optimal) solution_ C _for_ \(\Pi_{\mathcal{P},\alpha,h}(\gamma_i,h_i,\theta_i)_{i\in[b]}\)_, where for_ \(i\in[\tilde{p}]\), \(\widetilde{\mathcal{C}}_i=\mathcal{C}\cap V(\mathcal{T}_{\widetilde{\gamma}_i})\)_, and the following holds: i)_ \(\mathcal{C}\backslash(\cup_{i\in[\tilde{p}]}\widetilde{\mathcal{C}}_i)=\widehat{\mathcal{C}}\backslash(\cup_{i\in[\tilde{p}]}\widehat{\mathcal{C}}_i)\)_, ii) for_ \(i\in[\tilde{p}]\), \(\widetilde{\gamma}_i\) _is the_ \((\alpha,\mathcal{C})\) _representative for_ \(\widetilde{\beta}_i\in\mathcal{C}\)_, and iii)_ \(w(\mathcal{C}\cup\mathcal{P})\ge w(\widehat{\mathcal{C}}\cup\mathcal{P})\).

We are ready to prove Lemma 5.6.

_Proof of Lemma 5.6._ This follows from Observation 5.8 and Corollary 5.1.

We have proved Lemma 5.6, which completes the proof of Lemma 5.5, which in turn finishes the proof of Theorem 1.2.

## 6 Conclusion and Open Questions

In this paper we resolved two open questions from \[4, 3\] on packing shortest cycles. First, we showed that Edge-Disjoint Shortest Cycle Packing is W\[1\]-hard parameterized by _k_ already on unweighted subcubic graphs, ruling out FPT algorithms for the problem on general graphs. Second, we obtained a single-exponential algorithm for Diverse Shortest Cycle Coverage on planar graphs. Several questions remain open.

**Kernelization.** First, does Diverse Shortest Cycle Coverage admit a polynomial-in-_k_ kernel on planar graphs? We are able to establish kernelization for some special cases, but the general case remains open. More precisely, for planar graphs, \[4, 3\] show that Edge-Disjoint<tbc>

