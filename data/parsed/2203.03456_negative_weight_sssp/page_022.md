_Proof._ By Observation 6.4, for every edge _e_, there are _O_(log_n_) calls LDD(_G<sub>i</sub>_, _D_) such that _G<sub>i</sub>_ contains _e_. The corollary follows by Union Bound.

## 6.5 Diameter Analysis

We now show that the set _E<sup>rem</sup>_ returned by LDD(_G,D_) satisfies the first output property of Lemma 1.2. The proof is essentially trivial, since the low-diameter condition is ensured by Line 20.

**Lemma 6.11.** _For any graph G,_ LDD(_G,D_) _returns E<sup>rem</sup> such that each SCC of G_\\_E<sup>rem</sup> has weak diameter_ \(\le D\).

_Proof._ The proof will be induction on |_V(G_)|. The base case where |_V(G_)|=1 trivially holds. We now assume by induction that the Lemma holds for all \(\text{LDD}(G',D)\) with \(|V(G')|<|V(G)|\). Note that in the remaining of this proof we let _G_ denote the initial input to LDD(_G,D_) and not the graph that changes throughout the execution of the algorithm.

Consider any two vertices \(x,y\in V(G)\). We want to show that LDD(_G,D_) always returns _E<sup>rem</sup>_ such that

\(\text{\textit{if}}x\text{\textit{and}}y\text{\textit{are in the same SCC in}}G\backslash E^{rem}\text{\textit{, then}}\text{dist}_G(x,y)\le D\text{\textit{and}}\text{dist}_G(y,x)\le D.\) (10)

Note that if a vertex is in \(V(G')\) for recursive call \(\text{LDD}(G',D)\) in Line 16 then it is immediately removed from the graph _G_ (Line 18) and never touched again during the execution of the current call LDD(_G,D_). There are thus three possible cases regarding _x_ and _y_.

**Case 1** There is some recursive call \(\text{LDD}(G',D)\) in Line 16 such that one of _x,y_ is in \(G'\) and the other is not.

**Case 2** There is some recursive call \(\text{LDD}(G',D)\) in Line 16 such that both _x_ and _y_ are in \(G'\).

**Case 3** Neither _x_ or _y_ participate in any recursive call.

In Case 1, we know by Observation 6.5 that _x_ and _y_ cannot end up in the same SCC of _G_\\_E<sup>rem</sup>_, so the property (10) holds.

In Case 2, note that for recursive call \(\text{LDD}(G',D)\) we have that \(G'\) is an induced subgraph of _G_, and also that \(V(G')\le.7V(G)\), because otherwise the algorithm would have terminated in Line 15. Thus, by the induction hypothesis, the Lemma holds for \(\text{LDD}(G',D)\). In particular, there are two options: **(1)** If _x_ and _y_ are in the same SCC of \(G'\backslash E^{rem}\), then \(\text{dist}_G(x,y)\le\text{dist}_{G^\prime}(x,y)\le D\) and \(\text{dist}_G(y,x)\le\text{dist}_{G^\prime}(y,x)\le D\) and **(2)** if _x_ and _y_ are not in the same SCC in \(G'\backslash E^{rem}\), then they are also not in the same SCC of _G_\\_E<sup>rem</sup>_, because by Observation 6.5, none of the vertices of \(V(G)\backslash V(G')\) can be in the same SCC as either _x_ or _y_ in _G_\\_E<sup>rem</sup>_.

Finally, Case 3 holds because if _x_ and _y_ don’t participate in any recursive calls, then they are not removed from graph _G_. In Line 20 the algorithm checks that all vertices which weren’t removed have weak diameter \(\le D\). If the check fails then the algorithm sets \(E^{rem}\leftarrow E(G)\), in which case the Lemma trivially holds because all SCCs of _G_\\_E<sup>rem</sup>_ will be singletons.

## Acknowledgement

We thank Sepehr Assadi, Joakim Blikstad, Thatchaphol Saranurak, and Satish Rao for their comments on the early draft of the paper and the discussions. We thank Mohsen Ghaffari, Merav Parter, Satish Rao, and Goran Zuzic for pointing out some literature on low-diameter decomposition. A<tbc>

