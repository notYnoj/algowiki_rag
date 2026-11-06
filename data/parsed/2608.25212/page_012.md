We begin by introducing a data structure problem for reporting interval intersections, called Interval-Intersect, and we show how to solve this problem in total linear time. In Interval- Intersect, we are given as input a unary-encoded integer \(N\ge 1\) (the universe size) and a finite set _A_ of labels, where every label \(a\in A\) is assigned an integer interval \(I_a\subseteq[N]\). Initially, all labels are active. The data structure is required to answer the following online queries: given an integer interval \(J\subseteq[N]\), report all active labels \(a\in A\) with the corresponding intervals _I<sub>a</sub>_ intersecting _J_, and deactivate all reported labels.

Subsequently, we will use the resulting data structure to show the linear-time algorithm for Theorem 5. In Section 4.1, we prove the following.

**Lemma 21.** _There exists a data structure for Interval-Intersect in the word RAM model of computation that processes an instance with universe size N, set of labels A, and q queries in_ O(_N_+|_A_|+_q_) _time._

The purpose of encoding _N_ in unary is to ensure that every element of the universe \[_N_\] fits within a single RAM word; hence we can assume _N\<_2_<sup>b</sup>_ where _b_ is the size of the machine word.

We show now to use Lemma 21 to solve SSSP in linear time in graphs with a given interval biclique partition, namely, we prove Theorem 5.

_Proof of Theorem 5._ Recall that \[_n_\] is the vertex set of the graph, and let the _i_th biclique in the edge partition (\(i\in[b]\)) have sides _A<sub>i</sub>_ and _B<sub>i</sub>_; each _A<sub>i</sub>_ and _B<sub>i</sub>_ is a subinterval of \[_n_\].

In the beginning, we set up two instances of the linear-time data structure for Interval- Intersect, both with universe \[_n_\]:

• _D_gather, with labels from \[_n_\], where the label \(i\in[n]\) is assigned the interval \[_i,i_\];<tbc>

• _D_scatter, with labels \(\bigcup_{i\in[b]}\{a_i,b_i\}\), with the interval _A<sub>i</sub>_ assigned to _a<sub>i</sub>_ and the interval _B<sub>i</sub>_ assigned to _b<sub>i</sub>_.

The active items in _D_gather are the vertices undiscovered by the run of the breadth-first search (BFS); hence, we initially query _D_gather with \[_s,s_\], where _s_ is the source of the BFS, to deactivate the label _s_. On the other hand, the active items in _D_scatter represent the sides of the bicliques that do not contain vertices visited by BFS.

We perform the usual BFS in _G_, with the usual queue holding the vertices discovered by the search (initially only _s_) that are yet to be visited. When a vertex \(v\in[n]\) is visited by the search, we find the yet undiscovered neighbors of _v_ as follows. We first use _D_scatter to enumerate the not yet processed sides of the bicliques by querying _D_scatter for the interval \[_v,v_\]. Suppose _D_scatter returns _a<sub>i</sub>_ (resp., _b<sub>i</sub>_) as one of the labels; then, we have that \(v\in A_i\) (resp., \(v\in B_i\)). In this case, all vertices in _B<sub>i</sub>_ (resp., _A<sub>i</sub>_) should become discovered if not yet discovered. In order to ensure that, we query _D_gather with the interval _B<sub>i</sub>_ (resp., _A<sub>i</sub>_), and enqueue all vertices returned as a result of the query, marking _v_ as the parent of each of them. We repeat this process for each label reported by _D_scatter.

The correctness of the algorithm is clear as it is simply a breadth-first search with a bespoke method for listing the yet undiscovered neighbors. To see the efficiency, observe that we issue at most _n_ queries to _D_scatter, and it reports at most O(_b_) labels throughout the entire run of SSSP. Thus, at most O(_b_) queries to _D_gather are issued. Hence both data structures for Interval-Intersect process all respective queries in total O(_n+b_) time. Moreover, it is clear that outside of the queries, the SSSP implementation above takes time linear in the size of the input; the claim follows.

