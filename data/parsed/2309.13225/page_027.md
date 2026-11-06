previous iteration. We take the edges \((x_j^*,x_{j+1}^*)\), \((x_{j+1}^*,x_{j+1})\in E^*\), and the remaining edges in \(E_{\ell(x_j)}\). By induction, we have,

\(\hat{\delta}_{\ell(x_j)}(x_j^*,x_{j-1})\le\hat{\delta}_{\ell(x_{j+1})}(x_j^*,x_{j+1}^*)+1+\delta(x_{j+1},x_{j-1})\)<br>
\(\le\delta(x_j,x_{j+1})+2(2+(a-(j+1)))+3+\delta(x_{j+1},x_{j-1})\)<br>
\(\le\delta(x_j,x_{j-1})+2(2+(a-j))+1\)

Thus, we have,<tbc>

\(\hat{\delta}_{\ell(v)}(v^*,u)=\hat{\delta}_{\ell(x_1)}(x_1^*,x_0)\le\delta(v,u)+2(a+1)+1\)

<tbc>From _u_, we take the edge (_u,v_<sup>∗</sup>), followed by \((v^*,v)\in E^*\) so that,

\(\hat{\delta}(u,v)\le\hat{\delta}_{\ell(v)}(u,v^*)+1\)<br>
\(\le\delta(u,v)+2(a+1)+2\)<br>
\(\le\delta(u,v)+k\)

### Time Complexity

_Proof._ We set _l_<sub>0</sub>=_k_-2 and leave _l_ to be optimized.

**Decompose** requires \(\tilde{O}(ln^2)\) time. Over all _D<sub>j</sub>_, the invocations of **Dijkstra** requires \(\tilde{O}(n^{2+1/l})\) time, as for each i, \(|D_i|=\tilde{O}(n/s_i)\) and |_E<sub>i</sub>_|=_O(ns_<sub>_i_-1</sub>) while \(|D_{j_1}\times D_{j_2}|=\tilde{O}\left(\frac{n}{s_{j_1}}\times\frac{n}{s_{j_2}}\right)=\tilde{O}\left(n^\frac{j_1+j_2}{l}\right)=\tilde{O}\left(n^{2-\frac{j-1}{l}}\right)\) as \(j_1+j_2\le 2l+1-j\).

**BK2APASP** on _G_<sub>_l_<sub>0</sub>+1</sub> requires _s_<sub>_l_<sub>0</sub></sub>_n_<sup>1.5</sup>=_n_<sup>1.5+1-\(\frac{k-2}{l}\)</sup> time. Balancing,<tbc>

\(2+\frac{1}{l}=2.5-\frac{k-2}{l}\)

<tbc>we solve to obtain,

\(2l+1=\frac{5}{2}l-k+2\)<br>
\(\frac{l}{2}=k-1\)<br>
\(l=2(k-1)\)

Thus, the algorithm runs in time \(\tilde{O}(n^{2+1/l})=\tilde{O}(n^{2+\frac{1}{2k-1}})\)

## 4.2 Faster Multiplicative Approximations for Long Paths with FMM

In this section, we improve upon Theorem 4.1 using fast matrix multiplication.

**Theorem 4.2.** _Let_ \(k\ge 4\) _be an even integer. Algorithm 4 computes a_ (2,0) _approximation for all paths of length_ \(\delta(u,v)\ge k\) _in expected time_ \(\tilde{O}(n^{2+\frac{x}{l-k+2}})\) _where x,l are chosen to minimize,_

\(max\left(\omega\left(1-\frac{k-2}{2(l-k+2)}x,1-x,1-\frac{k-4}{2(l-k+2)}x\right),2+\frac{x}{l-k+2},1.5+x\right)\)

In  1 and Proposition C.4, we exhibit a few running times for \(6\le k\le 10\).

