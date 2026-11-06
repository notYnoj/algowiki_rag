Thus we are taking the minimum over all (_i_<sub>1</sub>_,...,i<sub>k</sub>_) in

\(\{j_1\}\times\dots\times\{j_k\}\times[1,n]\bigcup_{1\le\ell\le k-1}\left([1,j_1]\times\dots[1,j_{\ell-1}]\times[1,j_\ell-1]\times[1,j_{\ell+1}]\times\dots\times[1,j_{k-1}]\times[1,n]\right)=[1,j_1]\times\dots\times[1,j_{k-1}]\times[1,n],\)

which concludes the induction.

**Theorem 3.2.** (kD LWS \(\rightarrow[\mathsf{Static}]\mathsf{kD LWS}\)) _Suppose there exists an algorithm for_ \[Static\]kD LWS<sub>_n,N,d_</sub> _with running time_ \(O(N^{2-\varepsilon}\cdot n^{k-1})\) _for some_ \(\varepsilon>0\)_, then there exists an algorithm for_ kD LWS<sub>_n,d_</sub> _with running time_ \(O(n^{k+1-\delta})\) _for some_ \(\delta>0\).

_Proof._ Given an kD LWS instance, we define a subproblem<tbc>

\(\mathcal{S}\big(D_{\alpha,\beta},\big\{t\big[j_1,\dots,j_k\big]:(j_1,\dots,j_k)\in D_{\alpha,\beta}\big\}\big)\)

<tbc>as follows: Given \(D_{\alpha,\beta}\) and _t_\[_j_<sub>1</sub>_,...,j<sub>k</sub>_\] for all \((j_1,\dots,j_k)\in D_{\alpha,\beta}\) where<tbc>

\(t\big[j_1,\dots,j_k\big]=min_{1\le\ell\le k}\big\{min_{1\le i_\ell<\alpha-J_\ell}\big\{T\big[j_1,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]+w_\ell\big[j_1,\dots,j_k,i_\ell\big]\big\},\infty\big\},\)

<tbc>computes<tbc>

\(T\big[j_1,\dots,j_k\big]=min_{1\le\ell\le k}\big\{min_{1\le i_\ell<j_\ell}\big\{T\big[j_1,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]+w_\ell\big[j_1,\dots,j_k,i_\ell\big]\big\}\big\}\)

<tbc>for all \((j_1,\dots,j_k)\in D_{\alpha,\beta}\). Notice that a call<tbc>

\(\mathcal{S}\big(D_{k,kn},\big\{t\big[j_1,\dots,j_k\big]:(j_1,\dots,j_k)\in D_{k,kn}\big\}\big)\)

<tbc>with

\(t\big[j_1,\dots,j_k\big]=\left\{\begin{array}{ c c }
w_\ell\big[j_1,\dots,j_k,1\big] & \text{if}j_\ell=1\text{for some}\ell \\
\infty & \text{otherwise}
\end{array}\right.\)

will solve the instance because only those who have a coordinate with 1 will be assigned a value.

Now we solve S using Algorithm 1 below.

To see that the algorithm is correct, we use induction on \(\beta-\alpha\). When \(\alpha=\beta\) we want to compute _T_\[_j_<sub>1</sub>_,...,j<sub>k</sub>_\] for all \((j_1,\dots,j_k)\in D_\alpha\), but by definition _t_\[_j_<sub>1</sub>_,...,j<sub>k</sub>_\]=_T_\[_j_<sub>1</sub>_,...,j<sub>k</sub>_\] so we are done.

Now line 4 of the algorithm correctly outputs \(\big\{T\big[j_1,\dots,j_k\big]:(j_1,\dots,j_k)\in D_{\alpha,\alpha+m-1}\big\}\) because we input the correct \(t\big[j_1,\dots,j_k\big]\) and by induction hypothesis. In line 6 we compute for all \((j_1,\dots,j_k)\in D_{\alpha+m,\beta-1}\):

\(t'\big[j_1,\dots,j_k\big]=min\big\{t\big[j_1,\dots,j_k\big],T'\big[j_1,\dots,j_k\big]\big\}\)<br>
\(=min\big\{min_{1\le\ell\le k}\big\{min_{1\le i_\ell<\alpha-J_\ell}\big\{T\big[j_1,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]+w\big[j_1,\dots,j_k,i_\ell\big]\big\}\big\},\)<br>
\(min_{1\le\ell\le k}\big\{min_{\alpha-J_\ell\le i_\ell<\alpha+m-J_\ell}\big\{T\big[j_1,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]+w\big[j_1,\dots,j_k,i_\ell\big]\big\}\big\}\big\}\)<br>
\(=min_{1\le\ell\le k}\big\{min_{1\le i_\ell<\alpha+m-J_\ell}\big\{T\big[j_1,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]+w\big[j_1,\dots,j_k,i_\ell\big]\big\}\big\}.\)

Therefore, these are the correct values for all \((j_1,\dots,j_k)\in D_{\alpha+m,\beta-1}\) for applying S again in line 7, where we correctly output \(\big\{T\big[j_1,\dots,j_k\big]:(j_1,\dots,j_k)\in D_{\alpha+m,\beta-1}\big\}\). Finally, if \(\beta-\alpha=2m\), our algorithm computes<tbc>

