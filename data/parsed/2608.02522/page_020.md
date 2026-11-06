Now observe that since every independent set in \(G'\) is also an independent set in _G_, we have that \((y_v)_{v\in V(G^\prime)}\) is a feasible solution for the dual program (D) for the subgraph \(G'\). Hence, it follows that

\(\chi_f(G')\ge\sum_{v\in V(G^\prime)}y_v\ge z(1-e^{-1})\ge\chi_f(G)/C,\)

by our definition of _C_. On the other hand, we have \(\chi(G')\le k=\lceil z\rceil\le 2z=\frac{2}{1-e^{-1}}z(1-e^{-1})\le C\chi_f(G')\). This shows that \(G'\) is a subgraph of _G_ satisfying both properties claimed in the lemma, concluding the proof of the part about the fractional chromatic number.

We now turn to the second part of the claim about the Hall ratio. So let _G_ be any given graph, and let \(z:=\rho(G)\ge 1\). Let \(H\subseteq G\) be a nonempty subgraph attaining the maximum in the definition of \(\rho(G)\), i.e., such that \(z=\frac{|V(H)|}{\alpha(H)}\). Set \(k:=\lceil z\rceil\) and let _I_<sub>1</sub>_,...,I<sub>k</sub>_ be a sequence of disjoint independent sets in _H_ defined as follows: For each _i_=1_,...,k_, we pick _I<sub>i</sub>_ as a maximum-size independent set in the induced subgraph \(H-\bigcup_{1\le j<i}I_j\). Let \(G':=H[I_1\cup\cdots\cup I_k]\). It is then clear that \(\chi(G')\le k\). Also observe that since \(G'\) is an induced subgraph of _H_, we have \(\alpha(G')\le\alpha(H)=\frac{|V(H)|}{z}\) . Next, we want to give a lower bound on the number of vertices of \(G'\). For this, observe that by definition of the Hall ratio and by definition of _I_<sub>1</sub>_,...,I<sub>k</sub>_, for every _i_=1_,...,k_ we have that<tbc>

\(|I_i|=\alpha\left(H-\bigcup_{1\le j<i}I_j\right)\ge\frac{|V(H-\bigcup_{1\le j<i}I_j)|}{\rho(G)}=\frac{1}{z}\left(|V(H)|-\sum_{j=1}^{i-1}|I_j|\right).\)

<tbc>Rearranging yields that<tbc>

\(|V(H)|-\sum_{j=1}^i|I_j|\le\left(|V(H)|-\sum_{j=1}^{i-1}|I_j|\right)-|I_i|\le(1-1/z)\left(|V(H)|-\sum_{j=1}^{i-1}|I_j|\right).\)

<tbc>This immediately yields that

\(|V(H)|-\sum_{j=1}^k|I_j|\le(1-1/z)^k|V(H)|\le exp(-k/z)|V(H)|\le e^{-1}|V(H)|,\)

so \(|V(G')|=\sum_{j=1}^k|I_j|\ge(1-e^{-1})|V(H)|\).

All in all, from this we may conclude that

\(\rho(G')\ge\frac{|V(G')|}{\alpha(G')}\ge\frac{(1-e^{-1})|V(H)|}{|V(H)|/z}=z(1-e^{-1})\ge\frac{k}{2}(1-e^{-1})=k/C.\)

In particular, we have \(\rho(G')\ge\rho(G)(1-e^{-1})\ge\rho(G)/C\) and \(\chi(G')\le k\le C\rho(G')\). This concludes the proof of the second part of the lemma. \(\square\)

The previous lemma shows that also \(\chi_f\) and \(\rho\) satisfy the second condition in the definition of \(\chi\)-amenability, with \(C=\frac{2}{1-e^{-1}}\). All in all, this shows that each of \(\chi\), \(\chi_f\), \(\rho\) is \(\chi\)-amenable.

