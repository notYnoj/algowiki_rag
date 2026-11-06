**Algorithm 12** \[Lemma 8\] Single Symbol Approximation Var (_x_<sub>1</sub>_,...,x<sub>n/m</sub>,y_<sub>1</sub>_,...,y<sub>n/m</sub>,q_)

**Require:** Strings _x_<sub>1</sub>_,...,x<sub>n/m</sub>,y_<sub>1</sub>_,...,y<sub>n/m</sub>_ of length _m_ and a parameter _q\>_0

**Ensure:** For each \(i,j\in[n/m]\) computes \(\widetilde{L}_{ij}\) satisfying \(\frac{M_{ij}-q}{16m}\le\widetilde{L}_{ij}\le L_{ij}\) w.h.p.

1: Repeat steps 1-19 of Algorithm 10

2: **for** \(i\in[n/m]\) **do**

3: **for** \(j\in[n/m]\) **do**

4: \(\bar{L}_{ij}\leftarrow max_{(\sigma,\ell,r)\in\widetilde{U}_{ij}}2^{min\{\ell,r\}}\)

5: \(\widetilde{L}_{ij}\leftarrow\) repeat steps 1-4 for _c_log_n_ times and find the median of all \(\bar{L}_{ij}\) for each _i,j_

6: **return** \(\widetilde{L}_{ij}\) for each _i,j_

## B.2 Main Algorithm

In this section we describe the pseudocode for the main algorithm and it’s four subparts.

**Algorithm 13** \[Theorem 9\] ApproxLCS (_x,y,T_)

**Require:** Strings _x,y_ of length _n_; parameter \(T\in[n,n^2]\)

**Ensure:** Computes a common subsequence \(\widetilde{L}\) of _x,y_ satisfying \(\widetilde{L}=\widetilde{\Omega}(LT^{0.4}/n^{0.8})\) w.h.p.

1: \(\widetilde{L}_1\leftarrow\) result of Algorithm 1 on (_x,y,T_)

2: \(\widetilde{L}_2\leftarrow\) result of Algorithm 2 on (_x,y,T_)

3: \(\widetilde{L}_3\leftarrow\) result of Algorithm 14 on (_x,y,T_)

4: \(\widetilde{L}\leftarrow max\{\widetilde{L}_1,\widetilde{L}_2,\widetilde{L}_3\}\)

5: **return** \(\widetilde{L}\)

### B.2.1 Algorithm 1: Small _L_

**Algorithm 1** \[Theorem 10\] Small _L_ (_x,y,T_)

**Require:** Strings _x,y_ of length _n_; parameter \(T\in[n,n^2]\)

**Ensure:** Computes a common subsequence \(\widetilde{L}\) of _x,y_ satisfying \(\widetilde{L}\ge min\{L,\sqrt{LT/n}\}\) w.h.p.

1: \(M\leftarrow\) result of Algorithm 8 on (_x,y_)

2: \(\widetilde{L}_1\leftarrow\) result of Algorithm 11 on (_x,y_)

3: \(\widetilde{L}_2\leftarrow Query(x,y,max\{1,\frac{M}{2T}\})\) of Algorithm 6

4: \(\widetilde{L}\leftarrow max\{\widetilde{L}_1,\widetilde{L}_2\}\)

5: **return** \(\widetilde{L}\)

