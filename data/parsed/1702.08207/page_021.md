The eventual deterministic coupling, which is obtained in all cases for the strategies starting at _v_ and _u_, extends by induction to the execution of A_<sub>S</sub>_ for trees rooted at a vertex _v_ and its arbitrary descendant \(u'\) lying on the path from _v_ to _x_, hence the claim holds.

For the chosen value \(\omega\), we can apply Lemma 4.7 with \(\omega^*=\omega-\frac{1}{cn}\), obtaining:<tbc>

\(\left(\omega-\frac{1}{cn}\right)L=\omega^*L<\left(1+\frac{11}{c}\right)\mathsf{OPT}(T),\)

<tbc>thus, by Corollary 4.12,

\(\mathsf{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)\le\left(1+\frac{11}{c}\right)\mathsf{OPT}(T)+\frac{L}{cn}\le\left(1+\frac{12}{c}\right)\mathsf{OPT}(T),\)

where we took into account that trivially \(L\le n\) and \(\mathsf{OPT}(T)\ge 1\). We thus, by Lemmas 4.9, and 4.13 obtain the claim of Proposition 3.1.

## 5 Proof of Proposition 3.2: Reducing the Number of Down- Queries

We start with defining a function \(\ell:V\rightarrow\{1,\dots,\lceil log_2n\rceil\}\) which in the following will be called a _labeling of T_ and the value \(\ell(v)\) is called the _label of v_. We say that a subset of nodes \(H\subseteq V\) is an _extended heavy part_ in _T_ if \(H=\{v\}\cup H'\), where all nodes in \(H'\) are heavy, no node in \(H'\) has a heavy neighbor in _T_ that does not belong to \(H'\) and _v_ is the parent of some node in \(H'\). Let _H_<sub>1</sub>_,...,H<sub>l</sub>_ be all extended heavy parts in _T_. Obtain a tree _T<sub>C</sub>_=(_V<sub>C</sub>,E<sub>C</sub>_) by contracting, in _T_, the subgraph _H<sub>i</sub>_ into a node denoted by _h<sub>i</sub>_ for each \(i\in\{1,\dots,l\}\). In the tree _T<sub>C</sub>_, we want to find its labeling \(\ell':V_C\rightarrow\{1,\dots,\lceil log_2|V_C|\rceil\}\) that satisfies the following condition: for each two nodes _u_ and _v_ in _V<sub>C</sub>_ with \(\ell'(u)=\ell'(v)\), the path between _u_ and _v_ has a node _z_ satisfying \(\ell'(z)<\ell'(u)\). One can obtain such a labeling by a following procedure that takes a subtree \(T'_C\) of _T<sub>C</sub>_ and an integer _i_ as an input. Find a central node _v_ in \(T'_C\), set \(\ell'(v)=i\) and call the procedure for each subtree \(T''_C\) of \(T'_C-v\) with input \(T''_C\) and _i_+1. The procedure is initially called for input _T_ and _i_=1. We also remark that, alternatively, such a labeling can be obtained via vertex rankings \[16, 33\].

Once the labeling \(\ell'\) of _T<sub>C</sub>_ is constructed, we extend it to a labeling \(\ell\) of _T_ in such a way that for each node _v_ of _T_ we set \(\ell(v)=\ell'(v)\) if \(v\notin H_1\cup\cdots\cup H_l\) and \(\ell(v)=\ell'(h_i)\) if \(v\in H_i\), \(i\in\{1,\dots,l\}\).

Having the labeling \(\ell\) of _T_, we are ready to define a query sequence _R(v_) for each node \(v\in V\) . The _R(v_) contains all nodes _u_ from _T<sub>v</sub>_ such that \(\ell(u)<\ell(v)\) and each internal node _z_ of the path connecting _v_ and _u_ in _T_ satisfies \(\ell(z)>\ell(u)\). Additionally, the nodes in _R(v_) are ordered by increasing values of their labels. See Figure 5.1 for an example.

We start by making some simple observations regarding the sequence assignment _R_.

**Observation 5.1.** _For each_ \(v\in V\) _and for each_ \(u\in R(v)\), \(w(u)\le c\omega\).

**Observation 5.2.** _For each_ \(v\in V\) _, any two nodes in R(v_) _have different labels._

**Observation 5.3.** _The sequence assignment R can be computed in time O(n_log_n)._

By _x_ we refer to the target node in _T_. Fix _S_ to be a stable sequence assignment in the remaining part of this section and by _R_ we refer to the sequence assignment constructed above. Then, we fix _S_<sup>+</sup> to be \(S^+(v)=R(v)\circ S(v)\) for each \(v\in V\) . Denote by _U<sub>i</sub>_ the first _i_ nodes queried by A<sub>_S_<sup>+</sup></sub> and let \(C_i=min\ell(T\langle U_{i-1},x\rangle)\) for each \(i\ge 1\). For brevity we denote \(U_0=\emptyset\) and _C_<sub>0</sub>=0; we also denote by _u<sub>i</sub>_ the node in _U<sub>i</sub>_\\_U_<sub>_i_-1</sub>, \(i\ge 1\). A query made by A<sub>_S_<sup>+</sup></sub> to a node that belongs to _R(v_) for some \(v\in V\) is called an _R-query_; otherwise it is an _S-query_.

