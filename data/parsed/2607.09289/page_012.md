A fast polynomial-space algorithm for the Subset-Sum problem was given in \[5\], and the non- standard assumptions used in its analysis were later removed in \[11\].

**Lemma 4.3** (\[5, 11\])**.** _There is a Monte Carlo algorithm for Subset Sum that runs in O_<sup>∗</sup>(2<sup>0.86_n_</sup>) _time using polynomial space._

We use the polynomial-space algorithm for the Subset Sum problem as a subroutine to prove Theorem 4.4.

**Theorem 4.4.** _Let_ \(\ell'\) _be the minimum solution ratio. Then there is a Monte Carlo algorithm for ESS that runs in_ \(O^*(2^{(H(\ell^\prime)+0.86\ell^\prime)n})\) _time using polynomial space._

_Proof._ Let \(\ell=\ell'n\) be the minimum solution size. We iterate over all subsets \(X\subseteq S\) of size \(\ell\), keeping only the current subset in memory. For each such subset _X_, if \(\sum(X)\) is odd, then _X_ cannot be partitioned into two subsets of equal sum, so we skip this case. Otherwise, we run the polynomial-space Subset-Sum algorithm of Lemma 4.3 on the instance _X_ with target \(\sum(X)/2\).

Since there exists a minimum ESS solution \(A,B\subseteq S\) such that \(|A|+|B|=\ell\) and \(A\cap B=\emptyset\), the iteration eventually considers \(X=A\cup B\), and the corresponding Subset-Sum instance with target \(\sum(X)/2\) has a solution. The running time is therefore

\(O^*\left(\genfrac(){pt}{2}{n}{\ell}2^{0.86\ell}\right)\le O^*(2^{(H(\ell^\prime)+0.86\ell^\prime)n}).\)

The space usage remains polynomial, since we iterate over the subsets _X_ one by one while storing only the current subset, and each call to the Subset-Sum algorithm uses polynomial space.

We combine Theorems 4.2 and 4.4 to prove Theorem 1.4, which we restate here.

**Theorem 1.4.** _There exists a Monte Carlo algorithm for ESS that runs in O_<sup>∗</sup>(2.5430_<sup>n</sup>_) _time and uses polynomial space._

_Proof._ Let \(\gamma_2\) be the larger value of \(\ell'\) at which the functions \(\ell'+1/2\) and \(H(\ell')+0.86\ell'\) intersect, namely the solution to

\(\ell'+\frac{1}{2}=H(\ell')+0.86\ell'\text{for}\frac{1}{2}<\ell'<1.\)

Numerically, \(0.8465<\gamma_2<0.84651\).

For \(\ell'\in(0,\gamma_2]\), we apply Theorem 4.2. For \(\ell'\in(\gamma_2,1]\), we apply Theorem 4.4. Since Theorems 4.2 and 4.4 both solve ESS in polynomial space, it remains to bound the running time. Then the worst-case time exponent, namely the constant _c_ such that the running time is _O_<sup>∗</sup>(2_<sup>cn</sup>_), can be expressed as

\(max\left\{max_{\ell^\prime\in(0,\gamma_2]}\left\{\ell'+\frac{1}{2}\right\},max_{\ell^\prime\in(\gamma_2,1]}\left\{H(\ell')+0.86\ell'\right\}\right\}.\)

This expression is maximized at \(\ell'=\gamma_2\), and its value is at most \(\gamma_2+1/2=H(\gamma_2)+0.86\gamma_2\le 1.34651\). Thus, the worst-case running time is \(O^*(2^{1.34651n})\le O^*(2.5430^n)\).

## 5 Time-Space Tradeoffs

We consider the setting where the space usage is bounded by \(O^*(2^{\alpha n})\) for a constant \(\alpha\), and study the resulting time complexity. In Section 5.1, we give an overview of the tradeoffs by summarizing, in a table, which lemma or theorem is used for each range of \(\alpha\) and \(\ell'\). In Sections 5.2 to 5.5, we explain the theorems used in Section 5.1.

