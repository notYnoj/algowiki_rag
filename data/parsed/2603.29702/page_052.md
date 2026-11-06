_Proof._ We can see that the left-hand side of (24) depends on the sign of _p(r_)-_p(l_). Since the cases for the two signs are identical, we only need to show this for intervals where \(p(r)\le p(l)\) -- we want to show that for a column _x_ such that the weight of _p_ before column _x_ is 1, with probability \(1-o\left(\frac{1}{M\mathrm{log}^{0.02}(n)}\right)\), every interval \((l,r]\unknown x\) on an active scale satisfies

\(\frac{\mathrm{TD}_{M^3}(\Delta(p(l,r]))}{p(r)-p(l)+(r-l)}=o\left(\frac{1}{M^3}\right).\) (29)

Let _A_={_a<sub>i</sub>_} be the non-negative sequence whose \((i\cdot\mathcal{B}_x)\)-th element is<tbc>

\(a_{i\cdot\mathcal{B}_x}:=p(i\cdot\mathcal{B}_x)-p((i-1)\cdot\mathcal{B}_x)+\mathcal{B}_x=(\Delta p)_i+\mathcal{B}_x\)

<tbc>(we will never explicitly use indices that are not multiples of B_<sub>x</sub>_ and these entries are treated as zeros) which measures how close each block of _p_ is to a (+1,-1)-diagonal path, and let _B_=(_b<sub>i</sub>_) be the non-negative sequence whose \((i\cdot\mathcal{B}_x)\)-th element is<tbc>

\(b_{i\cdot\mathcal{B}_x}:=w(p\left((i-1)\cdot\mathcal{B}_x,i\cdot\mathcal{B}_x\right]).\)

<tbc>Since total deviation is invariant under a universal translation (i.e., by +B_<sub>x</sub>_ everywhere), for every interval (_l,r_\] on a scale that is a multiple of 3, the _M_<sup>3</sup>-way total deviation of \(\Delta(p(l,r])\) and _A(l,r_\] are equal:

\(\mathrm{TD}_{M^3}(\Delta(p(l,r]))=\mathrm{TD}_{M^3}(A(l,r]).\) (30)

It is straightforward to see that if we choose a random column _x_ before which the weight of _p_ is 1, the expected value of the total sum over every interval \((l,r]\unknown x\) on a scale that is a multiple of 3 of the left-hand side of (29) is

\(\sum_{s\in[S]\cap\unknown\mathbb{Z}}\left(\sum_{(l,r]\in s\text{s.t.}|p(r)-p(l)|<r-l}\underbrace{\frac{w(l,r)}{w(p)}}_\text{probability of}x\in(l,r]}\cdot\frac{\mathrm{TD}_{M^3}(\Delta(p(l,r]))}{p(r)-p(l)+(r-l)}\right)\)<br>
\(=\sum_{s\in[S]\cap\unknown\mathbb{Z}}\left(\sum_{(l,r]\in s\text{s.t.}|p(r)-p(l)|<r-l}\frac{B_{\Sigma(l,r]}}{w(p)}\cdot\frac{\mathrm{TD}_{M^3}(\Delta(p(l,r]))}{A_{\Sigma(l,r]}}\right)\text{by definition of}A\text{and}B\)<br>
\(=\sum_{s\in[S]\cap\unknown\mathbb{Z}}\left(\sum_{(l,r]\in s\text{s.t.}|p(r)-p(l)|<r-l}\frac{B_{\Sigma(l,r]}}{w(p)}\cdot\frac{\mathrm{TD}_{M^3}(A(l,r])}{A_{\Sigma(l,r]}}\right)\text{due to (30)}\)<br>
\(=\frac{1}{w(p)}\sum_{s\in[S]\cap\unknown\mathbb{Z}}\sum_{(l,r]\in s}\mathrm{SD}_{M^3}(A(l,r],B(l,r])\text{by definition of SD}\)<br>
\(=\frac{1}{w(p)}\unknown\mathrm{SD}_{M^3,S/3}(A,B)\text{by definition of}\unknown\mathrm{SD}.\)

To bound this total sum, we can apply Lemma 4.3 on _A,B_, but we need to make sure that the _B_-to-_A_ ratio satisfies the bound in the lemma. We call a column _x_ "dispensable" if there exists an recursion interval \((l,r]\unknown x\) such that _w(p(l,r_])_\<(r-l)/_2<sup>log<sup>0.01</sup>(_n_)</sup> (i.e., at most a 1/2<sup>log<sup>0.01</sup>(_n_)</sup> fraction of (_l,r_\] contributes<tbc>

