**Diagonals:** A _diagonal_ is a set of the form \(\mathcal{D}_d=\{(i,j)\in[n/m]^2|i-j=d\}\). Each diagonal is a block sequence, so we have \(\sum_{(i,j)\in\mathcal{D}_d}M_{ij}\le\mu\). Note that there are \(2n/m-1<2\sqrt{T}\) (non-empty) diagonals. Moreover, we have \(\sum_d\sum_{(i,j)\in\mathcal{D}_d}M_{ij}=M\). This yields the inequality

\(M<2\mu\sqrt{T}.\) (3)

## 5.3 Algorithm 2: Large _L_, Large \(\mu\)

In this section we present Algorithm 2, which works well if \(\mu\) is large, i.e., if some block sequence has a large total number of matching pairs. The algorithm makes use of the single symbol approximation that we designed in Lemma 8. This yields estimates \(0\le\widetilde{L}_{ij}\le L_{ij}\), over which we then perform dynamic programming to determine the maximum of \(\sum_{(i,j)\in\mathcal{S}}\widetilde{L}_{ij}\) over all block sequences S. (This is similar to \[24, Algorithm 3\], but we obtain concentration in a wider regime, see Remark 14 for a comparison.)

**Theorem 13** (Algorithm 2)**.** _We can compute in expected time_ \(\widetilde{O}(T)\) _an estimate_ \(\widetilde{L}\le L\) _that w.h.p. satisfies_

\(\widetilde{L}=\Omega\big(\frac{\mu\sqrt{T}}{n}\big).\)

_Proof._ Algorithm 2 works as follows.

1. Run Lemma 8 with \(q:=\frac{M}{4T}\) to compute values \(\widetilde{L}_{ij}\).<tbc>

2. Perform dynamic programming over \[_n/m_\]<sup>2</sup> to determine the maximum \(\sum_{(i,j)\in\mathcal{S}}\widetilde{L}_{ij}\) over all block sequences S. Output this maximum value \(\widetilde{L}\). More precisely:<tbc>

• Initialize _D_\[_i,_0\]=_D_\[0_,i_\]=0 for any \(0\le i\le n/m\).<tbc>

• For _i_=1_,...,n/m_ and _j_=1_,...,n/m_: _D_\[_i,j_\]=max\(\big\{\widetilde{L}_{ij}+D[i-1,j-1],D[i-1,j],D[i,j-1]\big\}\).<tbc>

• Output _D_\[_n/m,n/m_\].

We analyze this algorithm in the following.

**Upper Bound:** Since Lemma 8 ensures \(\widetilde{L}_{ij}\le L_{ij}\), the dynamic programming step ensures \(\widetilde{L}\le L\).

**Approximation Guarantee:** Let S be a block sequence achieving \(\sum_{(i,j)\in\mathcal{S}}M_{ij}=\mu\). Step 2 computes an estimate \(\widetilde{L}\ge\sum_{(i,j)\in\mathcal{S}}\widetilde{L}_{ij}\), and Lemma 8 yields w.h.p.<tbc>

\(\widetilde{L}\ge\sum_{(i,j)\in\mathcal{S}}\widetilde{L}_{ij}\ge\sum_{(i,j)\in\mathcal{S}}\frac{M_{ij}-q}{16m}=\frac{\mu}{16m}-|\mathcal{S}|\frac{q}{16m}.\)

<tbc>By the monotonicity property of block sequences, we have \(|\mathcal{S}|\le n/m\). Using our definitions of \(q=\frac{M}{4T}\) and \(m=n/\sqrt{T}\) as well as inequality (3), we obtain<tbc>

\(|\mathcal{S}|\frac{q}{16m}\le\frac{qn}{16m^2}=\frac{M}{64n}\le\frac{\mu\sqrt{T}}{32n}.\)

<tbc>Plugging this into our bound for \(\widetilde{L}\) yields<tbc>

\(\widetilde{L}\ge\frac{\mu\sqrt{T}}{16n}-\frac{\mu\sqrt{T}}{32n}=\frac{\mu\sqrt{T}}{32n}.\)

