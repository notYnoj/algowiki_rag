is \(\sum_i(d_i+1)^{-1}\ge Y^2/(Y+2J)\). Thus, if _K<sub>n</sub>_ is the maximum number of vertex-disjoint favorable candidate cycles, set to zero outside B_<sub>n</sub>_, then

\(K_n\rightarrow\infty\text{in probability.}\) (195)

On a completed graph, subtracting any subset of _k_ disjoint favorable circulations from the sampled error gives 2_<sup>k</sup>_ distinct errors with the same syndrome, each with probability at least that of the sampled error. Its posterior probability within the syndrome is therefore at most 2<sup>-_k_</sup>. Splitting according to whether a decoder’s selected error has \(K_n\ge k\) gives, for every fixed positive integer _k_,

\(\mathbb{E}[P_\mathrm{S}^\mathrm{ML}(G_n,p,\theta)|\mathcal{E}_n]\le\frac{\mathrm{Pr}(K_n<k)}{\mathrm{Pr}(\mathcal{E}_n)}+2^{-k}.\) (196)

The favorable circulations in \(G_n^T\) remain circulations after later edges are added. Taking \(n\rightarrow\infty\) in (196) and then \(k\rightarrow\infty\) proves Theorem 4, including arbitrary likelihood ties.

For the _q_SC, _Z=Z<sub>q</sub>(p_) and (_D_-1)_Z\>_1 throughout \(\delta_\mathrm{cyc}(D,q)<p\le(q-1)/q\). Hence the converse holds on the full _q_SC range. In particular, at _p_=(_q_-1)_/q_ the noise is uniform and \(P_\mathrm{S}^\mathrm{ML}(G_n,(q-1)/q)=q^{-(m-n+1)}\).

## A.6 The binary endpoint and scope of the conclusion

For _q_=2, a flow support is an even subgraph and decomposes into edge-disjoint simple cycles. A favorable flow therefore contains a favorable cycle. If _R_=(_D_-1)_Z_<sub>2</sub>(_p)\<_1, Eqs. (122) and (189) give, uniformly for \(g\le\ell\le K_0\mathrm{log}n\),

\(\mathbb{E}[\mathbf{1}_{\mathcal{A}_n}C_\ell(G_n)]\le(1+o(1))\frac{(D-1)^\ell+O_D(1)}{2\ell}.\) (197)

The resulting cycle union bound is _O<sub>D</sub>(R<sup>g</sup>/g_)=_o_(1). For longer cycles use

\(C_\ell(G)\le\frac{nD(D-1)^{\ell-1}}{2\ell}.\) (198)

Choosing _K_<sub>0</sub> sufficiently large makes the tail _O<sub>D</sub>(nR_<sup>_K_<sub>0</sub>log_n_</sup>)=_o_(1). Adding the graph bad-event probability proves binary recovery below \(\delta_\mathrm{cyc}(D,2)\) at every degree. The converse gives (79).

This recovery guarantee also holds simultaneously after every single-coordinate modification of the error. A failure after such a modification implies a cycle whose Hamming comparison score on the original error is at least -2; at \(t=\frac{1}{2}\mathrm{log}[(1-p)/p]\), its probability is at most \(e^{2t}Z_2(p)^\ell\), and the same cycle sums tend to zero.

## A.7 The remaining fixed-parameter question

For uniform replacement, the cycle-entropy conjecture below is not settled by these asymptotic bounds. At fixed _G_, put

\(\Phi_n(G,p):=\frac{1}{m}H(\mathbf{E}|B^T\mathbf{E}),\overline{\Phi_n}(p):=\mathbb{E}_G\Phi_n(G,p).\) (199)

