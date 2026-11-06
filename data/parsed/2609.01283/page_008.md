_Can this algebraic paradigm be lifted from reachability (k_=1_) to k-bounded flow-- deciding whether at least k edge-disjoint_ (_s,t)-paths survive f edge updates?_

We answer this question by building a general algebraic framework based on matroids.

## Modeling Flow as Matroid Intersection.

Given a directed graph _H_=(_V<sub>H</sub>,E<sub>H</sub>_) with designated terminals _s_ and _t_, we can encode the existence of exactly \(\lambda\) edge-disjoint (_s,t_)-paths as a matroid intersection problem. We first augment _H_ by adding exactly _k_ zero-cost self-loops at every vertex \(v\in V_H\backslash\{s,t\}\), and \(k-\lambda\) zero-cost self-loops at _s_ and _t_. We then define two partition matroids on this augmented edge set:

• _M_<sub>out</sub>: A subset \(S\subseteq E_H\) is independent if every vertex \(v\in V_H\backslash\{t\}\) has at most one outgoing edge in _S_.<tbc>

• _M_<sub>in</sub>: A subset \(S\subseteq E_H\) is independent if every vertex \(v\in V_H\backslash\{s\}\) has at most one incoming edge in _S_.

A common basis of _M_<sub>out</sub> and _M_<sub>in</sub> is a subset _S_ that satisfies both degree constraints tightly. Combinatorially, such a set _S_ forces the existence of exactly \(\lambda\) edge-disjoint (_s,t_)-paths, with the self-loops absorbing the remaining degree budget at each vertex. Furthermore, a minimum-weight common basis corresponds exactly to the minimum-cost routing of these paths.

To test for _k_-bounded flow, we must check if the graph can support the packing of _k_ such structures. This is equivalent to checking if the ground set _E<sub>H</sub>_ contains a subset that can be partitioned into _k_ common bases of _M_<sub>out</sub> and _M_<sub>in</sub>.

Our resolution to this is to pass to _k-fold unions_. The _k_-fold union \(M^{\vee k}\) of a matroid _M_ is a matroid whose independent sets are the union of _k_ independent sets of _M_. Because partition matroids are strongly base-orderable, checking for a _k_-packing of common bases is perfectly equivalent to checking for a _single_ common basis of the _k_-fold unions \(M_\mathrm{out}^{\vee k}\) and \(M_\mathrm{in}^{\vee k}\).

To represent these unions algebraically, we use the randomized construction of Narayanan, Saran and Vazirani \[NSV94\]. If a linear matroid _M_ of rank _r_ has a representation matrix \(A\in\mathbb{F}^{r\times m}\), its _k_-fold union \(M^{\vee k}\) can be represented by stacking _k_ copies of _A_, each scaled column-wise by a random diagonal matrix _C<sub>i</sub>_:

\(U=\big(AC_1;AC_2;\dots;AC_k\big)\in\mathbb{F}^{kr\times m}\)

Let _U_<sub>out</sub> and _U_<sub>in</sub> be the \(kr\times m\) union representation matrices for \(M_\mathrm{out}^{\vee k}\) and \(M_\mathrm{in}^{\vee k}\). We associate a formal variable _Y_ and an independent random scalar _x<sub>e</sub>_ with each element _e_, forming a diagonal weight matrix \(D\in\mathbb{F}[Y]^{m\times m}\) where _D<sub>e,e</sub>=x<sub>e</sub>Y_<sup>_W_+**_wt_**(_e_)</sup>.

Then the _mixed Laplacian_ is defined as:

\(\mathcal{L}_\mathrm{pack}=U_\mathrm{out}DU_\mathrm{in}^T\in\mathbb{F}^{kr\times kr}\)

By a _k_-fold Cauchy-Binet expansion, the determinant of L<sub>pack</sub> enumerates the common bases of the unions. _Thus, k-bounded flow is reduced entirely to evaluating whether_ \(\mathrm{det}(\mathcal{L}_\mathrm{pack})\neq 0\) _(for existence) and isolating its minimum Y-degree (for minimum cost)._

## Sensitivity via Sparse Determinant Updates.

The power of this formulation in the sensitivity setting lies in sparsity. An update to an edge _e_ in the graph only modifies the _e_-th rank-one term in the Laplacian sum \(\mathcal{L}_\mathrm{pack}=\sum_{e\in E}D_{e,e}(u_\mathrm{out})_e(u_\mathrm{in})_e^T\). Because the base partition matroids are extremely sparse (_O_(1) non-zeros per column), the union columns (_u_<sub>out</sub>)_<sub>e</sub>_ and (_u_<sub>in</sub>)_<sub>e</sub>_ have at most _O(k_) non-zeros. Consequently:

