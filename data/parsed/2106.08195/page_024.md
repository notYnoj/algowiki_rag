**Algorithm 10** \[Lemma 6\] Approximating Matching Pairs (_x_<sub>1</sub>_,...,x<sub>n/m</sub>,y_<sub>1</sub>_,...,y<sub>n/m</sub>,q_)

**Require:** Strings _x_<sub>1</sub>_,...,x<sub>n/m</sub>,y_<sub>1</sub>_,...,y<sub>n/m</sub>_ of length _m_ over alphabet \(\Sigma\); a parameter _q\>_0

**Ensure:** For each \(i,j\in[n/m]\) computes \(\widetilde{M}_{ij}\) satisfying \(M_{ij}/8-q\le\widetilde{M}_{ij}\le 4M_{ij}\) w.h.p.

1: \(\widetilde{U}\leftarrow\emptyset\)

2: **for** \(i\in[n/m]\) **do**

3: **for** \(j\in[n/m]\) **do**

4: \(\widetilde{U}_{ij}\leftarrow\emptyset\)

5: \(\widetilde{M}_{ij}\leftarrow 0\)

6: \(G\leftarrow\) GraphConstruction(_x_<sub>1</sub>_,...,x<sub>n/m</sub>,y_<sub>1</sub>_,...,y<sub>n/m</sub>_)

7: we have _G_=(_V,E_) with \(V=L\cup U\cup R\)

8: **for** \((\sigma,\ell,r)\in U\) **do**

9: \(p_{\ell,r}\leftarrow min\{1,2^{\ell+r+3}/q\}\)

10: \(q_{\ell,r}\leftarrow 1\) with probability \(p_{\ell,r}\) and 0 otherwise

11: **if** \(q_{\ell,r}=1\) **then**

12: \(\widetilde{U}\leftarrow\widetilde{U}\cup\{(\sigma,\ell,r)\}\)

13: **for** \((\sigma,\ell,r)\in\widetilde{U}\) **do**

14: \(L_{(\sigma,\ell,r)}=\{i\in L|(i,(\sigma,\ell,r))\in E\}\)

15: \(R_{(\sigma,\ell,r)}=\{j\in R|(j,(\sigma,\ell,r))\in E\}\)

16: **for** \((\sigma,\ell,r)\in\widetilde{U}\) **do**

17: **for** \(i\in L_{(\sigma,\ell,r)}\) **do**

18: **for** \(j\in R_{(\sigma,\ell,r)}\) **do**

19: \(\widetilde{U}_{ij}\leftarrow\widetilde{U}_{ij}\cup\{(\sigma,\ell,r)\}\)

20: **for** \(i\in[n/m]\) **do**

21: **for** \(j\in[n/m]\) **do**

22: **for** \((\sigma,\ell,r)\in\widetilde{U}_{ij}\) **do**

23: \(\widetilde{M}_{ij}\leftarrow\overline{M_{ij}}+2^{\ell+r}/p_{\ell,r}\)

24: \(\widetilde{M}_{ij}\leftarrow\) repeat steps 1-23 for _c_log_n_ times and find the median of all <o>_M_</o><sub>ij</sub> for each _i,j_

25: **return** \(\widetilde{M}_{ij}\) for each _i,j_

## B.1.3 Single Symbol Approximation Algorithm

**Algorithm 11** \[Lemma 7\] Single Symbol Approximation (_x,y_)

**Require:** Strings _x,y_ of length _n_

**Ensure:** Computes a common subsequence \(\widetilde{L}\) of _x,y_ satisfying \(\frac{M}{2n}\le\widetilde{L}\le L\)

1: \(\Sigma\leftarrow\) Compute the set of symbols appearing in _x,y_

2: Compute the frequencies \(\#_\sigma(x)\) for all \(\sigma\in\Sigma\) by one linear scan over _x_

3: Compute the frequencies \(\#_\sigma(y)\) for all \(\sigma\in\Sigma\) by one linear scan over _y_

4: \(\widetilde{L}\leftarrow max_{\sigma\in\Sigma} min\{\#_\sigma(x),\#_\sigma(y)\}\)

5: **return** \(\widetilde{L}\)

