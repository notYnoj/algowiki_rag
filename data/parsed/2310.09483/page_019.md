If \(L_x\cap S=\emptyset\) and _V\>k/n_<sup>2/3</sup>-_n_<sup>1/6</sup>, since `Sort` is _gap-preserving_ by Lemma 3.6, _L_\[_i_\] cannot increase in this iteration. It thus follows by a union bound that _L_\[_i_\] increases with probability at most \(\frac{2}{10}+e^{-2}<0.4\). Thus, \(Pr[x_i\in S\) and _L_\[_i_\] increases\(]<\frac{0.4}{n^{2/3}}\). Let \(\mu=\mathbb{E}[L[i]]\le cn^{2/3}\mathrm{log}n\frac{0.4}{n^{2/3}}=0.4c\mathrm{log}n\). By a Chernoff bound:

\(Pr\big[L[i]>\frac{c}{2}\mathrm{log}n\big]\le Pr[L[i]>(1+1/4)\mu]\)<br>
\(\le e^{-(1/4)^2\mu/(2+1/4)}\)<br>
\(\le e^{-0.4c\mathrm{log}n/36}\)

Choosing _c\>_90_r_:

\(<\frac{1}{n^r}\)

as desired.

**Corollary 6.3.** _If_ \(|L_x|\le\frac{1}{10}n^{2/3}\)_, for any r\>_0 _there exists c large enough that_ \(Pr[Z\cap(x_L,\infty)=\emptyset]>1-\frac{1}{n^r}\).

_Proof._ This follows by a union bound and the previous lemma.

**Corollary 6.4.** _If_ \(|L_x|\le\frac{1}{10}n^{2/3}\)_, for any r\>_0 _there exists c large enough that_ \(Pr[\Gamma\cap(-\infty,x_L-1)=\emptyset]>1-\frac{1}{n^r}\).

_Proof._ Symmetric.

Let _x_<sup>∗</sup> be the value returned by `SelectSparse`.

**Lemma 6.5.** _If_ \(|L_x|\le\frac{1}{10}n^{2/3}\)_, for any r\>_0 _there exists c large enough that_ \(Pr[x^*\ge_{200}x_k]>1-\frac{1}{n^r}\).

_Proof._ We claim it suffices that \(Z\cap(x_L,\infty)=\emptyset\) and \(\Gamma\cap(-\infty,x_L-1)=\emptyset\). If \(|Z|\ge k\), then there must be an element of _Z_ that is \(\ge x_k\). Thus, since `GetMax` returns a 5-approximation with sufficiently large probability, \(x^*\ge_5x_k\) with sufficiently large probability. If |_Z_|+|_Y|\<k_, then we return some element of \(\Gamma\) which is \(\ge_1x_k\) if \(\Gamma\cap(-\infty,x_L-1)=\emptyset\). Otherwise, if |_Z|\<k_ and \(|Z|+|Y|\ge k\), there must be at most _k_-|_Z_|-1 elements of _Y_ that are _\<x<sub>k</sub>_. Thus, the (_k_-|_Z_|)-th element of _Y_ is \(\ge x_k\). Since `100-Sort` returns a 200-approximation, it follows that \(x^*\ge_{200}x_k\) with sufficiently large probability as desired.

**Corollary 6.6.** _If_ \(|R_x|\le\frac{1}{10}n^{2/3}\)_, for any r\>_0 _there exists c large enough that_ \(Pr[x_k\ge_{200}x^*]>1-\frac{1}{n^r}\).

_Proof._ Symmetric.

**Theorem 6.7.** _`SelectSparse` uses n_<sup>1+_O_(1_/d_)</sup>_d_log_n comparisons and d_+max(100,log<sub>2</sub>_d_) _rounds._

_Proof._ All of the comparisons come from `Sort`, `100-Sort`, and `GetMax/GetMin`. The number of comparisons is thus bounded by _cn_<sup>2/3</sup>log_n(n_<sup>1/3</sup>)<sup>1+_O_(1_/d_)</sup>+_n_<sup>1+\(\frac{1}{d-1}\mathrm{log}d\mathrm{log}n+(cn^{5/6}\mathrm{log}n)^{6/5}=n^{1+O(1/d)}d\mathrm{log}n\) as desired. All iterations of the loop can be done in parallel, so the number of rounds is bounded by _d_+log<sub>2</sub>_d_ if `GetMax` is called, and by _d_+100 if `100-Sort` is called.

