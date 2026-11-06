**Part I:** \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))\) **is small** Using the bound on tree total deviation in Lemma 4.1 we know that,

\(\unknown\mathrm{TD}_{M,S}(W(p))=O\left(w(p)\cdot S^{0.51}+\underbrace{\mathcal{B}_x}_{\mathrm{maxlengthof}p\text{overscale}0\text{interval}}\cdot\underbrace{(n/\mathcal{B}_x)}_{\mathrm{numberofscale}0\text{intervals}}/2^{\mathrm{log}_M^{0.015}(n)}\right)\)<br>
\(=O\left(w(p)\cdot S^{0.51}+n/2^{\mathrm{log}_M^{0.015}(n)}\right).\)

Since each scale is in \(\widetilde{S}\) u.a.r with probability 1_/S_<sup>0.98</sup>, and _p_ does not depend on \(\widetilde{S}\), with probability at least 9/10,

\(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))=O\left(\left(w(p)\cdot S^{0.51}+n/2^{\mathrm{log}_M^{0.015}(n)}\right)/S^{0.98}\right)\)<br>
\(=\left(O\left(\left(w(p)\cdot S^{0.51}\right)+o\left(\frac{w(p)}{M}\right)\right)\right)/S^{0.98}\text{since}w(p)=n/2^{o\left(\mathrm{log}^{0.01}(n)\right)}\)<br>
\(=w(p)/S^{0.47}+o\left(\frac{w(p)}{M}\right)\)<br>
\(=o\left(\frac{w(p)}{M}\right).\text{since}M=\Theta\left(\mathrm{log}^{0.109}(n)\right)\)

**Part II:** \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))\) **is not too different from** \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))\) From Lemma 6.3, with probability at least 19/20. We can round _p_ to an \(\widetilde{S}\)-regular path \(\widehat{p}\) such that there are at most \(o\left(\frac{w(p)}{M\mathrm{log}^{0.02}(n)}\right)\) columns _x_ before which their weights differ. Each of these columns contributes at most \(O(\left|\widetilde{S}\right|)\) to the difference between \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))\) and \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))\). Since the size of \(\widetilde{S}\) is \(O\left(\mathrm{log}^{0.02}(n)\right)\) with probability 1-_o_(1)_\>_19/20, by the union bound, with probability at least 9/10, the difference between \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(p))\) and \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))\) is at most \(o\left(\frac{w(p)}{M}\right)\).

Combining the two parts, with probability at least 4/5, we have \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))=o\left(\frac{w(\widehat{p})}{M}\right)\).

## 6.3.3 Our Estimate Is Sound

We now show that our algorithm is sound. In order to rule out potential overfitting from our algorithm, we will need the following ingredient showing that certain random 0-1 weighted graphs with a few 1 in weights likely does not admit a path from a fixed source that visits too many of these 1’s:

**Claim 6.13.** _Let G be an N-vertex h-layer directed graph with 0-1 edge weights with a source u. Specifically:_

• _Every vertex belongs to a layer in_ \[_h_\];<tbc>

• _For any edge from vertex v to vertex w, v’s layer is equal to w’s layer minus one;_<tbc>

• _Each edge has a weight_ \(\in\{0,1\}\).

_We say an edge is a layer-L edge if it connects a layer-L vertex to a layer_-(_L_+1) _vertex._

_Suppose that for any vertex v on layer L, for any layer_ \(L'<L+B\)_, the number of layer-L_\('\) _edges reachable by v is at most d._

_Suppose that the edge weights satisfy the following:_

