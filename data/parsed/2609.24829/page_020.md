We will need the following prior result about the communication complexity of \(\text{TRITEST}_{\tau,m}\).

**Theorem 5.3** (McGregor and Vorotnikova \[MV20\])**.** _Let_ \(m\in\mathbb{N}\) _be sufficiently large and suppose:_

\(0<\tau<\sqrt{m}p=\tau^{-0.5}/10\delta=1/m^4.\)

_Then_ \(\mathrm{R}_{\delta,p}(\text{TRITEST}_{\tau,m})=\Omega(m/\sqrt{\tau})\).

Note that in the hard instances used to establish the above bound, the number of nodes is \(O(\sqrt{m}\tau)\) and therefore the graph is sparse when \(\tau\) is large.

Our main communication complexity result is proven in the next lemma. Essentially it establishes that even if there are at least \(\tau_2\) triangles in the input graph, any protocol for \(\text{TOLTRITEST}_{\tau_1,\tau_2,m}\) must use sufficient communication to distinguish between 0 and \(\tau_1\) triangles because the first player may have no information where there were \(\tau_2\) triangles.

**Lemma 5.1** (Tolerant Triangle Testing)**.** Let \(m\in\mathbb{N}\) be sufficiently large and suppose:

\(0<\tau_1<\sqrt{m/2}\tau_1<\tau_2<m/4p=\tau_1^{-0.5}/10\delta=1/m^4\)

Then \(\mathrm{R}_{\delta,p}^\mathcal{K}(\text{TOLTRITEST}_{\tau_1,\tau_2,m})=\Omega(m/\sqrt{\tau_1})\) where K is the set of graphs with at most _m_ edges and at least \(\tau_2\) triangles.

_Proof._ Let _P_ be a protocol for \(\text{TOLTRITEST}_{\tau_1,\tau_2,m}\) with error probability at most \(\delta\). Suppose Alice and Bob want to evaluate \(\text{TRITEST}_{\tau_1,m/2}\) on a graph _G_<sub>1</sub> with at most _m/_2 edges, where each edge is given to Alice independently with probability _p_ and to Bob otherwise. They can use _P_ to solve \(\text{TRITEST}_{\tau_1,m/2}\) in the following way:

1. Define a gadget graph _J_ where \(V(J)=\{u_1,\dots,u_{\tau_2},t_1,t_2\}\) and let _E(J_) contain all edges {_u<sub>i</sub>,t<sub>j</sub>_} for \(i\in[\tau_2]\) and \(j\in\{1,2\}\). Let \(H=G_1\sqcup J\) be the disjoint union of _G_<sub>1</sub> and _J_.<tbc>

2. Use public randomness to distribute the edges of _J_ between themselves such that each edge in _J_ is received by Alice with probability _p_.<tbc>

3. Run _P_ to compute \(\text{TOLTRITEST}_{\tau_1,\tau_2,m}(H)\) with probability at least \(1-\delta\). Note that since _J_ is triangle free, \(\text{TOLTRITEST}_{\tau_1,\tau_2,m}(H)=\text{TRITEST}_{\tau_1,m/2}(G_1)\).

The above reduction defines a protocol \(P'\) for \(\text{TRITEST}_{\tau_1,m/2}\) with error at most \(\delta\). Hence,<tbc>

\(\mathrm{cost}(P')\ge\mathrm{R}_{\delta,p}(\text{TRITEST}_{\tau_1,m/2})=\Omega(m/\sqrt{\tau_1})\)

<tbc>by Theorem 5.3. Therefore, there exists a graph _G_<sup>∗</sup> with at most _m/_2 edges, a partition \(\sigma^*\) of the edges of \(H^*=G^*\sqcup J\), and a setting _r_<sup>∗</sup> of the public randomness such that Alice’s message in protocol \(P'\) has length

\(|M(S_A^*,r^*)|=\Omega(m/\sqrt{\tau_1})\text{where}S_A^*=\{e\in E(H^*):\sigma^*(E(H^*))=A\}.\) (6)

Now consider the graph \(H^+=G^*\sqcup J^+\), where _J_<sup>+</sup> is obtained from _J_ by adding the edge _e_<sup>∗</sup>={_t_<sub>1</sub>_,t_<sub>2</sub>}. Note that _H_<sup>+</sup> has at least \(\tau_2\) triangles. To bound cost<sub>K</sub>(_P_) we proceed as follows:

\(\mathrm{cost}_\mathcal{K}(P)=\mathrm{max}_{G\in\mathcal{K},\sigma:E(G)\rightarrow\{A,B\},R}|M(\sigma_A(E(G)),R)|\ge\mathrm{max}_{G=H^+,\sigma=\sigma^+,R=r^*}|M(\sigma_A(E(G)),R)|\) (7)

\(\ge|M(\sigma_A^+(E(H^+)),r^*)|\) (8)

\(=|M(S_A^*,r^*)|\)

where \(\sigma^+\) is the partition that extends \(\sigma^*\) to a partition of _E(H_<sup>+</sup>) by assigning _e_<sup>∗</sup> to Bob and assigning every other edge exactly as in \(\sigma\). Note that with this definition \(\sigma_A^+(E(H^+))=S_A^*\) as required in the last step. Hence, combined Equation 6, we conclude \(\mathrm{cost}_\mathcal{K}(P)\ge\Omega(m/\sqrt{\tau_1})\) as required.

