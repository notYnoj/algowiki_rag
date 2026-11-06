Substituting \(\lambda_*\) into _g_, we obtain

\(g(\lambda_*)=x\left(\sqrt{\frac{Nv_L}{2x}}+c_L\right)+\frac{Nv_L}{2\sqrt{Nv_L/(2x)}}\)<br>
\(=\sqrt{\frac{Nv_Lx}{2}}+\sqrt{\frac{Nv_Lx}{2}}+c_Lx\)<br>
\(=\sqrt{2v_LNx}+\frac{b_Lx}{3}.\)

Therefore<tbc>

\(Pr\big(\exists n\le N:S_n\ge\sqrt{2v_LNx}+\frac{b_Lx}{3}\big)\le e^{-x}.\)

<tbc>Recalling that _N_=2<sup>_j_+1</sup> and \(x=x_j(\gamma)\), we get<tbc>

\(Pr\big(\exists n\le 2^{j+1}:S_n\ge\sqrt{2v_L2^{j+1}x_j(\gamma)}+\frac{b_Lx_j(\gamma)}{3}\big)\le e^{-x_j(\gamma)}.\)

<tbc>Finally, if \(n\in\{2^j,\dots,2^{j+1}-1\}\), then \(n\ge 2^j\), and so<tbc>

\(\sqrt{2v_L2^{j+1}x_j(\gamma)}=2\sqrt{v_L2^jx_j(\gamma)}\le 2\sqrt{v_Lnx_j(\gamma)}.\)

<tbc>Hence

\(Pr\big(\exists n\in\{2^j,\dots,2^{j+1}-1\}:S_n\ge 2\sqrt{v_Lnx_j(\gamma)}+\frac{b_Lx_j(\gamma)}{3}\big)\le e^{-x_j(\gamma)},\)

as claimed.

**Lemma 18** (Confidence sequence for the clipped target)**.** _Define_<tbc>

\(x_n(\gamma):=log\big(\frac{\pi^2(\lfloor log_2n\rfloor+1)^2}{3\gamma}\big).\)

<tbc>_Then with probability at least_ \(1-\gamma\)_, simultaneously for all_ \(n\ge 1\),<tbc>

\(|\bar{Z}_n-\theta_L|\le 2\sqrt{\frac{v_Lx_n(\gamma)}{n}}+\frac{b_Lx_n(\gamma)}{3n}.\)

<tbc>_Proof._ For each \(j\ge 0\), apply Lemma 17 to both _S<sub>n</sub>_ and -_S<sub>n</sub>_. This yields<tbc>

\(Pr\big(\exists n\in\{2^j,\dots,2^{j+1}-1\}:|S_n|\ge 2\sqrt{v_Lnx_j(\gamma)}+\frac{b_Lx_j(\gamma)}{3}\big)\le 2e^{-x_j(\gamma)}.\)

<tbc>Now<tbc>

\(e^{-x_j(\gamma)}=\frac{3\gamma}{\pi^2(j+1)^2},\)

<tbc>and therefore<tbc>

\(\sum_{j=0}^\infty 2e^{-x_j(\gamma)}=\frac{6\gamma}{\pi^2}\sum_{j=0}^\infty\frac{1}{(j+1)^2}=\frac{6\gamma}{\pi^2}\cdot\frac{\pi^2}{6}=\gamma.\)

<tbc>Hence, by a union bound over all dyadic epochs, with probability at least \(1-\gamma\), for every \(j\ge 0\) and every \(n\in\{2^j,\dots,2^{j+1}-1\}\),<tbc>

\(|S_n|\le 2\sqrt{v_Lnx_j(\gamma)}+\frac{b_Lx_j(\gamma)}{3}.\)

<tbc>Since \(j=\lfloor log_2n\rfloor\) on this epoch, this can be written as<tbc>

\(|S_n|\le 2\sqrt{v_Lnx_n(\gamma)}+\frac{b_Lx_n(\gamma)}{3}\text{for all}n\ge 1.\)

<tbc>Dividing by _n_ gives

\(|\bar{Z}_n-\theta_L|=\frac{|S_n|}{n}\le 2\sqrt{\frac{v_Lx_n(\gamma)}{n}}+\frac{b_Lx_n(\gamma)}{3n}\text{for all}n\ge 1,\)

which proves the claim.

