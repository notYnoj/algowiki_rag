## Vertex Set.

Fix \(\ell=r^c\). The vertex set _V_ is partitioned into a collection of \(k\ell+1\) disjoint layers \(\{L_i\}_{i\in[0,k\ell]}\). We will frequently use _L<sub>i,j</sub>_ to denote layer _L_<sub>_i:k+j_</sub>, so for example _L<sub>i,k</sub>_ is another name for _L_<sub>_i_+1,0</sub>.

The vertices of _L<sub>i,j</sub>_ are identified with tuples ((_i,j),(p_<sub>0</sub>_,...,p_<sub>_k_-1</sub>)), where each point \(p_0,\dots,p_{k-1}\in\mathbb{Z}^d\) is contained in the rectangle \((-(r+1)r\ell,(r+1)r\ell]^d\). Let \(N=|L_{i,j}|=(2(r+1)r\ell)^{kd}\), so the total number of vertices is \((k\ell+1)N\).

## Critical Subdirections.

Recall that \(B(r,d)=\{\vec{v}\in\mathbb{Z}^d|\|\vec{v}\|\le r\}\) is the radius-_r_ ball in dimension _d_ and \(\mathcal{B}(r,d)\subseteq B(r,d)\) is the set of extreme points of the convex hull of _B(r,d_). Each vector in B(_r,d_) defines a _critical subdirection_ and by \[BL98\] the number of critical subdirections is \(\Delta=|\mathcal{B}(r,d)|=\Theta\left(r^{d,\frac{d-1}{d+1}}\right)\).

## Edge Set.

The edge set _E_ consists of all \((x,y)\in V\times V\) where

\(x=((i,j),(p_0,\dots,p_j,\dots,p_{k-1}))\in L_{i,j},\)<br>
\(y=((i,j+1),(p_0,\dots,p_j+\vec{v},\dots,p_{k-1}))\in L_{i,j+1},\)<br>
\(\text{and}\vec{v}\in\mathcal{B}(r,d).\)

Naturally (_i,j_+1) would be interpreted as (_i_+1,0) when _j_+1=_k_. In this way each vertex has out-degree at most \(\Delta\).

## Critical Directions, Critical Pairs, and Critical Paths.

A _critical direction_ is a _k_-tuple \((\vec{v}_0,\dots,\vec{v}_{k-1})\in(\mathcal{B}(r,d))^k\) of critical subdirections, so there are clearly \(\Delta^k\) critical directions. Define \(S\subset L_{0,0}\) to be a rectangle around the origin.

\(S=\{((0,0),(p_0,\dots,p_{k-1}))\in L_{0,0}|p_i\in(-r^2\ell,r^2\ell]^d\text{for each}i\in[0,k)\}.\)

For each vertex \(s=((0,0),(p_0,\dots,p_{k-1}))\in S\) and a critical direction \((\vec{v}_0,\dots,\vec{v}_{k-1})\in(\mathcal{B}(r,d))^k\), let _t_ be the vertex \(t=((\ell,0),(p_0+\ell\vec{v}_0,\dots,p_{k-1}+\ell\vec{v}_{k-1}))\in L_{\ell,0}\). We call (_s,t_) a _critical vertex pair_; let \(P\subseteq S\times L_{\ell,0}\) denote the set of all critical vertex pairs in _G_.

**Lemma 2.5** (Cf. \[Hes03\])**.** _Let_ \(G\in\mathcal{G}_k\) _with critical pair set P._

• \(|P|=\frac{N\Delta^kr^{dk}}{(r+1)^{dk}}\) .<tbc>

• _Every critical pair_ \((s,t)\in P\) _has a unique s-t path P<sub>s,t</sub> in G, called its_ critical path.<tbc>

• _If two critical paths intersect at_ \(u\in L_i\) _and_ \(v\in L_{i^\prime}\) _then_ \(i'<i+k\).

Lemma 2.5 has a similar geometric interpretation as Lemma 2.4. The main difference is that the division into subdirections allows for two critical paths to have small overlap, but they still cannot overlap in two layers at distance _k_, which implies the third property. See Section D.1 for formal proof.

**Definition 2.6** (Summary of Parameters)**.** Let us summarize the relevant parameters of graph \(G\in\mathcal{G}_k\) with size parameter _r_.

• _G_ has \(k\ell+1=kr^c+1\) layers in total, each with \(N=(2(r+1)r\ell)^{kd}\) vertices, hence \(|V|=O(k\ell N)=O(k\ell(2(r+1)r\ell)^{kd})\).<tbc>

