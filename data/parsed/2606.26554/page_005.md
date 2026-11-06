#### Hop-sets.

A (weighted) set of edges _F_ is a \(\beta\)-hop-set for graph _G_=(_V,E_) if every pair of vertices (_u,v_) in \(H=(V,E\cup F)\) has the same distance as in _G_ and there exists a shortest path of at most \(\beta\) hops. Research in hop-sets (and the related concept of shortcut sets) aims to minimize both the size of the hop-set (ideally linear) and the hop diameter \(\beta\). A folklore sampling algorithm produces \(\beta\)-hop-sets of size \(n^2/\beta^2\): sample a set _S_ of \(n/\beta\) vertices, and add all edges between \((u,v)\in S\times S\) with weight dist(_u,v_). In particular, we may obtain an \(\widetilde{O}\left(n^{1/2}\right)\)-hop-set of size \(\widetilde{O}\left(n\right)\). Bodwin and Hoppenworth showed that the folklore sampling is optimal up to polylogarithmic factors: any exact hop-set of size \(\widetilde{O}\left(n\right)\) must have \(\beta=\widetilde{\Omega}\left(n^{1/2}\right)\) \[BH23\].

However, the sampling algorithm does not compute a hop-set efficiently, since previous algorithms for computing all distances between \(S\times S\) for _S_ of size \(\sqrt{n}\) require time \(\widetilde{O}(min(n^{2.5},n^\omega))=O(n^{2.372})\). Our improved MSSP algorithm allows us to compute all \(S\times S\) distances in time \(n^{\omega(0.5,1,1)}=O(n^{2.043})\) \[ADV<sup>+</sup>25\].<sup>6</sup>

#### Distance Emulators.

Emulators are sparse graphs that faithfully preserve the distances of a graph. Formally, given a graph _G_=(_V,E_), a (possibly weighted) set of edges _F_ is a +_k_-emulator if \(dist_G(u,v)\le dist_{(V,F)}(u,v)\le dist_G(u,v)+k\) for all pairs of vertices _u,v_. Emulators (and related constructions such as graph spanners) have been the subject of intense study since their introduction \[PS89\], and have been useful objects with many applications, including compact routing schemes \[PU89, CW00, Cow01, TZ01, RTZ08\], distance oracles \[TZ05, BK06\], and broadcasting \[FPZW04\].

Several constructions of additive emulators are known: +2-emulators of size \(\widetilde{O}\left(n^{3/2}\right)\) \[ACIM99\], +4- emulators of size \(\widetilde{O}\left(n^{4/3}\right)\) \[DHZ00\], and +6-emulators of size \(\widetilde{O}\left(n^{4/3}\right)\) \[BKMP05\]. We remark that both the +2 and +6 constructions are spanners (_F_ is a subset of _E_). However, the sparsest +4-spanner known has size \(\widetilde{O}\left(n^{7/5}\right)\) \[Che13\]. Furthermore, it is known that no emulator (or any data structure) of size \(n^{4/3-\Omega(1)}\) can achieve error _k=n_<sup>_o_(1)</sup> \[AB17\]. Thus, significant effort has been devoted to characterizing the additive error of emulators of linear size \[TZ06, BV15, HP21, EGN23, KP23b, Hop24, HJVX24\].

Both the +2 and +6-emulators can be constructed in near-linear time \(\widetilde{O}\left(n^2\right)\) \[DHZ00, Woo10\]. However, the best known algorithm for constructing the +4-emulator requires time \(\widetilde{O}\left(n^{7/3}\right)\) \[DHZ00\]. With our MSSP algorithm, we obtain a construction in time \(\widehat{O}(n^{\omega(2/3,1,1)})=O(n^{2.1321})\) \[ADV<sup>+</sup>25\].

## 1.2 Reachability in Directed Graphs

In the Multiple-Source Reachability problem, the goal is to determine whether _s_ can reach _v_ for every pair \((s,v)\in S_\mathrm{in}\times V\) . As all-pairs reachability can be solved in \(\widehat{O}(n^\omega)\) time \[FM71, Mun71\], and single-source reachability can be solved in _O(m_) time, Multiple-Source Reachability can be solved in \(\widehat{O}(min(|S_\mathrm{in}|m,n^\omega))\) time, similar to MSSP on undirected unweighted graphs. Standard reduction from BMM(_S_<sub>in</sub>_,n,n_) also works for Multiple-Source Reachability, establishing an \(\Omega(\mathsf{T}_\mathrm{BMM}(S_\mathrm{in},n,n))\) lower bound.

Recently, Elkin and Trehan \[ET24, ET25\] gave an alternative algorithm for Multiple-Source Reachability. Their algorithm runs in \(\widehat{O}\left(n\mathsf{T}_\mathrm{MUL}(S_\mathrm{in},n,n)^{2/3}\right)\), which beats \(\widehat{O}(min(S_\mathrm{in}m,n^\omega))\) for certain values of |_S_<sub>in</sub>|, but unfortunately never meets the \(\Omega(\mathsf{T}_\mathrm{BMM}(S_\mathrm{in},n,n))\) lower bound (see Figure 1).

In our second main result, we design an algorithm for Multiple-Source Reachability that matches the \(\Omega(\mathsf{T}_\mathrm{BMM}(S_\mathrm{in},n,n))\) lower bound.

**Theorem 1.5.** _Multiple Source Reachability is equivalent to_ BMM(|_S_<sub>in</sub>|_,n,n), up to_ polylog(_n_) _factors. In particular, there is a deterministic algorithm computing Multiple-Source Reachability in_ \(\widetilde{O}\left(\mathsf{T}_\mathrm{BMM}\left(|S_\mathrm{in}|,n,n\right)\right)\) _time._

The following figure illustrates a comparison of our algorithm with the baseline algorithm and the algorithm of Elkin and Trehan \[ET24, ET25\].

<sup>6</sup>\(\omega(a,b,c)\) is the rectangular matrix multiplication exponent, or the smallest constant _d_ such that an \(n^a\times n^b\times n^c\) matrix product can be computed in _n_<sup>_d+o_(1)</sup> time.

