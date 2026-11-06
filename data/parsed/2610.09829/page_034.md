_R_. Let \(\mathcal{S}_{\delta,R,\gamma}=\{\mathsf{e},\mathsf{n}\}\cup\left(\Gamma_{\delta,R,\gamma}\times\Gamma_{\delta,R,\gamma}\right)\), for \(\gamma\in R\). We will use \(\mathcal{S}_{\delta,R,\gamma}\) to capture the discussed intersections of a descendant of \(\gamma\) in the solution with other cycles in \(\Gamma_{\delta,R,\gamma}\).

Consider \(\gamma\in R\), and we let \(\gamma^\circ\) be the clockwise cyclic ordering of edges in \(E(\gamma)\). We use the convention that, for instance, (_a,b,c),(b,c,a),(c,a,b_), denote the same cyclic ordering. We attach the symbol \(\circ\) to denote cyclic ordering, and all such orderings will be the clockwise cyclic ordering obtained using the given planar embedding of _G_. We now create the cyclic ordered set of elements in \(\Gamma_{\delta,R,\gamma}\), in the order in which the (starting) point of their intersections with \(\gamma\) appears in \(\gamma^\circ\). Note that from Observation 5.4 for distinct \(\iota,\iota'\in\Gamma_{\delta,R,\gamma}\), \(E(\iota)\cap E(\iota')\cap E(\gamma)=\emptyset\). Due to the above we obtain the unique (clockwise) cyclic ordering \(\Gamma_{\delta,R,\gamma}^\circ\) of \(\iota\in\Gamma_{\delta,R,\gamma}\), based on the order in which the path \(\iota\cap\gamma\) appears in \(\gamma\). For (not necessarily distinct) \(\psi,\tau\in\Gamma_{\delta,R,\gamma}\) we let \(\Gamma_{\delta,R,\gamma}[\psi,\tau]\) be the ordered set of elements starting from \(\psi\) till \(\tau\) in \(\Gamma_{\delta,R,\gamma}^\circ\) (inclusive of both \(\psi,\tau\)). We note that \(\Gamma_{\delta,R,\gamma}[\psi,\tau]\) is not a cyclic ordering, but a linear ordering. For simplicity, we will also treat \(\Gamma_{\delta,R,\gamma}[\psi,\tau]\) as a set (when the ordering is irrelevant).

Let \(\beta\) be a descendant of \(\gamma\), i.e., \(\beta\le\gamma\) (see Proposition 5.2 (1)), or a sub-path of a descendant of \(\gamma\), such that \(\beta\neq\gamma\) and \(E(\beta\cap\gamma)\neq\emptyset\). As \(\beta\neq\gamma\), note that \(\beta\cap\gamma\) must be a path (not a cycle) in _G_ (see Proposition 5.1). Let \(\Gamma_{\delta,R,\gamma,\beta}\) be the subset of elements from \(\Gamma_{\delta,R,\gamma}\) that share an edge with \(\beta\), i.e., \(\Gamma_{\delta,R,\gamma,\beta}=\{\iota\in\Gamma_{\delta,R,\gamma}|E(\iota)\cap E(\beta)\neq\emptyset\}\). We have the following simple observation regarding the set \(\Gamma_{\delta,R,\gamma,\beta}\) which follows from Proposition 5.1.

**Observation 5.6.** _If_ \(\Gamma_{\delta,R,\gamma,\beta}\neq\emptyset\)_, then there are (not necessarily distinct) elements_ \(\psi,\tau\in\Gamma_{\delta,R,\gamma}\) _such that_ \(\Gamma_{\delta,R,\gamma,\beta}=\Gamma_{\delta,R,\gamma}[\psi,\tau]\).

## Auxiliary .

The next definition will allow us to guess the discussed intersection properties and look for solutions that have these properties.

**Definition 5.9.** Consider an \(\alpha\)-lineage-free set \(R=\{\gamma_i|i\in[b]\}\), integers \(h_1,h_2,\dots,h_b\ge 1\) with \(\sum_{i=1}^bh_i=h-1\), and for each \(i\in[b]\), \(\theta_i\in\mathcal{S}_{\alpha,R,\gamma_i}\). We define \(\Pi_{\mathcal{P},\alpha,h}(\gamma_i,h_i,\theta_i)_{i\in[b]}\) as the maximum over \(w(\mathcal{C}\cup\mathcal{P})\), where C is a solution for \(\Pi_\mathcal{P}(\alpha,h)\) and it additionally satisfies the following:

1. _R_ is the set of representatives for the solution descendants \(\{\beta_i|i\in[b]\}\) of \(\alpha\) in C. For each \(i\in[b]\), \(\gamma_i\) is the representative for \(\beta_i\).<tbc>

2. For each \(i\in[b]\), exactly _h<sub>i</sub>_ cycles of C are nodes in the subtree \(\mathcal{T}_{\beta_i}\).<tbc>

3. For \(i\in[b]\), the following holds (see Figure 5):

(a) If \(\theta_i=\mathsf{e}\), then \(\beta_i=\gamma_i\).<tbc>

(b) If \(\theta_i=\mathsf{n}\), then \(\beta_i\neq\gamma_i\) and \(E(\beta_i)\cap E(\delta)=\emptyset\) for all \(\delta\in\Gamma_{\alpha,R,\gamma_i}\).<tbc>

(c) Otherwise, let \(\theta_i=(\psi_i,\tau_i)\). We have \(\beta_i\neq\gamma_i\) and \(\emptyset\neq\Gamma_{\alpha,R,\gamma_i,\beta_i}=\Gamma_{\alpha,R,\gamma_i}[\psi_i,\tau_i]\).

In the above, a C that satisfies the stated conditions (but may or may not achieve the maximum) is a _solution_ for \(\Pi_{\mathcal{P},\alpha,h}(\gamma_i,h_i,\theta_i)_{i\in[b]}\). Moreover, if it additionally achieves the maximum, then it is an _optimal_ solution for \(\Pi_{\mathcal{P},\alpha,h}(\gamma_i,h_i,\theta_i)_{i\in[b]}\).

The next lemma (proved in Section 5.4) helps us identify the correct solution descendants of an optimal solution, if we know how the solution behaves with respect to the definition stated above. For the remainder of this section we show how we can compute \(\Pi_\mathcal{P}(\alpha,h)\) using this lemma.

