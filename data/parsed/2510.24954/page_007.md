**Theorem 2.2.** _Let_ \(k\ge 2\) _be an integer, and let_ \(G=(V,E)\in\mathcal{G}_k\) _be an n-vertex, n_<sup>1+_O_(1_/k_)</sup>_-edge graph with associated critical vertex pairs_ \(P\subseteq V\times V\)_. Then G admits a k-thick Steiner shortcut graph_ \(G_+=(V\cup V_+,E\cup E_+)\) _with_ \(|E_+|=|E|/n^{\Omega(1/k)}\)_, such that every_ \((s,t)\in P\) _has_ dist<sub>_G_<sub>+</sub></sub>(_s,t_)=_k._

_Remark_ 2.3. All existing lower-bound constructions for (non-Steiner) shortcut sets have the same high-level structure: they tailor the construction to produce a set of critical vertex pairs _P_, and then show that these particular pairs are hard to shortcut. The constructions make no claims about other vertex pairs. For this reason, to show that these lower-bound proofs fail in our new setting, it is enough to show that the critical pairs in particular can be shortcut using Steiner vertices. We strongly believe that for all these constructions one can in fact use Steiner vertices to shortcut _all_ pairs in the graph, but we did not think this would be instructive, since by design only the critical pairs have interesting structure.

In Section 3 we show that Theorem 2.2 is essentially tight for the family G_<sub>k</sub>_, in that any _t_-thick Steiner shortcut set with \(t\checkmark k\) must have size superlinear in _m_ or diameter polynomial in _m_. Before reviewing Hesse’s construction of G_<sub>k</sub>_ we begin with G<sub>1</sub>, which introduces some of the key ideas and is sufficient to prove lower bounds on \(\tilde{O}(n)\)-size shortcuts; see Huang and Pettie \[HP21\].

## 2.1 Warm-up Construction -- Graph Family G<sub>1</sub>

We construct a graph family G<sub>1</sub> that does not quite imply polynomial diameter lower bounds for \(\tilde{O}(m)\)-size shortcut sets. This will motivate some of the design choices introduced in the graph family G_<sub>k</sub>_ in Section 2.2.

Graph family G<sub>1</sub> is parameterized by constants \(c\in\mathbb{R}^+\) and \(d\in\mathbb{N}^+\). We denote a specific parameterization of G<sub>1</sub> by G<sub>1</sub>(_c,d_). The size of each graph \(G=(V,E)\in\mathcal{G}_1(c,d)\) is controlled by a parameter \(r\in\mathbb{N}^+\).

### Vertex Set _V_ .

Let \(\ell=r^c\). Graph _G_ has \(\ell+1\) layers, \(L_0,L_1,\dots,L_\ell\). The vertices of each layer can be written as a collection of points in a _d_-dimensional grid. Formally, for \(i\in[0,\ell]\), we define _L<sub>i</sub>_ to be

\(L_i=\{i\}\times(-r(r+1)\ell,r(r+1)\ell]^d,\)

and let \(V=\cup_{i=0}^\ell L_i\).

### Edge Set _E_ .

Let \(B(r,d)\subseteq\mathbb{Z}^d\) denote the set of all integer vectors \(\vec{v}\) in Z_<sup>d</sup>_ of magnitude \(\|\vec{v}\|\le r\), where \(\|\cdot\|\) denotes the standard Euclidean norm. Let \(\mathcal{B}(r,d)\subseteq B(r,d)\) denote the set of extreme points of the convex hull of _B(r,d_). By Bárány and Larman \[BL98\], \(|\mathcal{B}(r,d)|=\Theta\left(r^{d\cdot\frac{d-1}{d+1}}\right)\). The edge set _E_ of _G_ consists of all \((x,y)\in V\times V\) where

\(x=(i,p)\in L_i,\)<br>
\(y=(i+1,p+\vec{v})\in L_{i+1},\)<br>
\(\text{and}\vec{v}\in\mathcal{B}(r,d).\)

### Critical Pairs and Critical Paths.

We will define a collection of vertex pairs and associated paths in _G_ that are particularly useful in the analysis of _G_. We first specify a set of source nodes \(S\subseteq L_0\) in the first layer of _G_ that will be useful for defining our set of critical vertex pairs. Let _S_ be the set

\(S=\{0\}\times(-r^2\ell,r^2\ell]^d.\)

For each vertex \(s=(0,p)\in S\) and a vector \(\vec{v}\in\mathcal{B}(r,d)\), let _t_ be the vertex \(t=(\ell,p+\ell\vec{v})\). Note that _t_ is guaranteed to lie in \(L_\ell\) due to \(p\in(-r^2\ell,r^2\ell]^d\) and \(\|\vec{v}\|\le r\). We call (_s,t_) a _critical vertex pair_;<tbc>

