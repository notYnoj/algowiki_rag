## 3.2 Slice Rank 2D LWS

In this section, we show that 2D LWS, \[Static\]2D LWS with even slice rank 3 is APSP-hard, but 2D LWS,\[Static\]2D LWS with slice rank 1 is truly sub-cubic.

**Theorem 3.5.** _Assuming the_ APSP _conjecture, there is no truly sub-cubic algorithm for_ 2D LWS _with slice rank_ 3.

_Proof._ We reduce NegativeTriangle to 2D LWS with slice rank 3. Given an undirected graph _G_=(_V,E_) where _V_={_v_<sub>1</sub>_,...,v<sub>n</sub>_}, we use _w_ to denote the weight function of an edge or a triangle. For convenience we let \(w(v_a,v_a)=\infty\). We define both our tensors to be<tbc>

\(\alpha[i,j,k]=f_1(i,k)\cdot g_1(j)+f_2(i,j)\cdot g_2(k)+f_3(k,j)\cdot g_3(i),\)

<tbc>where

\(f_1(i,k)=\left\{\begin{array}{ c c }
w(v_{i-n},v_k) & \text{if}i\in[n+1,2n],k\in[1,n] \\
0 & \text{otherwise}
\end{array}\right.,g_1(j)=\left\{\begin{array}{ c }
1\text{if}j\in[n+1,2n] \\
0\text{otherwise}
\end{array}\right.\)<br>
\(f_2(i,j)=\left\{\begin{array}{ c c }
w(v_{i-n},v_{j-n}) & \text{if}i,j\in[n+1,2n] \\
0 & \text{otherwise}
\end{array}\right.,g_2(k)=\left\{\begin{array}{ c }
1\text{if}k\in[1,n] \\
0\text{otherwise}
\end{array}\right.\)<br>
\(f_3(k,j)=\left\{\begin{array}{ c c }
w(v_k,v_{j-n}) & \text{if}k\in[1,n],j\in[n+1,2n] \\
0 & \text{otherwise}
\end{array}\right.,g_3(i)=\left\{\begin{array}{ c }
1\text{if}i\in[n+1,2n] \\
0\text{otherwise}
\end{array}\right.\)

We claim that running 2D LWS with \(\alpha\) will solve the NegativeTriangle instance by _T_\[2_n,_2_n_\] being the minimum weight of all triangles. In fact, we prove that for all \(n+1\le i,j\le 2n\), _T_\[_i,j_\] is the minimum weight of all triangles _v<sub>a</sub>,v<sub>b</sub>,v<sub>c</sub>_ such that \(1\le a\le i-n,1\le b\le j-n,1\le c\le n\).

Observe that:

• When \(i,j,k\in[1,n]\), we have \(\alpha[i,j,k]=0\). Therefore, _T_\[_i,j_\]=0 for all \(1\le i,j\le n\).<tbc>

• When \(i\in[n]\) and \(j\in[n+1,2n]\), \(\alpha[i,j,k]=0\). Therefore, _T_\[_i,j_\]=0 when \(i\in[n],j\in[n+1,2n]\).<tbc>

• When \(j\in[n]\) and \(i\in[n+1,2n]\), \(\alpha[i,j,k]=0\). Therefore, _T_\[_i,j_\]=0 when \(j\in[n],j\in[n+1,2n]\).<tbc>

• When \(i,j\in[n+1,2n]\), \(\alpha[i,j,k]=w(v_{i-n},b_{j-n},v_k)\) if \(k\in[n]\) and \(\alpha[i,j,k]=0\) if \(k\in[n+1,2n]\).

Finally, we use induction on (_i,j_) to prove the claim. When _i=j=n_+1, we have<tbc>

\(T[n+1,n+1]=min_{1\le k\le n}\left\{\alpha[n+1,n+1,k]\right\}=min_{1\le k\le n}\left\{w(v_{i-n},v_{j-n},v_k)\right\}=\infty.\)

<tbc>When _i=n_+2_,j=n_+1,<tbc>

\(T[n+2,n+1]=min_{1\le k\le n}\left\{\alpha[n+2,n+1,k]\right\}=min_{1\le k\le n}\left\{w(v_2,v_1,v_k)\right\}.\)

<tbc>Similarly, when _i=n_+1_,j=n_+2,<tbc>

\(T[n+1,n+2]=min_{1\le k\le n}\left\{w(v_1,v_2,v_k)\right\}.\)

<tbc>Now for general \((i,j)\in[n+1,2n]^2\), we have

\(T[i,j]=min\left\{min_{1\le k<i}\left\{T[k,j]+\alpha[i,j,k]\right\},min_{1\le k<j}\left\{T[i,k]+\alpha[i,j,k]\right\}\right\}\)<br>
\(=min\left\{min_{1\le k\le n}\left\{T[k,j]+\alpha[i,j,k]\right\},min_{n+1\le k<i}\left\{T[k,j]+\alpha[i,j,k]\right\},min_{1\le k\le n}\left\{T[i,k]+\alpha[i,j,k]\right\},\)<br>
\(min_{n+1\le k<j}\left\{T[i,k]+\alpha[i,j,k]\right\}\right\}\)<br>
\(=min\left\{min_{1\le k\le n}\left\{w(v_{i-n},v_{j-n},v_k)\right\},min_{n+1\le k<i}\left\{T[k,j]\right\},min_{n+1\le k<j}\left\{T[i,k]\right\}\right\}.\)

