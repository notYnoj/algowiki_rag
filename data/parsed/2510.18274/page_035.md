• _O_(log_n_) _cut queries to G if_ FindEdge(_A,B_) _outputs an edge_ \((a,b)\in E\cap(A\times B)\).<tbc>

<tbc>_Proof._ A useful intermediate tool for our analysis is an _Independent-Set_ (IS) Query which takes in as inputs disjoint sets \(A,B\subseteq V\) , and produces an output IS(_A,B_) which is "YES" or "NO" whether there exists an edge of _G_ among \(A\times B\); i.e. whether or not \(E\cap(A\times B)\neq\emptyset\). Such query can be simulated via 3 cut queries. To see this, we observe that

\(|E\cap(A\times B)|=\frac{1}{2}\cdot(|E_G(A,V\backslash A)|+|E_G(B,V\backslash B)|-|E_G(A\cup B,V\backslash(A\cup B)|).\)

Thus, IS(_A,B_) is equivalent to determining whether or not the RHS is 0. Each cut size can be determined via a single query (via setting _S=A,B_, and \(A\cup B\) respectively.) Therefore, we can obtain IS(_A,B_) via only three cut queries.

Our algorithm for answering FindEdge(_A,B_) proceeds as follows. We first compute IS(_A,B_). If the answer is "NO", then output "NONE" immediately. This only takes a single IS query to confirm that \(E\cap(A\times B)=\emptyset\). Otherwise, we are assured that \(E\cap(A\times B)\neq\emptyset\). In this case, we perform the binary search to find an edge \((a,b)\in E\cap(A\times B)\). Specifically, we partition _A_ into \(A_1\cup A_2\) of equal size, and _B_ into \(B_1\cup B_2\) of equal size. We then call IS(_A<sub>i</sub>,B<sub>j</sub>_) for \((i,j)\in\{1,2\}^2\), and recurse on a pair whose answer is "YES" until we can identify such edge. This recursion has depth _O_(log_n_), thus we only need to make _O_(log_n_) IS queries.

**Lemma 2.11.** _Let_ (_V_<sub>1</sub>_,...,V<sub>z</sub>_) _be a partition of a vertex set of G_=(_V,E). Then, we can learn all edges of_ \(G\langle V_1,\dots,V_z\rangle\) _using_ \(\widetilde{O}\left(z+|G\langle V_1,\dots,V_z\rangle|\right)\) _cut queries._

_Proof._ Our algorithm proceeds in iteration _i_=1,2_,...,z_. In iteration _i_, we wish to recover all edges in \(V_i\times V_{>i}\). To do so, we first make a query FindEdge(_V<sub>i</sub>,V<sub>\>i</sub>_). If the answer comes back "NONE", we remove _V<sub>i</sub>_ from the graph and proceeds to the next iteration. Otherwise, we have learned one edge in \(V_i\times V_{>i}\). Then, we remove such edge from the graph, and repeat the same query again until the answer comes back "NONE", then proceed to the next iteration. Upon finishing iteration _i=z_, we have learned all edges of \(G\langle V_1,\dots,V_z\rangle\).

As a result, in each iteration _i_, we only require 1+|_E(V<sub>i</sub>,V<sub>\>i</sub>_)| find-edge queries. In total, this sums up to \(z+|G\langle V_1,\dots,V_z\rangle|\) find-edge queries which can be simulated via \(\widetilde{O}\left(z+|G\langle V_1,\dots,V_z\rangle|\right)\) cut queries to _G_. We note here that each find-edge query, although not made with respect to the original graph _G_, can be simulated via \(\widetilde{O}(1)\) cut queries to _G_, as we have an explicit knowledge of the already-deleted edges and vertices.

**Lemma 2.12.** _For any_ \(\varepsilon\in(0,1)\)_, there is a deterministic protocol such that Alice and Bob jointly computes an_ \(\varepsilon\)_-cut sparsifier of G with_ \(\widetilde{O}(n/\varepsilon^2)\) _edges and maximum weight_ \(\widetilde{O}(\varepsilon^2n)\)_. The protocol communicates_ \(\widetilde{O}(n/\varepsilon^2)\) _bits and always succeeds._

_Proof._ To do so, Alice locally computes _H<sub>A</sub>_ which is an \(\varepsilon\)-cut sparsifier of _G<sub>A</sub>_ with \(\widetilde{O}(n/\varepsilon^2)\) edges and maximum weight \(\widetilde{O}(\varepsilon^2n)\). One way to do so is to exhaustively search over all integrally-weighted graphs with \(\widetilde{O}(n/\varepsilon^2)\) edges and maximum weight \(\widetilde{O}(\varepsilon^2n)\), and set _H<sub>A</sub>_ to be the one that is an \(\varepsilon\)-cut sparsifier of _G<sub>A</sub>_. Such graph must exist due to Theorem 2.6, thereby must be found by Alice. Bob then does the same to compute _H<sub>B</sub>_ w.r.t. his graph _G<sub>B</sub>_. The player then exchange _H<sub>A</sub>_ and _H<sub>B</sub>_, and output \(H_A\cup H_B\) as an \(\varepsilon\)-cut sparsifier of \(G=G_A\cup G_B\).

It is clear that the amount of communication is bounded by \(\widetilde{O}(n/\varepsilon^2)\) which is the size of _H<sub>A</sub>_ and _H<sub>B</sub>_. Moreover, for any cut (_S,T_) we have

\(w_{H_A\cup H_B}(S,T)=w_{H_A}(S,T)+w_{H_B}(S,T)\)<br>
\(\le(1+\varepsilon)\cdot|E_{G_A}(S,T)|+(1+\varepsilon)\cdot|E_{G_B}(S,T)|\)<br>
\(=(1+\varepsilon)\cdot|E_{G_A\cup G_B}(S,T)|.\)

