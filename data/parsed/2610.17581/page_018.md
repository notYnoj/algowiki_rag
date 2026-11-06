<tbc>of hyperedges. The query edge_<sub>H</sub>(S_) can be simulated by both players communicating a cut(_S_) query on their respective hypergraphs, say _H<sub>x</sub>_ and _H<sub>y</sub>_, and then ‘giving the token’ to player _x_ with probability cut_<sub>H<sub>x</sub></sub>(S)/_cut_<sub>H</sub>(S_), and otherwise giving it to player _y_ (we can arbitrarily put all the \(A_j\cup B_j\) hyperedges in _H<sub>x</sub>_). When player _z_ receives the token, they sample a hyperedge \(e\leftarrow\mathsf{edge}_{H_z(S)}\) and then communicate _e_ using _r_log_n_ bits by specifying its _r_ endpoints. Thus, cut, add, and edge queries can all be communicated using _O(r_log_n_) bits. Since DISJ_<sub>N</sub>_ has randomized communication complexity \(\Omega(N)=\Omega(ln/r)\), our reduction shows that any algorithm for D_k_SH using cut, add, and edge queries on a hypergraph with _n_ vertices requires at least \(\Omega(n\genfrac(){pt}{2}{n/2}{\lfloor(2r-1)/3\rfloor}/(r^2logn))\) queries.

For hypergraphs with rank _r=O_(1), this result gives a lower bound of \(\Omega(n^{\lfloor(2r+2)/3\rfloor}/logn)\) on the query complexity of D_k_SH. Up to constant factors, this construction exactly matches that of Proposition 8 for _r_=2, implicitly yielding the same \(\Omega(n^2/logn)\)-query lower bound for any \((\frac{t+2}{t+1}-\delta)=(3/2-\delta)\)-approximation to D_k_S as Lemma 5.4. However, this implicit \((\frac{t+2}{t+1}-\delta)\) factor blows up exponentially with _r_, and so we state Theorem 5.5 as a lower bound on exact query complexity for clarity. We now give a different construction which yields an asymptotically stronger lower bound and meaningful hardness of approximation.

**Theorem 5.6.** The randomized query complexity of a \((1+1/(r+1)-\delta)\)-approximation of D_k_SH on rank-_r_ hypergraphs is at least \(\Omega(\genfrac(){pt}{2}{n}{r-1}/(n^2rlogn))\), for any \(\delta>0\) and any combination of cut, add, and edge queries. If _r=O_(1), this yields a lower bound of \(\Omega(n^{r-3}/logn)\) queries.

_Proof._ Reduction from DISJ_<sub>N</sub>(x,y_) on \(N=\genfrac(){pt}{2}{n-2}{r-1}\) bits to Densest (_r_+1)-Subhypergraph on rank-_r_ hypergraphs with _n_ vertices. Let _H_ be a rank-_r_ multihypergraph with vertices _a_ and _b_ as well as a set _S_ of _n_-2 vertices. We include edge (_a,b_) with multiplicity _r_-1. Order the subsets of \(\genfrac(){pt}{2}{S}{r-1}\) as _R_<sub>1</sub>_,...,R<sub>N</sub>_. For each _R<sub>i</sub>_, we include hyperedges \(R_i\cup\{a\}\) if and only if _x<sub>i</sub>_=1, and similarly include \(R_i\cup\{b\}\) if and only if _y<sub>i</sub>_=1.

If DISJ_<sub>N</sub>(x,y_) is `False`, i.e., _x<sub>i</sub>=y<sub>i</sub>_=1 for some index \(i\in[N]\), then the set \(R_i\cup\{a,b\}\) has _r_+1 edges. Otherwise, every (_r_+1)-subhypergraph has at most _r_ hyperedges, whether it is, whether it is, without loss of generality:

• a set \(R_i\cup\{a,b\}\) for which _x<sub>i</sub>_=1 and _y<sub>i</sub>_=0,<tbc>

• or a set \(R\cup\{a\}\) where \(R\subseteq S\) and |_R_|=_r_.<tbc>

<tbc>Thus, we can reduce DISJ_<sub>N</sub>(x,y_) to determining whether the densest (_r_+1)-subhypergraph on _H_ has _r_+1 edges, for which any \((1+1/(r+1)-\delta)\)-approximation to D_k_SH with \(\delta>0\) suffices. By the fact that the hypergraph _H_ has \(m\le 2N+r=O(N)\) hyperedges, a similar argument as Theorem 5.5 gives that D_k_SH has query complexity \(\Omega(N/logn)\). We complete the proof using a lower bound of

\(N=\frac{(n-2)!}{(r-1)!(n-2-r+1)!}\ge\frac{n!}{(r-1)!(n-r+1)!n^2}=\genfrac(){pt}{2}{n}{r-1}/n^2,\)

alongside a rough upper bound of log_N=O(r_log_n_).

Theorem 5.6 gives a lower bound of \(\Omega(n^{r-3}/logn)\) queries when the rank _r=O_(1). In the regime of \(r\le 8\), this is weaker than Theorem 5.5, but yields a sharper bound once \(r\ge 11\). We combine these two results to obtain a unified lower bound, giving the exact powers of the exponent for small _r_ in  2.

**Theorem 5.7.** The randomized query complexity of D_k_SH on rank-_r_ hypergraphs where _r=O_(1) is \(\Omega(n^{max\{r-3,\lfloor(2r+2)/3\rfloor\}}/logn)\).

