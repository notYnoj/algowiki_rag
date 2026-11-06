**Definition 2.12** (LWS)**.** _Consider a sequence of n data items x_<sub>1</sub>_,...,x<sub>n</sub> and a weight matrix w of size_ \(n\times n\) _where_ \(w[i,j]\in\{-W,\dots,W,\infty\}\) _for all_ \(1\le i<j\le n\)_. The_ LWS _problem asks to determine T_\[_n_\]_, which is defined by the following DP formulation:_<tbc>

\(T[j]=\left\{\begin{array}{ c c }
0 & \text{\textit{if}}j=0 \\
\mathrm{min}_{0\le i<j}\left\{T[i]+w[i,j]\right\} & \text{\textit{otherwise}}.
\end{array}\right.\)

<tbc>Given a sequence of _n_ items, LWS computes a subsequence of those items which minimizes the total weight from the items chosen. We assume all the entries of _w_ can be accessed in _O_(1) time. Figure 4 captures the idea of LWS.

\[KPS17\] also defines a "static" version of LWS which is central to their reductions.

**Definition 2.13.** (\[Static\]LWS) _Fix an instance of_ LWS _with matrix w. Given intervals I_={_a,a_+1_,...,a+N_-1}_,J_={_a+N,a+N_+1_,...,a_+2_N_-1}_, together with correctly computed values T_\[_i_\] _for all_ \(i\in I\)_, the_ \[Static\]LWS _problem asks to determine_

\(T'[j]=\mathrm{min}_{i\in I}\left\{T[i]+w[i,j]\right\}\text{for all}j\in J.\)

\[Static\]LWS is a parallel, batch version of LWS that applies the LWS recurrence relation to many values of j at once, rather than to just a single _j_ value at a time. Indeed, we can compute all \(T'[j]\) values where \(j\in J\) in parallel because each \(T'[j]\) only depends on the _T_\[_i_\] values where \(i\in I\), not on any other \(T'[j]\) values.

We use the notation \(T'\) to highlight that \(T'[j]\) may not equal _T_\[_j_\] since \(T'[j]\) is computed with partial information (in _I_). Figure 5 captures the idea of \[Static\]LWS.

## 2.5 Higher Dimension LWS

We now define the core problems that this paper discusses again, which is a generalization of LWS to higher dimensions.

**Definition 2.14** (kD LWS)**.** _Fix a positive integer k. Consider_ (_k_+1)_-dimensional tensors_ \(w_1,\dots,w_\ell\) _such that_ \(w_\ell[i_1,\dots,i_k,j]\in\{-W,\dots,W,\infty\}\) _for all_ \(1\le i_1,\dots,i_k,j\le n,1\le\ell\le k\)_. The_ kD LWS _problem asks to determine T_\[_n,...,n_\] _given the dynamic programming recurrence relation:_

\(T\big[j_1,j_2,\dots,j_k\big]=\left\{\begin{array}{ c c }
0 & \text{if}j_1=j_2=\dots=j_k=1 \\
\mathrm{min}_{1\le\ell\le k}\left\{\mathrm{min}_{1\le i_\ell<j_\ell}\left\{T\big[j_1,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]+w_\ell\big[j_1,j_2,\dots,j_k,i_\ell\big]\right\}\right\} & \text{otherwise}.
\end{array}\right.\)

T
0
i
j

T
0
a
a+N
j
a+2N

Figure 4: LWS. To compute the value of \(T'[j]\) (black circle), we start from _T_\[0\] and go through all possible _T_\[_i_\] such that \(1\le i<j\le n\) and takes the minimum of all possible values (plus their respective weight values _w_).

Figure 5: \[Static\]LWS. To compute \(T'[j]\) (black circle), we take the minimum of all possible white circles from _T_\[_a_\] to _T_\[_a+N_-1\] (plus their respective weight values _w_).

