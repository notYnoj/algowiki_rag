\(\bullet\) whenever \(\text{Couple}(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho)\) is recursively called at Line 10 or Line 17, append the original unpinned constraint \(c^O\in\mathcal{C}\) to the end of _L_.<tbc>

<tbc>For any sequence \((c_1,c_2,\dots,c_\ell)\) of (unpinned) constraints from C, we say that \((c_1,c_2,\dots,c_\ell)\) is a _proper execution log_ if it appears in the support of _L=L_(C_,c_<sub>0</sub>), i.e.,

\(\mathbf{Pr}\left[L=(c_1,c_2,\dots,c_\ell)\right]>0.\)

Recall the definition of the incidence hypergraph in Definition 2.2. The following notion of a witness tree is inspired by the witness tree introduced for analyzing the Moser-Tardos algorithm \[MT10\]. A key distinction in our context is that in the execution log constructed as in Definition 4.3, a constraint can never appear twice. Thus, the witness tree here is a subgraph of \(G_\Phi\).

**Definition 4.4** (witness tree)**.** A _witness tree T_ is a finite rooted tree with vertex set \(V(T)\subseteq\mathcal{C}\) such that _T_ is a subgraph of \(G_\Phi\).

Given a witness tree _T_ and a constraint \(c\in\mathcal{C}\), define \(T\oplus c\) as the witness tree \(T'\) obtained as follows:

\(\bullet\) if \(T=\emptyset\), then \(T'\) is the rooted tree containing a single vertex _c_;<tbc>

\(\bullet\) otherwise, if \(\exists c'\in V(T)\) such that \(\text{vbl}(c)\cap\text{vbl}(c')\neq\emptyset\), then \(T'\) is obtained by adding _c_ as a child of the deepest such \(c'\) in _T_, breaking ties by choosing the lexicographically smallest \(c'\) in case multiple \(c'\)s with the same largest depth exist;<tbc>

\(\bullet\) otherwise, \(T'=T\).

Given a proper execution log \(L=(c_1,c_2,\dots,c_\ell)\), the _witness tree of the execution log L_, denoted by _T=T(L_), is defined as follows: Let \(T_i=T_{i-1}\oplus c_i\) for \(1\le i\le\ell\) and initialize \(T_0=\emptyset\). Thus, \(T(L)=T_\ell\).

The following proposition states several basic properties of the witness tree. The proof is straightforward and is therefore omitted.

**Proposition 4.5.** _Let L be a proper execution log, and let T=T(L_) _be the rooted tree constructed by Definition 4.4. For each_ \(c\in T\)_, denote the depth of c in T as_ dep(_c). The following properties hold:_

(_1)_ _T is a witness tree, i.e., T is a rooted tree and is a subgraph of_ \(G_\Phi\).<tbc>

(_2)_ |_V(T_)|=|_L|, meaning that every constraint in L is included as a vertex in T_.<tbc>

(_3)_ _For any distinct_ \(c,c'\in V(T)\) _with_ \(\text{dep}(c)=\text{dep}(c')\)_, it holds that_ \(\text{vbl}(c)\cap\text{vbl}(c')=\emptyset\).<tbc>

_(4)_ _For any_ \(c,c'\in V(T)\)_, if_ \(\text{vbl}(c)\cap\text{vbl}(c')\neq\emptyset\) _and_ \(c'\) _appears later than c in the execution log L, then_ \(\text{dep}(c')>\text{dep}(c)\).

Besides the witness tree, another main source of randomness in the coupling procedure of Algorithm 2 comes from the non-violating partial assignments drawn in Lines 9 and 16 of Algorithm 2. This is formalized by the following notion of witness assignment.

**Definition 4.6** (witness assignment)**.** Given a run of Algorithm 2 from \(\text{Couple}(\mathcal{C}\backslash\{c_0\},\mathcal{C},\emptyset,\emptyset)\), the _witness assignment_ is a random partial assignment \(\varsigma\) constructed as follows:

\(\bullet\) initially, \(\varsigma=\emptyset\), the empty assignment;<tbc>

\(\bullet\) whenever a recursive call \(\text{Couple}(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho)\) is made in Line 10 of Algorithm 2, with \(\pi=\mathtt{False}(c)\) being the unique violating assignment of constraint _c_, update \(\varsigma\leftarrow\varsigma\wedge\rho\);<tbc>

\(\bullet\) whenever a recursive call \(\text{Couple}(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho)\) is made in Line 17 of Algorithm 2, with \(\rho=\mathtt{False}(c)\) being the unique violating assignment of constraint _c_, update \(\varsigma\leftarrow\varsigma\wedge\pi\).

For any witness tree _T_, we define

\(\text{vbl}(T)\unknown\bigcup_{c\in V(T)}\text{vbl}(c),\)

which represents the set of all variables involved in the constraints that appear as vertices in _T_. Based on Proposition 4.5 and definition 4.6, it follows that the witness assignment \(\varsigma\) is a partial assignment specified over the variables in vbl(_T_), i.e. \(\varsigma\in[q]^{\text{vbl}(T)}\), where _T=T(L_) is the witness tree of the execution log _L_ that belongs to a run of Algorithm 2 from \(\text{Couple}(\mathcal{C}\backslash\{c_0\},\mathcal{C},\emptyset,\emptyset)\).

The witness tree, together with the witness assignment, fully determines the random choices made by Algorithm 2, except for the optimal coupling step at the end of the recursion.

