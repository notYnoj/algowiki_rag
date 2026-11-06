3. _Total sum events:_<tbc>

\(\mathsf{E}_{\mathsf{TS},q}^{(i)}:\mathbf{u}_i\cdot\mathbf{a}^{(q)}\equiv s_2modq,\)<br>
\(\mathsf{E}_{\mathsf{TS},q}^{(j)}:\mathbf{u}_j\cdot\mathbf{a}^{(q)}\equiv s_2modq,\)<br>
\(\mathsf{E}_{\mathsf{TS},q}^{(l)}:\mathbf{u}_l\cdot\mathbf{a}^{(q)}\equiv s_2modq,\)<br>
\(\mathsf{E}_{\mathsf{TS},q}^{(k)}:\mathbf{u}_k\cdot\mathbf{a}^{(q)}\equiv s_2modq,\)<br>
\(\mathsf{E}_{\mathsf{col},r}^{(ij)}:\mathbf{u}_i\cdot\mathbf{a}^{(r)}\equiv\mathbf{u}_j.\mathbf{a}^{(r)}modr\)<br>
\(\mathsf{E}_{\mathsf{col},r}^{(lk)}:\mathbf{u}_l\cdot\mathbf{a}^{(r)}\equiv\mathbf{u}_k\cdot\mathbf{a}^{(r)}modr,\)

As we mentioned in the technical overview, the main difficulty in analyzing the second moment stems from dependencies between the above-mentioned events, that is induced by linear relationships among the binary vectors. To address this issue, we partition the set _S_ of all possible 4-tuples into cells such that, for every tuple within a given cell, the joint probability

\(\mathbb{P}_\mathbf{a}\left(\mathcal{C}_{ij}=1\wedge\mathcal{C}_{lk}=1\right)\)

admits a uniform upper bound, while the size of each cell can also be tightly bounded. This structured partitioning allows us to control the contribution of dependent events to the second moment. As we have discussed previously, the events mod _r_ are independent of the events mod _p_ and _q_. Hence, first, we analyze them separately. Consider the following claim

**Claim 6.0.1.** _Let_ \(r\ge 2\) _be an integer, let_ **w**:=**u**_<sub>i</sub>_-**u**_<sub>j</sub> and_ \(\mathbf{w}':=\mathbf{u}_l-\mathbf{u}_k\)_, and let_ **a**<sup>(_r_)</sup> _be uniform on_ \(\mathbb{Z}_r^n\)_. Write_ \(P:=\mathbb{P}_{\mathbf{a}^{(r)}}\left[\mathbf{w}\cdot\mathbf{a}^{(r)}\equiv_r0\wedge\mathbf{w}'\cdot\mathbf{a}^{(r)}\equiv_r0\right]\).

1. _If_ \(\mathbf{w}\equiv\pm\mathbf{w}'(modr)\)_, then P_=1_/r._<tbc>

_2._ _If_ \(\mathbf{w}\unknown\equiv\pm\mathbf{w}'(modr)\)_, then_ \(P\in\{1/r^2,2/r^2\}\)_; moreover P_=1_/r_<sup>2</sup> _whenever r is odd._

_Proof._ refer to Section D.1.

Using this claim, we can rewrite the second moment as follows

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}^2\right)=\sum_{i<j,l<k(i,j)\neq(l,k)}\mathbb{P}_\mathbf{a}\left(\mathcal{C}_{ij}=1\wedge\mathcal{C}_{lk}=1\right)+\mathbb{E}_\mathbf{a}\left(\mathcal{C}\right)=S_1+S_2+\mathbb{E}_\mathbf{a}\left(\mathcal{C}\right),\text{(4)}\)

where

\(S_1=\frac{1}{r}\cdot\sum_{i<j,l<k(i,j)\neq(l,k)\mathbf{u}_i-\mathbf{u}_j=\pm(\mathbf{u}_l-\mathbf{u}_k)}\mathbb{P}_{\mathbf{a}^{(pq)}}\left(\mathcal{D}_{ij}=1\wedge\mathcal{D}_{lk}=1\right),S_2\le\frac{2}{r^2}\cdot\sum_{i<j,l<k(i,j)\neq(l,k)\mathbf{u}_i-\mathbf{u}_j\neq\pm(\mathbf{u}_l-\mathbf{u}_k)}\mathbb{P}_{\mathbf{a}^{(pq)}}\left(\mathcal{D}_{ij}=1\wedge\mathcal{D}_{lk}=1\right),\)

and D_<sub>ij</sub>_ is a binary random variable equal to 1 if and only if events \(\mathsf{E}_{\mathsf{LS},p}^{(i)}\), \(\mathsf{E}_{\mathsf{RS},p}^{(i)}\), \(\mathsf{E}_{\mathsf{LS},p}^{(j)}\), \(\mathsf{E}_{\mathsf{RS},p}^{(j)}\), \(\mathsf{E}_{\mathsf{TS},q}^{(i)}\), and \(\mathsf{E}_{\mathsf{TS},q}^{(j)}\) occur simultaneously. And, the random variable is D_<sub>lk</sub>_ is defined similarly. These two random variables are defined over the random choice of **a**<sup>(_p_)</sup> and **a**<sup>(_q_)</sup>.

