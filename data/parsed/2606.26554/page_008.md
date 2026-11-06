### 1.4 Related Works

Question 1 is a long-term research paradigm that has been approached from many angles:

1. Single-Source Shortest Paths (SSSP): The most classical and successful example \[Dij59, FT87\], SSSP computes a set of _n_ distances from _s_.<tbc>

2. Extremal distances: The diameter, radius, and eccentricities are well-studied problems in distance computation, resulting in both approximation algorithms \[RV13, CLR<sup>+</sup>14, BRS<sup>+</sup>18, CGR16\] and hardness results \[RV13, Bon22, DLV25\].<tbc>

3. _n_-Pairs Shortest Paths (NPSP): Given _n_ pre-specified pairs of vertices (_s<sub>i</sub>,t<sub>i</sub>_), compute dist(_s<sub>i</sub>,t<sub>i</sub>_) for all _i_. In contrast to SSSP, the NPSP problem computes _n_ arbitrary pre-specified distances. The study of NPSP was initiated by \[ACIM99\], with several recent works reigniting interest in the question \[DJVW22, CHL25\].<tbc>

4. Distance Oracles: Preprocess _G_ so that given any query (_u,v_), return dist(_u,v_) efficiently. Distance oracles capture the setting where we do _not_ know what distances are interesting in advance. A long line of work has established a variety of approximation algorithms \[Tho04, TZ05, PR10, Che14, CDW17, CGMW19, CZ22\] and hardness results \[ABKZ22, JX23, ABF23\].

### 1.5 Open Questions

We conclude the introduction with some open questions.

1. We establish an equivalence between BMM and MSSP on unweighted, undirected graphs. Can a similar equivalence (with some other matrix product) be established for MSSP on directed graphs? Concretely, can Theorem 1.6 be generalized to compute shortest paths on directed graphs (not necessarily DAGs)?<tbc>

2. In our work, we have shown that a \((d,\phi)\)-low diameter small neighborhood decomposition can be computed efficiently, where \(d,\phi=n^{o(1)}\). In principle, it may be possible to obtain a decomposition where |_N(V<sub>i</sub>_)|=_O_(|_V<sub>i</sub>_|) and diam(_V<sub>i</sub>_)=_O_(log_n_) for all _V<sub>i</sub>_. Can we obtain such a decomposition, and do so efficiently? Even the weaker setting where \(d,\phi=\text{polylog}(n)\) would be interesting.<tbc>

3. Our decomposition algorithm runs in _n_<sup>2+_o_(1)</sup> time, which is efficient for dense graphs, but is inefficient on sparse graphs. Can we compute a low diameter small neighborhood decomposition in _m_<sup>1+_o_(1)</sup> time? Are there other applications of low diameter small neighborhood decompositions?<tbc>

4. Currently, our algorithm for computing MSSP is randomized, since our algorithm for computing our low diameter small neighborhood decomposition requires randomness. Can we derandomize our low diameter small neighborhood decomposition algorithm?<tbc>

5. We use MSSP to develop faster algorithms for hop-set, shortcut-set, and distance emulator constructions. It would be interesting to find further applications of an efficient MSSP algorithm.

#### Outline.

In Section 2, we give an overview of our main results and techniques. In Section 4, we present our algorithm for computing low diameter small neighborhood decompositions. In Section 5, we give our algorithms for computing MSSP on undirected graphs and their applications. In Section 6, we present our algorithms on directed graphs and their applications.

## 2 Technical Overview

We give an overview of our techniques. Recall that our goal is to design an MSSP algorithm that performs better than the naive \(\widetilde{O}\left(min(|S_\text{in}|n^2,n^{\omega+o(1)})\right)\) time obtained by either running SSSP from every source or computing APSP. We begin with a simple algorithm that makes an improvement for some regimes of |_S_in|.

