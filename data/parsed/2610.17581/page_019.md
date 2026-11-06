<tbc>Finally, we observe that Theorem 5.6 unconditionally rules out any fully polynomial-time approximation schemes for D_k_SH in the query model. Taking \(\delta=1/(r+1)-1/r\) and then _r=n/_2, we find that a (1+2_/n_)-approximation to D_k_SH requires \(\Omega(\genfrac(){pt}{2}{n}{n/2}/(n^3logn))\ge\Omega(2^n/(n^{3.5}logn))\) queries, applying Stirling’s approximation here. We can take this lower bound to be \(\Omega(2^{n/2})\) for sufficiently large _n_ (roughly \(n\ge 40\)). Since this rules out \(\mathrm{poly}(n,\varepsilon)\)-time \((1+\varepsilon)\)-approximations in the regime \(\varepsilon=\Theta(1/n)\), then there is no FPTAS for Densest _k_-Subhypergraph with only query access to a hypergraph.

## 6 Impossibility of Simulating add with cut and is-edge? queries

Studying the power of cut queries in hypergraphs, Chakrabarty and Liao \[11\] conjecture that exponentially-many cut and even is-edge? queries are required to simulate an add oracle on hypergraphs. We answer this question in the affirmative, building upon a pair of hypergraphs with identical cut profiles introduced in their work to show barriers for hypergraph reconstruction.

**Proposition 9** (\[11, Theorem 8\])**.** Let \(r\ge 3\) be an odd number. There are two unweighted _r_-uniform hypergraphs \(H_0^{A,B}\) and \(H_1^{A,B}\) on the same vertex set \(A\cup B\) whose cut profiles are identical.

To construct these hypergraphs, we label the 2_r_ vertices as _A_={_a_<sub>1</sub>_,...,a<sub>r</sub>_} and _B_={_b_<sub>1</sub>_,...,b<sub>r</sub>_}. An _r_-cardinality subset \(e\subseteq A\cup B\) is a hyperedge in \(H_0^{A,B}\) (respectively, in \(H_1^{A,B}\)) if and only if _e_ contains exactly one vertex from {_a<sub>i</sub>,b<sub>i</sub>_} for each \(i\in[r]\) and \(|e\cap B|\) is even (respectively, odd). Notably, the hyperedge _A_ is in \(H_0^{A,B}\) but not \(H_1^{A,B}\). Figure 2 illustrates the construction for _r_=3. We take advantage of this fact and construct a hypergraph where a single copy of \(H_0^{A^*,B^*}\) is hidden among exponentially many copies of _H_<sub>1</sub>. We do this in such a way that there is a set of nodes _S_ which satisfies add(_S)\>_0 if and only if \(S\supseteq A^*\). Since the hypergraphs are indistinguishable by cut queries, our lower bound shows that is-edge? queries must be used exhaustively to compute add(_S_) with non-negligible advantage.

\begin{tabular}{cccccccccccc}
_r_ & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 \\
_z_ & 2 & 2 & 3 & 4 & 4 & 5 & 6 & 6 & 7 & 8 & 9 \\
Lem & 5.5 & 5.5 & 5.5 & 5.5 & 5.5 & 5.5 & 5.5, 5.6 & 5.5, 5.6 & 5.5, 5.6 & 5.6 & 5.6 \\
\end{tabular}

a1
a2
a3
b1
b2
b3

a1
a2
a3
b1
b2
b3

(a) \(H_0^{A,B}\), where \(|e\cap B|\) is even.

(b) \(H_1^{A,B}\), where \(|e\cap B|\) is odd.

Figure 2: The construction in Proposition 9 for _r_=3. These hypergraphs agree on on every cut, but _A_={_a_<sub>1</sub>_,a_<sub>2</sub>_,a_<sub>3</sub>} is only an edge in \(H_0^{A,B}\).

2: Exact lower bounds of Theorem 5.7 on the query complexity of D_k_SH for hypergraphs up to rank 12. Entry (_r,z,X_) indicates that Lemma X yields a lower bound of \(\Omega(n^z/logn)\) queries on rank-_r_ hypergraphs.

