<tbc>Let _Q_:=_n/|N(V<sub>i</sub>_)| so that the time is \(n^{o(1)}\cdot Q\mathsf{T}_\mathrm{MUL}(|S_\mathrm{in}|/Q,n/Q,n/Q)\). Since there are at most _n_<sup>1+_o_(1)</sup>/|_N(V<sub>i</sub>_)| clusters of size _O_(|_N(V<sub>i</sub>_)|), we may bound the total time over all large clusters as \(n^{o(1)}\cdot Q^2\mathsf{T}_\mathrm{MUL}(|S_\mathrm{in}|/Q,n/Q,n/Q)\), which can be upper bounded by \(n^{o(1)}\cdot\mathsf{T}_\mathrm{MUL}(|S_\mathrm{in}|,n,n)\) as desired (see the running time analysis of Theorem 5.1 for the deduction).

## 2.3 Low Diameter Small Neighborhood Decomposition

We now describe how to efficiently obtain a low diameter small neighborhood decomposition (Theorem 4.2). We say \(V_1\sqcup\cdots\sqcup V_k\) is a \((d,\phi)\)-low diameter small neighborhood decomposition (LDSND) if \(\mathrm{max}_i\mathrm{diam}(V_i)\le d\) and \(\sum_i|N(V_i)|\le\phi n\) (see Definition 4.1).

Consider the following algorithm for obtaining a single low diameter cluster. Pick an arbitrary vertex _v_ and let \(N(v,r):=\{u\in V:\mathrm{dist}(v,u)\le r\}\) denote the _r_-neighborhood of _v_. We claim \(|N(v,3^k)|\le\phi^k\) for some \(k\le\lceil\mathrm{log}_\phi n\rceil\). Otherwise \(|N(v,3^{\lceil\mathrm{log}_\phi n\rceil})|>n\) becomes a contradiction (see Figure 3). Setting \(\phi=2^{O(\sqrt{\mathrm{log}n})}\), we get that \(k\le O(\sqrt{\mathrm{log}n})\) and \(3^k\le 2^{O(\sqrt{\mathrm{log}n})}\) so that _N(v,_3_<sup>k</sup>_) has small diameter.

Motivated by this observation, our decomposition C will consist of balls _N(v,_3_<sup>k</sup>_) for some _v_ and _k_. For each \(0\le k\le\mathrm{log}_\phi n\), we sample \(S_k\subseteq V\) by including each vertex with probability \(p_k\sim\phi^{-k}\). Then, for each \(u\in S_k\), we add _N(u,_3_<sup>k</sup>_) to C if \(|N(u,3^k+1)|\le\phi^{k+1}\). Since \(|S_k|=O(n\phi^{-k})\) with high probability, the total time required is at most \(O(\sum_k|S_k|\phi^{2k+2})=O(\sum_kn\phi^{k+2})=n^{2+o(1)}\).

Above, we have argued that each set has small diameter. Furthermore, since \(|S_k|=O(n\phi^{-k})\) with high probability, we have that \(\sum_{u\in S_k}|N(u,3^k+1)|=O(n\phi)=n^{1+o(1)}\), as desired.

It remains to argue that every vertex \(v\in N(u,3^k)\) for some \(N(u,3^k)\in\mathcal{C}\). Let \(k\ge 1\) be the smallest positive integer satisfying \(|N(v,3^k)|\le\phi^k\) so that \(|N(v,3^{k-1})|>\phi^{k-1}\). Note that such a _k_ always exists since |_N(v,_1)|_\>_1 unless _v_ is an isolated vertex. Then, with high probability, some \(u\in S_{k-1}\) hits _N(v,_3<sup>_k_-1</sup>). Then, since \(\mathrm{dist}(u,v)\le 3^{k-1}\) and \(2\cdot 3^{k-1}+1\le 3^k\), we have \(|N(u,3^{k-1}+1)|\le|N(v,2\cdot 3^{k-1}+1)|\le|N(v,3^k)|\le\phi^k\) , resulting in _N(u,_3<sup>_k_-1</sup>) being added to C, as desired.

Note that the above process gives a covering of the vertices. We can obtain a decomposition by removing duplicated vertices from the clusters.



Figure 3: Process of growing one cluster until it stops expanding. Here, \(\phi=3\), and we look for the first _k_ such that \(|N(v,3^k)|\le 3^k\). Each shaded circle illustrates _N(v,_3_<sup>k</sup>_) for some _k_. The process must terminate before _k_=log<sub>3</sub>_n_.

