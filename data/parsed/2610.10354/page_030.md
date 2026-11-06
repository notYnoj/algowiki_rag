where _A_<sub>1</sub>_,B_<sub>1</sub> have entries less than \(n/q\le n^\gamma\) (or \(\perp\)), and _A_<sub>0</sub>_,B_<sub>0</sub> have entries less than _q_ (or \(\perp\)). In fact, we may assume without loss of generality that _A_<sub>0</sub>_,B_<sub>0</sub> have entries bounded by _q/_2 (or \(\perp\)). Indeed, simply split _A_<sub>0</sub> into two subsequences, retaining in one the entries less than _q/_2 and in the other the remaining entries. From the second one subtract _q/_2 globally. This leaves two subproblems for which _A_<sub>0</sub> is as claimed. Proceeding similarly with _B_<sub>0</sub> yields at most four subinstances for which _A_<sub>0</sub>_,B_<sub>0</sub> have entries less than _q/_2.

We compute _C_<sub>1</sub>=_A_<sub>1</sub>∗_B_<sub>1</sub> in time \(O(\text{MPConv}(n|u\le n^\gamma))\) (which is dominated by the first term in Equation (7)). As _A_<sub>0</sub>_,B_<sub>0</sub> have entries less than _q/_2, we know that<tbc>

\(C[k]=C_1[k]\cdot q+C_0[k],\)

<tbc>where

\(C_0[k]=min\{A_0[i]+B_0[k-i]:i\in[0,n],A_1[i]+B_1[k-i]=C_1[k]\},\)

so the remaining task is to compute _C_<sub>0</sub>\[_k_\].

In fact, we can learn a close approximation of _C_<sub>0</sub>\[_k_\] by a simple scaling trick. Let \(A'_0=\lfloor A_0/2\rfloor\) and \(B'_0=\lfloor B_0/2\rfloor\) (applied coordinate-wise), and _recursively_ compute

\(C'_0[k]=min\{A'_0[i]+B'_0[k-i]:i\in[0,n],A_1[i]+B_1[k-i]=C_1[k]\}.\)

It is easy to check that \(2C'_0[k]\le C_0[k]\le 2C'_0[k]+2\), leaving only three candidates for each _C_\[_k_\]. In what follows we will determine the correct choice among these three candidates.

We call an index _i_ satisfying _A_<sub>1</sub>\[_i_\]+_B_<sub>1</sub>\[_k-i_\]=_C_<sub>1</sub>\[_k_\] a _pseudo-witness_ of _k_. We say that _k_ is _popular_ if it has at least \(n^{1-\gamma+\epsilon}\) pseudo-witnesses, and _unpopular_ otherwise. We will compute the value of _C_\[_k_\] by one of the two following algorithms, depending on whether _k_ is popular or unpopular.

• _(Unpopular)_ We first show how to compute (_A∗B_)\[_k_\] for all unpopular indices _k_. For any such _k_, we can afford to list all \(n^{1-\gamma+\epsilon}\) pseudo-witnesses, then compute _C_<sub>0</sub>\[_k_\] and _C_\[_k_\] via the previous identities. This takes time<tbc>

<tbc>\(O(\text{MPConvList}(n,n^{1-\gamma+\epsilon}|u\le n^\gamma))=O(n^\epsilon\cdot\text{MPConvList}(n,n^{1-\gamma}|u\le n^\gamma)),\)<tbc>

<tbc>by Lemma 2.14, which constitutes the first term in Equation (7).<tbc>

• _(Popular)_ It remains to compute _C_\[_k_\] for all popular indices _k_. Let \(X\subseteq[0,n]\) be a random subset including each index independently with probability \(p=\sqrt{(100logn)/n^{1-\gamma+\epsilon}}\). Then let

\(\mathcal{X}_1=\{(i,A_1[i]\cdot q+a):i\in X,0\le a<\lceil\sqrt{q}\rceil\},\)<br>
\(\mathcal{X}_2=\{(j,B_1[j]\cdot q+b\cdot\lceil\sqrt{q}\rceil):j\in X,0\le b<\lceil\sqrt{q}\rceil\},\)<br>
\(\mathcal{X}=\mathcal{X}_1\cup\mathcal{X}_2.\)

Consider the All-Integer 3SUM instance (A,B,C) on the following index sets

\(\mathcal{A}=\{(i,A[i]):i\in[0,n]\},\)<br>
\(\mathcal{B}=\{(j,B[j]):j\in[0,n]\},\)<br>
\(\mathcal{C}=\{(k,C_1[k]\cdot q+2C'_0[k]+z):k\in[0,2n],z\in\{0,1,2\}\}\cap(\mathcal{X}_1+\mathcal{X}_2).\)

