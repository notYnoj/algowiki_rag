the minimum over all \(i_\ell\) such that \((j_1,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k)\in D_{1,\beta-1}\), so we are outputting the correct values.

The runtime of our algorithm for S, when \(\beta-\alpha=N\), can be expressed as<tbc>

\(T_\mathcal{S}(n,N)\le 2T_\mathcal{S}\big(n,\frac{N}{2}\big)+T_\text{Static}\big(n,\frac{N}{2}\big)+O(Nn^{k-1})\)

<tbc>because we have 2 recursive calls with size \(\frac{N}{2}\) , run a \[Static\] algorithm with length \(\frac{N}{2}\) , and computes \(t'[i_1,\dots,i_k]\) for _O(Nn_<sup>_k_-1</sup>) values. By assumption we have \(T_\text{Static}\big(\frac{N}{2}\big)\le O(N^{2-\varepsilon} n^{k-1})\), so this recursive formula becomes<tbc>

\(T_\mathcal{S}(n,N)\le 2T_\mathcal{S}\big(n,\frac{N}{2}\big)+O(N^{2-\varepsilon} n^{k-1}).\)

<tbc>Solving it gives \(T_\mathcal{S}(n,N)\le O(N^{2-\varepsilon}\cdot n^{k-1}\cdot\mathrm{log}N)\le O(N^{2-\delta} n^{k-1})\) for some \(\delta>0\). Therefore,

\(T_\mathcal{S}(n,n)\le O(n^{k+1-\delta}).\)

Since SAT reduces to kMin-IP<sub>_n,_2<sup>_O_(log<sup>∗</sup>_n_)</sup></sub> (Appendix A), we immediately get hardness results of kD LWS and \[Static\]kD LWS from SETH:

**Corollary 3.3.** _Assuming_ SETH_, there is no_ \(O(n^{k+1-\varepsilon})\) _time algorithm for_ kD LWS _or_ \[Static\]kD LWS _with rank at least_ 2<sup>_O_(log<sup>∗</sup>_n_)</sup> _for any_ \(\varepsilon>0\).

Finally, we show that just like kMin-IP, \[Static\]kD LWS also exhibits a hierarchy.

**Theorem 3.4.** (\[Static\]kD LWS \(\rightarrow[\text{Static}]\)(k-1)D LWS) _Suppose there exists an algorithm for_ \[Static\](k-1)D LWS<sub>_n,N,d_</sub> _with running time_ \(O(N^{2-\varepsilon}\cdot n^{k-2})\) _for some_ \(\varepsilon>0\)_, then there exists an algorithm for_ \[Static\]kD LWS<sub>_n,N,d_</sub> _with running time_ \(O(N^{2-\delta}\cdot n^{k-1})\) _for some_ \(\delta>0\).

_Proof._ Given an \[Static\]kD LWS<sub>_n,d_</sub> instance with _D_<sub>_a,a+N_</sub>_,D_<sub>_a+N,a_+2_N_</sub> together with correctly computed values _T_\[_j_<sub>1</sub>_,...,j<sub>k</sub>_\] for all \(1\le\ell\le k,(i_1,\dots,i_k)\in D_{a,a+N}\), we want to compute<tbc>

\(T\big[j_1,\dots,j_k\big]=\mathrm{min}_{1\le\ell\le k}\big\{\mathrm{min}_{a-J_\ell\le i_\ell<a+N-J_\ell}\big\{T\big[j_1,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]+w_\ell\big[j_1,\dots,j_k,i_\ell\big]\big\}\big\}\)

<tbc>for all \((j_1,j_2,\dots,j_k)\in D_{a+N,a+2N}\). Fix some \(n-a-N\le j\le n\). For any \((j,j_2,\dots,j_k)\in D_{a+N,a+2N}\) we have

\(T\big[j,j_2,\dots,j_k\big]=\mathrm{min}_{1\le\ell\le k}\big\{\mathrm{min}_{a-J_\ell\le i_\ell<a+N-J_\ell}\big\{T\big[j,j_2,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]+w_\ell\big[j,j_2,\dots,j_k,i_\ell\big]\big\}\big\}\)<br>
\(=\mathrm{min}\big\{\mathrm{min}_{2\le\ell\le k}\big\{\mathrm{min}_{1\le i_\ell<j_\ell}}T\big[j,j_2,\dots,j_{\ell-1},i_{\ell-1},j_{\ell+1},\dots,j_k\big]+w_\ell\big[j,j_2,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]\big\},\)<br>
\(\mathrm{min}_{1\le i_1<j_1}\big\{T\big[i_1,j_2,\dots,j_k\big]+w_1\big[i_1,j_2,\dots,j_k\big]\big\}\big\}\)

We can compute the first term in the minimum using a \[Static\](k-1)D LWS algorithm with time \(O(N^{2-\varepsilon}\cdot n^{k-2})\) and the second term using a LWS algorithm with time at most \(O(N^2\cdot n)\). This is because after we fix _j_, _w_\[_j,..._\] still has rank _d_ but one less dimension. Repeat this process for all the _j_ on all _k_ coordinates to solve \[Static\]kD LWS, and the total running time is at most

\(kn\cdot\big(O(N^2\cdot n)+O(N^{2-\varepsilon}\cdot n^{k-2})\big)=O(N^{2-\delta}\cdot n^{k-1})\)

for some \(\delta>0\).

