• if there is a directed path in _T_, that starts with \(s\in E(T)\) and ends with \(e\in E(T)\), then \(i\le j\), where \(i,j\in[t]\) are such that \(e\in P_i\) and \(s\in P_j\).

Note that the last point in the definition above is a topological-like ordering of paths required for our strategy. We also have to introduce the notion of edge orderings that agree with proper path covers. Order the edges inside the paths, so the last edge goes first, and the first edge goes last. We call the resulting total edge ordering the P_-respecting ordering_. The formal definition is given below.

**Definition 7** (P-respecting orderings)**.** Let (_G,_**w**) be a weakly-connected digraph with positive edge weights, and let P be a proper path cover of _G_. We say that an ordering _e_<sub>1</sub>_,e_<sub>2</sub>_,...,e_<sub>_n_-1</sub> of _E(T_) is P_-respecting_ if

• if there is a directed path in _T_ that starts with _e<sub>j</sub>_ and ends with _e<sub>i</sub>_, then \(i\le j\) holds, and<tbc>

• for each \(1\le i\le j<n\), it holds that \(\ell\le\ell'\), where \(e_i\in P_\ell\) and \(e_j\in P_{\ell^\prime}\).

The definition of P-respecting orderings implies that edges of a single path of P form consecutive segments in the ordering. Such a segment starts with the last edge of a path and ends with a first edge of a path. We are now ready to formulate the lemma itself.

**Lemma 4.** _Let_ I=(_G,_**w**_,k_) _be an instance of_ \(MAS/MaxST(\mathbb{Z}_{\ge 1})\)_, and let_ P _be a proper path cover of T. Let e_<sub>1</sub>_,e_<sub>2</sub>_,...,e_<sub>_n_-1</sub> _be a_ P_-respecting ordering of E(T). If_ I _is a yes-instance, then there exists a solution_ \(G'\) _to_ I _with_ \(S=E(T)\backslash E(G')\) _such that_

• _If_ \(e_i\in S\)_, then_ \(\mathbf{rp}(S_{i-1},e_i)\ge-\mathbf{w}(A)\)_, and_<tbc>

• _If_ \(e_i,e_j\in S\) _for i\<j, and e<sub>i</sub>,e<sub>j</sub> belong to the same path in_ P_, then_ **rp**(_S_<sub>_j_-1</sub>_,e<sub>j</sub>)\>_0_, and_<tbc>

• _If_ \(e_i\notin S\) _and_ \(e_j\in S\) _for i\<j, S_<sub>_j_-1</sub>=_S_<sub>_i_-1</sub> _and e<sub>i</sub>,e<sub>j</sub> belong to the same path in_ P_, then_ **rp**(_S_<sub>_i_-1</sub>_,e<sub>i</sub>)\<_**rp**(_S_<sub>_i_-1</sub>_,e<sub>j</sub>),_

_where_ \(S_0=\emptyset\) _and_ \(S_i=S_{i-1}\cup(S\cap\{e_i\})\) _for each_ \(i\in[n-1]\).

_Proof._ Suppose that I is a yes-instance. We start with an arbitrary solution _X_ and aim to obtain a solution \(G'\) that satisfies all the required properties by applying a sequence of local modifications. Each modification is of one of three types, corresponding to each property in the lemma statement.

Let _S_ be the set of tree edges that do not belong to the current solution. Initially, _S=E(T_)\\_E(X_). Modifications of the first type help us eliminate edges in _S_ that are _very unprofitable_ (in terms of remaining profit). We make use of the following claim:

**Claim 8.** _If there is an edge_ \(e_i\in S\) _such that_ \(\mathbf{rp}(S_{i-1},e_i)\le-\mathbf{w}(A)\)_, then_ \(X':=X+e_i-A-(Inv(e_i)\backslash Inv(S_{i-1}))\) _is also a solution for_ I.

_Proof of Claim 8._ Since _X_ is acyclic, we have \(X\subseteq T-S+Inv(S)+A\). Let \(S':=S\backslash\{e_i\}\). From the definition of \(X'\), it follows that \(X'\subseteq T-S'+Inv(S)\). Moreover, notice that if \(X'\) contains an inverse edge from Inv(_e<sub>i</sub>_), then this edge also belongs to \(Inv(S_{i-1})\subseteq Inv(S')\). Consequently, we obtain the stronger inclusion: \(X'\subseteq T-S'+Inv(S')\). Then \(X'\) is acyclic by Lemma 1. Recall that **rp**(_S_<sub>_i_-1</sub>_,e<sub>i</sub>_) is defined as \(\mathbf{w}(Inv(e_i)\backslash Inv(S_{i-1}))-\mathbf{w}(e_i)\). Hence,

\(\mathbf{w}(X')\ge\mathbf{w}(X)-\mathbf{w}(A)+(\mathbf{w}(e_i)-\mathbf{w}(Inv(e_i)\backslash Inv(S_{i-1})))\)<br>
\(=\mathbf{w}(X)-\mathbf{w}(A)-\mathbf{rp}(S_{i-1},e_i)\ge\mathbf{w}(X)\)

