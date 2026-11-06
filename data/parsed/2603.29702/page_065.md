## Lower bound if there are no outliers

_Let the true mean of A be_ \(\overline{A}:=\sum_ia_i/M\)_. If we have_ \(max_ia_i\le log^{0.02}(n)\overline{A}\)_, then_

\(\text{\textit{EstSUM}}(A_I)\ge\left(1-O\left(1/log^{0.02}(n)\right)\right)\cdot\left(\sum_{i=1}^Ma_i\right).\)

_Proof._ As a warm-up, suppose that \(\widetilde{A}\) is exactly equal to the actual mean of _A_ which is \(\overline{A}:=\sum_{i=1}^Ma_i/M\). Then \(\text{EstSUM}(A_I)=2\sum_{i\in I}min\left(a_i,2log^{0.02}(n)\overline{A}\right)\) is an estimate for the sum \(\sum_{i=1}^Mmin\left(a_i,2log^{0.02}(n)\overline{A}\right)\). Since every term \(min\left(a_i,2log^{0.02}(n)\overline{A}\right)\) is clipped to be at most 2log<sup>0.02</sup>(_n)<o>A</o>_, we can apply Hoeffding’s Inequality to obtain that \(\text{EstSUM}(A_I)\left(1\pm O\left(1/log^{0.02}(n)\right)\right)\)-approximates \(\sum_{i=1}^Mmin\left(a_i,2log^{0.02}(n)\overline{A}\right)\) with the desired probability. We can see that this satisfies both conditions in the lemma.

Now we begin the analysis using the actual \(\widetilde{A}\). For the upper bound, notice that:

\(\widetilde{A}=\sum_{i\in I}a_i/\left(\frac{M}{2}\right)\)<br>
\(\le\sum_{i=1}^Ma_i/\left(\frac{M}{2}\right)\)<br>
\(=2\sum_{i=1}^Ma_i/M\)<br>
\(=2\overline{A}.\)

Thus \(\text{EstSUM}(A_I)\le 2\sum_{i\in I}min\left(a_i,4log^{0.02}(n)\overline{A}\right)\), which is an estimate for the sum \(\sum_{i=1}^Mmin\left(a_i,4log^{0.02}(n)\overline{A}\right)\). Since <o>_A_</o> is the mean of _A_, we have \(\sum_{i=1}^Mmin\left(a_i,\omega(\overline{A})\right)=\Omega(M\overline{A})\). Thus we can apply Hoeffding’s Inequality (Lemma 3.1, with \(c:=4log^{0.02}(n)\overline{A},\delta:=\Theta\left(\frac{1}{log^{0.02}(n)}\sum_{i=1}^M\left(a_i,4log^{0.02}(n)\overline{A}\right)\right)\)) to obtain that<tbc>

\(\text{EstSUM}(A_I)\le\left(1+O\left(1/log^{0.02}(n)\right)\right)\sum_{i=1}^Mmin\left(a_i,4log^{0.02}(n)\overline{A}\right)\) (33)

<tbc>holds except with probability at most \(exp\left(-\Omega\left(M/log^{0.08}(n)\right)\right)=exp\left(-\omega\left(log^{0.02}(n)\right)\right)\). Since we have \(min\left(a_i,4log^{0.02}(n)\overline{A}\right)\le a_i\), when (33) holds, we indeed have<tbc>

\(\text{EstSUM}(A_I)\le\left(1+O\left(1/log^{0.02}(n)\right)\right)\sum_{i=1}^Ma_i.\)

<tbc>For the lower bound, suppose that every \(a_i\le log^{0.02}(n)\overline{A}\). We can apply Hoeffding’s Inequality (Lemma 3.1, with \(c:=log^{0.02}(n)\overline{A},\delta:=\frac{1}{2}\sum_{i=1}^Ma_i\)) to obtain that<tbc>

\(\widetilde{A}\ge\frac{1}{2}\overline{A}\) (34)

