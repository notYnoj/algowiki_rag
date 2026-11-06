## 5.2 Proof of Theorem 1.2

We start the proof of Theorem 1.2, which we restate here.

**Theorem 1.2.** Diverse Shortest Cycle Coverage _on planar graphs admits an algorithm with running time_ \(2^{\mathcal{O}(k)}\cdot n^{\mathcal{O}(1)}\).

Consider an instance \((G,w:E(G)\rightarrow\mathbb{Z}_{>0},k,d,\ell)\) of Diverse Shortest Cycle Coverage (Planar DSC), where _G_ is a planar graph with _V(G_)=\[_n_\]. Recall our goal is to check if there is a set C={_C_<sub>1</sub>_,C_<sub>2</sub>_,...,C<sub>k</sub>_} of exactly _k_ many _d_-diverse shortest cycles in _G_ such that \(w(\cup_{i\in k}E(C_i))\ge\ell\). We will make the following assumptions regarding the instance:

