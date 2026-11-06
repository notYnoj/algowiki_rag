### Inductive Case.

Let _t\<r_, and assume that _X_ contains all (_t,k_)-hyperstars. We will show that _X_ contains all (_t_+1_,k_)-hyperstars.

_Step 1 (difference of adjacent_ (_t_+1_,k_-1)_-hyperstars):_ \(v_{A\cup\{a\},L}-v_{A\cup\{b\},L}\in X\) for all \(A\cap L=\emptyset,|A|=t,|L|=k-1\), and \(a,b\notin A\cup L\).

We have \(v_{A,L\cup\{a\}}-v_{A,L\cup\{b\}}\in X\) since _X_ is a subspace and (_t,k_)-hyperstars are in _X_ by inductive hypothesis. Now,

\(v_{A,L\cup\{a\}}-v_{A,L\cup\{b\}}=\sum_{U\in\genfrac(){pt}{2}{L}{r-t-1}}\left[v_{A\cup\{a\},U}-v_{A\cup\{b\},U}\right]=v_{A\cup\{a\},L}-v_{A\cup\{b\},L}\in X.\)

_Step 2 ((t_+1_,k)-hyperstars):_ \(v_{A,L}\in X\) for all \(A\cap L=\emptyset,|A|=t+1\), and |_L_|=_k_.

Take some \(a\in A\) and let _B=A_\\{_a_}, so that |_B_|=_t_. Since \(v_{B,L}\in X\) by inductive hypothesis and the fact that _X_ is a subspace,

\((r-t)\cdot v_{B,L}=\sum_{b\in L}v_{B\cup\{b\},L\backslash\{b\}}\in X,\) (5)

where we observe that the summation counts each hyperedge \(v_{B\cup U}\) in the hyperstar _v<sub>B,L</sub>_ once for every vertex \(b\in U\). By Step 1, we also have

\(\sum_{b\in L}\left[v_{B\cup\{a\},L\backslash\{b\}}-v_{B\cup\{b\},L\backslash\{b\}}\right]=\sum_{b\in L}\left[v_{A,L\backslash\{b\}}-v_{B\cup\{b\},L\backslash\{b\}}\right]\in X.\) (6)

Summing the RHS of eqs. (5) and (6), we get

\(\sum_{b\in L}v_{A,L\backslash\{b\}}=\sum_{b\in L}\sum_{U\in\genfrac(){pt}{2}{L\backslash\{b\}}{r-t-1}}v_{A\cup U}=(k-(r-t-1))\cdot\sum_{U\in\genfrac(){pt}{2}{L}{r-t-1}}v_{A\cup U}\)<br>
\(=(k-(r-t-1))\cdot v_{A,L}\in X.\)

To see the second equality, note that the summation of the second expression counts each hyperedge \(v_{A\cup U}\) in the hyperstar _v<sub>A,L</sub>_ once for every vertex \(b\in L\backslash U\). Since \(t\ge 0\) and \(k\ge r\), then we have _k_-(_r-t_-1)_\>_0 and so we can divide by this scalar to obtain \(v_{A,L}\in X\), completing the proof.

The assumption \(k\le n-r\) is implicitly used in this inductive argument by the fact that an (_r,k_)-hyperstar must have _r+k_ total vertices, as _A_ and _L_ are necessarily disjoint.

**Corollary 5.3.** The deterministic query complexity of D_k_S on weighted graphs is at least \(\genfrac(){pt}{2}{n}{2}\), for any \(2\le k\le n-2\).

This lower bound is asymptotically tight, as one can deterministically learn a weighted graph in _O(n_<sup>2</sup>) cut queries with exhaustively Cross({_u},{v_}) calls.

## 5.2 Randomized Complexity of D_k_S, and D_k_SH with all queries

While our \(\genfrac(){pt}{2}{n}{r}\)-query lower bound for the query complexity of D_k_SH only holds for deterministic cut algorithms, we are still able to prove exponential lower bounds for the more general setting of randomized algorithms with access to any queries. We first demonstrate the approach with Densest _k_-Subgraph, where we obtain a lower bound of \(\Omega(n^2/logn)\) cut queries for exact algorithms and approximation schemes.

**Lemma 5.4.** The randomized query complexity of a \((1.5-\delta)\)-approximation for D_k_S on unweighted graphs is \(\Omega(n^2/logn)\), for any \(\delta>0\).

