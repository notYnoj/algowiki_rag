let \(P\subseteq S\times L_\ell\) denote the set of all critical vertex pairs in _G_. Each \((s,t)\in P\) is identified with the _critical path P<sub>s,t</sub>_, defined as follows.

\(P_{s,t}=((0,p),(1,p+\mathaccent\unknown{v}),\dots,(\ell,p+\ell\mathaccent\unknown{v})).\)

Let \(\mathcal{P}=\{P_{s,t}|(s,t)\in P\}\) be the set of critical paths.

We summarize several properties of graph _G_, critical pairs _P_, and critical paths P in the following lemma, which we state without proof.

**Lemma 2.4** (Cf. \[HP21, Lemma 2.2 and 2.6\])**.** _Graph G and paths_ P _have the following properties:_

**Sizes.** \(|V|=\Theta(r^{c+2d+cd})\), \(|E|=\Theta(r^{d\cdot\frac{d-1}{d+1}}\cdot|V|)\)_, and_ \(|P|=|\mathcal{P}|=\Theta(r^{2d+cd+d\cdot\frac{d-1}{d+1}})\).

**Uniqueness.** _Every path_ \(P_{s,t}\in\mathcal{P}\) _is a unique_ (_s,t)-path in G._

**Disjointness.** _Paths in_ P _are pairwise edge-disjoint._

### A remark on the geometry of graph _G_.

Vertex set _V_ and paths P have a very natural geometric interpretation as an arrangement of points and lines in R<sup>_d_+1</sup>. Notice that the vertices of each path \(P_{s,t}\in\mathcal{P}\) lie on a line of the form \(\{x\cdot(1,\mathaccent\unknown{v})+(0,p)|x\in\mathbb{R}\}\) in R<sup>_d_+1</sup> for \(\mathaccent\unknown{v}\in\mathcal{B}(r,d)\) and \((0,p)\in S\). Moreover, because B(_r,d_) consists only of extreme points, each such direction \(\mathaccent\unknown{v}\) _cannot_ be expressed as a convex combination of other vectors in B(_r,d_). This geometric perspective is useful for interpreting the Uniqueness and Disjointness properties of Lemma 2.4.

### Implications and Limitations of G<sub>1</sub>.

Graph class G<sub>1</sub> already gives an interesting lower bound: any _O(n_)-sized shortcut-set of G<sub>1</sub> has diameter at least \(\Omega(\mathrm{poly}(n))\). This follows almost immediately from Lemma 2.4: Since the critical paths are pairwise disjoint, a shortcut edge can only be relevant to a single critical path, so shortcutting every critical pair would require at least |_P_| edges; by the construction of G<sub>1</sub>, we have \(|P|=\Omega(n)\). Unfortunately it is impossible to have \(|P|=\Omega(m)\) in G<sub>1</sub>. In order to force \(|P|\gg m\), Hesse \[Hes03\] defines graph G_<sub>k</sub>_ to be a kind of _k_-fold product of G<sub>1</sub>.

### Optimizing G<sub>1</sub> for Steiner shortcut lower bounds.

Technically, the construction we consider differs slightly from \[Hes03\] and \[HP21\], although the difference is essentially aesthetic for the non-Steiner parts of our discussion. We define \(L_i=\{i\}\times(-r(r+1)\ell,r(r+1)\ell]^d\) as opposed to \(\{i\}\times(-4r\ell,4r\ell]^d\) as in \[Hes03\]. Consequently, we can define _S_, the starting points of our critical paths, as \(\{0\}\times(-r^2\ell,r^2\ell]^d\). _S_ is instead defined as \(\{0\}\times(-2r\ell,2r\ell]^d\) in \[Hes03\]. This means that in Hesse’s construction only a constant fraction of vertices in the starting layer are the first vertex in a critical path; for our modified construction, all but a vanishing fraction of the vertices are. When we prove Theorem 1.3 via Theorem 3.1, this makes the difference between a thickness lower bound of \(o(\sqrt{\mathrm{log}n})\) versus _o_(log_n/_loglog_n_).

## 2.2 Hesse’s G_<sub>k</sub>_ Family

### Construction parameters.

Graph family G_<sub>k</sub>_ is parameterized by constants \(c\in\mathbb{R}^+\) and \(d\in\mathbb{N}^+\). We denote a specific parameterization of G_<sub>k</sub>_ by G_<sub>k</sub>(c,d_). The size of each _G_=(_V,E_) in G_<sub>k</sub>_ is controlled by a parameter \(r\in\mathbb{N}^+\).

