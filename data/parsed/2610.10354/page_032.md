**Proof.** Let (_A,B_) denote the given Min-Plus Convolution instance; each entry of _A_ and _B_ is either an integer in \[_u_\] or \(\perp\) (viewed as \(+\infty\)). We call \(i\in[0,n]\) a _witness_ of (_A∗B_)\[_k_\] if _A_\[_i_\]+_B_\[_k-i_\]=(_A∗B_)\[_k_\], and a _q-pseudo-witness_ if _A_\[_i_\]+_B_\[_k-i_\]_\<(A∗B_)\[_k_\]+_q_. Let \(L=\lceil log(2u)\rceil\) and let \(t=100\lceil n^{2\rho}\rceil\). We classify the indices _k_ into three different kinds, based on their number of pseudo- witnesses:

1. _k_ is _exceptionally popular_ if (_A∗B_)\[_k_\] has at least _t_ 1-pseudo-witnesses (i.e., witnesses),<tbc>

2. _k_ is _exceptionally unpopular_ if (_A∗B_)\[_k_\] has at most _t_ 2_<sup>L</sup>_-pseudo-witnesses,<tbc>

3. and otherwise _k_ is _ordinary_. In this case, there is some scale \(0\le\ell<L\) such that (_A∗B_)\[_k_\] has at most \(t2^\ell\)-pseudo-witnesses, and simultaneously at least \(t2^{\ell+1}\)-pseudo-witnesses. We say that (_A∗B_)\[_k_\] is _relevant_ at that scale \(\ell\).

The reduction deals with the exceptionally popular, exceptionally unpopular, and ordinary pairs in three different cases (though we never have to explicitly determine which index falls into which case). Out of these only the third one is interesting; the others are corner cases. Throughout we maintain a sequence _C_ initialized to \(\perp\). We will only ever modify _C_ via updates of the form \(C[k]\leftarrow min\{C[k],A[i]+B[k-i]\}\), ensuring that we never underestimate the convolution.

1. _(Exceptionally Popular)_ Repeat the following \(N=\lceil n^{2-2\rho}\cdot 100logn\rceil\) times: Randomly sample \(i,j\in[0,n]\), and update \(C[k]\leftarrow min\{C[k],A[i]+B[j]\}\) for _k=i+j_. We argue that, afterwards, _C_\[_k_\] is correctly assigned for each exceptionally popular index _k_. Indeed, for any such index the probability of missing all pairs (_i,k-i_) where _i_ is a witness of _k_ is at most<tbc>

<tbc>\(\left(1-\frac{t}{n^2}\right)^N\le exp\left(-\frac{tN}{n^2}\right)\le\frac{1}{n^{100}}.\)<tbc>

<tbc>Thus, with high probability we list one such pair and consequently assign _C_\[_k_\]=(_A∗B_)\[_k_\].<tbc>

2. _(Exceptionally Unpopular)_ By definition, a 2_<sup>L</sup>_-pseudo-witness _i_ of (_A∗B_)\[_k_\] is any index satisfying that \(A[i]\neq\perp\) and \(B[k-i]\neq\perp\). Thus, to list the at most _t_ 2_<sup>L</sup>_-pseudo-witnesses of the exceptionally unpopular indices _k_, we can simply construct the sequences \(A',B'\in\{0,\perp\}^{[0,n]}\) obtained from _A,B_ by replacing any non-\(\perp\) entry by 0, and then for each exceptionally unpopular index we can directly list _t_ witnesses of a Boolean convolution (Lemma 2.15), running in time \(\widetilde{O}(tn)=\widetilde{O}(n^{1+2\rho})\). The output is a set of witnesses, i.e., triples (_i,j,k_) with \(A'[i]+B'[j]=(A'*B')[k]\), or equivalently, \(A[i]\neq\perp\) and \(B[j]\neq\perp\). For each such triple update \(C[k]\leftarrow min\{C[k],A[i]+B[j]\}\).<tbc>

3. _(Ordinary)_ For all \(0\le\ell<L\), all \(x,y\in\{0,1\}\) and all \(z\in[-4,4]\), repeat the following steps 100log_n_ times:<tbc>

3.1. Construct the sequences \(P,Q\in\mathbb{Z}^{[0,n]}\) by<tbc>

\(P[i]=\left\{\begin{array}{ c c }
\left\lfloor\frac{A[i]}{2^\ell}\right\rfloor & \text{if}(A[i]mod2^\ell)\in x2^{\ell-1}+[0,2^{\ell-1}), \\
\perp & \text{otherwise,}
\end{array}\right.\)<br>
\(Q[j]=\left\{\begin{array}{ c c }
\left\lfloor\frac{B[j]}{2^\ell}\right\rfloor & \text{if}(B[j]mod2^\ell)\in y2^{\ell-1}+[0,2^{\ell-1}), \\
\perp & \text{otherwise.}
\end{array}\right.\)

