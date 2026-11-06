**Algorithm 4** RESTARTPHASEDCLIP-1BITBAI

Require: arms A=\[_K_\], variance proxy \(\sigma\), accuracy \(\varepsilon\), confidence \(\delta\), anchors \((c_k)_{k=1}^K\) or range \(\lambda\)<br>
if anchors are not supplied then<br>
   for k=1,...,K do<br>
   \(c_k\leftarrow\text{MEDIANEST}(k,\lambda,\sigma,\delta/(2K))\)<br>
   end for<br>
   Set \(\delta_0\leftarrow\delta/2\)<br>
   else<br>
   Set \(\delta_0\leftarrow\delta\)<br>
   end if<br>
   Set \(J\leftarrow\lceil log_2(\sigma/\varepsilon)\rceil\), active set \(A\leftarrow\mathcal{A}\), and \(\gamma\leftarrow\delta_0/[K(J+1)]\)<br>
   for j=0,1,...,J do<br>
   Set \(\rho_j\leftarrow 2^{-j}\sigma\), \(L_j\leftarrow 32\sigma^2/\rho_j\), \(r_j\leftarrow\rho_j/16\)<br>
   for \(k\in A\) do<br>
   Restart a fresh phase list \(\mathcal{Z}_{k,j}\leftarrow\emptyset\)<br>
   end for<br>
   loop<br>
   for \(k\in A\) do<br>
   if |Z<sub>k,j</sub>|=0 then<br>
   \(\beta_{k,j}\leftarrow+\infty\), \(\text{LCB}_{k,j}\leftarrow-\infty\), \(\text{UCB}_{k,j}\leftarrow+\infty\)<br>
   else<br>
   \(N_{k,j}\leftarrow|\mathcal{Z}_{k,j}|\), \(\widehat{\mu}_{k,j}\leftarrow c_k+N_{k,j}^{-1}\sum_{Z\in\mathcal{Z}_{k,j}}Z\)<br>
   \(\beta_{k,j}\leftarrow\beta_j(N_{k,j})\)<br>
   \(\text{LCB}_{k,j}\leftarrow\widehat{\mu}_{k,j}-\beta_{k,j}\), \(\text{UCB}_{k,j}\leftarrow\widehat{\mu}_{k,j}+\beta_{k,j}\)<br>
   end if<br>
   end for<br>
   \(m\leftarrow max_{i\in A}\text{LCB}_{i,j}\) and remove every \(k\in A\) with \(\text{UCB}_{k,j}<m-\varepsilon\)<br>
   if |A|=1 then<br>
   return the unique arm in A<br>
   end if<br>
   \(h\leftarrow argmax_{k\in A}\text{LCB}_{k,j}\), \(\ell\leftarrow argmax_{a\in A\backslash\{h\}}\text{UCB}_{a,j}\)<br>
   if \(\text{UCB}_{\ell,j}-\text{LCB}_{h,j}\le\varepsilon\) then<br>
   return h<br>
   end if<br>
   if \(max_{k\in A}\beta_{k,j}\le r_j\) then<br>
   if j=J then<br>
   return h<br>
   else<br>
   break and move to phase j+1<br>
   end if<br>
   end if<br>
   if \(max\{\beta_{h,j},\beta_{\ell,j}\}>r_j\) then<br>
   \(k_t\leftarrow argmax_{a\in\{h,\ell\}}\beta_{a,j}\)<br>
   else<br>
   \(k_t\leftarrow argmax_{a\in A}\beta_{a,j}\)<br>
   end if<br>
   Append TAILINTEGRALQUERY\((k_t,c_{k_t},L_j,\sigma)\) to Z<sub>k<sub>t</sub>,j</sub><br>
   end loop<br>
end for

## F Numerical experiment details

### F.1 1-bit mean estimation

### Experimental setting.

We compare our tail-integral estimator with the estimator of \[21\] on three scalar distributions: Normal\((\mu,1)\), Student-t(5) scaled to variance 1, and a shifted exponential law<tbc>

