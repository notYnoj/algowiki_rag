**Definition 2.12** (rank and subrank)**.** For a positive integer _k_ and a complex _k_-th order tensor _T_, its _rank_ is \(\mathrm{R}(T)=\mathrm{min}\{r\in\mathbb{N}:T\unknown\mathsf{I}_k(r)\}\). For \(k\ge 2\), its _subrank_ is \(\mathrm{Q}(T)=\mathrm{max}\{q\in\mathbb{N}:\mathsf{I}_k(q)\unknown T\}\). Equivalently, fix coordinates of dimensions (_n_<sub>1</sub>_,...,n<sub>k</sub>_) for _T_. Then R(_T_) is the smallest nonnegative integer _r_ for which

\(T=\sum_{h=1}^r\otimes_{d=1}^kv_{d,h},v_{d,h}\in\mathbb{C}^{n_d}(1\le d\le k,1\le h\le r).\)

An empty sum denotes the zero coefficient table in these coordinates. A tensor of the form \(\otimes_{Cd=1}^kv_d\), with \(v_d\in\mathbb{C}^{n_d}\) for \(1\le d\le k\), is called a _simple tensor_. The rank of the zero tensor is 0; for \(k\ge 2\), its subrank is also 0.

For \(r\ge 1\), the two definitions of rank agree by taking the vectors _v<sub>d,h</sub>_ as the columns of the local maps from I_<sub>k</sub>(r_); the case _r_=0 follows from the conventions for the zero tensor. The standard basis expansion is a finite sum of simple tensors, so every tensor has finite rank. A nonzero tensor restricts to I_<sub>k</sub>_(1) by selecting one nonzero entry and rescaling it. For \(k\ge 2\) and nonzero _T_, we also have \(\mathrm{Q}(T)\le\mathrm{min}_{1\le d\le k}n_d\): grouping leg_d_ against all other legs gives a matrix of rank at most _n<sub>d</sub>_, while the corresponding matrix of I_<sub>k</sub>(q_) has rank _q_. Local maps cannot increase this matrix rank. The general statement about such _flattenings_ is defined and proved in Definition A.1 and Lemma A.2. Hence the maximum defining subrank exists. Composing restrictions also shows that rank and subrank are unchanged under ∼.

**Definition 2.13** (asymptotic rank and subrank)**.** For every integer \(k\ge 2\) and every nonzero complex _k_-th order tensor _T_, define

\(\widetilde{\mathrm{R}}(T)=\mathrm{lim}_{N\rightarrow\infty}\mathrm{R}(T^{\otimes_KN})^{1/N},\widetilde{\mathrm{Q}}(T)=\mathrm{lim}_{N\rightarrow\infty}\mathrm{Q}(T^{\otimes_KN})^{1/N}.\)

Set \(\widetilde{\mathrm{R}}(0)=\widetilde{\mathrm{Q}}(0)=0\).

These limits exist by Fekete’s lemma \[PS98, no. 98\]; see also \[Sch03, Theorem 2.2\] and its application to asymptotic rank and subrank in \[WZ26, Lemma 2.10 and Corollaries 2.11-2.12\]. Indeed, taking products of rank decompositions and of subrank restrictions gives \(\mathrm{R}(A\otimes_KB)\le\mathrm{R}(A)\mathrm{R}(B)\) and \(\mathrm{Q}(A\otimes_KB)\ge\mathrm{Q}(A)\mathrm{Q}(B)\) for all complex tensors _A,B_ of the same order \(k\ge 2\). Fix a nonzero tensor _T_. The sequence \(\mathrm{logR}(T^{\otimes_KN})\) is subadditive, so Fekete’s lemma gives the first equality below. For the second equality, apply the same lemma to the nonnegative subadditive sequence _N_logR(_T_)-logQ(\(T^{\otimes_KN}\)). We obtain

\(\widetilde{\mathrm{R}}(T)=\mathrm{inf}_{N\ge 1}\mathrm{R}(T^{\otimes_KN})^{1/N},\widetilde{\mathrm{Q}}(T)=\mathrm{sup}_{N\ge 1}\mathrm{Q}(T^{\otimes_KN})^{1/N}.\)

Both limits are finite because \(1\le\mathrm{Q}(T^{\otimes_KN})\le\mathrm{R}(T^{\otimes_KN})\le\mathrm{R}(T)^N\) for every positive integer _N_ and every nonzero _T_.

We next recall the preordered semiring framework underlying Strassen’s theory. Its spectral points will turn asymptotic tensor comparisons into inequalities between nonnegative real numbers \[Str88, WZ26\].

**Definition 2.14** (Strassen preorder and asymptotic restriction)**.** Let S be a commutative semiring with identities 0<sub>S</sub> and 1<sub>S</sub>. For each \(r\in\mathbb{N}\), let _r_<sub>S</sub> denote the sum of _r_ copies of 1<sub>S</sub> in S (so 0<sub>S</sub> is the empty sum and 1<sub>S</sub> is the sum of one copy). A preorder \(\unknown\) on S is called a _Strassen preorder_ if the following properties hold:

(1) For all \(r,s\in\mathbb{N}\), we have \(r_\mathcal{S}\unknown s_\mathcal{S}\) if and only if \(r\le s\).<tbc>

