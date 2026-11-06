\(\widetilde{\gamma}_q[u,v]\}\).

Next, we define when a pair of vertices from \(\gamma_i\) or a descendant of \(\gamma_i\) is "abiding" for \(\theta_i\), for \(\gamma_i\in R_\mathbf{o}\). Intuitively speaking, it will be the case when Definition 5.9 (3c) is satisfied by them.

**Definition 5.10.** Consider \(i\in[b]\), where \(\gamma_i\in R_\mathbf{o}\). For distinct \(u,v\in V(\gamma_i)\), (_u,v_) is \(\theta_i\)_-abiding_ if \(\emptyset\neq\Gamma_{\delta,R,\gamma,\gamma[u,v]}=\Gamma_{\alpha,R,\gamma_i}[\psi_i,\tau_i]\). Similarly, \(\beta\in V(P_i)\) is \(\theta_i\)_-abiding_ if \(\emptyset\neq\Gamma_{\delta,R,\gamma,\beta}=\Gamma_{\alpha,R,\gamma_i}[\psi_i,\tau_i]\).

We next define the notion of _d-good_, which intuitively speaking will take into account the _d_- diversity of the choice of path intersection \(\widetilde{\gamma}_i[u,v]\) (or a descendant of \(\gamma\)) with edges in P, and with (the unknown) cycles \(\psi_i\) and \(\tau_i\), if these intersections are "partial" but they are not captured by the graph _H_. We remark here that we cannot simply add these missing edges as it will destroy the property that each connected component of _H_ is a path or a cycle--a property that aids us in our upcoming dynamic programming routine.<sup>7</sup>

**Definition 5.11.** Consider \(i\in[b]\), where \(\gamma_i\in R_\mathbf{o}\). For distinct \(u,v\in V(\gamma_i)\), (_u,v_) is _d_-good if the following holds:

1. For each \(P\in\mathcal{P}\), \(w(P\cap\gamma_i[u,v])\le d\), \(w(\alpha\cap\gamma_i[u,v])\le d\), and<tbc>

2. Consider \(i'\in[b]\backslash\{i\}\), where i) \(\gamma_{i^\prime}\in\{\psi_i,\tau_i\}\) and ii) \(\theta_{i^\prime}=\mathsf{e}\), or \(\gamma_{i^\prime}\in R_\mathbf{o}\) and \(\gamma_i\in\Gamma_{\alpha,R,\gamma_{i^\prime}}[\psi_{i^\prime},\tau_{i^\prime}]\backslash\{\psi_{i^\prime},\tau_{i^\prime}\}\). Then, we have \(w(\gamma[u,v]\cap\gamma_{i^\prime})\le d\).

Similarly, for \(\beta\in V(P_i)\), \(\beta\) is _d-good_ if the following holds:

1. For each \(P\in\mathcal{P}\), \(w(P\cap\beta)\le d\), \(w(\alpha\cap\beta)\le d\), and<tbc>

2. Consider \(i'\in[b]\backslash\{i\}\), where i) \(\gamma_{i^\prime}\in\{\psi_i,\tau_i\}\) and ii) \(\theta_{i^\prime}=\mathsf{e}\), or \(\gamma_{i^\prime}\in R_\mathbf{o}\) and \(\gamma_i\in\Gamma_{\alpha,R,\gamma_{i^\prime}}[\psi_{i^\prime},\tau_{i^\prime}]\backslash\{\psi_{i^\prime},\tau_{i^\prime}\}\). Then, we have \(w(\beta\cap\gamma_{i^\prime})\le d\).

For \(i\in[b]\), where \(\gamma_i\in R_\mathbf{o}\), let A_<sub>i</sub>_ be the set of ordered pairs of distinct vertices from \(V(\gamma_i)\) that are \(\theta_i\)-abiding and _d_-good. For \(i\in[\tilde{p}]\), let \(\widetilde{\mathcal{A}}_i=\mathcal{A}_{i_j}\) (recall, \(\widetilde{\gamma}_i=\gamma_{i_j}\)).

Consider a connected component \(\widetilde{H}=(\widetilde{\gamma}_1,\widetilde{\gamma}_2,\cdots,\widetilde{\gamma}_\tilde{p})\). Note for each \(i\in[\tilde{p}]\), we need to choose \(\widetilde{\beta}_i(=\beta_{i_j})\), that satisfies the requirements of Lemma 5.6 (see Figure 17). To do this, we will be fixing the intersections \(\widetilde{\beta}_1\cap\widetilde{\gamma}_1\) and \(\widetilde{\beta}_\tilde{p}\cap\widetilde{\gamma}_\tilde{p}\) (these two guesses helps us unify the cases for paths and cycles). To this end, we introduce the following. For \(\varepsilon_1=(u_1,v_1)\in\widetilde{\mathcal{A}}_1\) and \(\varepsilon_\tilde{p}=(u_\tilde{p},v_\tilde{p})\in\widetilde{\mathcal{A}}_\tilde{p}\), \((\varepsilon_1,\varepsilon_\tilde{p})\) is _d-diverse_ if \(w(\widetilde{\gamma}_1[u_1,v_1]\cap\widetilde{\gamma}_\tilde{p}[u_\tilde{p},v_\tilde{p}])\le d\).

**Dynamic programming states for computing** \(\beta_i\)**s.** We now formalize the intuitive description of the states that we gave previously, in the next definition. Consider a connected component \(\widetilde{H}=(\widetilde{\gamma}_1,\widetilde{\gamma}_2,\dots,\widetilde{\gamma}_\tilde{p})\). We remark that, for simplicity, our dynamic programming will actually be solving an optimization version of the problem, however, by simple memoizations, we can actual compute the \(\widetilde{\beta}_i\)s.

**Definition 5.12.** Consider \(\varepsilon_1=(u_1,v_1)\in\widetilde{\mathcal{A}}_1\) and \(\varepsilon_\tilde{p}=(u_\tilde{p},v_\tilde{p})\in\widetilde{\mathcal{A}}_\tilde{p}\) (see Definition 5.10), where \((\varepsilon_1,\varepsilon_\tilde{p})\) is _d_-diverse if \(\tilde{p}\ge 2\). For \(q\in[\tilde{p}]\), \((u,v)\in\widetilde{\mathcal{A}}_q\), we define \(\Lambda_{\varepsilon_1,\varepsilon_\tilde{p}}(q,u,v)\) as the maximum over \(\sum_{i\in[q]}\Pi_\mathcal{P}(\widetilde{\beta}_i,\widetilde{h}_i)-\sum_{i\in[q-1]}\zeta_{\widetilde{\beta}_i,\widetilde{\beta}_{i+1}}\), where \(\widetilde{\mathcal{C}}=\{\widetilde{\beta}_i|i\in[q]\}\) is a set of _q_ tree shortest cycles in _G_ such that:

<sup>7</sup>Note that not every 2-degenerate graphs have their connected components as paths and cycles.

