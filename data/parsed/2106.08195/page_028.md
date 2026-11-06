## B.2.5 Algorithm 4: Large_L_, Small \(\mu\), Small \(\lambda\)

**Algorithm 4** \[Theorem 17\] Large _L_, Small \(\mu\), Small \(\lambda(x,y,T,\hat{L},\hat{\lambda},\hat{\mu})\)

**Require:** Strings _x,y_ of length _n_; parameter \(T\in[n,n^2]\) and parameters \(\hat{L},\hat{\lambda},\hat{\mu}\)

**Ensure:** Computes a common subsequence \(\widetilde{L}\) of _x,y_ with the guarantees of Theorem 17.

1: \(\mathcal{X}\leftarrow\{x_1,\dots,x_{n/m}\}\) where _x<sub>i</sub>=x_\[(_i_-1)_m_+1_,im_\]\}

2: \(\mathcal{Y}\leftarrow\{y_1,\dots,y_{n/m}\}\) where _y<sub>i</sub>=y_\[(_i_-1)_m_+1_,im_\]\}

3: \(M\leftarrow\) result of Algorithm 8 on (_x,y_)

4: \(q\leftarrow\frac{M}{T}\)

5: \(\{\widetilde{M}_{ij}\}_{i,j\in[n/m]}\leftarrow\) result of Algorithm 10 on (X,Y_,q_)

6: **for** \(i\in[n/m]\) **do**

7: **for** \(j\in[n/m]\) **do**

8: \(\widetilde{L}_{ij}\leftarrow 0\)

9: **for** \(j\in[n/m]\) **do**

10: Run the preprocessing of basic decision algorithm (Lemma 5) on _y<sub>j</sub>_

11: \(p\leftarrow min\left\{\frac{\hat{L}}{n},\frac{\hat{L}T}{\lambda n},\frac{\hat{L}^2T}{\hat{\lambda}\hat{\mu}n}\right\}\)

12: **for** \(i\in[n/m]\) **do**

13: **for** \(j\in[n/m]\) **do**

14: \(q\leftarrow 1\) with probability _p_ and 0 otherwise

15: **if** _q_=1 **then**

16: **if** \(\widetilde{M}_{ij}\le 64\hat{\mu}n/(\hat{L}\sqrt{T})\) **then**

17: \(f\leftarrow Query(x_i,y_j,\frac{\hat{L}}{4\sqrt{T}})\) of Algorithm 7

18: **if** _f_=1 **then**

19: \(\widetilde{L}_{ij}\leftarrow\frac{\hat{L}}{4\sqrt{T}}\)

20: **for** \(0\le i\le n/m\) **do**

21: _D_\[_i,_0\]=0

22: _D_\[0_,i_\]=0

23: **for** \(i\in[n/m]\) **do**

24: **for** \(j\in[n/m]\) **do**

25: \(D[i][j]\leftarrow max\{\widetilde{L}_{ij}+D[i-1,j-1],D[i-1,j],D[i,j-1]\}\)

26: **return** _D_\[_n/m,n/m_\]

