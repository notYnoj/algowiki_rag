_Proof._ In a non-stopping round, \(B_h>\varepsilon\). By Lemma 21, for the sampled arm _k_,<tbc>

\(\varepsilon<min\{0,-\Delta_k+2\beta_k\}+2\beta_k.\)

<tbc>If \(2\beta_k\ge\Delta_k\), then the minimum is 0, so<tbc>

\(\beta_k>\frac{\varepsilon}{2}.\)

<tbc>If \(2\beta_k<\Delta_k\), then the minimum is \(-\Delta_k+2\beta_k\), so<tbc>

\(\varepsilon<-\Delta_k+4\beta_k,\text{and hence}\beta_k>\frac{\Delta_k+\varepsilon}{4}.\)

<tbc>Combining the two cases gives<tbc>

\(\beta_k>max\left\{\frac{\varepsilon}{2},\frac{\Delta_k+\varepsilon}{4}\right\}.\)

<tbc>Since \(r_\varepsilon(N_k,\delta/K)=\beta_k-\varepsilon/4\), we obtain

\(r_\varepsilon(N_k,\delta/K)>max\left\{\frac{\varepsilon}{4},\frac{\Delta_k}{4}\right\}=\frac{\widetilde{\Delta}_k}{4}.\)

**Lemma 23** (Fixed-clipping counting bound)**.** _On_ E<sub>fix</sub>, FIXEDCLIP-1BITBAI _uses at most_<tbc>

\(O\left(H_\mathrm{fix}(\varepsilon)\left[log\frac{K}{\delta}+loglogH_\mathrm{fix}(\varepsilon)\right]\right)\)

<tbc>_1-bit queries._

<tbc>_Proof._ For each arm, define<tbc>

\(A_k:=\alpha_\varepsilon\left(\frac{\sigma^2}{\widetilde{\Delta}_k^2}+\frac{\sigma^2}{\varepsilon\widetilde{\Delta}_k}\right),H_\mathrm{fix}(\varepsilon)=\sum_{k=1}^KA_k.\)

<tbc>Let<tbc>

\(x_n:=x_n(\delta/K)=log\left(\frac{\pi^2(1+\lfloor log_2n\rfloor)^2K}{3\delta}\right).\)

<tbc>We first record a deterministic implication. There exists a universal constant _c_<sub>0</sub>_\>_0 such that for all \(x\ge 1\),<tbc>

\(n\ge c_0A_kx\Longrightarrow 2\sqrt{\frac{3\alpha_\varepsilon\sigma^2x}{n}}+\frac{2\alpha_\varepsilon\sigma^2x}{n\varepsilon}\le\frac{\widetilde{\Delta}_k}{4}.\) (6)

<tbc>Indeed, take _c_<sub>0</sub> large enough. Since \(A_k\ge\alpha_\varepsilon\sigma^2/\widetilde{\Delta}_k^2\), the first term is at most<tbc>

\(2\sqrt{\frac{3\alpha_\varepsilon\sigma^2x}{c_0A_kx}}\le 2\sqrt{\frac{3}{c_0}}\widetilde{\Delta}_k,\)

<tbc>which is at most \(\widetilde{\Delta}_k/8\) for large enough _c_<sub>0</sub>. Similarly, since \(A_k\ge\alpha_\varepsilon\sigma^2/(\varepsilon\widetilde{\Delta}_k)\),

\(\frac{2\alpha_\varepsilon\sigma^2x}{c_0A_kx\varepsilon}\le\frac{2}{c_0}\widetilde{\Delta}_k\le\frac{\widetilde{\Delta}_k}{8}\)

for large enough _c_<sub>0</sub>. This proves (6).

Fix an integer \(T\ge 1\) and suppose, toward a contradiction, that the algorithm has not stopped by the time it has made _T_ total queries. Consider any query made to arm _k_ before time _T_. Since _x<sub>n</sub>_ is nondecreasing and the local count at that query is at most _T_, implication (6) with _x=x<sub>T</sub>_ shows that if \(N_k\ge c_0A_kx_T\), then<tbc>

\(r_\varepsilon(N_k,\delta/K)\le\frac{\widetilde{\Delta}_k}{4},\)

<tbc>contradicting Lemma 22. Hence every arm _k_ can be queried only while<tbc>

\(N_k<c_0A_kx_T.\)

