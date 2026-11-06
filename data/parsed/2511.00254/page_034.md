where the last inequality follows from the fact that \((1-1/x)^{x-2}\ge 1/e\) for all _x\>_1.

We repeat this process _C_=2_ek_<sup>2</sup>log|_E(U_)| times, independently, obtaining random subgraphs _H_<sub>1</sub>_,...,H<sub>C</sub>_ of _U_. For \(PP'\in E(U)\), let \(A_{PP^\prime}\) be the event that for all \(i\in[C]\), \(PP'\notin E(H_i)\). Then,

\(Pr\left[A_{PP^\prime}\right]\le\left(1-\frac{1}{ek^2}\right)^{2ek^2log|E(U)|}\le\left(\frac{1}{e}\right)^{2log|E(U)|}=|E(U)|^{-2},\)

where the second inequality follows from the fact that \((1-1/x)^x\le 1/e\) for _x\>_1.

Let _A_ be the event that there exists \(PP'\in E(U)\) such that for all \(i\in[C]\), \(PP'\notin E(H_i)\). That is, there exists \(PP'\in E(U)\) such that \(A_{PP^\prime}\) holds. By a basic union bound, \(Pr\left[A\right]\le|E(U)|\cdot|E(U)|^{-2}<1\). So there is an outcome in which _A_ does not hold. In this outcome, _U_ is covered by the graphs _H_<sub>1</sub>_,...,H<sub>C</sub>_. Hence _U_ is the sum of _C_ planar graphs.

From this, Theorem D.1 follows easily.

_Proof of Theorem D.1._ We show that _U_ is _O(k_<sup>2</sup>log|_E(U_)|)-degenerate, from which the result follows. As the property assumed in the theorem statement is hereditary (i.e. closed under node deletion), it suffices to show that _U_ contains a node with at most _O(k_<sup>2</sup>log|_E(U_)|) neighbours.

By Theorem D.2, _U_ is the sum of _O(k_<sup>2</sup>log|_E(U_)|) planar graphs. Each planar graph contributes at most 3|_V(U_)| parallel edge classes, so it follows that _E(U_) contains at most _O(k_<sup>2</sup>|_V(U_)|log|_E(U_)|) parallel edge classes. Hence it contains a node with at most _O(k_<sup>2</sup>log|_E(U_)|) neighbours.

