Motivated by this, we now consider partitioning the range of possible _B_-to-_A_ ratio \([\alpha,1]\) into \(\left\lceil log_2\left(\frac{1}{\alpha}\right)\right\rceil\) parts:<tbc>

\([\alpha,1]\subset\left[\frac{1}{2},1\right]\cup\left[\frac{1}{4},\frac{1}{2}\right]\cup\left[\frac{1}{8},\frac{1}{4}\right]\cup\cdots\cup\left[\frac{1}{2^{\left\lceil log_2\left(\frac{1}{\alpha}\right)\right\rceil}},\frac{1}{2^{\left\lceil log_2\left(\frac{1}{\alpha}\right)\right\rceil-1}}\right].\)

<tbc>For each part \(\left[\frac{1}{2^k},\frac{1}{2^{k-1}}\right]\), we define the sum<tbc>

\(\sigma_k:=\sum_{s\in[S]}\sum_{(l,r]\in s}\unknown\left[B_{\Sigma(l,r]}\in\left[\frac{1}{2^k}A_{\Sigma(l,r]},\frac{1}{2^{k-1}}A_{\Sigma(l,r]}\right]\right]\mathrm{SD}_M(A(l,r],B(l,r]),\)

<tbc>Namely the contribution to (5) from intervals whose _B_-to-_A_ ratios are within \(\left[\frac{1}{2^k},\frac{1}{2^{k-1}}\right]\). By definition we have<tbc>

\(\sum_{s\in[S]}\sum_{(l,r]\in s}\mathrm{SD}_M(A(l,r],B(l,r])\le\sum_{k=1}^{\left\lceil log_2\left(\frac{1}{\alpha}\right)\right\rceil}\sigma_k.\)

<tbc>Since \(\left\lceil log_2\left(\frac{1}{\alpha}\right)\right\rceil<1+log_2\left(\frac{1}{\alpha}\right)\), to show (5) it suffices to show that for each \(k\in\left[1,\left\lceil log_2\left(\frac{1}{\alpha}\right)\right\rceil\right]\), we have<tbc>

\(\sigma_k=O\left(\left(\sum_xb_x\right)S^{0.51}+\mathrm{max}_{x^\prime}\left(a_{x^\prime}\right)\cdot\left(n/2^{log_M^{0.015}(n)}\right)\right).\)

<tbc>Fix a \(k\in\left[1,\left\lceil log_2\left(\frac{1}{\alpha}\right)\right\rceil\right]\). Consider the set of intervals _I_ containing all recursion intervals (_l,r_] such that \(B_{\Sigma(l,r]}\in\left[\frac{1}{2^k}A_{\Sigma(l,r]},\frac{1}{2^{k-1}}A_{\Sigma(l,r]}\right]\), namely intervals that contribute to \(\sigma_k\). Consider length-_n_ sequences _C_={_c<sub>x</sub>_} and _D_={_d<sub>x</sub>_} defined as copies of _A,B_ with the regions that do not contribute to \(\sigma_k\) zeroed out:

\(c_x:=\left\{\begin{array}{ c c }
a_x & \text{if}\exists(l,r]\in I\text{s.t.}x\in(l,r] \\
0 & \text{otherwise}
\end{array}\right.,\)<br>
\(d_x:=\left\{\begin{array}{ c c }
b_x & \text{if}\exists(l,r]\in I\text{s.t.}x\in(l,r] \\
0 & \text{otherwise}
\end{array}\right..\)

For every \((l,r]\in I\), we then have

\(\mathrm{SD}_M(A(l,r],B(l,r])=\mathrm{SD}_M(C(l,r],D(l,r])\) (7)

and

\(\mathrm{SD}_M(C(l,r],D(l,r])=O\left(\frac{1}{2^k}\cdot\mathrm{TD}_M(C(l,r])\right).\) (8)

For any distinct \((l_0,r_0],(l_1,r_1]\in I\), either (_l_<sub>0</sub>_,r_<sub>0</sub>] and (_l_<sub>1</sub>_,r_<sub>1</sub>] are disjoint, or one contains another. Thus, it is possible to find a "dominating" subset \(I'\subset I\) of disjoint intervals such that for every \((l,r]\in I\), there exists \((l',r']\in I'\) such that \((l,r]\subseteq(l',r']\). By taking the sums over each of these disjoint intervals in \(I'\), we must have

\(\sum_xd_x=\Theta\left(\frac{1}{2^k}\sum_{x^\prime} c_{x^\prime}\right).\) (9)

