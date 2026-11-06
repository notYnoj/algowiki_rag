The third result will be used to compute balanced cycle separators. Therein, a fundamental cycle of an edge _e_ with respect to a spanning tree _T_ (which does not contain _e_) is the unique simple cycle that contains _e_ and all its other edges are contained in _T_.

**Lemma 3** (\[KM\], Lemma 5.3.2.)**.** _There is a linear-time algorithm that, given a triangulated plane graph G, a spanning tree T of G, and a proper weight assignment, returns a nontree edge e such that the fundamental cycle of e with respect to T is a <sup>3/4</sup>-balanced cycle separator for G._

We use this lemma in the following way.

**Corollary 1.** _Given a d-outerplanar triangulated graph G and a proper weight assignment, one can compute in_ O(_n_<sup>2</sup>) _time a <sup>3/4</sup>-balanced cycle separator of size at most_ 2_d_+1 _for G._

_Proof._ First, compute in O(_n_<sup>2</sup>) time a _d_-outerplanar embedding of _G_ \[Kam07\]. Let _L(v_) be the layer of _v_, that is, the vertices on the outer face have _L(v_)=0 and when removing all vertices with _L(v)\<i_ for some \(i\in[d-1]\), the vertices on the new outer face receive _L(v_)=_i_. Since _G_ is triangulated, the outer face is a triangle. Build a spanning tree _T_ for _G_ in O(_n_) time as follows. Start with any two edges on the outer face and then iteratively for increasing \(i\in[d-1]\) and each vertex _v_ with _L(v_)=_i_ add an edge between _v_ and a vertex _u_ with _L(u_)=_i_-1 to _T_. Note that such an edge exists as _G_ is triangulated. Now apply Lemma 3 to compute in O(_n_) time an edge _e_ not contained in _T_ such that the fundamental cycle of _e_ with respect to _T_ is a <sup>3/4</sup>-balanced cycle separator for _G_. Note that the fundamental cycle of _e_ can be computed in O(_n_) time and it contains at most two vertices of each layer (except for the outermost, where it can contain three) and therefore at most 2_d_+1 vertices in total.

Next, we use a result that bounds the treewidth of _k_-outerplanar graphs.

**Lemma 4** (\[Bod98\])**.** _Each k-outerplanar graph has treewidth at most_ 3_k_-1.

We use this in combination with a linear-time algorithm to compute an approximate tree decomposition in the case where the treewidth is a constant and a result to transform a tree decomposition into a binary tree decomposition of logarithmic depth without increasing the width too much.

**Theorem 2** (\[Kor21\])**.** _There is an algorithm that, given an n-vertex graph G and an integer k, in_ 2<sup>O(_k_)</sup>_n time either outputs a tree decomposition of G of width at most_ 2_k_+1 _or determines that the treewidth of G is larger than k._

**Lemma 5** (\[BH98\])**.** _There is an algorithm that, given an n-vertex graph G and a tree decomposition of width k, computes a binary tree decomposition of G of width at most_ 3_k_+2 _and depth_ O(log(_n_)) _in_ 2<sup>O(_k_)</sup>_n time._

The main ingredient of our subexponential parameterized algorithm is a lemma due to Nederlof \[Ned20\]. He mentions the lemma without formal statement or proof and he does not analyze the constants involved in the running time. However, the proof follows directly from the proof of his Lemma 3.7 and we will give a proof sketch for analyzing the running time.

**Lemma 6.** _There is an_ 2<sup>O(log<sup>2</sup>(_k_))</sup>_n_<sup>1+_o_(1)</sup>_-time algorithm that_

• _given a triangulated graph G_=(_V,E_) _and a cycle separator C on at most k vertices that is q-balanced for a (possibly unknown) proper weight assignment w,_<tbc>

