Our software for computing small reflective and dihedral Ramsey numbers relies on the following corollaries of Lemma 2.7.

**Corollary 2.8.** _Let H be any graph,_ \(n\in\mathbb{N}\) _and_ \(\text{type}\in\{\text{ord},\text{ref},\text{cyc},\text{dih}\}\)_. Then:_

**_(1)_** \(R_\text{type}(P_n^\text{mon},H)\le R_\text{type}(P_{n+1}^\text{mon},H)\);

**_(2)_** \(R_\text{type}(S_n^\text{sc},H)\le R_\text{type}(S_{n+1}^\text{sc},H)\)_; and_

**_(3)_** \(R_\text{type}(K_n,H)\le R_\text{type}(K_{n+1},H)\).

_Proof._ The result follows from Lemma 2.7 by observing that there exists an increasing injective homomorphism from \(P_n^\text{mon}\), \(S_n^\text{sc}\) and _K<sub>n</sub>_, to \(P_{n+1}^\text{mon}\), \(S_{n+1}^\text{sc}\) and _K_<sub>_n_+1</sub>, respectively.

**Corollary 2.9.** _Let H be any graph,_ \(n\in\mathbb{N}\) _be even and_ \(\text{type}\in\{\text{ord},\text{ref},\text{cyc},\text{dih}\}\)_. Then_ \(R_\text{type}(M_n^\text{nest},H)\le R_\text{type}(M_{n+2}^\text{nest},H)\).

_Proof._ The result follows from Lemma 2.7 by observing that there exists an increasing injective homomorphism from \(M_n^\text{nest}\) to \(M_{n+2}^\text{nest}\).

**Corollary 2.10.** _Let H be any graph,_ \(n\in\mathbb{N}\) _and_ \(\text{type}\in\{\text{ref},\text{dih}\}\)_. Then_ \(R_\text{type}(P_n^\text{alt},H)\le R_\text{type}(P_{n+1}^\text{alt},H)\).

_Proof._ Let \(P_{n+1}^\text{ralt}\) denote the reverse alternating path of order _n_+1, which arises by reflecting \(P_{n+1}^\text{alt}\) with respect to the natural vertex order. Then there exists an increasing injective homomorphism from \(P_n^\text{alt}\) to \(P_{n+1}^\text{ralt}\), so Lemma 2.7 gives \(R_\text{type}(P_n^\text{alt},H)\le R_\text{type}(P_{n+1}^\text{ralt},H)\). Since \(P_{n+1}^\text{ralt}\) and \(P_{n+1}^\text{alt}\) are equivalent in the context of reflective and dihedral Ramsey numbers, Proposition 2.1 gives \(R_\text{type}(P_{n+1}^\text{ralt},H)=R_\text{type}(P_{n+1}^\text{alt},H)\).

## 3 Methodology

In the present section, we describe how the computation of permutational Ramsey numbers can be carried out by solving SAT problems. Our approach is a direct generalization of the SAT-based approach originally proposed by Poljak for ordered Ramsey numbers \[23\] and recently extended to cyclic Ramsey numbers \[4\].

Let _H_<sub>1</sub> and _H_<sub>2</sub> be two graphs, and let \(\Gamma_1\) and \(\Gamma_2\) be two permutation groups on their respective vertex sets. Now, consider a 2-edge-coloring of _K<sub>n</sub>_ for some \(n\in\mathbb{N}\), and let _G<sub>j</sub>_ be the spanning subgraph of _K<sub>n</sub>_ comprising the edges of color _j_, for \(j\in\{1,2\}\). For each \(\{u,v\}\in\genfrac(){pt}{2}{V(K_n)}{2}\), let _x_<sub>{_u,v_}</sub> be a Boolean variable indicating whether the edge {_u,v_} is colored with color 2. Also, let Inc(_V(H_<sub>1</sub>)_,V(K<sub>n</sub>_)) and Inc(_V(H_<sub>2</sub>)_,V(K<sub>n</sub>_)) denote the sets of all increasing injections from _V(H_<sub>1</sub>) to _V(K<sub>n</sub>_) and from _V(H_<sub>2</sub>) to _V(K<sub>n</sub>_), respectively.

In the context of computing the permutational Ramsey number \(R(H_1^{\Gamma_1},H_2^{\Gamma_2})\), the search for a 2-edge- coloring of _K<sub>n</sub>_ containing no forbidden embeddings can be encoded as a SAT problem by observing that _H_<sub>1</sub> is not \(\Gamma_1\)-embeddable in _G_<sub>1</sub> if and only if<tbc>

\(\wedge_{\psi\in\text{Inc}(V(H_1),V(K_n))}\wedge_{\varphi\in\Gamma_1}\vee_{\{u,v\}\in E(H_1)}x_{\{(\psi\circ\varphi)(u),(\psi\circ\varphi)(v)\}},\) (1)

<tbc>while _H_<sub>2</sub> is not \(\Gamma_2\)-embeddable in _G_<sub>2</sub> if and only if

\(\wedge_{\psi\in\text{Inc}(V(H_2),V(K_n))}\wedge_{\varphi\in\Gamma_2}\vee_{\{u,v\}\in E(H_2)}\neg x_{\{(\psi\circ\varphi)(u),(\psi\circ\varphi)(v)\}}.\) (2)

Therefore, by combining (1) and (2), we obtain a SAT problem with \(\genfrac(){pt}{2}{n}{2}\) variables and \(\genfrac(){pt}{2}{n}{|H_1|}|\Gamma_1|+\genfrac(){pt}{2}{n}{|H_2|}|\Gamma_2|\) clauses. If the SAT problem is satisfiable, then there exists a 2-edge-coloring of _K<sub>n</sub>_ containing no forbidden embeddings, hence \(R(H_1^{\Gamma_1},H_2^{\Gamma_2})\ge n+1\). Otherwise, such a 2-edge-coloring of _K<sub>n</sub>_ does not exist, implying that \(R(H_1^{\Gamma_1},H_2^{\Gamma_2})\le n\). Therefore, solving the formulated SAT problem gives either a lower bound or an upper bound on \(R(H_1^{\Gamma_1},H_2^{\Gamma_2})\). The permutational Ramsey number can then be exactly computed by solving SAT instances for sufficiently many values of _n_.

Our computation of small reflective and dihedral Ramsey numbers of interest is automated through a pipeline of four `Python` modules:

**(1) sat\_problem\_generator.py;**

**(2) instance\_solver.py;**

**(3) number\_finder.py;** and

**(4) grid\_explorer.py.**<tbc>

