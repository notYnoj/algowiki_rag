[MN20] Sagnik Mukhopadhyay and Danupon Nanongkai. "Weighted min-cut: sequential, cutquery, and streaming algorithms". In: _Proceedings of the 52nd Annual ACM SIGACT Symposium on Theory of Computing, S 2020, Chicago, IL, USA, June 22-26, 2020_. Ed. by Konstantin Makarychev, Yury Makarychev, Madhur Tulsiani, Gautam Kamath, and Julia Chuzhoy. ACM, 2020, pp. 496–509.

[Nan24] Danupon Nanongkai. "Cross-Paradigm Graph Algorithms (Invited Talk)". In: _ICALP_. Vol. 297. LIPIcs. Schloss Dagstuhl - Leibniz-Zentrum für Informatik, 2024, 3:1–3:1.

[Orl07] James B. Orlin. "A Faster Strongly Polynomial Time Algorithm for Submodular Function Minimization". In: _Integer Programming and Combinatorial Optimization, 12th International IPCO Conference, Ithaca, NY, USA, June 25-27, 2007, Proceedings_. Ed. by Matteo Fischetti and David P. Williamson. Vol. 4513. Lecture Notes in Computer Science. Springer, 2007, pp. 240–251.

[Que98] Maurice Queyranne. "Minimizing symmetric submodular functions". In: _Math. Program_. 82 (1998), pp. 3–12.

[RSW18] Aviad Rubinstein, Tselil Schramm, and S. Matthew Weinberg. "Computing Exact Minimum Cuts Without Knowing the Graph". In: _9th Innovations in Theoretical Computer Science Conference, ITCS 2018, January 11-14, 2018, Cambridge, MA, USA_. Ed. by Anna R. Karlin. Vol. 94. LIPIcs. Schloss Dagstuhl - Leibniz-Zentrum für Informatik, 2018, 39:1–39:16.

[SS11] Daniel A. Spielman and Nikhil Srivastava. "Graph Sparsification by Effective Resistances". In: _SIAM J. Comput._ 40.6 (2011), pp. 1913–1926.

[ST11] Daniel A. Spielman and Shang-Hua Teng. "Spectral Sparsification of Graphs". In: _SIAM J. Comput._ 40.4 (2011), pp. 981–1025.

[Tro11] Joel A. Tropp. "User-Friendly Tail Bounds for Sums of Random Matrices". In: _Foundations of Computational Mathematics_ 12.4 (Aug. 2011), pp. 389–434.

[Vyg03] Jens Vygen. "A note on Schrijver’s submodular function minimization algorithm". In: _J. Comb. Theory B_ 88.2 (2003), pp. 399–402.

## A Missing Proofs from Section 2

**Lemma 2.2.** _Let F_=(_V,E_) _be a non-circular flow graph of value f with n vertices. Then, F contains_ \(|E|\le O(n\sqrt{f})\) _edges._

_Proof._ Since _F_ contains no cycles, there exists an topological ordering \(\phi:V\rightarrow[n]\) such that for any directed edge \((a,b)\in E\), we have \(\phi(a)<\phi(b)\). For any edge \(e=(a,b)\in E\), denote \(\phi(e)=\phi(b)-\phi(a)\). We shall also write _e_ and (_a,b_) interchangeably.

We will compute \(X=\sum_{e\in E}w_F(e)\cdot\phi(e)\) in two different ways:

1. Let the _f_ units of flow of _F_ be F<sub>1</sub>_,...,_F_<sub>f</sub>_ where each flow is a (disjoint) directed path from _s_ to _t_. Consider any flow F_<sub>i</sub>_=(_s=v_<sub>0</sub>_,v_<sub>1</sub>_,...,v<sub>d</sub>=t_). Then, we have:

\(\sum_{e\in\mathcal{F}_i}\phi(e)=\sum_{j=0}^{d-1}\phi(v_{j+1})-\phi(v_j)=\phi(v_d)-\phi(v_0)\le n.\)

