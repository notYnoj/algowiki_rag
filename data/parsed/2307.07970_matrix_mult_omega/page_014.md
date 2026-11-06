## 3.2 Tensor Rank

Given a tensor _T_ over _X,Y,Z_, the tensor rank _R(T_) is defined to be the minimum integer \(r\ge 0\) such that _T_ can be written as

\(T=\sum_{t=1}^r\left(\sum_{i=1}^{|X|}a_{t,i}\cdot x_i\right)\left(\sum_{j=1}^{|Y|}b_{t,j}\cdot y_j\right)\left(\sum_{k=1}^{|Z|}c_{t,k}\cdot z_k\right),\)

where the above sum is called the _rank decomposition_ of _T_.

Given two tensors \(T,T'\), the tensor rank satisfies the following property with respect to tensor operations.

• \(R(T+T')\le R(T)+R(T')\).<tbc>

• \(R(T\oplus T')\le R(T)+R(T')\).<tbc>

• \(R(T\otimes T')\le R(T)\cdot R(T')\).<tbc>

<tbc>The _asymptotic rank_ \(\widetilde{R}(T)\) of _T_ is defined as

\(\widetilde{R}(T):=lim_{n\rightarrow\infty}\big(R(T^{\otimes n})\big)^{1/n}.\)

Due to the third item above and Fekete’s lemma, the asymptotic rank is well-defined and upper bounded by \(R(T^{\otimes m})^{1/m}\) for any fixed integer _m\>_0.

## 3.3 Degenerations, Restrictions, Zero-outs

Let _T_ be a tensor over _X,Y,Z_ and \(T'\) be a tensor over \(X',Y',Z'\). Both _T_ and \(T'\) are tensors over a field F.

### Degeneration.

Let \(\mathbb{F}[\lambda]\) be the ring of polynomials of the formal variable \(\lambda\). We say that \(T'\) is a degeneration of _T_, written as \(T\unknown T'\), if there exists \(\mathbb{F}[\lambda]\)-linear maps

\(\phi_X:\text{span}_{\mathbb{F}[\lambda]}(X)\rightarrow\text{span}_{\mathbb{F}[\lambda]}(X'),\)<br>
\(\phi_Y:\text{span}_{\mathbb{F}[\lambda]}(Y)\rightarrow\text{span}_{\mathbb{F}[\lambda]}(Y'),\)<br>
\(\phi_Z:\text{span}_{\mathbb{F}[\lambda]}(Z)\rightarrow\text{span}_{\mathbb{F}[\lambda]}(Z'),\)

and \(d\in\mathbb{N}\) such that

\(T'=\lambda^{-d}\left(\sum_{i=1}^{|X|}\sum_{j=1}^{|Y|}\sum_{k=1}^{|Z|}a_{i,j,k}\cdot\phi_X(x_i)\cdot\phi_Y(y_j)\cdot\phi_Z(z_k)\right)+O(\lambda).\)

It is not hard to check that if \(T'\unknown T\), then \(\widetilde{R}(T')\le\widetilde{R}(T)\).

