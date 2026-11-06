## A Randomized maximal and almost maximal matchings

Israeli and Itai’s \[8\] algorithm for finding a maximal matching works by identifying a sparse subgraph of _G_, then finding a large matching _M_<sub>1</sub> in the sparse subgraph. The edges and incident vertices of _M_<sub>1</sub>, as well as remaining isolated vertices, are removed from _G_ resulting in a subgraph _G_<sub>1</sub>. The process is iterated, giving a sequence of subgraphs _G_<sub>1</sub>_,G_<sub>2</sub>_,..._ and matchings _M_<sub>1</sub>_,M_<sub>2</sub>_,..._, until \(G_k=\varnothing\). At this point, \(M=\bigcup_{i=1}^KM_i\) is a maximal matching. We give pseudocode for Israeli and Itai’s main subroutine, which we call **MatchingRound**, in Algorithm 4. In \[8\], Israeli and Itai prove the following performance guarantee for **MatchingRound**.

**Algorithm 4 MatchingRound**(_G_): Finds a large matching in a graph

1: Each \(v\in V\) picks a neighbor _w_ uniformly at random, forms oriented edge (_v,w_).<br>
2: Each \(v\in V\) with deg<sub>_in_</sub>(_v)\>_0 picks one in-coming edge (_w,v_) uniformly at random, deletes remaining in-edges. Let \(G'\) be the (undirected) graph formed by the chosen edges with orientation ignored.<br>
3: Each \(v\in V\) with \(\mathrm{deg}_{G^\prime}(v)>0\) chooses one incident edge (_v,w_) uniformly at random.<br>
4: The matching _M_<sub>1</sub> consists of edges \((v,w)\in G'\) which were chosen by both _v_ and _w_ in the previous round. _G_<sub>1</sub>=(_V_<sub>1</sub>_,E_<sub>1</sub>) is the induced subgraph of _G_ formed by removing all vertices contained in _M_<sub>1</sub> and any remaining isolated vertices from _G_.<br>
5: Output (_G_<sub>1</sub>_,M_<sub>1</sub>).

**Lemma A.1.** (Israeli and Itai \[8\]) There exists an absolute constant _c\<_1 such that on input _G=G_<sub>0</sub>=(_V_<sub>0</sub>_,E_<sub>0</sub>), the resulting graph _G_<sub>1</sub>=(_V_<sub>1</sub>_,E_<sub>1</sub>) found by **MatchingRound** satisfies \(\mathbf{E}(|V_1|)\le c|V_0|\).

As a consequence of Lemma A.1, we obtain the following useful result.

**Corollary A.2.** Let \(\eta>0\) be a parameter. Then \(s=O(\mathrm{log}(n/\eta))\) iterations of **MatchingRound** suffice to produce a maximal matching in _G_ with probability at least \(1-\eta\).

_Proof._ By Lemma A.1, we have \(\mathbf{E}(|V_s|)\le c^sn\). Therefore, applying Markov’s inequality gives<tbc>

\(\mathrm{Pr}(|V_s|\ge 1)\le\frac{\mathbf{E}(|V_s|)}{1}\le c^sn.\)

