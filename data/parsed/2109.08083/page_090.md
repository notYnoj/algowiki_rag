<tbc>In addition we have that every \(\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}\) appears in \(\sum_{e\in H_i}\mathcal{P}_{e,2}\) at most when any of the \(\genfrac(){pt}{2}{l}{2}\) pairs from \(\bar{v}\) are in an edge \(e\in H_i\), and so it follows that<tbc>

\(\sum_{e\in H_i}\mathcal{P}_{e,2}\le\genfrac(){pt}{2}{l}{2}\Delta^{1-\eta}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v}).\)

<tbc>Hence, using Bernstein’s inequality with parameter \(\frac{\Delta^{1-\eta}}{s}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\), we get that whp<tbc>

\(\Gamma_i<\frac{1}{s}\genfrac(){pt}{2}{l}{2}\Delta^{1-\eta}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})+\frac{\Delta^{1-\eta}}{s}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\le\frac{l^2\Delta^{1-\eta}}{s}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p(\bar{v}),\)

<tbc>for every _i_, and so whp

\(\Gamma<\frac{tl^2\Delta^{1-\eta}}{s}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p(\bar{v})<\Delta^{-20Lr\epsilon}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v}).\)

□

Now, since \(\prod_{v\in\bar{v}}\frac{d_H(v)}{\Delta}\ge\left(\frac{\delta(H)}{\Delta}\right)^l\ge\Delta^{-\frac{\eta}{5Lr}}\), we have that<tbc>

\(\Gamma\le\Delta^{-20Lr\epsilon+\frac{\eta}{5Lr}}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}\frac{d_H(v)}{\Delta}=\Delta^{-10Lr\epsilon}\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}\frac{d_H(v)}{\Delta}.\)

<tbc>Thus using (6.8),

\(\sum_{\bar{v}\in\genfrac(){pt}{2}{V(M)}{l}}p_l(\bar{v})=\left(1\pm\frac{\Delta^{-\epsilon}}{2}\right)\left(1\pm\left(\frac{l^2r}{\Delta^{\eta-\psi}}+\Delta^{-10Lr\epsilon}\right)\right)\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}\frac{d_H(v)}{\Delta}\)<br>
\(=\left(1\pm\frac{2\Delta^{-\epsilon}}{3}\right)\sum_{\bar{v}\in\genfrac(){pt}{2}{V(H)}{l}}p_l(\bar{v})\prod_{v\in\bar{v}}\frac{d_H(v)}{\Delta},\)

as required. □

Finally we prove Theorem 6.2.

Proof of Theorem 6.2. By Corollary 6.4 we know that there exists a distribution on matchings _M_ in _H_ such that the theorem holds with high probability for each \(q\in\mathcal{Q}\) individually. The same distribution on matchings _M_ in _H_ is used to obtain Theorem 6.6. Thus we prove the theorem by showing that whp the conclusion of the theorem holds for any individual \(l\in[L]\) and \(p_l\in\mathcal{P}_l\). We prove this via precisely the same strategy as that for proving Corollary 6.4, but now appealing to Theorem 6.6. In particular, from (_H,w_) we define an unweighted multigraph \(H'\) where \(V(H')=V(H)\) and every edge \(e\in E(H)\) appears in \(E(H')\) with multiplicity \(\lfloor Dw(e)\rfloor\), where \(D=\Delta^2\). Recall, as in the proof of Corollary 6.4, that \(Dw(e)\ge\Delta\) yielding \(\lfloor Dw(e)\rfloor=(1\pm\Delta^{-1})Dw(e)\), \(\Delta(H')=max_{v\in V(H)}\sum_{e\unknown v}\lfloor Dw(w(e)\rfloor\le D\), and

\(\Delta^\mathrm{co}(H')=max_{\{u,v\}\in\genfrac(){pt}{2}{V(H)}{2}}\sum_{e\supseteq\{u,v\}}\lfloor Dw(e)\rfloor\le D\cdot\Delta^{-\eta}=D^{1-\frac{\eta}{2}}.\)

