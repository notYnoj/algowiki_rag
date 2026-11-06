## B.1.2 Approximating the Number of Matching Pairs

**Algorithm 8** Counting Matching Pairs (_x,y_)

**Require:** Strings _x,y_ of length _n_

**Ensure:** Computes the number of matching pairs _M=M(x,y_)

1: \(M\leftarrow 0\)

2: \(\Sigma\leftarrow\) Compute the set of symbols appearing in _x,y_

3: Compute the frequencies \(\#_\sigma(x)\) for all \(\sigma\in\Sigma\) by one linear scan over _x_

4: Compute the frequencies \(\#_\sigma(y)\) for all \(\sigma\in\Sigma\) by one linear scan over _y_

5: **for** \(\sigma\in\Sigma\) **do**

6: \(M\leftarrow M+\#_\sigma(x)\cdot\#_\sigma(y)\)

7: **return** _M_

**Algorithm 9** Graph Construction (_x_<sub>1</sub>_,...,x<sub>n/m</sub>,y_<sub>1</sub>_,...,y<sub>n/m</sub>_)

**Require:** Strings _x_<sub>1</sub>_,...,x<sub>n/m</sub>,y_<sub>1</sub>_,...,y<sub>n/m</sub>_ of length _m_

**Ensure:** Constructs a three-layered graph _G_

1: \(\Sigma\leftarrow\) Compute the set of symbols appearing in _x_<sub>1</sub>_,...,x<sub>n/m</sub>,y_<sub>1</sub>_,...,y<sub>n/m</sub>_

2: **for** \(i\in[n/m]\) **do**

3: Compute the frequencies \(\#_\sigma(x_i)\) for all \(\sigma\in\Sigma\) by one linear scan over _x<sub>i</sub>_

4: Compute the frequencies \(\#_\sigma(y_i)\) for all \(\sigma\in\Sigma\) by one linear scan over _y<sub>i</sub>_

5: \(L\leftarrow\{1,\dots,n/m\}\)

6: \(R\leftarrow\{1,\dots,n/m\}\)

7: \(U\leftarrow\{(\sigma,\ell,r)|\sigma\in\Sigma,0\le\ell,r\le logm\}\)

8: \(V\leftarrow L\cup U\cup R\)

9: \(E_1\leftarrow\{(i,(\sigma,\ell,r))\in L\times U|\#_\sigma(x_i)\in[2^\ell,2^{\ell+1})\}\)

10: \(E_2\leftarrow\{(j,(\sigma,\ell,r))\in R\times U|\#_\sigma(y_j)\in[2^r,2^{r+1})\}\)

11: \(E\leftarrow E_1\cup E_2\)

12: **return** _G_=(_V,E_)

