<tbc>**Claim 3.9.** _For any iteration i such that_ \(\mathcal{W}(H_i)\neq\emptyset\)_, there exists an edge_ \(e_i\in G\backslash H_i\) _such that_

\(|\mathcal{W}(H_i\cup e_i)|\le\left(1-\Omega\left(\frac{k'}{n\sqrt{k}}\right)\right)\cdot|\mathcal{W}(H_i)|.\)

For now, we will only sketch the proof of Claim 3.9. Later down the line, we will give a constructive variant of this claim which allows us to efficiently recover such edge _e<sub>i</sub>_ via cut-queries.

_Proof Sketch._ Let \(Q\subseteq G\backslash H_i\) be such that \(|Q|=O(n\sqrt{k})\) and \(\nu(H_i\cup Q)\ge f\). Such set _Q_ exists by construction: take a flow subgraph \(F\unknown H_i\) of size _f-k_ and let _Q_ be the set of all edges in a non-circular flow of size _k_ of _G<sub>F</sub>_ that has not appeared in _H<sub>i</sub>_. The bound of \(|Q|=O(n\sqrt{k})\) is obtained via Lemma 2.2.

Suppose we were to add _Q_ to _H<sub>i</sub>_. For any witness W=(_S,T,Y_) of _H<sub>i</sub>_, there will be at least _f_ edges among \(H_i\cup Q\) that crosses the cut (_S,T_). However, we only pre-allocate \(f-k'-1\) edges to _Y_ and those already include _E<sub>H<sub>i</sub></sub>(S,T_). Thus, there are at least \(k'+1\) edges among _Q_ that kills W. Since this holds for any witness W, via an averaging argument, some edge(s) among _Q_ must kill at least a \(\frac{k'+1}{|Q|}\ge\Omega\left(\frac{k'}{n\sqrt{k}}\right)\) fraction of W(_H<sub>i</sub>_).

**Claim 3.9 is good (enough) for two-player communication.** When edges of _G_ are partitioned across Alice and Bob, each player can locally evaluate, via brute-force, whether each edge is \(\gamma\)-good w.r.t. \(\gamma=\Omega\left(\frac{k'}{n\sqrt{k}}\right)\). Claim 3.9 guarantees that such good edge always exists among _G_\\_H_; thus must be found by one of the players. Such player then spends \(\widetilde{O}(1)\) bits of communication to send over that edge, adds it to _H_, and then proceeds to the next iteration. As a result, the total communication cost is \(\widetilde{O}(n/\gamma)=\widetilde{O}(n^2\cdot\frac{\sqrt{k}}{k'})\). Then, following a line of reduction, we can recover a weaker version of Lemma 3.5 with communication cost replaced by \(\widetilde{O}\left(\frac{n^2}{\sqrt{\Delta}}+\frac{n^3}{\Delta^2}\right)\). For all intents and purposes, we can use this weaker result to recover an \(\widetilde{O}(n^{11/7})\) communication protocol by combining it with Lemma 3.3. However, to get a parameterized complexity of \(\widetilde{O}(n\cdot\nu(G)^{4/7})\) as promised in Lemma 3.5, we need to strengthen our strategy. We defer this improvement to Section C.

**It is a bit more complicated for cut-query.** In the communication model, our search for a \(\gamma\)-good edge leverages a crucial feature: the input graph is _explicitly_ given, although being split between players. This guarantees that any \(\gamma\)-good edge must already be visible to at least one of them. In contrast, the cut-query model lacks this advantage, as we can only make queries to a _hidden_ graph. Given the somewhat-artificial definition of a \(\gamma\)-good edge, it is not immediately clear whether such an edge can be efficiently identified. Fortunately, we develop an alternative proof of Claim 3.9 that is constructive! This new approach--combined with a few additional subroutines--allows us to locate an \(\Omega(\gamma)\)-good edge (with a slightly worse constant factor) using only _O_(log_n_) cut queries to _G_. We explore this approach in detail in Section 5.

## 3.1 Proofs of Main Theorems

We wrap up this overview by combining the main lemmas to prove our main results.

**Theorem 1.1** (Main result #1)**.** _There is a randomized algorithm that computes a minimum s-t cut of an undirected unweighted graph G. The algorithm always makes_ \(\widetilde{O}(n^{8/5})\) _cut queries to G and succeeds with high probability._

