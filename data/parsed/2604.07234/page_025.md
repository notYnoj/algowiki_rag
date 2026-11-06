<tbc>and we invoke the standardization algorithm on it to get<tbc>

\(\varphi_y\big(y^{(1)},\dots,y^{(B)}\big)=\big(\tilde{y}^{(1)},\dots,\tilde{y}^{(B)}\big)\in\mathcal{N}\mathcal{E}_\text{std}(y).\)

<tbc>We proceed with the bound, where we note that the second summation below (and all similar sums of this form) ranges over the contiguous block-intervals<tbc>

\(\big(y^{(i+1)},\dots,y^{(j)}\big)\)

<tbc>produced by the standardization algorithm of Definition 3.10, i.e., the maximal consecutive sequences of blocks between successive stopping points of the algorithm. These intervals form a partition of the _B_ blocks of the fixed induced near-equipartition. We have that

\(\frac{1}{B}\sum_{i=1}^BA_\text{loc}\big(X'^{(i)},y^{(i)}\big)=\frac{1}{B}\sum_{(y^{(i+1)},\dots,y^{(j)})}\sum_{k=i+1}^jA_\text{loc}\big(X'^{(k)},y^{(k)}\big)\)<br>
\(\le^\text{(3.7),(3.26)}\frac{1}{B}\left[\sum_{(y^{(i+1)},\dots,y^{(j)}):y^{(i+1)}\dots y^{(j)}\text{is a biased stretch}}\sum_{k=i+1}^j1+\sum_{(y^{(i+1)},\dots,y^{(j)}):y^{(i+1)}\dots y^{(j)}\text{is an unbiased stretch}}\sum_{k=i+1}^j\big(A_\text{loc}\big(X'^{(k)},\tilde{y}^{(k)}\big)+2b^{-\epsilon}\big)\right]\)<br>
\(\le^\text{(Definition 3.10, Cond. (b))}\frac{1}{B}\left[B\cdot 2b^{-\epsilon}+\sum_{(y^{(i+1)},\dots,y^{(j)}):y^{(i+1)}\dots y^{(j)}\text{is a biased stretch}}b^\epsilon+\sum_{(y^{(i+1)},\dots,y^{(j)}):y^{(i+1)}\dots y^{(j)}\text{is an unbiased stretch}}\sum_{k=i+1}^jA_\text{loc}\big(X'^{(k)},\tilde{y}^{(k)}\big)\right]\)<br>
\(\le\frac{1}{B}\left[B\cdot 2b^{-\epsilon}+b^\epsilon\cdot M\cdot b^{-(1+2\epsilon)}+\sum_{k=1}^BA_\text{loc}\big(X'^{(k)},\tilde{y}^{(k)}\big)\right]\)<br>
\(\le 2b^{-\epsilon}+\alpha b^{1+\epsilon}\cdot b^{-(1+2\epsilon)}+\frac{1}{B}\sum_{k=1}^BA_\text{loc}\big(X'^{(k)},\tilde{y}^{(k)}\big)\le^\text{(3.6),(b large)}T_\text{std}(X',y)+\frac{\beta^\star(\alpha)}{2}.\) (3.30)

The bound (3.30) holds uniformly over the choice of induced near-equipartition \((y^{(1)},\dots,y^{(B)})\in\mathcal{N}\mathcal{E}_\text{ind}(y)\) and holds irrespective of the choice of the string \(y\in\{0,1\}^M\) with \(\le M\cdot b^{-(1+2\epsilon)}\) biased stretches. Thus, Proposition 3.12 and the preceding discussion together imply that with probability \(\ge 1-e^{-\Omega(N)}\), the inequality (3.23) holds, i.e., that

(3.31) \(\mathbb{P}\left(Y\notin\mathcal{G}\left(X'\right)\right)\ge 1-e^{-\Omega(N)}.\)

## 3.4. Proof of Theorem 1.1.

We are finally ready to prove the first strict inequality of Theorem 1.1. Towards this end, we first define the event

(3.32) \(E_N:=\left\{X'\text{is typical}\right\}\cap\left\{Y\notin\mathcal{G}(X')\right\}.\)

Then we may write

\(\mathbb{E}\left[Z_{X^\prime,Y}\cdot\unknown\{E_N\}\right]=^\text{(3.32)}\mathbb{E}\left[\left(\sum_{S\in\genfrac(){pt}{2}{[N]}{M}}\unknown\left\{X'|_S=Y\right\}\right)\unknown\left\{X'\text{is typical}\right\}\unknown\left\{Y\notin\mathcal{G}(X')\right\}\right]\)

