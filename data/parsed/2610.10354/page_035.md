By definition of _P,Q_ and Property (i) of Claim 5.4, it holds that<tbc>

\(\left\lfloor\frac{(A*B)[k^*]}{2^\ell}\right\rfloor-2\le P[i^*]+Q[j^*]\le\left\lfloor\frac{(A*B)[k^*]}{2^\ell}\right\rfloor.\)

<tbc>Putting all these bounds together, there must be some \(z\in[-4,4]\) such that

\(R[k^*]=min_{i,j\in Xi+j=k^*}\left\lfloor\frac{A[i]}{2^\ell}\right\rfloor+\left\lfloor\frac{B[j]}{2^\ell}\right\rfloor+z=P[i^*]+Q[j^*],\)

completing the proof of the claim.

In light of Claim 5.5, with high probability over the 100log_n_ trials there is some iteration \(\ell,x,y,z\) in which we assign _P_\[_i_<sup>∗</sup>\]+_Q_\[_j_<sup>∗</sup>\]=_R_\[_k_<sup>∗</sup>\]. We argue that in this iteration we correctly assign _C_\[_k_<sup>∗</sup>\]. In step 3.2 we construct the 3SUM instance (P,Q,R), and by definition it contains the solution (_i_<sup>∗</sup>_,P_\[_i_<sup>∗</sup>\])+(_j_<sup>∗</sup>_,Q_\[_j_<sup>∗</sup>\])=(_k_<sup>∗</sup>_,R_\[_k_<sup>∗</sup>\]). Lemma 4.3 guarantees that this solution is either listed in T , in which case we correctly assign _C_\[_k_<sup>∗</sup>\] in step 3.3, or is part of one of the subinstances \((\mathcal{P}',\mathcal{Q}',\mathcal{R}')\). In the latter case, focus on the corresponding iteration of step 3.4. By construction, we have \(P'[i^*]=P[i^*]\) and \(Q'[j^*]=Q[j^*]\). Thus, \((P'*Q')[k^*]=(P*Q)[k^*]\), recalling that _i_<sup>∗</sup> is a witness of (_P∗Q_)\[_k_<sup>∗</sup>\] by Property (i) of Claim 5.4. Moreover, Property (ii) of Claim 5.4 guarantees that every witness _i_ of \((P'*Q')[k^*]\) must be a \(2^\ell\)-pseudo-witness of (_A∗B_)\[_k_<sup>∗</sup>\]. However, since _k_<sup>∗</sup> is relevant at level \(\ell\), there are at most _t_ such pseudo-witnesses, and consequently, \((P'*Q')[k^*]\) has at most _t_ witnesses. We are therefore guaranteed to find _i_<sup>∗</sup> by the listing algorithm, and thus update _C_\[_k_<sup>∗</sup>\] as intended. This completes the correctness analysis.

Finally, it remains to analyze the running time. Step 1 runs in time \(\widetilde{O}(n^{2-2\rho})\) and step 2 runs in time \(\widetilde{O}(n^{1+2\rho})\). Step 3 runs in _O_(log_u_) iterations. In each iteration, step 3.1 runs in time \(O(n+n^{2-2\rho})\), step 3.2 is dominated by the call to Lemma 4.3 running in time \(O(n^{2-\delta})\) for some constant \(\delta=\delta(\rho,\epsilon)>0\), step 3.3 can be charged to the running time of that lemma as well, and step 3.4 constructs \(O(n^\epsilon)\) Min-Plus Convolution Listing instances, passes them to the reduction, and processes their \(O(n^{1+2\rho})\) reported witnesses per instance. The total time is \(O((n^{1+2\rho+\epsilon}+n^{2-2\rho}+n^{2-\delta})logu)\). This is as claimed, by possibly reducing \(\delta\) to account for the second term.

## 5.3 Universe Reduction for Monotone Min-Plus Convolution

Recall that a sequence \(A\in\mathbb{Z}^{[0,n]}\) is _monotone_ if \(A[0]\le A[1]\le\cdots\le A[n]\). We refer to the Min-Plus Convolution problem with _both_ input sequences _A,B_ being monotone as the _Monotone_ Min-Plus Convolution problem. We emphasize that this convention applies to Section 5 only; in other parts of this paper (notably, Section 6.3) we often consider the variant where only one of the two input sequences is monotone.

It is easy to see that the general Min-Plus Convolution problem is trivially equivalent to Monotone Min-Plus Convolution: On the one hand, any monotone instance can trivially be regarded as non-monotone. And on the other hand, any non-monotone instance (_A,B_) over a universe \[_u_\] can be converted to the equivalent monotone instance \((A',B')\) for

\(A'[i]=i\cdot 10u+A[i],\)<br>
\(B'[j]=j\cdot 10u+B[j].\)

