<tbc>Centering removes the mean edge density: the off-diagonal entries of _W_ are independent symmetric signs divided by \(\sqrt{n}\), and _W<sub>ii</sub>_=0. The term involving **1** in _F<sub>n</sub>_ accounts for the removed mean. The identity<tbc>

\(\langle A,X\rangle=\frac{1}{2}\big(\mathbf{1}^\top X\mathbf{1}-n-\sqrt{n}\langle W,X\rangle\big)\)

<tbc>shows that maximizing _F<sub>n</sub>_ on E_<sub>n</sub>_ is equivalent to the Max-Cut relaxation. Define

\(M_r(W)=max\{\langle W,X\rangle:X\in\mathcal{E}_n,rankX\le r\},\)<br>
\(c_r=\frac{\mathbb{E}\|g\|_2}{\sqrt{r}}=\sqrt{\frac{2}{r}}\frac{\Gamma((r+1)/2)}{\Gamma(r/2)},g\sim N(0,I_r).\)

The Gaussian norm ratio satisfies 2_c<sub>r</sub>_=2-1/(2_r_)+_O(r_<sup>-2</sup>). Our two estimates are, with probability tending to one,

\(\frac{M_r(W)}{n}\le 2c_r+C\big[r\sqrt{\frac{logn}{n}}+\frac{(rlogn)^{3/4}}{n^{1/4}}\big],\) (2)

\(\frac{1}{n}max_{X\in\mathcal{E}_n}F_n(X)\ge 2-C_0n^{-1/5}.\) (3)

The constants are absolute, and (2) holds for deterministic integer sequences \(1\le r\le\sqrt{n}\). The first estimate bounds all rank-_r_ representations; the second supplies a feasible competitor. We establish them in three steps, then compare the errors with the gap 1_/r_.

## 1. The low-rank gap for Gaussian entries.

First replace _W_ by a matrix _B_ from the normalized Gaussian orthogonal ensemble (GOE), whose independent upper-triangular entries are centered Gaussian with variances 1_/n_ off the diagonal and 2_/n_ on it. For a matrix \(U\in\mathbb{R}^{n\times r}\) with unit rows \(u_i^\top\), set \(H_U=\langle B,UU^\top\rangle\) and \(Q_U=U^\top U/n\). The matrix _Q<sub>U</sub>_ records how the row vectors are distributed among the _r_ coordinates. It satisfies \(Q_U\unknown 0\), tr_Q<sub>U</sub>_=1, and<tbc>

\(\mathbb{E}H_UH_V=\frac{2}{n}\|U^\top V\|_F^2.\)

<tbc>The quadratic process _H<sub>U</sub>_ is easier to bound when compared with a process that is linear in the rows. Fix \(Q\unknown 0\) of trace one and independent _g<sub>i</sub>∼N_(0_,I<sub>r</sub>_), and let \(Y_U=2\sum_ig_i^\top Q^{1/2}u_i\). Direct expansion gives

\(\mathbb{E}(H_U-H_V)^2-\mathbb{E}(Y_U-Y_V)^2\)<br>
\(=\frac{2}{n}\big(\|U^\top U-nQ\|_F^2+\|V^\top V-nQ\|_F^2\)<br>
\(-2\|U^\top V-nQ\|_F^2\big).\)

Thus the difference is at most \(4n\delta^2\) whenever _Q<sub>U</sub>_ and _Q<sub>V</sub>_ lie within Frobenius distance \(\delta\) of _Q_.

To use this comparison, we discretize the row vectors and group configurations with nearby matrices _Q<sub>U</sub>_. Use \(\delta=n^{-3}\) for both discretizations. A \(\delta\)-net of the unit sphere with at most \((3/\delta)^r\) points gives a row net N with \(log|\mathcal{N}|\le nrlog(3/\delta)\). Cover the trace-one positive semidefinite matrices by at most \(K=(1+2/\delta)^{r(r+1)/2}\) Frobenius balls of radius \(\delta\), centered in that set, and assign each \(U\in\mathcal{N}\) to one ball according to _Q<sub>U</sub>_.

Within a cell centered at _Q_, add to _Y<sub>U</sub>_ independent Gaussian variables _Z<sub>U</sub>_ of variance \(2n\delta^2\). The increments of _Y<sub>U</sub>+Z<sub>U</sub>_ dominate those of _H<sub>U</sub>_, so the Gaussian comparison inequality \[21, Theorem 7.2.11\] gives

\(\mathbb{E}max_{U\text{in cell}}H_U\le 2n\mathbb{E}\sqrt{g^\top Qg}+2\delta\sqrt{nlog|\mathcal{N}|}\)<br>
\(\le 2nc_r+C\delta n\sqrt{rlog(3/\delta)}.\)

