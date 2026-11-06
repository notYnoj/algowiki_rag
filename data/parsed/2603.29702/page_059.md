We can see that \(\mathcal{P}_0=w(\widehat{p})\), and that \(\mathcal{P}_S=\mathrm{est}[0,n_X,n_X+n_Y,n_Y]\), namely our final estimate for \(w(\widehat{p})\). We want to know how much smaller P_<sub>S</sub>_ can be compared to P<sub>0</sub>.

The important part of the upcoming analysis will be to analyze the error due to outliers. Namely, we want to argue on average, for an interval (_l,r_\] on an active scale, the estimates from sub-intervals, or \(\mathrm{est}[m_{i-1},\widehat{p}(m_{i-1}),m_i,\widehat{p}(m_i)]\)’s, are "balanced," as is required by Claim 7.8. The main technicality is that there is already error inside each \(\mathrm{est}[m_{i-1},\widehat{p}(m_{i-1}),m_i,\widehat{p}(m_i)]\), and the errors can have a cascading effect: if estimates inside a subset of sub-intervals have a large error, it can make the estimates across sub-intervals imbalanced, thereby also giving the parent interval a large error.

To better analyze this cascading effect, we first obtain a lower bound \(\mathrm{est}'\) for est in the following way:

\(\mathrm{est}'[l,y_l,r,y_r]:=\left\{\begin{array}{ c c }
\mathrm{ew}[l,y_l,r,y_r], & \text{if}s=0 \\
\mathrm{max}_{\widehat{Y}\in\text{\textbf{L}}}\sum_{i=1}^M\mathrm{est}'[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i], & \text{if}s\notin\widetilde{S}, \\
\mathrm{min}\left(w(\widehat{p}(l,r]),\text{\textbf{EstSUM}}\left((\mathrm{est}'[m_{i-1},\overline{y_i},m_i,\overline{y_i}])_{\eta_{l,r,i}=i|i\in[M]}\right)\right) & \text{if}s\in\widetilde{S}
\end{array}\right.\)

Namely, we do the same recursion scheme as in est, but on active scales, we clamp our estimates on interval (_l,r_\] down to at most \(w(\widehat{p}(l,r])\). Note that this clamping is not algorithmic and we use it for analysis purposes only. The purpose of this lower bound is that it makes errors one-directional: for every recursion interval (_l,r_\] we have \(\mathrm{est}'[l,\widehat{p}(l),r,\widehat{p}(r)]\le w(\widehat{p}(l,r])\). Moreover, \(\mathrm{est}'\) is indeed a lower bound for est: observe that EstSum is monotone. Namely if we have two sets of inputs \(A_I,A'_I\) such that \(a_i\le a_i^{^\prime}\) for every \(i\in I\), then \(\text{EstSUM}(A_I)\le\text{EstSUM}(A'_I)\). This means that we always have \(\mathrm{est}'[l,y_l,r,y_r]\le\mathrm{est}[l,y_l,r,y_r]\).

For each active scale _s_, if there were no subsampling on active scales larger than _s_, we can see that the final estimate would be at least:

\(\mathcal{P}_s^{^\prime}:=\sum_{i=1}^{n/I_s}\mathrm{est}'[(i-1)\cdot I_s,\widehat{p}((i-1)\cdot I_s),i\cdot I_s,\widehat{p}(i\cdot I_s)].\)

We can see that \(\mathcal{P}_0^{^\prime}=w(\widehat{p})\), and that \(\mathcal{P}_S^{^\prime}=\mathrm{est}'[0,n_X,n_X+n_Y,n_Y]\le\mathrm{est}[0,n_X,n_X+n_Y,n_Y]\), namely \(\mathcal{P}_s^{^\prime}\) is a lower bound for our final estimate for \(w(\widehat{p})\). To see how much smaller \(\mathcal{P}_S^{^\prime}\) can be compared to \(\mathcal{P}_0^{^\prime}\), we go through each scale _s_ and examine the difference between \(\mathcal{P}_{s-1}^{^\prime}\) and \(\mathcal{P}_s^{^\prime}\).

If scale-_s_ is passive, then since we compute every \(\mathrm{est}'[l,\widehat{p}(l),r,\widehat{p}(r)]\) to be the length of the longest \(\widetilde{S}\)-regular \(\langle l,\widehat{p}(l)\rangle\)-\(\langle r,\widehat{p}(r)\rangle\) path in the Scale-(_s_-1) Sparsified Grid Graph (defined on \(\mathrm{est}'\)), \(\mathcal{P}_s^{^\prime}\ge\mathcal{P}_{s-1}^{^\prime}\).

If scale-_s_ is active, fix a scale-_s_ interval (_l,r_\]. From Claim 7.8, we can have at most the following types of errors:

• Type I: A multiplicative error of \(1-O\left(\frac{1}{\mathrm{log}^{0.02}(n)}\right)\);<tbc>

• Type II: If \(\mathrm{max}_i\mathrm{est}'[m_{i-1},\widehat{p}(m_{i-1}),m_i,\widehat{p}(m_i)]=\Omega\left(\frac{\mathrm{log}^{0.02}(n)}{M}\sum_i\mathrm{est}'[m_{i-1},\widehat{p}(m_{i-1}),m_i,\widehat{p}(m_i)]\right)\), an additive underestimation of at most \(w(\widehat{p}(l,r])\) (since our estimate is non-negative);<tbc>

• Type III: With probability \(\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\), an additive underestimation of at most \(w(\widehat{p}(l,r])\).

We can first see that with probability 1-_o_(1) the multiplicative error accumulated over \(\widetilde{S}\) (whose size is \(O(S^{0.02})=o\left(\mathrm{log}^{0.02}(n)\right)\) with probability 1-_o_(1)) active scales is 1-_o_(1).

The total sum of type III error is at most \(\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\) times the total sum of \(w(\widehat{p}(l,r])\) on every interval (_l,r_\] on an active scale. The total sum of \(w(\widehat{p}(l,r])\) is at most \(O(w(\widehat{p})\left|\widetilde{S}\right|)\) and the total total sum of type III error is at most \(w(\widehat{p})\cdot\left|\widetilde{S}\right|\cdot\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)=o(w(\widehat{p}))\).

