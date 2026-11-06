## 5. Fixed-parameter recognition

The composition laws in Section 4 retain exactly the local information needed for repair, but those data can be large. We now address computation on arbitrary graphs. Small weak villainy forces a small vertex cover in the graph or its complement, so the relevant colorings can be described by boundedly many vertex types.

The classifications of graphs with _B(G_)=0 in \[2\] and with _B(G_)=2 in \[12\] give polynomial- time recognition algorithms for those two classes. We prove the stronger conclusion that recognition is fixed-parameter tractable in the threshold, for both repair rules.

**Theorem 5.1** (Exact computation and recognition)**.** _There are computable functions f,h and an absolute constant c such that both B(G_) _and B_<sub>w</sub>(_G_) _can be computed exactly on an n-vertex graph in time_<tbc>

\(h(B_\mathrm{w}(G))(n+1)^c,\)

<tbc>_without either value being supplied. Moreover, given an integer_ \(t\ge 0\)_, both_

\(\mathrm{min}\{B(G),t+1\}\text{\textit{and}}\mathrm{min}\{B_\mathrm{w}(G),t+1\}\)

_can be computed in time f(t_)(_n_+1)_<sup>c</sup>. Consequently, equality and threshold recognition for either parameter are fixed-parameter tractable in t, and belong to_ P _for every fixed t._

The exponent _c_ is independent of the threshold. The proof first forces a small vertex cover in the graph or its complement, and then uses different descriptions of repair in the two cases. The small-cover case uses effective quantifier elimination; no practical bound on _f_ is asserted. Throughout this section, \(\nu(H)\) denotes the matching number of a graph _H_.

### 5.1. A structural consequence of a matching bound.

For an optimal coloring profile **m**=(_m_<sub>1</sub>_,...,m<sub>k</sub>_), where \(k=\chi(G)\), put

\(p(\mathbf{m})=\sum_{i=1}^k\left\lfloor\frac{m_i}{2}\right\rfloor.\)

This is the number of disjoint pairs of equal-colored tokens available in a word of profile **m**. The next lemma extends the matching argument of Jahanbekam and Lin \[12, Lemma 8\].

**Lemma 5.2.** _For every optimal coloring profile_ **m** _of G,_

\(B(G)\ge B_\mathrm{w}(G)\ge\mathrm{min}\{p(\mathbf{m}),\nu(G)\}.\)

_Proof._ Let \(q=\mathrm{min}\{p(\mathbf{m}),\nu(G)\}\). Choose _q_ edges of a matching and _q_ disjoint pairs of equal- colored tokens. Place each pair at the ends of one chosen edge and distribute the remaining tokens arbitrarily. The resulting word has profile **m**. Every proper coloring differs from it at an endpoint of each of the _q_ selected edges. The edges are disjoint, so these discrepancies occur at distinct vertices. This argument does not require the repaired coloring to have profile **m**, and therefore proves the bound for _B_<sub>w</sub>(_G_). □

The matching bound forces a graph of small weak villainy to have either a small vertex cover or very many colors. In the latter case, the complement has a small vertex cover instead.

**Corollary 5.3.** _If_ \(B_\mathrm{w}(G)\le t\)_, then_

\(\nu(G)\le t\text{\textit{or}}\chi(G)\ge n-2t.\)

_In the first case G has a vertex cover of size at most_ 2_t. In the second case_ \(\nu(\overline{G})\le 2t\)_, and <o>G</o> has a vertex cover of size at most_ 4_t. The same conclusions hold if_ \(B(G)\le t\).

_Proof._ Fix an optimal profile **m**. Since every _m<sub>i</sub>_ is positive,

\(n-\chi(G)=\sum_i(m_i-1)\le 2\sum_i\left\lfloor\frac{m_i}{2}\right\rfloor=2p(\mathbf{m}).\)

If \(\nu(G)>t\), Theorem 5.2 forces \(p(\mathbf{m})\le t\), and hence \(\chi(G)\ge n-2t\).

