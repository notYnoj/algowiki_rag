We claim that running (k-1)D LWS_<sub>n,d</sub>_ algorithm with

\(w_\ell[i_1,\dots,i_k]=\langle y_{1,i_1},\dots,y_{k,i_k}\rangle\)

for all \(\ell\) will give us \(T[kn,\dots,kn]=\mathrm{min}\langle x_{1,i_1},\dots,x_{k,i_k}\rangle\). First notice that by our construction, when \((i_1,\dots,i_{k-1})\notin[(k-1)n+1,kn]^{k-1}\), we have \(w_\ell[i_1,\dots,i_k]=0\). Therefore, _T_\[_i_<sub>1</sub>_,...,i<sub>k</sub>_\]=0 for all (_i_<sub>1</sub>_,...,i<sub>k</sub>_) such that \((i_1,\dots,i_{k-1})\notin[(k-1)n+1,kn]^{k-1}\).

Now we use induction to show that<tbc>

\(T\big[(k-1)n+j_1,\dots,(k-1)n+j_{k-1}\big]=\mathrm{min}\big\langle x_{1,i_1},\dots,x_{k,i_k}\big\rangle\)

<tbc>where the minimum is taken over all \(1\le i_1\le j_1,\dots,1\le i_{k-1}\le j_{k-1}\) and \(1\le i_k\le n\). This would suffice because if \(j_\ell=n\) for all \(1\le\ell\le k-1\), we would get the minimal inner product. The base case is when \(j_\ell=1\) for all \(1\le\ell\le k-1\). Then we have

\(T\big[(k-1)n+1,\dots,(k-1)n+1\big]\)<br>
\(=\mathrm{min}_{1\le\ell\le k-1}\big\{\mathrm{min}_{1\le i_\ell<(k-1)n+1}\big\{T\big[(k-1)n+1,\dots,(k-1)n+1,i_\ell,(k-1)n+1,\dots,(k-1)n+1\big]+\)<br>
\(w_\ell\big[(k-1)n+1,\dots,(k-1)n+1,i_\ell\big]\big\}\big\}\)<br>
\(=\mathrm{min}_{1\le\ell\le k-1}\big\{\mathrm{min}_{1\le i_\ell<(k-1)n+1}\big\{w_\ell\big[(k-1)n+1,\dots,(k-1)n+1,i_\ell\big]\big\}\big\}\)<br>
\(=\mathrm{min}_{1\le\ell\le n}\big\langle x_{11},x_{21},\dots,x_{k-1,1},x_{k,\ell}\big\rangle.\)

For the induction step, we have

\(T\big[(k-1)n+j_1,\dots,(k-1)n+j_{k-1}\big]\)<br>
\(=\mathrm{min}_{1\le\ell\le k-1}\big\{\mathrm{min}_{1\le i_\ell<(k-1)n+j_\ell}\big\{T\big[(k-1)n+j_1,\dots,(k-1)n+j_{\ell-1},(k-1)n+i_\ell,(k-1)n+j_{\ell+1},\dots,(k-1)n+j_{k-1}\big]+\)<br>
\(w_\ell\big[(k-1)n+j_1,\dots,(k-1)n+j_{k-1},i_\ell\big]\big\}\big\}\)<br>
\(=\mathrm{min}_{1\le\ell\le k-1}\big\{\mathrm{min}_{1\le i_\ell<(k-1)n+1}\big\{w_\ell\big[(k-1)n+j_1,\dots,(k-1)n+j_{k-1},i_\ell\big]\big\},\)<br>
\(\mathrm{min}_{(k-1)n+1\le i_\ell<(k-1)n+j_\ell}\big\{T\big[(k-1)n+j_1,\dots,(k-1)n+j_{\ell-1},(k-1)n+i_\ell,(k-1)n+j_{\ell+1},\dots,(k-1)n+j_{k-1}\big]\big\}\big\}\)<br>
\(=\mathrm{min}_{1\le\ell\le k-1}\big\{\mathrm{min}_{1\le\ell\le n}\big\langle x_{1,j_1},\dots,x_{k-1,j_{k-1}},x_{k,\ell}\big\rangle,\)<br>
\(\mathrm{min}_{(k-1)n+1\le i_\ell<(k-1)n+j_\ell}\big\{T\big[(k-1)n+j_1,\dots,(k-1)n+j_{\ell-1},(k-1)n+i_\ell,(k-1)n+j_{\ell+1},\dots,(k-1)n+j_{k-1}\big]\big\}\big\}.\)

By induction hypothesis,<tbc>

\(\mathrm{min}_{(k-1)n+1\le i_\ell<(k-1)n+j_\ell}\big\{T\big[(k-1)n+j_1,\dots,(k-1)n+j_{\ell-1},(k-1)n+i_\ell,(k-1)n+j_{\ell+1},\dots,(k-1)n+j_{k-1}\big]\big\}\)

<tbc>is the minimum over all \(\langle x_{1,i_1},\dots,x_{1,i_k}\rangle\) over

\((i_1,\dots,i_k)\in[1,j_1]\times\dots[1,j_{\ell-1}]\times[1,j_\ell-1]\times[1,j_{\ell+1}]\times\dots\times[1,j_{k-1}]\times[1,n].\)

