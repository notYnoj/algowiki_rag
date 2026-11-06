_Proof._ Let us consider the constant-ratio case where \(\alpha=\Omega(1)\). In which case, we have<tbc>

\(\mathrm{SD}_M(A(l,r],B(l,r])=\frac{B_{\Sigma(l,r]}}{A_{\Sigma(l,r]}}\mathrm{TD}_M(A(l,r])=O(\mathrm{TD}_M(A(l,r]))\)

<tbc>(when \(A_{\Sigma(l,r]}=0\), this term becomes 0 by definition of scaled total deviation, which is also _O_(TD_<sub>M</sub>(A(l,r_])) since total deviation is non-negative). Therefore, we have

\(\includegraphics{}\mathrm{SD}_{M,S}(A,B)=\sum_{s\in[S]}\sum_{(l,r]\in s}\mathrm{SD}_M(A(l,r],B(l,r])\)<br>
\(=\sum_{s\in[S]}\sum_{(l,r]\in s}O(\mathrm{TD}_M(A(l,r]))\)<br>
\(=O(\includegraphics{}\mathrm{TD}_{M,S}(A))\)<br>
\(=O\left(\left(\sum_xa_x\right)S^{0.51}+\mathrm{max}_{x^\prime}\left(a_{x^\prime}\right)\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right)\text{(from Lemma 4.1).}\)

Since \(\alpha=\Omega(1)\), we have \(B_{\Sigma(0,n]}=\Omega(A_{\Sigma(0,n]})\). Thus we also have

\(\includegraphics{}\mathrm{SD}_{M,S}(A,B)=O\left(\left(\sum_xb_x\right)S^{0.51}+\mathrm{max}_{x^\prime}\left(a_{x^\prime}\right)\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right).\) (6)

Before going into the fully general case, we partially generalize (6) by stating that it holds when for some \(\alpha\le\beta\le 1\) we have

\(B_{\Sigma(l,r]}=\Theta(\beta A_{\Sigma(l,r]})\)

for every recursion interval (_l,r_\] (i.e., the _B_-to-_A_ ratio falls within an _O_(1)-narrow range for every recursion interval). To see this, we can easily see that \(\includegraphics{}\mathrm{SD}\) is a linear function of _B_: for any \(\gamma\in\mathbb{R}\),

\(\includegraphics{}\mathrm{SD}_{M,S}(A,\gamma\cdot B)=\gamma\cdot\includegraphics{}\mathrm{SD}_{M,S}(A,B),\)

where \(\gamma\cdot b\) is the element-wise product of \(\gamma\) and _B_. Note that the case with _A_ and \((1/\beta)\cdot B\) falls into the constant-ratio case above. We have

\(\includegraphics{}\mathrm{SD}_{M,S}(A,B)=\beta\cdot\includegraphics{}\mathrm{SD}_{M,S}(A,(1/\beta)\cdot B)\text{from linearity}\)<br>
\(=\beta\cdot O\left(\left(\sum_x\left(b_x/\beta\right)\right)S^{0.51}+\mathrm{max}_{x^\prime}\left(a_{x^\prime}\right)\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right)\text{from (6)}\)<br>
\(=O\left(\left(\beta\cdot\sum_x\left(b_x/\beta\right)\right)S^{0.51}+\beta\cdot\mathrm{max}_{x^\prime}\left(a_{x^\prime}\right)\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right)\)<br>
\(=O\left(\left(\beta\cdot\sum_x\left(b_x/\beta\right)\right)S^{0.51}+\mathrm{max}_{x^\prime}\left(a_{x^\prime}\right)\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right)\text{since}\beta\le 1\)<br>
\(=O\left(\left(\sum_xb_x\right)S^{0.51}+\mathrm{max}_{x^\prime}\left(a_{x^\prime}\right)\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right).\)

