**Lemma B.2** (\[BW21, Section 4.1\])**.** _Let X be a non-empty multiset supported on_ \[_N_\]_, and_

\(C_\delta=1699200\cdot\mathrm{log}(2|X|)\mathrm{log}^2(2\mu_X),\) (28)

\(C_2=4+2\cdot 169920\cdot\mathrm{log}(2\mu_X).\) (29)

_If_ \(|X|^2\ge C_\delta\cdot\mu_X\cdot N\)_, then there exists an integer_<tbc>

\(1\le d\le 4\mu_X\Sigma(X)/|X|^2\)

<tbc>_such that for any integer_

\(t\in[C_2\mu_XN\Sigma(X)/|X|^2,\Sigma(X)/2]\)

_that is a multiple of d, it holds that_ \(t\in\mathcal{S}(X)\).

**Remark B.3.** This statement is paraphrased from \[BW21, Theorem 4.3\] (see also \[BW21, Definition 3.1\]). The original statement there stated more generally that \(t\in\mathcal{S}(X)\) if and only if \(t\mathrm{mod}d\in\mathcal{S}(X)\mathrm{mod}d\); since \(0\in\mathcal{S}(X)\), the statement here applies in particular to _t_ that is a multiple of _d_. The upper bound \(d\le 4\mu_X\Sigma(X)/|X|^2\) stated here can be found in \[BW21, Theorem 4.1\].

_Proof of Lemma B.1._ The proof uses a similar strategy as \[CLMZ24\] (and also \[ES90\]). By the assumption Eq. (26), we can pick \(X\subseteq A\) such that

\(\mu_X(x)=r\text{for all}x\in X,\) (30)

\(|\mathrm{supp}(X)|\ge C\sqrt{N/r}\cdot\sqrt{\mathrm{log}(2N)}\mathrm{log}(2r),\) (31)

and<tbc>

\(|X|=r\cdot|\mathrm{supp}(X)|\ge C\sqrt{Nr}\cdot\sqrt{\mathrm{log}(2N)}\mathrm{log}(2r).\)

<tbc>Observe that the precondition of Lemma B.2, \(|X|^2\ge C_\delta\cdot\mu_X\cdot N\), is satisfied (assuming constant _C_ is large enough), and hence by Lemma B.2 there exists an integer

\(1\le d\le 4r\Sigma(X)/|X|^2,\) (32)

such that for any integer

\(t\in[C_2rN\Sigma(X)/|X|^2,\Sigma(X)/2]\) (33)

that is a multiple of _d_, it holds that \(t\in\mathcal{S}(X)\subseteq\mathcal{S}(A)\).

By Eq. (30) and Eq. (31), we have<tbc>

\(\Sigma(X)\ge r\cdot\left(1+2+\cdots+|\mathrm{supp}(X)|\right)>r\cdot|\mathrm{supp}(X)|^2/2>100N.\)

<tbc>Take the largest subset sum \(s\in\mathcal{S}(B)\) that satisfies \(s\le\Sigma(X)/2\) and _s_ is a multiple of _d_, and let \(S\subseteq B\) be the subset achieving \(\Sigma(S)=s\). Such _s_ exists, for example by taking \(S=\varnothing\). By the assumption Eq. (27),

\(\Sigma(B)-\Sigma(S)\ge(\Sigma(A)-N)-\Sigma(X)/2\ge(\Sigma(X)-N)-\Sigma(X)/2>\Sigma(X)/3,\)

