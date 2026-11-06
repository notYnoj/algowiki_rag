## 4. Rotations in _k_-cut trees

As discussed in §1, an essential feature of the classical BST model is that the rotation- distance between two trees of size _n_ is O(_n_).<sup>2</sup> In particular, if we only do rotations on the search path, as in most natural algorithms, then the cost of rotations can be charged to the cost of searching, i.e. of simply traversing the search path. In STTs the situation is different, as there are pairs of trees of size _n_ that are \(\Omega(nlogn)\) rotations apart \[CLP18\]. Nonetheless, for _k_-cut STTs we show the following.

**Theorem 2.** _Given two k-cut search trees T and_ \(T'\) _on the same n-node tree S, we can transform T into_ \(T'\) _through a sequence of at most_ (2_k_-1)_n_-(_k_+1)_k_+1 _rotations. Moreover, starting with a pointer at the root, we can transform T into_ \(T'\) _through a sequence of_ O(_k_<sup>2</sup>_n_) _pointer moves and rotations at the pointer. All intermediate trees are k-cut trees._

In our study of adaptive STTs (i.e. our generalized Splay) in §5 and §6 we will only make use of the case _k_=2, Theorem 2 is thus more general than strictly necessary for our immediate purposes. STTs are in bijection with vertices of _tree associahedra_, whose edges correspond to rotations. In terms of this structure, Theorem 2 can be interpreted as follows. While the skeleton of a tree associahedron (for a tree of size _n_) can have diameter \(\Omega(nlogn)\), its vertices corresponding to _k_-cut STTs induce a connected subgraph of diameter _O(kn_).

Before proceeding with the proof, we make an observation that will be useful later.

**Observation 7.** _Let T be an STT, and let_ \(T'\) _be the STT that we obtain by rotating at node q with parent p. Then, for each_ \(x\in V(T)\backslash\{p,q\}\)_, we have_ \(V(T'_x)=V(T_x)\) _and thus_ \(|\delta(T'_x)|=|\delta(T_x)|\).

In particular, if _T_ is a _k_-cut STT, then we only have to consider the boundary \(\delta(T'_p)\) to see if \(T'\) is still a _k_-cut STT, since \(|\delta(T'_q)|=|\delta(T_p)|\le k\).

We prove Theorem 2 by induction. For _k_=1, we directly rotate _T_ into \(T'\). For _k\>_1, we reduce _k_ by rotating both _T_ and \(T'\) into (_k_-1)-cut trees. By reversing the rotation sequence that we used to transform \(T'\), we obtain a sequence of rotations from _T_ to \(T'\).

We first focus on the number of rotations and ignore the number of pointer moves needed; in §4.1 we present a refined algorithm. The following lemma concerns the case _k_=1. Recall that 1-cut trees are precisely those that can be obtained by rooting _S_ at some node _r_. Let _S<sup>r</sup>_ denote this rooted tree.

**Lemma 8.** _There is a sequence of at most n_-1 _rotations that transforms S_<sup>_r_<sub>1</sub></sup> _into S_<sup>_r_<sub>2</sub></sup>_, for arbitrary nodes_ \(r_1,r_2\in V(S)\)_. All intermediate trees are_ 1_-cut trees._

_Proof._ Let _P_=(_x_<sub>1</sub>_,...,x<sub>t</sub>_) be the search path of _r_<sub>2</sub> in _S_<sup>_r_<sub>1</sub></sup>, with _x_<sub>1</sub>=_r_<sub>1</sub> and _x<sub>t</sub>=r_<sub>2</sub>. We rotate at the nodes _x_<sub>2</sub>_,...,x<sub>t</sub>_ (in this order).

As \(t\le n\), we clearly make at most _n_-1 rotations. We show inductively that after rotating at _x<sub>i</sub>_, for all _i_=2_,...,t_, the obtained tree is _S<sup>x<sub>i</sub></sup>_. The claim follows, as the last rotation is at _x<sub>t</sub>=r_<sub>2</sub>.

<sup>2</sup>The number of rotations needed to transform one _n_-node BST into another is at most 2_n_-6 and there are pairs of trees requiring this many rotations for all _n\>_10 \[STT88, Pou12\]. As BSTs are trivially Steiner-closed (i.e. 2-cut), a similar lower bound also holds for Steiner-closed STTs.

