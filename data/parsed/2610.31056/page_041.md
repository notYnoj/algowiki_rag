**Proposition 7.0.1.** _Fix_ \(\mathbf{u}_i,\mathbf{u}_j\in\mathsf{A}\) _such that they satisfy the same constraints as Lemma 7.0.3. Then, we have the following_

1.<tbc>

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(\mathsf{E}_{\mathsf{LS},\mathbf{a},i}^{(p)}\wedge\mathsf{E}_{\mathsf{LS},\mathbf{a},j}^{(p)}\wedge\mathsf{E}_{\mathsf{TS},\mathbf{a},i}^{(pq)}\wedge\mathsf{E}_{\mathsf{TS},\mathbf{a},j}^{(pq)}\wedge\mathsf{E}_{\mathsf{C},pq,\mathbf{a},i,j}\right)\)<br>
\(=\Omega\left(\frac{1}{p^4q^2\sqrt{n}}\right).\)

2.<tbc>

\(\mathbb{P}_{\mathbf{a}^{(r)}}\left(\mathsf{E}_{\mathsf{TS},r,\mathbf{a},i,j}\right)=\Omega\left(\frac{1}{r\sqrt{n}}\right).\)

_Proof._ Refer to Section 7.3.1.

Using Proposition 7.0.1 in equation (8), we get the desired result. This completes the proof.

Now that we have computed a lower bound on the expectation of the random variable \(\mathcal{C}_{ij}^{(\mathsf{int})}\) for vectors with constrained Hamming weights, we are left with the problem of counting such constrained vectors.

## Counting "Big Weight" Vectors.

To apply the Local Central Limit Theorem effectively, the vectors under consideration must have sufficiently large Hamming weight so that the distribution of their associated sums converges to a normal distribution with a small approximation error. In our setting, this requires counting pairs of vectors whose non-overlapping components have Hamming weight \(\Theta(n)\) on both the left and right halves of the vector. To enumerate such pairs, we rely on the following proposition.

**Proposition 7.0.2.** _For any large integer m and constants_ \(1/8\le\alpha<1/4\) _and_ \(c>1/\sqrt{2}\)_, we have the following_

\(\sum_{t_1,t_2}\genfrac(){pt}{2}{m}{t_1}\genfrac(){pt}{2}{m-t_1}{t_2}2^{m-(t_1+t_2)}=\Theta\left(4^m\right),\)

_where_ \(\alpha m\le t_1,t_2<m\), \(t_1+t_2\le m\)_, and_ \(|t_1-t_2|\le c\sqrt{m}\).

_Proof._ Refer Section E.3.

Using the above proposition, we conclude that there exists a set \(\mathsf{T}\subseteq\mathsf{A}\times\mathsf{A}\) such that for any element \((\mathbf{u}_l,\mathbf{u}_k)\in\mathsf{T}\), their corresponding auxiliary binary vectors \(\mathbf{u}_{lk}^{(10)},\mathbf{u}_{lk}^{(01)}\), and \(\mathbf{u}_{lk}^{(11)}\), as defined above in the equation (7), will satisfy the following constraints

\(\frac{n}{16}\le\left\|\mathbf{u}_{lk}^{(10)(L)}\right\|_1,\left\|\mathbf{u}_{lk}^{(10)(R)}\right\|_1,\frac{n}{16}\le\left\|\mathbf{u}_{lk}^{(01)(L)}\right\|_1,\left\|\mathbf{u}_{lk}^{(01)(R)}\right\|_1,\left\|\mathbf{u}_{lk}^{(10)}\right\|_1-\left\|\mathbf{u}_{lk}^{(01)}\right\|_1\right|\le c\sqrt{n},\text{for some constant}c>1/\sqrt{2}\text{(9)}\)

and \(|\mathsf{T}|=\Theta(4^n)\). Firstly, using Claim 7.0.1, for every pair \((\mathbf{u}_l,\mathbf{u}_k)\in\mathsf{T}\), we have the following

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{lk}^{(\mathsf{int})}\right)\ge\mathbb{E}_\mathbf{a}\left(\mathcal{D}_{lk}^{(\mathsf{int})}\right).\) (10)

