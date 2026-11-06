<tbc>definitions and Stirling’s formula one easily derives the following asymptotic estimates:

\(s=(4+o(1))H^2(logH)^2,\)<br>
\(M_H=(4+o(1))H^3(logH)^3,\) (2)

\(logN_H=(1+o(1))M_HlogH=(4+o(1))H^3(logH)^4,\) (3)

\(log^{(2)}N_H=(3+o(1))logH.\)

Consequently,

\(M_H=(3+o(1))\frac{logN_H}{log^{(2)}N_H},\frac{logN_H}{logN_{H-1}}\longrightarrow 1,\) (4)

and, for every fixed \(i\ge 2\),

\(log^{(i+1)}N_H=(1+o(1))log^{(i)}H.\) (5)

We now use these estimates as well as Lemma 3.3 to prove by induction on \(r\ge 1\) that

\(a_r(n)\le(3+o(1))\frac{logn}{log^{(r+1)}n}(n\rightarrow\infty).\) (6)

Throughout the following, we will use the following reformulation of the inequality proved in Lemma 3.3:

\(a_{r+1}(N_H)\le M_Ha_r(H+1)\)

for every fixed _r_ and _H_ sufficiently large.

We first prove (6) in the base case _r_=1. Noting that _a_<sub>0</sub>(_n_)=1, Lemma 3.3 implies that \(a_1(N_H)\le M_H\) for _H_ sufficiently large. Now consider any sufficiently large integer _n_, and let _H_ be the smallest integer satisfying \(n\le N_H\). Clearly, \(H\rightarrow\infty\) as \(n\rightarrow\infty\) and \(N_{H-1}<n\le N_H\). Equation (4) now implies that log_n_=(1+_o_(1))log_N<sub>H</sub>_, which in turn implies loglog_n_=(1+_o_(1))loglog_N<sub>H</sub>_. Consequently, using Equation (4) we find that

\(a_1(n)\le a_1(N_H)\le M_H=(3+o(1))\frac{logN_H}{loglogN_H}=(3+o(1))\frac{logn}{loglogn}.\)

This proves (6) for _r_=1, settling the base of the induction.

For the induction step, suppose that \(r\ge 1\) is fixed and we already proved that (6) holds for _r_. For every sufficiently large integer _H_, by Lemma 3.3 we then find:

\(a_{r+1}(N_H)\le M_Ha_r(H+1)\le(3+o(1))\frac{M_HlogH}{log^{(r+1)}H}=(3+o(1))\frac{logN_H}{log^{(r+2)}N_H},\)

where the final equality follows from (3) and (5). Now, for any sufficiently large integer _n_, let _H_ be the smallest integer such that \(N_H\ge n\). So \(N_{H-1}<n\le N_H\). Since \(\frac{logN_H}{logN_{H-1}}\rightarrow 1\) for \(H\rightarrow\infty\) and since \(n\le N_H\) implies that \(H\rightarrow\infty\) as \(n\rightarrow\infty\), we find that log_n_=(1+_o_(1))log_N<sub>H</sub>_, implying in particular that<tbc>

\(a_{r+1}(n)\le a_{r+1}(N_H)\le(3+o(1))\frac{logN_H}{log^{(r+2)}N_H}=(3+o(1))\frac{logn}{log^{(r+2)}n},\)

