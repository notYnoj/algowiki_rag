_Proof._ From Corollary 3.10, we know that one execution of PartialVoteCover on each set cover instance, after having bounded the frequency each target by means of adding random edges, takes _O(n_<sup>2</sup>) time. We follow this with a call to VerifyNav, which takes \(O(n^\omega log(\Delta)/\varepsilon)\). This dominates the _O(n_<sup>2</sup>) time for the calls to PartialVoteCover, as \(\omega\) is necessarily at least 2. We perform this combination of these PartialVoteCover and VerifyNav up to \(logn+\gamma\) times for a given choice of `opt`, ensuring that any active set cover instance _s_ where `opt` is sufficiently close to \(\mathsf{OPT}_{\alpha(1+\varepsilon)}(s)\) completes. Finally, we run this on up to log_n_ values of `opt` before guaranteeing that `opt` is sufficiently close to \(\mathsf{OPT}_{\alpha(1+\varepsilon)}(s)\) for every _s_ at least once. Therefore, the total running time of BatchedVoteCover is \(O(n^\omega(log(\Delta)/\varepsilon)log^2n)\).

The combination of Lemma 3.11 and Lemma 3.8 yields Theorem 3.1.

## 3.3 Extension to \(\tau\)-Monotonic Graphs

Although we have presented our algorithm in terms of \(\alpha\)-navigability, the underlying set cover and batched verification framework is not specific to multiplicative progress. We briefly observe that the preceding framework also applies to the construction of sparse \(\tau\)-monotonic graphs \[12, 36\]. For \(\tau>0\), a directed graph _G_=(_P,E_) is \(\tau\)_-monotonic_ if, for every pair of distinct points \(s,t\in P\), either \((s,t)\in E\), or there exists an edge \((s,v)\in E\) such that

\(d(v,t)<d(s,t)-\tau.\)

Thus, each step makes additive, rather than multiplicative, progress toward the target. The direct- edge alternative is necessary when \(d(s,t)\le\tau\), since in this case no point can satisfy the displayed inequality.

As with \(\alpha\)-navigability, selecting the out-neighbors of each source _s_ is a set cover problem. For each potential edge (_s,v_), define

\(T_{s\rightarrow v}=\{t\in P\backslash\{s\}:v=t\text{or}d(v,t)<d(s,t)-\tau\}.\)

The MemberOf, FreqOf, and SetOf operations from Section 2.4 continue to be supported in constant time after _O(n_<sup>2</sup>log_n_) preprocessing. In particular, for a fixed source _s_ and target _t_, the points _v_ satisfying \(d(v,t)<d(s,t)-\tau\) form a prefix of the points sorted by distance from _t_. The length of this prefix can be found by binary search and stored for every pair (_s,t_). The possible additional set \(T_{s\rightarrow t}\), corresponding to the direct edge (_s,t_), is handled separately.

The other change is that distance discretization is additive. By rescaling the distance function and \(\tau\), assume without loss of generality that the minimum nonzero pairwise distance is 1, so the maximum pairwise distance is \(\Delta\). We use the additive scales \(r_\ell=\ell\epsilon\) for \(\ell=0,\dots,\left\lceil\frac{\Delta}{\epsilon}\right\rceil\) and round each distance _x_ down to \(\rho(x)=\epsilon\left\lfloor\frac{x}{\epsilon}\right\rfloor\). Consequently,

\(x-\epsilon<\rho(x)\le x,\)

and there are \(O(\Delta/\epsilon)\) distance scales.

The corresponding VerifyNav procedure performs one matrix multiplication for each scale. At scale \(r_\ell\), in the notation of Lemma 2.4, we define<tbc>

\(B_{j,k}^{(\ell)}=\left\{\begin{array}{ c c }
1, & j=k\text{or}d(p_j,p_k)<r_\ell-\tau, \\
0, & \text{otherwise}.
\end{array}\right.\)

