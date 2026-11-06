Theorem 15 is originally shown by reduction to least common ancestor (LCA) in the suffix tree. To avoid computing the suffix tree, one can alternatively go through suffix array, longest common prefix (LCP) array, and range minimum query (RMQ). See \[6\] for a simple proof of optimal LCA and RMQ data structures.

Theorem 15 yields a surprisingly fast check for _d_-near-twinness in graphs.

**Theorem 16.** _There is an_ O(_n_<sup>2</sup>)_-time algorithm that, given an n-vertex graph G, builds a data structure that given a query_ \(u,v\in V(G),d\in\mathbb{N}\) _reports if_ \(sd_G(u,v)\le d\) _in_ O(_d_) _time._

_Proof._ We build a binary word _w_ of length _n_<sup>2</sup> by concatenating the adjacency vectors of all vertices. Formally, assuming _V(G_)=\[_n_\], for every \(a,b\in[n]\), _w_\[(_a_-1)_n+b_\]=1 if \(ab\in E(G)\) and _w_\[(_a_-1)_n+b_\]=0 otherwise. The word _w_ can easily be built in O(_n_<sup>2</sup>) time.

By Theorem 15, we build, in O(_n_<sup>2</sup>) time, a data structure D_<sub>w</sub>_ that answers each LCE query on _w_ in constant time. Given a query \(u,v\in V(G),d\in\mathbb{N}\), we proceed as follows. We initialize \(p\leftarrow 1\) and \(q\leftarrow d\).

While \(p\le n\) and \(q\ge 0\), we feed D_<sub>w</sub>_ with the query (_u_-1)_n+p,(v_-1)_n+p_. (Note that, for _p_=1, those are the positions where the adjacency vectors of _u_ and _v_, respectively, start.) Let _k_ be the query answer, found in constant time. If \(p+k\le n\), we decrement _q_ by 1 and set \(p\leftarrow p+k+1\), else we exit the while loop.

When we exit the while loop, if \(q\ge 0\), we report that \(sd_G(u,v)\le d\), and otherwise (_q_=-1) that sd_<sub>G</sub>(u,v)\>d_.

**Time.** We have already checked that D_<sub>w</sub>_ is built in O(_n_<sup>2</sup>) time. Note that each query _u,v,d_ makes at most _d_+1 LCE queries. Indeed, in the end of the while loop, we decrement _q_ (initially set to _d_) by 1 or we exit the loop, whereas continuing looping requires that _q_ is nonnegative. Hence a query is met in time (_d_+1)O(1)+O(1)=O(_d_).

**Correctness.** Let 1_,p_<sub>1</sub>_,...,p<sub>h</sub>_ be the successive values _p_ is set to. In particular, \(h\le d\). The following properties hold:

• \(1<p_1<\dots<p_h\le n+1\);<tbc>

• for every \(i\in[h]\), \(w[(u-1)n+p_i-1]\neq w[(v-1)n+p_i-1]\);<tbc>

• for every \(j\in[p_h-1]\), if \(w[(u-1)n+j]\neq w[(v-1)n+j]\) then there exists \(i\in[h]\) such that _j=p<sub>i</sub>_-1.

The main invariant is that there are exactly _i_ vertices with label smaller than _p<sub>i</sub>_ adjacent to exactly one of _u,v_. As we check both if more than _d_ such positions where found (\(q\le 0\)) and if the current position overflows to the next adjacency vectors (\(p\le n\)), we correctly decide whether or not \(sd_G(u,v)\le d\) holds when exiting the while loop.

In particular, we can list _all_ pairs of _d_-near-twins in quadratic time, when _d_ is constant.

**Corollary 17.** _There is an_ O(_dn_<sup>2</sup>)_-time algorithm that, given an n-vertex graph and a positive integer d, lists all the pairs of vertices_ \(u,v\in V(G)\) _such that_ \(sd_G(u,v)\le d\).

_Proof._ We compute in O(_n_<sup>2</sup>) time the data structure D of Theorem 16. For every \(u,v\in V(G)\) with \(u\neq v\), we present D with the query _u,v,d_. If the answer is positive (\(sd_G(u,v)\le d\)), we add _u,v_ to the output pairs. Overall, this takes O(_dn_<sup>2</sup>) time.

We obtain the objective of this section by repeatedly appling Corollary 17.

