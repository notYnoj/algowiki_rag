So when _n_ is large enough,<tbc>

\(B_1(2n)-B_2(2n)\le\frac{2\upsilon}{n},\)

<tbc>and from the convexity of _B_, and using the lower bound \(0<C\le B_1(2n)\) (see Theorem 4.5),<tbc>

\(\mathrm{Var}LC_n=B_1(2n)+\cdots+B_{2n}(2n)\ge\sum_{i=1}^\frac{Cn}{2\upsilon}C-\frac{2\upsilon(i-1)}{n},\)

<tbc>which is equivalent to \(C^2n/(4\upsilon)\). So for some constant \(C'>0\),

\(\mathrm{Var}LC_n\ge C'n^{1-\alpha}.\)

Once again, this is under the assumption that \(\mathbb{E}\widetilde{\Delta_j}\le\mathrm{exp}(-tn)\). If, additionally, this assumption holds for some \(\alpha<1/10\), then by \[10\] there is convergence of the properly rescaled _LC<sub>n</sub>_ to a Gaussian.

There is also a somewhat weaker assumption that would guarantee the linearity of the variance. Recalling the percolation interpretation of the LCS, we denote by Geo the (random) set of geodesics, and for any \(a,b\in\{1,\dots,2n\}\), Geo_<sup>a</sup>_ the set of geodesics when the _Z<sub>a</sub>_ is turned into \(Z'_a\), and Geo<sup>_a,b_</sup> the set of geodesics when _Z<sub>a</sub>_ is turned into \(Z'_a\) and _Z<sub>b</sub>_ is turned into \(Z'_b\). For \(j,k\in\{1,\dots,m\}\), let _A<sub>j,k</sub>_ be the event: there exists (_p,q_) such that _j\<p\<k_ and there exist \((g_1,g_2,g_3,g_4)\in\mathrm{Geo}\cap\mathrm{Geo}^j\cap\mathrm{Geo}^k\cap\mathrm{Geo}^{j,k}\) such that \((p,q)\in g_1\cap g_2\cap g_3\cap g_4\). In words, this is the event that it is possible to find _X<sub>p</sub>_ aligned with _Y<sub>q</sub>_ no matter the values of _X<sub>j</sub>_ and _X<sub>k</sub>_. Similarly, let _B<sub>j,k</sub>_ be the event: there exists (_p,q_) such that _j\<p_ and _k\>q_ or _j\>p_ and _k\<q_ and there exists \((g_1,g_2,g_3,g_4)\in\mathrm{Geo}\cap\mathrm{Geo}^j\cap\mathrm{Geo}^{k+n}\cap\mathrm{Geo}^{j,k+n}\) such that \((p,q)\in g_1\cap g_2\cap g_3\cap g_4\). In words, this is the event that it is possible to find _X<sub>p</sub>_ aligned with _Y<sub>q</sub>_ no matter the values of _X<sub>j</sub>_ and _X<sub>k</sub>_, and such that _X<sub>j</sub>,Y<sub>k</sub>_ are not both "on the same side". Now suppose that \(\mathbb{P}(A_{j,k}^c),\mathbb{P}(B_{j,k}^c)\le\mathrm{exp}(\alpha|k-j|)\) for some constant \(\alpha>0\). Then an adaptation of the proof above shows that the variance is lower bounded by \(C'n\) for some constant \(C'>0\).

**Acknowledgements:** Many thanks to the ICTS in Bengaluru as well as the GESDA program at IHP in Paris for their hospitalities and support while part of this research was carried out and to R. van Handel for his comments on Theorem 2.1, and to Alexandros Eskenazis for pointing out to us the references \[7\] and \[17\].

## References

