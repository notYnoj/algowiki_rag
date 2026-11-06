1 Let \(M\le k^{n/(4k)}\) and _W_:=2<sup>_n/_(2_k_)</sup><br>
Partition _S_ arbitrarily into \(S_1\unknown\cdots\unknown S_k\) with |_S<sub>i</sub>_|=_n/k_<br>
\(\mathcal{A}_i^{(0)}\leftarrow\{\Sigma(X)|X\subseteq S_i\}\) for every \(i\in[k]\) and return collision if found<br>
\(p_i^{(0)}\leftarrow 0\) for every \(i\in[k]\).<br>
for j=1,...,log_k and i_=1_,...,k/_2<sup>_j_</sup> do<br>
  \(\mathcal{B}\leftarrow\mathcal{A}_{2i-1}^{(j-1)}+\mathcal{A}_{2i}^{(j-1)}\) and \(b\leftarrow p_{2i-1}^{(j-1)}+p_{2i}^{(j-1)}\) and return a collision if found<br>
   \(\mathcal{L}_{i,p}^{(j)}\leftarrow\{a\in\mathcal{B}|a\equiv p\cdot W^{j-1}+b(modW^j)\}\) for all \(0\le p<W\)<br>
   \(p^\star\leftarrow argmax_{0\le p<W}|\mathcal{L}_{i,p}^{(j)}|\)<br>
   \(p_i^{(j)}\leftarrow p^\star\cdot W^{j-1}+b\)<br>
   \(\mathcal{A}_i^{(j)}\) is arbitrary subset of \(\mathcal{L}_{i,p^\star}^{(j)}\) of size W<br>
end

In each level _j_, we have _k/_2<sup>_j_</sup> pairwise disjoint sets of size at most _W_. Transition in each level can be computed in quadratic time; hence the total time is \(\mathrm{poly}(n)\cdot W^{\mathcal{O}(1)}=2^{\mathcal{O}(n/k)}=M^{\mathcal{O}(1/\mathrm{log}k)}=M^{o(1)}\) if _k_ is allowed to be large enough.

For correctness, we claim that we maintain the following invariants: if no collision was detected until level _j_, then each \(\mathcal{A}_i^{(j)}\) has size _W_ and consists of subset sums that are all congruent to some value \(p_i^{(j)}\) modulo _W<sup>j</sup>_ . Hence, if no collision was detected, the last set \(\mathcal{A}_i^{(\mathrm{log}k)}\) contains two different numbers that are congruent modulo _W_log_k_. By the choice of _W_ and _k_ this means that _W_log_k\>nM_, which implies equality as integers, contradicting the invariant that \(|A_1^{(j)}|=W\ge 2\). Therefore, at some level \(j\le\mathrm{log}k\), the algorithm detects a collision! We include the full proof of Theorem 1.1 in Section 4.

## 2.2 Techniques behind Theorem 1.2

Very recently, the connection between the Karmarkar-Karp differencing method and lattice problems was highlighted by Vafa and Vaikuntanathan \[VV25\]. Their work studies an average-case version of the _Number Partitioning Problem_ (NPP), where one is given a random vector **a**=(_a_<sub>1</sub>_,...,a<sub>n</sub>_)∼N(**0**,**I**_<sub>n</sub>_) and the goal is to find a vector \(\mathbf{x}\in\{-1,1\}^n\) such that \(\left|\mathbf{a}^\top\mathbf{x}\right|\le\kappa(n)\sqrt{n}\).

They prove a worst-case-to-average-case reduction from the lattice problem _Incremental Guaranteed Distance Decoding_ (IncGDD) to NPP. In particular, they show that an average-case polynomial- time algorithm for NPP achieving \(\kappa(n)=2^{-\Omega(\mathrm{log}^{3+\varepsilon} n)}\) would contradict their assumed subexponential hardness of approximate lattice problems \[VV25\] including the Shortest Independent Vector Problem (SIVP) (see Hypothesis 2). Thus, under these assumptions, Karmarkar-Karp is nearly optimal in polynomial time.

They also note that their reduction extends to related variants, including the _Number Balancing Problem_ (NBP) where the Gaussian distribution is replaced with the uniform distribution on \[0,1\] and solution vectors are {-1,0,1}_<sup>n</sup>_\\{**0**} \[VV25\]. At a high level, one may view NBP as closely related to an equal-sum type problem after an appropriate discretization of the input numbers. In particular, if the target error is \(\kappa(n)\), then the relevant integer range after scaling is roughly of magnitude \(1/\kappa(n)\). This suggests that the hardness result of \[VV25\] is consistent with the absence of polynomial-time algorithms for average-case PESS when \(M\approx\frac{1}{\kappa(n)}=2^{\Omega(\mathrm{log}^{3+\varepsilon} n)}\).

Consequently, this also provides evidence against polynomial-time algorithms for the corre<tbc>

**Algorithm 1:** Algorithm behind Theorem 1.1.

