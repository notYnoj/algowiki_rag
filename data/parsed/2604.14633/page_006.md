_The data structure maintains a tuple_ (_g,u_) _where_ \(g\le 0\) _and u\>_0 _such that for some implicit cut_ \(C\subseteq V\) _we have_ **g**(_C_)=_g and_ \(\mathbf{u}(\partial C)\le u\)_, and the (negative) ratio g/u is at most_ \(1/\alpha\) _times the minimum possible over all_ \(C\subseteq V\) .

_The data structure has an additional operation_ \(\mathrm{ToggleCut}(\eta)\) _based on the current tuple_ (_g,u_) _with implicit cut C: given a parameter_ \(0<\eta\le 1/u\)_, the data structure implicitly updates_ \(\mathbf{y}(v)\leftarrow\mathbf{y}(v)+\eta\) _for all_ \(v\in C\)_. Then, the data structure returns some edge set_ \(E'\) _that includes every edge_ \(e=\{u,v\}\in E\) _for which the value_ **u**(_e_)(**y**(_u_)-**y**(_v_)) _has changed by at least an additive_ \(\epsilon\) _since it was inserted/last returned in_ \(E'\).

**Theorem 8** (Theorem 5.4 of \[VDBCK<sup>+</sup>24\])**.** _There is a deterministic_ \(\alpha\)_-approximate min-ratio cut data structure for_ \(\alpha=n^{o(1)}\) _such that every operation is processed in amortized time n_<sup>_o_(1)</sup>log_U. Furthermore, the total number of edges returned by the algorithm after t calls to_ \(\mathrm{ToggleCut}(\cdot)\) _is at most_ \(n^{o(1)}\cdot t/\epsilon\).

## 3 Maximum Flow Algorithm

In this section, we present our maximum flow algorithm. We assume access to a dynamic _sparsifier_ data structure which is the focus of the next section (Section 4).

**Definition 9** (Dynamic sparsifier with quality _g_)**.** _For a weighted directed graph H_=(_V,E,_**u**) _where_ \(\mathbf{u}\in\mathbb{R}^E\) _and_ \(\mathbf{u}(e)\in[1/U,U]\) _for_ \(\mathrm{log}U=\widetilde{O}(1)\)_, a dynamic sparsifier with quality q supports the following operations:_

• InsertArc(_e),_DeleteArc(_e): inserts/deletes the arc e with weight_ **u**(_e)._<tbc>

• Sparsifier\((\beta)\)_: given_ \(\beta\ge 1\)_, returns a subgraph_ \(\widetilde{H}\subseteq H\) _on at most_ \(q\cdot\beta n\) _arcs such that with high probability, any cut_ \(S\subseteq V\) _with_ \(\mathbf{u}(\partial_H^+S)\ge\frac{1}{\beta}\mathbf{u}(\partial_HS)\) _has at least one sampled out-arc, i.e.,_ \(\partial_H^+S\neq\emptyset\).

**Theorem 10.** _There is a randomized dynamic sparsifier data structure with quality q=n_<sup>_o_(1)</sup>log_U such that each call to_ InsertArc(_e),_DeleteArc(_e_) _is processed in amortized time n_<sup>_o_(1)</sup>log_U, and each call to_ Sparsifier\((\beta)\) _takes time_ \(O(q\beta n\mathrm{log}U)\).

The algorithm initializes an \(\alpha\)-approximate min-ratio cut data structure (Theorem 8) on the input graph, where **y**=0 and all edges have weight \(w(u,v)=\frac{1}{\mathrm{max}\{\mathbf{y}(v)-\mathbf{y}(u),0\}+1}=1\). The detection threshold parameter \(\epsilon\) is fixed to \(\epsilon=1/(8\alpha)\). The algorithm only updates arc/edge weights when they pass the detection threshold from the data structure. That is, whenever the data structure returns some edge set \(E'\), the algorithm makes the following updates for each edge \(e\in E'\) with corresponding arc (_u,v_): first, call DeleteEdge(_e_) and UpdateGradient(_u,v,_-**u**(_e_)) to remove the old contribution, and then call InsertEdge(_u,v,w(u,v_)) and UpdateGradient(_u,v,w(u,v_)), where the new weight _w(u,v_) is computed by querying Potential(_u_) and Potential(_v_) to determine **y**(_u_) and **y**(_v_).

The algorithm also initializes a dynamic sparsifier data structure (Theorem 10) with the initial arc weights of 1. Whenever an edge weight is changed in the min-ratio cut data structure, the algorithm propagates the change to the sparsifier data structure.

To find the next augmenting path, the algorithm first computes balancing weights as follows. While the data structure maintains an implicit cut \(C\subseteq V\) with \(g/u\le-1/(3\alpha)\), the algorithm<tbc>

