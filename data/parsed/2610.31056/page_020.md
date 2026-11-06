where each _r<sub>j</sub>_ is a prime in \[_N_<sup>3</sup>\] and each \(s_j\in[N^2]\). We first bound the individual "digits" appearing in this encoding. Since \(\|\mathbf{x}'^{(i)}\|_\infty\le N^2B\tilde{\lambda}_n\) and \(1\le s_j\le N^2\), we have, for every \(i\in[N]\) and \(j\in[n]\),<tbc>

\(-N^2B+1\le\frac{(\mathbf{x}'^{(i)})_j}{\tilde{\lambda}_n}+s_j\le N^2B+N^2.\)

<tbc>Since \(r_j\ge 1\) and \(\|\mathbf{v}^*\|_\infty\le\tilde{\lambda}_n\), it follows that

\(-(N^2B+N^2+2)\le\left\lfloor\frac{(\mathbf{x}'^{(i)}+\mathbf{v}^*)_j/\tilde{\lambda}_n+s_j}{r_j}\right\rfloor\)<br>
\(\le N^2B+N^2+1.\)

In particular, every encoded digit has absolute value at most \(\ell:=N^2B+N^2+2\). It follows that each _a<sub>i</sub>_ is positive and satisfies

\(a_i\le W^n+\sum_{j=1}^nW^{j-1}\ell\)<br>
\(\le W^n+\ell\sum_{j=0}^{n-1}W^j\)<br>
\(\le W^n+\ell\cdot nW^{n-1}.\)

Since _W_=8_BN_<sup>3</sup> and \(\ell=N^2B+N^2+2\le 2BN^2\) for all sufficiently large _N_, we have

\(\ell\cdot nW^{n-1}\le\frac{n}{4N}\cdot W^n\le W^n\)

for all sufficiently large _n_, because \(N=\Omega(nlogn)\). Hence \(0<a_i\le 2W^n=:M\) for all \(i\in[N]\). Since _W_=8_BN_<sup>3</sup>, we have _M_=2(8_BN_<sup>3</sup>)_<sup>n</sup>_. Using the fact that \(N\le B\checkmark 2^{N/n}\), it follows that \(M\le 2^{o(N)}\). In other words, we have verified that the input instance lies in the pigeonhole regime required by the PESS algorithm.

Since each _a<sub>i</sub>_ is positive, the multiset A is a valid strong-regime instance for PESS. Consequently, the PESS algorithm returns unequal subsets \(X,Y\subseteq[N]\) such that \(\sum_{i\in X}a_i=\sum_{j\in Y}a_j\).

Define \(\mathbf{v}:=\sum_{i\in X}\mathbf{x}^{(i)}-\sum_{j\in Y}\mathbf{x}^{(j)}\in\mathcal{L}\). We next show that the length of **v** is well-bounded. From the equality \(\sum_{i\in X}a_i=\sum_{j\in Y}a_j\) and the definition of the encoding, we obtain<tbc>

\((|X|-|Y|)W^n+\sum_{k=1}^nW^{k-1}\cdot\left(\sum_{i\in X}\left\lfloor\frac{(\mathbf{x}^{(i)})_k/\tilde{\lambda}_n+s_k}{r_k}\right\rfloor-\sum_{j\in Y}\left\lfloor\frac{(\mathbf{x}^{(j)})_k/\tilde{\lambda}_n+s_k}{r_k}\right\rfloor\right)=0.\)

<tbc>For each \(k\in[n]\), define<tbc>

\(C_k:=\sum_{i\in X}\left\lfloor\frac{(\mathbf{x}^{(i)})_k/\tilde{\lambda}_n+s_k}{r_k}\right\rfloor-\sum_{j\in Y}\left\lfloor\frac{(\mathbf{x}^{(j)})_k/\tilde{\lambda}_n+s_k}{r_k}\right\rfloor.\)

<tbc>Since each digit lies in \[-_M,M_\], we have \(|C_k|\le(|X|+|Y|)M\le 2NM\). Using \(M\le 2BN^2\) for large _N_, this gives\(|C_k|\le 4BN^3<\frac{W}{2}\) . Thus, every coefficient in the base-_W_ expansion above has magnitude strictly less than _W/_2. It follows that no carries or overflows are possible, and hence each coefficient must vanish individually. In particular,<tbc>

\(|X|-|Y|=0\text{and}C_k=0\text{for every}k\in[n].\)

