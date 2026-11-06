event corresponds to a linear equation. In particular, the events<tbc>

\(\mathsf{E}_{\mathsf{LS},p}^{(i)},\mathsf{E}_{\mathsf{RS},p}^{(i)},\mathsf{E}_{\mathsf{LS},p}^{(j)},\mathsf{E}_{\mathsf{RS},p}^{(j)},\mathsf{E}_{\mathsf{LS},p}^{(l)},\mathsf{E}_{\mathsf{RS},p}^{(l)},\mathsf{E}_{\mathsf{LS},p}^{(k)},\mathsf{E}_{\mathsf{RS},p}^{(k)}\)

<tbc>occur simultaneously if **a**<sup>(_p_)</sup> satisfies<tbc>

\(\mathbf{a}^{(p)}\left[\begin{array}{ c c }
\mathbf{U}_{ijlk}^{(L)} & \mathbf{0} \\
\mathbf{0} & \mathbf{U}_{ijlk}^{(R)}
\end{array}\right]\)<br>
\(\equiv_p\left[s_0s_0s_0s_0s_0s_1s_1s_1s_1s_1\right].\)

<tbc>Writing \(\mathbf{a}^{(p)}=\left(\mathbf{a}^{(p)(L)},\mathbf{a}^{(p)(R)}\right)\), this is equivalent to<tbc>

\(\mathbf{a}^{(p)(L)}\mathbf{U}_{ijlk}^{(L)}\equiv_p\left[s_0s_0s_0s_0\right],\)

<tbc>and<tbc>

\(\mathbf{a}^{(p)(R)}\mathbf{U}_{ijlk}^{(R)}\equiv_p\left[s_1s_1s_1s_1\right].\)

<tbc>Similarly, the events \(\mathsf{E}_{\mathsf{TS},q}^{(i)}\), \(\mathsf{E}_{\mathsf{TS},q}^{(j)}\), \(\mathsf{E}_{\mathsf{TS},q}^{(l)}\), \(\mathsf{E}_{\mathsf{TS},q}^{(k)}\) occur simultaneously if **a**<sup>(_q_)</sup> satisfies<tbc>

\(\mathbf{a}^{(q)}\mathbf{U}_{ijlk}\equiv_q\left[s_2s_2s_2s_2\right].\)

<tbc>Since the above systems of linear equations are over independent variables, we obtain

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(\mathcal{D}_{ij}=1\wedge\mathcal{D}_{lk}=1\right)\le\frac{1}{p^{t_1}\cdot p^{t_2}\cdot q^{t_3}}.\)

## E Additional Proofs for Section 7

### E.1 Proof of Lemma 7.1.1

For Property (1), consider the following relation<tbc>

\(S_{\mathsf{TS},pq,i}=S_{\mathsf{C},pq,i}\cdot pq+S_{\mathsf{TS},i}^{(pq)}.\)

<tbc>Using the law of total probability, we have the following<tbc>

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{C},pq,i}=c\right)=\sum_{j=0}^{pq-1}\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{TS},pq,i}=c\cdot pq+j\right)\)

<tbc>Since \(c=w_i/2+\mathcal{O}(\sqrt{w_i})\), we have the following

\(s_j=c\cdot pq+j=(w_ipq)/2+\mathcal{O}(pq\sqrt{w_i})\)

for all \(0\le j<pq\).

