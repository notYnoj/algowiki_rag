2. Set \(M\leftarrow\lfloor(L+R)/2\rfloor\) and run `complete`(_G,S_<sub>in</sub>_,L,M_).<tbc>

3. Construct \(S_\mathrm{in}\times[L,M]\) matrix _X_ and \([L,M]\times[M,R]\) matrix _Y_ with entries<tbc>

<tbc>\(X[s,u]=\widehat{\mathrm{d}}(s,u),Y[u,v]=\left\{\begin{array}{ c c }
\mathrm{wt}(u,v) & (u,v)\in E \\
\infty & \mathrm{o}/\mathrm{w}
\end{array}\right..\)<tbc>

<tbc>Compute _X∗Y_ and update \(\widehat{\mathrm{d}}(s,v)\leftarrow^\mathrm{min}(X*Y)[s,v]\) for all \(s\in S_\mathrm{in},v\in[M,R]\).<tbc>

4. Run `complete`(_G,S_<sub>in</sub>_,M,R_).

<tbc>In the base case when \(R-L\unknown 2\), we compute APSP on the induced subgraph _G_\[_L,R_\] which has _O_(1) vertices and contains the shortest path between any pair of vertices \(u,v\in[L,R]\). This requires _O_(1) time and we can update distances analogously to Equation (4) as follows for all \(s\in S_\mathrm{in},v\in[L,R]\):

\(\widehat{\mathrm{d}}(s,v)\leftarrow^\mathrm{min}\mathrm{min}_{L\unknown u\unknown R}\widehat{\mathrm{d}}(s,u)+\widehat{\mathrm{d}}(u,v).\) (5)

Our algorithm for MSSP sets \(\widehat{\mathrm{d}}(s,v)=0\) for all \(s\in S_\mathrm{in},v\in N(s)\) and computes `complete`(_G,S_<sub>in</sub>,0,|_V_|).

The correctness proof follows similarly to Theorem 1.5, we highlight the necessary modifications here. As before, without loss of generality let the first vertex in topological order denoted _s_<sup>∗</sup> be in _S_<sub>in</sub>. At the root level, when we invoke `complete`(_G,S_<sub>in</sub>,0,|_V_|), we have \(\widehat{\mathrm{d}}(s,v)=\mathrm{dist}(s,v)\) for all \(s\in S_\mathrm{in}\) and \(\mathrm{pred}(s,v)\unknown 0\) i.e. pred(_s,v_)=_s_<sup>∗</sup>, satisfying the input assumption.

In the base case (i.e. \(R-L\unknown 2\)) we compute \(\widehat{\mathrm{d}}(u,v)=\mathrm{dist}(u,v)\) for all \(u,v\in[L,R]\) as _G_\[_L,R_\] contains all shortest paths between \(u,v\in[L,R]\) since _G_ is a DAG. Thus, we obtain correct distances following Equation (5) if \(s\unknown L\) and from APSP on _G_\[_L,R_\] if \(L\unknown s\unknown R\). The proof of the inductive case follows identically to Theorem 1.5.

To bound the running time, we have the recursion

\(T(\ell)=2T(\ell/2)+\mathsf{T}_\mathrm{MPP}(S_\mathrm{in},\ell,\ell|D,B)\)

since _X_ has finite entries bounded by _D_ and _Y_ has finite entries bounded by _B_. Following the same analysis as Claim 6.3, we obtain the time bound \(T(\ell)=\widetilde{O}\left(\mathsf{T}_\mathrm{MPP}(S_\mathrm{in},\ell,\ell|D,B)\right)\).

## 6.1 Application: Shortcut Sets

We give our improved algorithm for computing shortcut sets of linear size. Recall that for a directed graph _G_, TC(_G_) denotes the transitive closure of _G_ and diam(_G_) is the maximum of dist(_u,v_) over \((u,v)\in\mathrm{TC}(G)\).

**Definition 6.5.** _A set of edges F is a D-shortcut-set for directed graph G_=(_V,E_) _if_ \(\mathrm{TC}(G)=\mathrm{TC}(G\cup F)\) _and_ \(\mathrm{diam}(G\cup F)\unknown D\).

We give a faster algorithm for computing shortcut sets.

**Theorem 6.6.** _For_ \(D=O(\sqrt{n})\)_, there is an algorithm that computes a D-shortcut-set of size_ \(\widetilde{O}\left(n^2/D^3+n\right)\) _in time_ \(\widetilde{O}\left(n^2+\mathsf{T}_\mathrm{MPP}(n/D^2,n,n|D,1)\right)\).

We remark that using our algorithm for Multiple Source Reachability, one can achieve a running time of T<sub>BMM</sub>(_n/D,n,n_). However, Theorem 6.6 is at least as fast for all \(D=O(\sqrt{n})\).

_Proof of Theorem 6.6._ We recap the algorithm of \[KP22a\], beginning with the necessary definitions. Without loss of generality, we may assume that the input graph _G_ is directed and acyclic (DAG). Given a graph _G_, LP(_G_) denotes the length of the longest simple path in _G_. For a subset of vertices \(U\subseteq V\) , _G_\[_U_\] is the induced subgraph of _G_ on _U_. We define \(\ell\)-covers and chains.

