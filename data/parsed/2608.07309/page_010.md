### 3.4 Running Time

By Lemma 3.1 and Equation (1), with constant probability over \(p\in_R\mathcal{P}\), the quantum walk has a marked fraction \(\mu=\Omega(n^{2r-k_2-k_4})\). The quantum search over \(q\in\mathbb{Z}_p\) contributes a factor \(\widetilde{O}(\sqrt{p})\) to the checking time by Theorem 2.5. For each fixed residue, Claw Finding searches the domains X<sub>1</sub> and X<sub>3</sub>. For the parameter choices made below, we force \(k_1/2\le k_3\le 2k_1\), so Theorem 2.7 gives a claw finding of a fixed residue in time \(\widetilde{O}(n^{(k_1+k_3)/3})\). By Theorem 2.4, the walk setup builds the two dictionaries in \(\widetilde{O}(m)=\widetilde{O}(n^r)\) time. Since adjacent vertices differ by one tuple, a walk update maintains them using one deletion and one insertion in \(\widetilde{O}(1)\) time. Using Theorem 2.6 on G with parameters<tbc>

\(T_\mathrm{set}=\widetilde{O}(n^r),T_\mathrm{upd}=\widetilde{O}(1),\)<br>
\(T_\mathrm{chk}=\widetilde{O}(\sqrt{p}n^{(k_1+k_3)/3})=\widetilde{O}(n^{(k_1+k_3)/3+r/2}),\mu=\Omega(n^{2r-k_2-k_4})\)

<tbc>gives a total running time of the algorithm<tbc>

\(\widetilde{O}\left(n^r+n^{(k_2+k_4)/2-r}\left(n^{r/2}+n^{(k_1+k_3)/3+r/2}\right)\right)=\widetilde{O}\left(n^{\mathrm{max}\left\{r,\frac{k_1+k_3}{3}+\frac{k_2+k_4-r}{2}\right\}}\right).\)

<tbc>It remains to choose the block sizes and _r_. The bound depends on _k_<sub>2</sub> and _k_<sub>4</sub> only through their sum, except for the constraint \(r\le\mathrm{min}\{k_2,k_4\}\); hence we choose _k_<sub>2</sub>=_k_<sub>4</sub>. Similarly, it depends on _k_<sub>1</sub> and _k_<sub>3</sub> only through their sum, and choosing them as evenly as possible ensures the conditions of Theorem 2.7. For convenience in  1, put \(\ell=k_1+k_3\); then \(k_1=\lfloor\ell/2\rfloor\), \(k_3=\lceil\ell/2\rceil\), and \(k=\ell+2k_2\). With these choices, put

\(r=\mathrm{min}\left\{k_2,\frac{2}{3}\left(k_2+\frac{k_1+k_3}{3}\right)\right\}.\)

Let _k_=7_d+j_, where \(j\in\{0,1,\dots,6\}\).

This completes the proof of Theorem 1.2.

## 4 Application to Pigeonhole Modular Equal Subset Sum

**Definition 4.1.** _An instance of_ Pigeonhole Modular Equal Subset Sum _consists of a list A of n positive integers and a modulus_ \(q\le 2^n-1\)_. The task is to find two distinct subsets_ \(S_1,S_2\subseteq[n]\) _such that_<tbc>

\(\sum_{i\in S_1}A[i]\equiv\sum_{i\in S_2}A[i]\mathrm{mod}q.\)

\begin{tabular}{ccccc}
_j=k_mod7 & \(\ell=k_1+k_3\) & _k_<sub>2</sub>=_k_<sub>4</sub> & _r_ & \(\Psi_k=\mathrm{max}\{r,\ell/3+k_2-r/2\}\) \\
0 & 3_d_ & 2_d_ & 2_d_ & 2_d_ \\
1 & 3_d_+1 & 2_d_ & 2_d_ & 2_d_+1/3 \\
2 & 3_d_ & 2_d_+1 & 2_d_+2/3 & 2_d_+2/3 \\
3 & 3_d_+1 & 2_d_+1 & 2_d_+8/9 & 2_d_+8/9 \\
4 & 3_d_+2 & 2_d_+1 & 2_d_+1 & 2_d_+7/6 \\
5 & 3_d_+3 & 2_d_+1 & 2_d_+1 & 2_d_+3/2 \\
6 & 3_d_+2 & 2_d_+2 & 2_d_+16/9 & 2_d_+16/9 \\
\end{tabular}

** 1:** Optimal parameters for Algorithm 1, where \(d=\lfloor k/7\rfloor\) and _j=k_mod7.

