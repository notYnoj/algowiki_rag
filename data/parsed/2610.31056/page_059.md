Now, we have all the tools to compute the desired result. Consider the following

\(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{LS},i}^{(p)}=k,S_{\mathsf{TS},i}^{(pq)}=l,S_{\mathsf{C},pq,i}=c\right)\)<br>
\(=\sum_{y\equiv p}kf_{pq,i}(y),\)<br>
\(=\Theta\left(\sum_{y\in A_k}f_{pq,i}(y)\right)\text{(Using 14)},\)<br>
\(=\frac{1}{p}\cdot\Theta\left(\sum_{y=W_{pq}^{(L)}}f_{pq,i}(y)\right)\text{(Using Claim E.0.2)},\)<br>
\(=\frac{1}{p}\cdot\Theta\left(\sum_yf_{pq,i}(y)\right)\text{(Using 13)},\)<br>
\(=\frac{1}{p}\cdot\Theta\left(\mathbb{P}_{\mathbf{a}^{(pq)}}\left(S_{\mathsf{TS},pq,i}=s=c\cdot pq+l\right)\right)\)<br>
\(=\frac{1}{p}\cdot\Theta\left(\frac{1}{pq\sqrt{w_i}}\right)\text{(Using Corollary 1)}.\)

This completes the proof of Lemma 7.1.1.

## E.2 Discussion on _M=pqr+s_

Firstly, we divide _M_ by the product of integers _p_ and _q_. Let _r_ and _s_ be unique integers such that<tbc>

\(M=r\cdot pq+s,\)

<tbc>and assume that \(s\neq 0\). Let **a** be a vector uniformly distributed over the set \[_M_\]_<sup>n</sup>_={1,2_,...,M}<sup>n</sup>_. Let us split this random vector, **a**, into the following random variables

\(a_i=a_i^{(pq)}+a_i^{(r)}\cdot pq,\)

where \(a_i^{(pq)}\in[1,pq)\) and \(a_i^{(r)}=[0,r]\forall 1\le i\le n\).

Now, we look at the distribution of the random variable vectors **a**<sup>(_pq_)</sup> and **a**<sup>(_r_)</sup> over the random choice of **a**.

**Distribution of** \(a_i^{(pq)}\)**.**

\(\mathbb{P}_{a_i}\left(a_i^{(pq)}=x\right)=\left\{\begin{array}{ c c }
\frac{r+1}{M} & 1\le x\le s \\
\frac{r}{M} & x>s.
\end{array}\right.\) (15)

**Distribution of** \(a_i^{(r)}\)**.**

\(\mathbb{P}_{a_i}\left(a_i^{(r)}=y\right)=\left\{\begin{array}{ c c }
\frac{pq}{M} & 0\le y<r \\
\frac{s}{M} & y=r
\end{array}\right.\) (16)

