## B.2.2 Parameter Guessing

**Algorithm 14** Parameter Guessing (_x,y,T_)

**Require:** Strings _x,y_ of length _n_; parameter \(T\in[n,n^2]\)

**Ensure:** Computes a common subsequence \(\widetilde{L}\) of _x,y_.

1: \(\widetilde{L}\leftarrow 0\)

2: **for** \(0\unknown i\unknown\mathrm{log}n\) **do**

3: **for** \(0\unknown j\unknown 2\mathrm{log}n\) **do**

4: **for** \(0\unknown k\unknown 2\mathrm{log}n\) **do**

5: \(\hat{L}\leftarrow 2^i\)

6: \(\hat{\lambda}\leftarrow 2^j\)

7: \(\hat{\mu}\leftarrow 2^k\)

8: \(L_1\leftarrow\) result of Algorithm 3 on \((x,y,T,\hat{L},\hat{\lambda},\hat{\mu})\), abort after running for time \(\widetilde{O}(T)\)

9: \(L_2\leftarrow\) result of Algorithm 4 on \((x,y,T,\hat{L},\hat{\lambda},\hat{\mu})\), abort after running for time \(\widetilde{O}(T)\)

10: \(\widetilde{L}\leftarrow\mathrm{max}\{\widetilde{L},L_1,L_2\}\)

11: **return** \(\widetilde{L}\)

## B.2.3 Algorithm 2: Large _L_, Large \(\mu\)

**Algorithm 2** \[Theorem 13\] Large _L_, Large \(\mu\) (_x,y,T_)

**Require:** Strings _x,y_ of length _n_; parameter \(T\in[n,n^2]\)

**Ensure:** Computes a common subsequence \(\widetilde{L}\) of _x,y_ satisfying \(\widetilde{L}\unknown\frac{\mu\sqrt{T}}{32n}\) w.h.p.

1: \(\mathcal{X}\leftarrow\{x_1,\dots,x_{n/m}\}\) where _x<sub>i</sub>=x_\[(_i_-1)_m_+1_,im_\]\}

2: \(\mathcal{Y}\leftarrow\{y_1,\dots,y_{n/m}\}\) where _y<sub>i</sub>=y_\[(_i_-1)_m_+1_,im_\]\}

3: \(M\leftarrow\) result of Algorithm 8 on (_x,y_)

4: \(q\leftarrow\frac{M}{4T}\)

5: \(\{\widetilde{L}_{ij}\}_{i,j\in[n/m]}\leftarrow\) result of Algorithm 12 on (X,Y_,q_)

6: **for** \(0\unknown i\unknown n/m\) **do**

7: _D_\[_i,_0\]=0

8: _D_\[0_,i_\]=0

9: **for** \(i\in[n/m]\) **do**

10: **for** \(j\in[n/m]\) **do**

11: \(D[i][j]\leftarrow\mathrm{max}\{\widetilde{L}_{ij}+D[i-1,j-1],D[i-1,j],D[i,j-1]\}\)

12: **return** _D_\[_n/m,n/m_\]

