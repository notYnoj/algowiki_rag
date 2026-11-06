Although the proofs of the two preceding lemmas are constructive, the final algorithm does not need to build the corresponding constraint sets. Instead, because the sets \(B'\), _F_ and _R_ enjoy the special structure, we can enumerate all triples with the required properties. In particular, this enumeration covers every element of the constraint set.

## 5.3 Summing up

We are ready to prove our second main result, Theorem 2. For convenience, we restate the theorem below.

**Theorem 2.** \(MAS/MaxST(\mathbb{Q}_{\ge 1})\) _admits an algorithm with_ \(n^{k^\mathcal{O}(1)}\cdot|\mathcal{I}|^{\mathcal{O}(1)}\) _running time._

_Proof._ Let I=(_G,_**w**_,k_) be an instance of \(MAS/MaxST_{\mathbb{Q}_{\ge 1}}\). If \(\mathbf{w}(A)\ge 3k\), then the algorithm from Lemma 2 constructs a solution to I in polynomial time. From now on, we assume that **w**(_A)\<_3_k_.

We iterate over all possible choices of a set \(D\subseteq B\) of weight at most **w**(_A_), a set \(B'\subseteq B\backslash D\) of weight at most (**w**(_A_)+_k_)<sup>2</sup>, and sets \(P_F,P_R\subseteq V\times V\) , each of size at most 4(**w**(_A_)+_k_+1)<sup>4</sup>. Additionally, we require that for every (_u,v_) from \(P_F\cup P_R\), _T_ contains a directed path from _u_ to _v_. For a fixed choice of _D_, \(B'\), _P<sub>F</sub>_ and _P<sub>R</sub>_, we begin by constructing the sets

\(F=\bigcup_{(u,v)\in P_F}E_{u,v},\)<br>
\(R=\bigcup_{(u,v)\in P_R}E_{u,v},\)

where _E<sub>u,v</sub>_ denotes the set of edges on the path from _u_ to _v_ in _T_.

Let \(G'=G-D\), and let \(\mathbf{w}'\) be the restriction of **w** to \(E(G')\). Since _D_ consists only of blocked edges, we know that \(T\subseteq G'\), and hence \(MaxST(G',\mathbf{w}')=T\). Therefore, \(F,R\subseteq E(MaxST(G',\mathbf{w}'))\) by the definition of these sets.

We check whether \(B'\subseteq Inv(G',\mathbf{w}',R)\), and if so, apply the algorithm from Lemma 7 to \((G',\mathbf{w}')\) and the triple \((F,R,B')\), which returns a set \(S\subseteq E(T)\). For each \(A'\subseteq A\), we check whether the subgraph \(T-S+Inv(S)+A'\) is a solution to I.

If no check succeeds over all choices of _D_, \(B'\), _P<sub>F</sub>_, _P<sub>R</sub>_, and \(A'\), we report that I is a no-instance.

**Running time.** We note that for a fixed choice of the sets _D_, \(B'\), _P<sub>F</sub>_, _P<sub>R</sub>_, and \(A'\), our algorithm works in polynomial time. Indeed, we first construct _F_, _R_, and \(G'\), then we check that \(B'\subseteq Inv(G',\mathbf{w}',R)\), apply the algorithm from Lemma 7, and finally verify that \(T-S+Inv(S)+A'\) is a feasible solution to I. All these parts are polynomial. Therefore, it remains to bound the number of choices of the sets _D_, \(B'\), _P<sub>F</sub>_, _P<sub>R</sub>_ and \(A'\).

Recall that all edge weights are at least one. Hence, if the weight of a set is bounded by some value, then the same bound applies for its size. Since \(|B|\le m\le n^2\), there are at most _n_<sup>2</sup>**w**(_A_) ways to choose _D_ and at most _n_<sup>2(**w**(_A_)+_k_)<sup>2</sup></sup> possible sets \(B'\). Similarly, because |_E(T_)|=_n_-1, we have at most _n_<sup>4(**w**(_A_)+_k_+1)<sup>4</sup></sup> ways to choose each of the sets _P<sub>F</sub>_ and _P<sub>R</sub>_. Finally, \(|A|\le\mathbf{w}(A)\), and hence there are at most 2<sup>**w**(_A_)</sup> possible sets \(A'\). Combining these bounds with **w**(_A)\<_3_k_, we obtain that there are _n_<sup>O(_k_<sup>4</sup>)</sup> ways to choose these sets.

**Correctness.** By construction, our algorithm outputs only feasible solutions. Therefore, it remains to check that it does not report false negatives. Suppose that I is a yes-instance. In this case, by<tbc>

