1 if \(\alpha=\beta\) then<br>
Return<br>
\(T\big[j_1,j_2,\dots,j_k\big]=t\big[j_1,j_2,\dots,j_k\big]\)<br>
for all \((j_1,j_2,\dots,j_k)\in D_\alpha\)<br>
\(m\leftarrow\big\lceil\frac{\beta-\alpha}{2}\big\rceil\)<br>
\(\big\{T\big[j_1,j_2,\dots,j_k\big]:j_1,j_2,\dots,j_k\in D_{\alpha,\alpha+m}\big\}\leftarrow S\big(D_{\alpha,\alpha+m},\big\{t\big[j_1,j_2,\dots,j_k\big]\in D_{\alpha,\alpha+m}\big\}\big)\)<br>
Solve a \[Static\]kD LWS instance on \(D_{\alpha,\alpha+m},D_{\alpha+m,\beta}\) with correctly computed values<br>
\(\big\{T\big[j_1,j_2,\dots,j_k\big]:(j_1,j_2,\dots,j_k)\in D_{\alpha,\alpha+m}\big\}\)<br>
and output<br>
\(\big\{T'\big[j_1,j_2,\dots,j_k\big]:(j_1,j_2,\dots,j_k)\in D_{\alpha+m,\beta}\big\}\)<br>
Let \(t'\big[j_1,j_2,\dots,j_k\big]=\mathrm{min}\big\{t\big[j_1,j_2,\dots,j_k\big],T'\big[j_1,j_2,\dots,j_k\big]\big\}\) for all \((j_1,j_2,\dots,j_k)\in D_{\alpha+m,\beta}\)<br>
\(\big\{T\big[j_1,j_2,\dots,j_k\big]:(j_1,j_2,\dots,j_k)\in D_{\alpha+m,\beta}\big\}\leftarrow S\big(D_{\alpha+m,\beta},\big\{t'\big[j_1,j_2,\dots,j_k\big]:(j_1,j_2,\dots,j_k)\in D_{\alpha+m,\beta}\big\}\big)\)<br>
if \(\beta-\alpha=2m\) then<br>
\(T\big[j_1,j_2,\dots,j_k\big]=\mathrm{min}\big\{t\big[j_1,j_2,\dots,j_k\big],\mathrm{min}_{\alpha-J_\ell\le i_\ell<\beta-J_\ell}\big\{T\big[j_1,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]+w\big[j_1,\dots,j_k,i_\ell\big]\big\}\big\}\)<br>
for all \((j_1,j_2,\dots,j_k)\in D_\beta\).<br>
Return \(\big\{T\big[j_1,j_2,\dots,j_k\big]:(j_1,j_2,\dots,j_k)\in D_{\alpha,\beta}\big\}\)

**Algorithm 1:** \(\mathcal{S}\rightarrow[\mathsf{Static}]\mathsf{kD}\) LWS

