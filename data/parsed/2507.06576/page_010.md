_2. For all_ \(1\le k\le w\)_, we have_ \(rad_{F_i}(r)\le k-1\) _with probability_ \(\frac{k}{w}\)_. More precisely,_

\(\sum_{F_i:rad_{F_i}(r)\le k-1}y_{F_i}=\sum_{i=0}^{k-1}y_{F_i}=\frac{k}{w}\ge 1-\frac{2}{2w}(w-k)=1-\frac{\alpha_{\mathcal{M}(\text{\textit{TREE}})}}{2w}(w-k).\)

This observation shows that the _SDD(T,_2_w,_1_/w_) established in Theorem 3 not only meets the basic edge condition of equation (5), but also enjoys additional structural properties. These strengthened features are captured in the following Corollary 1. In the next Section 5, we will extend this idea and show that a similar phenomenon holds for families of graphs closed under the 1-sum operation, a property that the family of trees also satisfies.

**Corollary 1.** _Let T be a tree, and let_ \(r\in V(T)\) _be an arbitrary root. For the family_ F<sub>2_w_</sub>(_T_) _of all_ 2_w-diameter decompositions, there exists an SDD(T,_2_w,_1_/w), i.e., a distribution_ \(\mathcal{D}=\{y_F\}_{F\in\mathcal{F}_{2w}(T)}\)_, with the following additional properties:_

\(\sum_{F:rad_F(r)\le w-1}y_F=1,\)<br>
\(\sum_{F:rad_F(r)\le k-1}y_F\ge 1-\frac{\alpha_{\mathcal{M}(\text{\textit{TREE}})}}{2w}(w-k)\forall k=1,\dots,w.\)

## 5 A Structural Result for Small Diameter Decompositions

We now define the 1-sum operation on graphs, which will play a crucial role going forward.

**Definition 4.** _Let G_<sub>1</sub>_,...,G<sub>l</sub> be non-empty graphs, and let_ \(r_i\in V(G_i)\) _for i_=1_,...,l. The graph G<sup>S</sup> is obtained by taking the disjoint union of G_<sub>1</sub>_,G_<sub>2</sub>_,...,G<sub>l</sub>, and identifying the vertices r_<sub>1</sub>_,r_<sub>2</sub>_,...,r<sub>l</sub>. We say that G<sup>S</sup> is obtained by performing the_ 1-sum _of the G<sub>i</sub>’s at the vertices r<sub>i</sub>’s. The vertex_ \(r=r_1=\cdots=r_l\) _is called the main vertex of G<sup>S</sup>. See the following figure 2 for an illustration:_

Let G be a family of graphs. We say that G is closed under the 1-sum operation if for any \(G_1,\dots,G_l\in\mathcal{G}\) and \(r_i\in G_i\), the graph obtained by taking 1-sum of _G_<sub>1</sub>_,...,G<sub>l</sub>_ at _r_<sub>1</sub>_,r_<sub>2</sub>_,...,r<sub>l</sub>_ is a graph in G. Many natural classes of family are closed under the 1-sum operation, such as trees, cactus graphs and planar graphs. Note that 1-sum is a special case of a well known and a more general notion of clique-sums.<br>
In the remainder of this section, let \(w\in\mathbb{N}\) and 0_\<p\<_1 be fixed parameters, and assume that the graph family G is closed under minors, subdivisions, and the 1-sum operation, and is _SDD_(2_w,p_)-acceptable. Note that the existence of an _SDD(G,_2_w,p_) implies that one can sample a 2_w_-diameter decomposition of _G_ in which each edge is included with probability at most _p_.

We note down a few more definitions before stating the main theorems of this section. Let _G_ be a graph and \(r\in V(G)\) be an arbitrary vertex. Recall that F<sub>2_w_</sub>(_G_) denotes the set of all 2_w_-diameter decompositions of _G_. For \(k\in\{1,\dots,w\}\), we use \(\mathcal{F}_{2w}^k(G,r)\) to denote<tbc>

r1
r2
rk
r = r1, , , ,
G1
G2
G1
G2
Gl
Gl
G2

Figure 2: An illustration of the 1-sum operation

