_Proof._ Observe that \(|N(v,3^0)|=|N(v,1)|\ge 2>\psi^0\) (recall we assume the graph is connected). Also, \(|N(v,3^{\lceil log_\psi n\rceil})|=n\le\psi^{\lceil log_\psi n\rceil}\). The claim thus follows.

We now argue that an appropriate collection of _N(v,_3_<sup>k</sup>_) suffice to provide a low diameter small neighborhood decomposition of _G_. Consider the following procedure.

1. Let \(\mathcal{C}\leftarrow\emptyset\),\(\mathcal{N}\leftarrow\emptyset\).<tbc>

2. For \(0\le k<\lceil log_\psi n\rceil\):<tbc>

(a) Sample a random subset \(S_k\subseteq V\) by including each \(u\in V\) with probability \(p_k=min\left(1,\frac{3logn}{\psi^k}\right)\).<tbc>

(b) For each \(u\in S_k\):<tbc>

i. Compute _N(u,_3_<sup>k</sup>_+1) using BFS.<tbc>

ii. If \(|N(u,3^k+1)|\le\psi^{k+1}\): update \(\mathcal{C}\leftarrow^\sqcup\left\{N(u,3^k)\right\}\) and \(\mathcal{N}\leftarrow^\sqcup\left\{N(u,3^k+1)\right\}\).<br>
(Whenever \(|N(u,3^k+1)|>\psi^{k+1}\), we terminate the invocation of BFS early.)<tbc>

3. Return C,N.

We claim that our algorithm returns a low diameter small neighborhood decomposition. We begin with the first property. Let \(v\in V\) . Let _k_ be an arbitrary integer guaranteed by Claim 4.3. We claim that _S<sub>k</sub>_ contains a vertex in _N(v,_3_<sup>k</sup>_) with high probability. The claim holds trivially whenever _p<sub>k</sub>_=1 (i.e. _S<sub>k</sub>=V_). For _p<sub>k</sub>\<_1, since \(|N(v,3^k)|>\psi^k\),

\(Pr(N(v,3^k)\cap S_k=\emptyset)\le(1-p_k)^{\psi^k}<e^{-p_k\psi^k}<\frac{1}{n^3}.\)

Let \(u\in S_k\cap N(v,3^k)\). Then, since \(u\in N(v,3^k)\), we have \(v\in N(u,3^k)\). We now argue that \(N(u,3^k)\in\mathcal{C}\). To see this, since \(k\ge 0\), we have \(N(u,3^k+1)\subseteq N(v,2\cdot 3^k+1)\subseteq N(v,3^{k+1})\) so that \(|N(u,3^k+1)|\le|N(v,3^{k+1})|\le\psi^{k+1}\), as desired. Hence, by union bound, the collection of sets in C covers all vertices in _V_ with probability at least 1-1_/n_<sup>2</sup>.

Towards the second property, we bound the diameter of each set _N(u,_3_<sup>k</sup>_) with \(k\le\lceil log_\psi n\rceil\) by

\(2\left(3^k\right)\le 2\cdot 3^{\lceil log_\psi n\rceil}\le 6\cdot 3^{log_\psi n}.\)

Towards the third property, we can bound the size of all _N(V<sub>i</sub>_)=_N(u,_3_<sup>k</sup>_+1) by \(\sum_k|S_k|\psi^{k+1}\). Using a standard Chernoff bound, we can conclude with high probability that all \(|S_k|=O\left(\frac{nlogn}{\psi^k}\right)\). In particular, \(\sum_k|S_k|\psi^{k+1}=O\left(\psi nlognlog_\psi n\right)\). Thus, we have achieved a \(\left(6\cdot 3^{log_\psi n},O\left(\psi lognlog_\psi n\right)\right)\)-LDSND.

It remains to prove the running time. For a fixed \(u\in S_k\), since we terminate whenever \(N(u,3^k+1)>\psi^{k+1}\), we can bound the running time of each BFS by \(O\left(\psi^{2k+2}\right)\) since the number of edges incident to _N(u,_3_<sup>k</sup>_) can be bounded by _O_(|_N(u,_3_<sup>k</sup>_+1)|<sup>2</sup>). Summing over all _S<sub>k</sub>_, the total running time is

\(\sum_k|S_k|\psi^{2k+2}=O\left(n\psi^{log_\psi n+4}lognlog_\psi n\right)=O\left(n^2\psi^4lognlog_\psi n\right).\)

Above, we have used that \(|S_k|=O\left(\frac{nlogn}{\psi^k}\right)\) and \(\psi^k\le\psi^{\lceil log_\psi n\rceil}\).

From our above theorem, we obtain a specific decomposition.

**Theorem 1.4.** _There is a randomized n_<sup>2+_o_(1)</sup> _time algorithm that computes a_ \(\left(2^{O\left(\sqrt{logn}\right)},2^{O\left(\sqrt{logn}\right)}\right)\)_-low diameter small neighborhood decomposition._

_Proof._ Set \(\psi=2^{\sqrt{logn}}\) and apply Theorem 4.2. We obtain an \(n^2\cdot 2^{O\left(\sqrt{logn}\right)}\) time algorithm that computes a \(\left(2^{O\left(\sqrt{logn}\right)},2^{O\left(\sqrt{logn}\right)}\right)\)-LDSND.

