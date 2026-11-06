\(\blacktriangleright\) **Definition 3** (Parity-consistency _x∼_<sub>par</sub>_y)**.** _Two connected nodes x and y are parity- consistent if_

\(d_G(x,y)\equiv\phi(x)-\phi(y)(mod2).\)

_We denote that x and y are parity consistent as x∼_<sub>par</sub>y._

\(\blacktriangleright\) **Definition 4** (Potential-separation, \(x\unknown y\))**.** _Two connected nodes x and y are potential- separated if_

\(d_G(x,y)\ge|\phi(x)-\phi(y)|.\)

_We denote that x is potential-separated from y as_ \(x\unknown y\).

\(\blacktriangleright\) **Theorem 5** (Coloring from ∼<sub>par</sub> and \(\unknown\unknown\))**.** _If for all connected nodes x and y we have_ \(x\unknown y\) _and x∼_<sub>par</sub>y _for some graph G and potential function_ \(\phi\)_, then_ \(c(v)=mod(\phi(v),3)\) _is a proper 3-coloring of G._

**Proof.** Assume for contradiction that two neighboring nodes _x,y_ in _G_ have _c(x_)=_c(y_), then the definition of the coloring _c_ requires

\(\phi(x)-\phi(y)=3k.\)

The assumption _x∼_<sub>par</sub>y_ gives

\(\phi(x)-\phi(y)\equiv d_G(x,y)(mod2)\)<br> \(\Longrightarrow 3k\equiv 1(mod2)\)<br> \(\Longrightarrow k\neq 0.\)

We know from \(x\unknown y\) that

\(d_G(x,y)\ge|\phi(x)-\phi(y)|=|3k|\ge 3,\)

contradicting the assumption that _x_ and _y_ are neighbors. \(\blacktriangleleft\)

It is helpful to establish further properties of parity-consistency and potential-separation. The relations _x∼_<sub>par</sub>y and \(x\unknown y\) are clearly reflexive and symmetric. In the following we prove transitivity properties of these relations. We will make use of transitivity later to extend statements about pairs of nodes to an entire component.

\(\blacktriangleright\) **Lemma 6** (Transitivity of ∼<sub>par</sub>)**.** _If the graph G is bipartite, then parity-consistency is transitive, i.e.,_

\(x\sim_\mathrm{par}y\wedge y\sim_\mathrm{par}z\Longrightarrow x\sim_\mathrm{par}z.\)

**Proof.** We must have

\(d_G(x,z)\equiv d_G(x,y)+d_G(y,z)(mod2),\)

otherwise there would exist an odd-length closed walk passing through the vertices _x_, _y_, _z_, back to _x_, contradicting the assumption that _G_ is bipartite. Thus,

\(d_G(x,z)\equiv d_G(x,y)+d_G(y,z)(mod2)\)<br> \(\equiv(\phi(x)-\phi(y))+(\phi(y)-\phi(z))(mod2)\)<br> \(\equiv\phi(x)-\phi(z)(mod2)\)

as required. \(\blacktriangleleft\)

