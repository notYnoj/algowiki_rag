the prediction error and thus the running time is unchanged. For Stage 1, consider the matrices _D_ and \(D_\phi\) that satisfy the guarantees of Lemma 3 for _G_ and \(G_\phi\) respectively. We can verify inductively that \(D_\phi[u,v]=D[u,v]-\phi(u)+\phi(v)\) by noticing that for any \(w\in V\) we have

\(D[u,w]-\phi(u)+\phi(w)+D[w,v]-\phi(w)+\phi(v)=D[u,w]+D[w,v]-\phi(u)+\phi(v).\)

By the same observation, the detour function in \(G_\phi\) remains completely unchanged, i.e. detour\(_{D_\phi,u,v}(w)=\) detour_D,u,v(w_) since all offsets cancel. This already guarantees that \(U(G_\phi,C,p)=U(G,C,p)\) and \(\eta(G_\phi,C,p)=\eta(G,C,p)\) and the error is unaffected.

The overhead for running a negative-weight single-source shortest path algorithm depends on the algorithm we choose. One option is to use one of the near-linear-time scaling-based algorithms [8, 22]. These algorithms only work for integer weights, but lead to no overhead in the running time of Theorem 1 for any parameters _q_ and _p_, unless the edge weights are at least exponential. Another option is to use one of the recent algorithms for negative real weights [21, 26], with the fastest such algorithm running in time \(\tilde{\mathcal{O}}(mn^{4/5})\le\mathcal{O}(n^{2.83})\). For optimal parameter choices \(p=\Theta(n^{0.83})\) and \(q=\Theta(p)\), our algorithm hence still runs in time \(\mathcal{O}(n^{2.83}+\eta n)\), even for real and possibly negative edge weights.

## 6 The learning problem is NP-hard

This section is dedicated to the NP-hardness proof of the learning problem that corresponds to our error measure \(\eta\). In terms of the certificate size, we prove hardness for almost the full range of possible sizes for the certificate sets. However, the proof holds only for the regime with many instances for which we learn a certificate at the same time.

\(\blacktriangleright\) **Theorem 7.** _For every_ \(\gamma,\delta\in(0,1)\) _with_ \(\gamma\le\delta\)_, Problem 2 is NP-hard for_ \(p=n^\gamma\) _and_ \(q=n^\delta\) _with_ \(k=\Omega(q^2)\)_. The same holds for_ \(p=n-n^\delta\) _and_ \(q=n-n^\gamma\).

**Proof.** We reduce from (_q_-2)-Clique, where we are given a graph _G_ with |_V(G_)|=_n_ and are supposed to decide if it contains a clique on _q_-2 vertices. Notice that since \(q=n^\delta\), or \(q=n-n^\gamma\), that problem is NP-hard by a standard reduction from the normal Clique problem (see, e.g., Chapter 7 in [39]).

For every edge \(e_i=\{u,v\}\in E(G)\), we create a graph _G<sub>i</sub>_ with the following vertices, edges, and weights (see Figure 2). Set

\(V(G_i):=V(G)\cup\{s,t\},\)<br> \(E(G_i):=\{(s,u),(u,t),(s,v),(v,t)\},\) and

V(G) 1
u 1
S t
1 v
1

**Figure 2** A sketch of the reduction for Theorem 7. For every edge \(e_i=\{u,v\}\in E(G)\), we create this graph _G<sub>i</sub>_. With an optimal choice of the certificate _C_, this graph induces error 0 if and only if \(\{u,v\}\subseteq C[s,t]\).

