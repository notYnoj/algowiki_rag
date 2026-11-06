**Definition 1.2.** (\[Static\]kD LWS) _Given intervals D_<sub>_a,a+N_</sub>_,D_<sub>_a+N,a_+2_N_</sub> _together with correctly computed values T_\[_i_<sub>1</sub>_,...,i<sub>k</sub>_\] _for all_ \(1\le\ell\le k\) _and_ \((i_1,\dots,i_k)\in D_{a,a+N}\), \[Static\]kD LWS _asks to determine_

\(T'\big[j_1,\dots,j_k\big]=min_{1\le\ell\le k}\left\{min_{a-I_\ell\le i_\ell<a+N-I_\ell}\big\{T\big[j_1,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]+w_\ell\big[j_1,j_2,\dots,j_k,i_\ell\big]\big\}\right\}\)

_for all_ \((j_1,j_2,\dots,j_k)\in D_{a+N,a+2N}\).

For illustration purposes, consider the \[Static\]2D LWS problem: given correctly computed values _T_\[_i,j_\] for all \((i,j)\in D_{a,a+N}\), determine

\(T'[i,j]=min\left\{min_{a-i\le k<a+N-i}\{T[k,j]+w_1[i,j,k]\}min_{a-j\le k<a+N-j}\{T[i,k]+w_2[i,j,k]\}\right.\)

for all \((i,j)\in D_{a+N,a+2N}\). Figure 3 depicts the idea.

## 1.4 Polygon Triangulation

kD LWS as we defined above captures many different high-dimensional DP problems, but it is not the only conceivable way to generalize LWS. We consider here another example we call 2D LWS<sup>PT</sup>, which captures optimization over sets that are counted by the Catalan numbers.

j
1
T
1
i

D+N,a+2N
D+N,a+2N
j
T
i

Figure 2: 2D LWS. To compute _T_\[_i,j_\], we take the minimum of all possible white circles (plus their respective tensor values _w_) such that their coordinates differ from the target by one coordinate.

Figure 3: \[Static\]2D LWS. To calculate \(T'[i,j]\) (black circle), we take the minimum over all possible white circles (plus their respective weight values _w_) such that they share all but one coordinate with _T_\[_i,j_\].

