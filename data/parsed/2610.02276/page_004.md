in theorem 1.2. The literature search was broad but not exhaustive, so throughout we retain the assessment _plausibly new with bounded uncertainty_ rather than a priority claim.

## 4 The exact obstruction on trees

We first record a simple counting fact. Let _m(H_)=|M(_H_)|, with \(m(\varnothing)=1\).

**Lemma 4.1.** _For every finite graph H and vertex z,_

\(m(H)\le 2m(H-z).\)

_Proof._ Split M(_H_) according to whether _z_ is present. Maximal independent sets excluding _z_ are maximal in _H-z_, so there are at most _m(H-z_) of them. Those containing _z_, after deleting _z_, are in bijection with M(_H-N_\[_z_\]).

It remains to show \(m(H-N[z])\le m(H-z)\). For each \(J\in\mathcal{M}(H-N[z])\), choose a maximal independent extension \(\widehat{J}\) in _H-z_. This map is injective: maximality of _J_ in _H-N_\[_z_\] forces

\(\widehat{J}\cap V(H-N[z])=J.\)

Thus \(m(H-N[z])\le m(H-z)\) and the claim follows.

The tree geometry is equally elementary.

**Lemma 4.2** (Diameter-end structure)**.** _Let T have diameter at least_ 3 _and let_ \(v_0v_1\cdots v_d\) _be a diameter path. Put y=v_<sub>1</sub> _and z=v_<sub>2</sub>_. Every neighbour of y other than z is a leaf. Hence y has_ \(r\ge 1\) _leaf neighbours and exactly one nonleaf neighbour z._

_Proof._ The endpoint _v_<sub>0</sub> is a leaf. If a neighbour \(w\neq z\) of _y_ were nonleaf, the component beyond _w_ would contain a leaf _a_ with \(\mathrm{dist}(a,y)\ge 2\). The path from _a_ through _y,z,...,v<sub>d</sub>_ would then have length at least _d_+1, contradicting maximality of the diameter.

Let _L_ be the set of leaf neighbours of _y_, with _r_=|_L_|. Delete \(L\cup\{y\}\) and let _R_ be the remaining component containing _z_; put _F=R-z=T-N_\[_y_\]. The maximal independent sets containing _y_ are precisely<tbc>

\(\{y\}\cup A,A\in\mathcal{M}(F),\)

<tbc>so there are _m(F_). The maximal independent sets excluding _y_ must contain every leaf in _L_ and are precisely

\(L\cup B,B\in\mathcal{M}(R),\)

so there are _m(R_).

**Lemma 4.3** (Two or more pendant leaves)**.** _If_ \(r\ge 2\)_, then the greedy law on T is not uniform on_ M(_T)._

_Proof._ If _y_ is greedily selected, it must precede every leaf in _L_, since any earlier leaf is accepted immediately and blocks _y_. Hence

\(\mathbb{P}_\mathsf{G}(y\mathrm{selected})\le\frac{1}{r+1}.\)

When the nonleaf neighbour _z_ is present, the inequality is strict: among the orders in which _y_ is earliest in \(L\cup\{y\}\) are orders beginning _z,y_, but _z_ is then accepted first and blocks _y_.

Under the uniform law on maximal independent sets,<tbc>

\(\mathbb{P}_\mathsf{U}(y\in I)=\frac{m(F)}{m(F)+m(R)}.\)

