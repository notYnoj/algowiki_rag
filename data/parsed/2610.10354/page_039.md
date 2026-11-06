with probability \(O(\hat{p}^{-1}\mathrm{log}u)\). This is at most 1/4_n_ by choosing the constant in \(\hat{p}\) sufficiently large. Taking a union bound over all _n_ choices of \(i'\), it follows that we avoid all collisions with probability at least 3/4. Second, we analogously have \(Q[\hat{j}]=B_0[j]\) with probability at least 3/4.

The third success event is that the only indices \(i',j'\), anchored in \(X_\ell\) and \(Y_\ell\), respectively, and satisfying<tbc>

\((i'+j')\cdot 2n+A_1[i']+B_1[j']\equiv\hat{k}(\mathrm{mod}p),\)

<tbc>are those for which \(i'+j'=i+j=k\) and \(A_1[i']+B_1[j']=A_1[i]+B_1[j]\). To analyze this event, note that \((i'+j')\cdot 2n+A_1[i']+B_1[j']\) takes only \(O(|\mathcal{A}_\ell+\mathcal{B}_\ell|\Delta_X\Delta_Y)\) distinct values. Each undesired value, i.e., each value other than \((i+j)\cdot 2n+A_1[i]+B_1[j]\), collides with \(\hat{k}\) (modulo _p_) with probability at most \(O(\hat{p}^{-1}\mathrm{log}u)\), and thus the error probability is

\(O\big(\frac{|\mathcal{A}_\ell+\mathcal{B}_\ell|\Delta_X\Delta_Y\mathrm{log}u}{\hat{p}}\big)=O\big(\frac{\alpha^{-5}t^3|X|\Delta_X\Delta_Y\mathrm{log}u}{\hat{p}}\big)=O\big(\frac{\alpha^{-5}t^3n\Delta_Y\mathrm{log}u}{\hat{p}}\big),\)

by Property (ii) of Theorem 5.7. Choosing the constant in \(\hat{p}\) sufficiently large, this error probability is at most 1/4, say.

All three success events happen simultaneously with probability at least 1/4. In this case we have \((P*Q)[\hat{k}]\le P[\hat{i}]+Q[\hat{j}]=A_0[i]+B_0[j]\) by the first two events, and

\((P*Q)[\hat{k}]\ge\mathrm{min}\{A_0[i']+B_0[j']:i'+j'=k,A_1[i']+B_1[j']=A_1[i]+B_1[j]\}\)

by the third event. Put together, it follows that \((P*Q)[\hat{k}]=A_0[i]+B_0[j]\), and that any witness \(\hat{i}\) corresponds to a witness \(i'\) of _k_. Consequently, we correctly set _C_\[_k_\]. Over the 100log_n_ iterations this event happens at least once with high probability.

### Running Time.

We finally analyze the running time. Suppose that Min-Plus Convolution over the universe \[_u_\] is in time \(O(n^{2-\epsilon})\) for some \(\epsilon>0\).

The heavy step runs in time \(O(n^{2-\delta})\). The light step first applies the BSG Covering theorem (Theorem 5.7) in time \(\widetilde{O}(|X|^2)=\widetilde{O}(n^{2-2\delta})\). We then enumerate all pairs in the remainder R, and for each such pair further enumerate \(\Delta_X^2\) pairs of indices amounting to time \(O(|\mathcal{R}|\Delta_X^2)=O(\alpha|X|^2\Delta_X^2)=O(\alpha n^2)=O(n^{2-\delta})\), by Property (iii) of Theorem 5.7. We then enumerate all \(m=O(\alpha^{-1})=O(n^\delta)\) pairs of sets \(\mathcal{A}_\ell,\mathcal{B}_\ell\), where the upper bound is due to Property (ii) of Theorem 5.7, and run _O_(log_n_) repetitions of the randomized construction. In each repetition we construct and solve a length-\(\Theta(\hat{p})\) instance of Min-Plus Convolution. Each such instance can be trivially split into \(\lceil\hat{p}/n\rceil^2\) subinstances of length at most _n_. The total time to solve these instances is

\(\widetilde{O}\big(m\cdot\frac{\hat{p}^2}{n^2}\cdot n^{2-\epsilon}\big)=\widetilde{O}\big(\alpha^{-11}t^6\Delta_Y^2\cdot n^{2-\epsilon}\big)=\widetilde{O}(n^{2+27\delta-\epsilon}).\)

Choosing \(\delta=\epsilon/28>0\), the total running time becomes \(\widetilde{O}(n^{2-\delta})\). This is truly subquadratic as claimed.

## 5.4 Large-Universe Reduction

We are finally in the position to complete the large-universe reduction:

