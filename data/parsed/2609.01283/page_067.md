_Proof._ Let \(M'\) be an arbitrary maximum \(\alpha\)-factor in _G+U_. Since _f_ updates can change the size of the maximum \(\alpha\)-factor by at most _f_, we know that \(|M|-f\le|M'|\le|M|+f\). Without loss of generality, we can assume that for all \(v\in V\) , the local change is bounded: \(\|\delta_M(v)|-|\delta_{M^\prime}(v)\|\le f\).

Observe that \(M'\) can be extended to a perfect \(\beta\)-factor _M<sub>i</sub>_ in \(\mathcal{G}+\mathcal{U}^i\), where \(i=|M'|-|M|\). This is achieved by picking exactly \(\sum_{v\in V}\alpha(v)-2|M'|\) edges from _E_<sub>_z_<sub>1</sub></sub> (which is always possible since \(\|\delta_M(v)|-|\delta_{M^\prime}(v)\|\le f\)). This leaves a remaining demand of \(2f+2(|M'|-|M|)\) at vertex _z_<sub>1</sub>, which must be strictly satisfied using edges from _E<sub>triangle</sub>_.

Since _z_<sub>2</sub> and _z_<sub>3</sub> have fixed capacities of 2_f_, this remaining demand uniquely forces _M<sub>i</sub>_ to pick exactly \(f+(|M'|-|M|)\) edges on both (_z_<sub>1</sub>_,z_<sub>2</sub>) and (_z_<sub>1</sub>_,z_<sub>3</sub>), and exactly \(f-(|M'|-|M|)\) edges on (_z_<sub>2</sub>_,z_<sub>3</sub>). This assignment forms a valid perfect \(\beta\)-factor in \(\mathcal{G}+\mathcal{U}^i\).

Thus, the maximum possible _i_ (denoted _i_<sup>∗</sup>) that yields a perfect \(\beta\)-factor in \(\mathcal{G}+\mathcal{U}^i\) perfectly corresponds to the maximum \(\alpha\)-factor of _G+U_. This proves the cardinality equivalence. Finally, because all dummy edges carry zero cost, the min-cost perfect \(\beta\)-factor strictly optimizes and matches the cost of the min-cost maximum \(\alpha\)-factor. □

We can now construct any perfect \(\beta\)-factor sensitivity oracle over the graph G. By Theorem A.3, this oracle resolves sensitivity queries for the maximum \(\alpha\)-factor in _G_. When an update **U** is queried, the optimal integer _i_<sup>∗</sup> can be found using a binary search over the interval \[-_f,f_\]. This binary search introduces a logarithmic overhead of _O_(log_f_), mapping the previous \(O(f^{3\omega})\) query time to \(\widetilde{O}(f^{3\omega})\).

Hence, the following corollaries of Theorem 7.8 and Theorem 8.13 are immediate:

**Corollary A.4.** _Let G_=(_V,E,**c**_) _be an undirected graph with integer edge costs in_ \[-_W,W_\] _and arbitrary degree bounds_ \(\alpha\)_, and let M be a fixed initial (maximum)_ \(\alpha\)_-factor. Then there exist the following sensitivity oracles that, for any update set U with f_=|_U|, answer queries on G+U with high probability:_

**Corollary A.5.** _Let G_=(_V,E,**c**_) _be an undirected graph with integer edge costs in_ \[-_W,W_\]_, arbitrary degree bounds_ \(\alpha\)_, a fixed initial min-cost maximum_ \(\alpha\)_-factor M, and a susceptible edge set E<sub>Q</sub> of size_ \(\sigma\)_. Then there exist the following subset sensitivity oracles that, for any update set_ \(U\subseteq E_Q\) _with f_=|_U|, answer queries on G+U with high probability:_

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Maximum_ \(\alpha\)_-factor_ & \(O((fn)^\omega+T_\alpha)\) & \(O((fn)^2logn)\) & \(\widetilde{O}(f^{3\omega})\) & _Size of maximum_ \(\alpha\)_-factor in G+U_ \\
_Min-Cost Max_ \(\alpha\)_-factor_ & \(\widetilde{O}(W(fn)^3)\) & \(O(W(fn)^3logn)\) & \(\widetilde{O}(Wnf^{3\omega+1})\) & _Cost of min-cost max_ \(\alpha\)_-factor in G+U_ \\
\end{tabular}

\begin{tabular}{ccccc}
_Oracle_ & _Prep._ & _Space_ & _Query_ & _Output_ \\
_Maximum_ \(\alpha\)_-factor_ & \(O(\sigma^2(fn)^{\omega-2}+(fn)^\omega+T_\alpha)\) & \(O(\sigma^2)\) & \(\widetilde{O}(f^\omega)\) & _Size of maximum_ \(\alpha\)_-factor in G+U_ \\
_Min-Cost Max_ \(\alpha\)_-factor_ & \(\widetilde{O}(W\sigma^2(fn)^{\omega-1}+W(fn)^{\omega+1})\) & \(\widetilde{O}(Wfn\sigma^2)\) & \(\widetilde{O}(Wnf^{\omega+1})\) & _Cost of min-cost max_ \(\alpha\)_-factor in G+U_ \\
\end{tabular}

