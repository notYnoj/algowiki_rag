<tbc>\(S\subseteq V\) with \(|S|\ge(1-\frac{c}{4})n\). We have \(|\hat{A}\cap S|\ge|\hat{A}|-\frac{c}{4}n\ge\frac{3c}{4}n\), and similarly for \(\hat{B}\cap S\). Therefore,

\(\sum_{i,j\in S:i<j}\|v_i-v_j\|^2\ge\sum_{i\in\hat{A}\cap S,j\in\hat{B}\cap S}\|v_i-v_j\|^2=\sum_{i\in\hat{A}\cap S}\sum_{j\in\hat{B}\cap S}4=4|\hat{A}\cap S||\hat{B}\cap S|\ge 4\left(\frac{3c}{4}n\right)^2\)

The last expression equals \(\frac{9}{4}c^2n^2=\xi n^2\), and so eq. (1e) is indeed satisfied.

The dual of problem (1) is as follows. It has variables _y<sub>i</sub>_ for every node \(i\in V\) , \(\lambda_{ij}\) for every edge \(ij\in E\), _f<sub>p</sub>_ for every path _p_, and _z<sub>S</sub>_ for every set _S_ of size at least (1-_c/_4)_n_. Let `diag`(_y_) be the diagonal matrix with vector _y_ on the diagonal:

\(max\sum_iy_i+\xi n^2\sum_Sz_S\) (2a)

\(\mathtt{diag}(y)+\sum_pf_pT_p+\sum_Sz_SK_S\unknown\sum_{ij}\lambda_{ij}L_{ij}\) (2b)

\(\sum_{j:ij\in E}\lambda_{ij}\le w(i)\forall i\) (2c)

\(\lambda_{ij}\le w(ij)\forall ij\in E\) (2d)

\(f_p,z_S,\lambda_{ij}\ge 0\forall p,S,ij\) (2e)

For a vector \(\lambda\ge 0\) let \(G^\lambda=^\text{def}(V,E,\lambda)\) be the graph with edge weights \(\lambda\). Note that \(\lambda\) satisfies eq. (2c) if and only if \(\mathrm{deg}(G^\lambda)\le w|_V\) component-wise, where \(\mathrm{deg}(G^\lambda)\in\mathbb{R}^V\) is the vector of node degrees in \(G^\lambda\). Also, \(\sum_{ij}\lambda_{ij}L_{ij}=\mathcal{L}(G^\lambda)\) is the Laplacian of \(G^\lambda\).

## 3 A new matrix multiplicative weights method

As previously discussed, we are unable to apply the general primal-dual framework of Arora and Kale \[3\]. However, we still leverage some of the same high-level steps. Instead of solving optimization problem (1) directly, we will use a binary search on the objective value. Accordingly, let us fix value \(\alpha\in[1,8W]\). We will present a procedure that will either (i) certify that the optimum value of problem (1) is at least \(\alpha/2\), or (ii) produce a \(\Theta(1)\)-balanced element cut of cost at most \(\Theta(\kappa\alpha)\), for some parameter \(\kappa\) to be specified later. Clearly, by running this procedure for _O_(log_n_) values of \(\alpha\) we will obtain a \(O(\kappa)\) pseudo-approximation to the minimum element cut problem.

The procedure above will be implemented via the Matrix Multiplicative Weights Update (MMWU) algorithm of Arora and Kale \[3, Algorithm 1\] given below.

1 for t=1,2_,...,T_ do<br>
   Compute<br>
\(W^{(t)}=\mathrm{exp}\left(\eta\sum_{r=1}^{t-1}N^{(r)}\right),X^{(t)}=n\cdot\frac{W^{(t)}}{\text{Tr}(W^{(t)})}\)<br>
   Either output `Fail`, or find "feedback matrix" N<sup>(t)</sup> of the form<br>
\(N^{(t)}=\mathtt{diag}(y)+\sum_pf_pT_p+\sum_Sz_SK_S-\sum_{ij}\lambda_{ij}L_{ij}\)<br>
   where \(f_p\ge 0\), \(z_S\ge 0\), \(\sum_iy_i+\xi n^2\sum_Sz_S\ge\alpha\), \(\lambda_{ij}\) are non-negative variables with \(\mathrm{deg}(G^\lambda)\le w|_V\) and \(\lambda_{ij}\le w(ij)\), and \(N^{(t)}\bullet X^{(t)}\le 0\).

**Algorithm 1:** MMWU algorithm.

