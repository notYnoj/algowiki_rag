**Lemma 4.1** (Dyadic increment)**.** _Let_ \(\nu\) _be a level-r pseudo-distribution with_ \(r\ge 2\)_. Let_ \(U\subseteq V\) _be nonempty, and let_ \(\tau,\delta\in(0,1]\) _satisfy_ \(\nu(u)\ge\tau\) _for every_ \(u\in U\) _and_ \(d(U)\ge\delta\)_. Let_ \(\ell\) _be an odd positive integer with_ \(2^{-\ell}\le\delta/4\)_, and let_ \(J:=\lceil log(1/\tau)\rceil\)_. Then there are an integer j with_ \(-1\le j\le J-1\) _and a vertex_ \(v\in U\) _such that_

\(\big|\{u\in U:\nu(u,v)\ge(1+2^j)\nu(u)\nu(v)\}\big|\ge\frac{3\delta}{8}2^{-(j+1)(\ell+1)}|U|.\) (12)

_Proof._ Let _M_ be the normalized covariance matrix from Lemma 3.4. By Lemma 3.2-(b), if \(uv\in E\), then _M(u,v_)=-1. Moreover, for all \(u,v\in U\),

\(M(u,v)\le\frac{min\{\nu(u),\nu(v)\}}{\nu(u)\nu(v)}-1=\frac{1}{max\{\nu(u),\nu(v)\}}-1<\frac{1}{\tau}\le 2^J.\)

The first step follows from the definition of _M_ and Lemma 3.2-(b). The second step rewrites the quotient, the third step uses \(\nu(u),\nu(v)\ge\tau\), and the fourth step follows from the definition of _J_.

For each integer _j_ with \(-1\le j\le J-1\), define<tbc>

\(\rho_j:=\frac{|\{(u,v)\in U\times U:2^j\le M(u,v)<2^{j+1}\}|}{|U|^2}.\)

<tbc>Every pair with \(M(u,v)\ge 1/2\) belongs to exactly one of these classes. Partition the pairs in \(U\times U\) into four groups. Edges contribute exactly -_d(U_)|_U_|<sup>2</sup> to the sum of \(M(u,v)^\ell\), since \(\ell\) is odd. The remaining pairs with _M(u,v)\<_0 make negative contributions. Pairs with \(0\le M(u,v)<1/2\) contribute at most \(2^{-\ell}|U|^2\) in total. Finally, the pairs in class _j_ contribute at most \(\rho_j2^{(j+1)\ell}|U|^2\). Consequently,<tbc>

\(0\le\sum_{u\in U}\sum_{v\in U}M(u,v)^\ell\le\big(-d(U)+2^{-\ell}+\sum_{j=-1}^{J-1}\rho_j2^{(j+1)\ell}\big)|U|^2.\)

<tbc>The first step follows from Lemma 3.4; the second step follows from the preceding partition of the pairs. Rearranging gives<tbc>

\(\sum_{j=-1}^{J-1}\rho_j2^{(j+1)\ell}\ge d(U)-2^{-\ell}\ge\frac{3\delta}{4}.\)

<tbc>The first step rearranges the preceding display, and the second step uses \(d(U)\ge\delta\) and \(2^{-\ell}\le\delta/4\). Assign the weight _w<sub>j</sub>_:=2<sup>-(_j_+2)</sup> to class _j_. These weights satisfy<tbc>

\(\sum_{j=-1}^{J-1}w_j=1-2^{-(J+1)}<1.\)

<tbc>The first step sums a finite geometric series, and the second step uses \(J\ge 0\). Therefore some _j_ satisfies<tbc>

\(\rho_j2^{(j+1)\ell}\ge\frac{3\delta}{4}w_j.\)

<tbc>Otherwise, summing the strict reverse inequalities would contradict the preceding lower bound \(3\delta/4\). Rearranging gives

\(\rho_j\ge\frac{3\delta}{4}2^{-(j+2)}2^{-(j+1)\ell}=\frac{3\delta}{8}2^{-(j+1)(\ell+1)}.\)

The first step divides the preceding lower bound by \(2^{(j+1)\ell}\) and substitutes _w<sub>j</sub>_=2<sup>-(_j_+2)</sup>. The second step collects the powers of 2. The additional loss is determined by the selected scale _j_ and is independent of the number of classes.

