2_<sup>T</sup>_, output it; otherwise output a single vertex. If \(\alpha(G)\ge 2^{-T}N\), the output has size at least 2_<sup>T</sup>_, which is at least \(\alpha(G)2^T/N\) because \(\alpha(G)\le N\). If \(\alpha(G)<2^{-T}N\), a singleton has size greater than \(\alpha(G)2^T/N\). The algorithm runs in time _N_<sup>_O(T_)</sup> whether or not the promise holds: the SDP computation and the finite enumeration do not depend on the promise, and the enumeration reports failure if it finds no suitable candidate. This establishes the claimed running time \(N^{O(\sqrt{logN})}\).

## 4.7 A Limitation of the Analysis

We use the total singleton mass to measure the value of the relaxation at a given level.

**Definition 4.7** (Lasserre value)**.** _Let G_=(_V,E_) _be a graph and let_ \(r\ge 1\) _be an integer. The level-r Lasserre value of G is_<tbc>

\(\mathrm{Las}_r(G):=\mathrm{max}\{\sum_{u\in V}\mu(u):\mu\text{\textit{is a level-r pseudo-distribution for}}G\}.\)

<tbc>The proof of Theorem 4.6 uses \(\alpha(G)\ge 2^{-t}N\) only through the pseudo-distribution computed in Lemma 4.4. The proof of that lemma approximates Las<sub>2_t_+5</sub>(_G_) from below to additive error 1/2. Thus the same argument proves, for \(1\le t\le\sqrt{\mathrm{log}N}/12\),

\(\mathrm{Las}_{2t+5}(G)\ge 2^{-t}N\Longrightarrow\alpha(G)\ge 2^t.\) (17)

The following consequence of Tulsiani’s integrality-gap theorem limits the parameter range in which this implication can hold for every graph.

**Proposition 4.8** (A limit for implications from the Lasserre value)**.** _There are constants c,C\>_0 _and infinitely many integers_ \(N\ge 4\) _with the following property. Write_<tbc>

\(q_N:=\sqrt{\mathrm{log}N\mathrm{loglog}N},R_N:=\lfloor 2^{cq_N}\rfloor.\)

<tbc>_There exist a graph G on N vertices and an integer T with_ \(1\le T\le Cq_N\) _such that, simultaneously for every integer_ \(1\le r\le R_N\),<tbc>

\(\mathrm{Las}_r(G)\ge 2^{-T}N\text{\textit{and}}\alpha(G)<2^T.\) (18)

<tbc>_Proof._ By Tulsiani’s integrality-gap theorem \[Tul09, Theorem 5.3\], there are constants _C_<sub>0</sub>_,c_<sub>0</sub>_\>_0 and graphs on arbitrarily large numbers _N_ of vertices for which the independent-set relaxation after \(L_N:=\lfloor 2^{c_0q_N}\rfloor\) rounds has a feasible vector solution of value

\(B\ge\frac{\alpha(G)N}{2^s},s:=C_0q_N.\) (19)

Adjusting the constants accounts for the choice of logarithm base and for integer rounding. We first convert the vector solution into a pseudo-distribution, retaining half the original number of rounds, rounded down.

In Tulsiani’s formulation, the vectors _u<sub>A</sub>_ are indexed by subsets \(A\subseteq V\) of size at most _L<sub>N</sub>_. They satisfy \(\|u_\emptyset\|=1\), the edge constraints \(\langle u_{\{v\}},u_{\{w\}}\rangle=0\) for \(\{v,w\}\in E\), and the consistency constraints

\(\langle u_A,u_B\rangle=\langle u_C,u_D\rangle\text{whenever}A\cup B=C\cup D.\)

Each of the four sets must index an available vector. The objective is \(B=\sum_{v\in V}\|u_{\{v\}}\|^2\).

