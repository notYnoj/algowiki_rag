\(m_1+\cdots+(m_i-(k+1))+\cdots+m_{b+1}=a-k-1\). By stars and bars, there are \(\genfrac(){pt}{2}{a+b-k-1}{b}\) such sequences. Therefore, the probability that _m<sub>i</sub>\>k_ is \(\genfrac(){pt}{2}{a+b-k-1}{b}/\genfrac(){pt}{2}{a+b}{b}\). Continuing,<tbc>

\(\mathbb{P}[m_i>k]=\frac{(a+b-k-1)\cdots(a-k)}{(a+b)\cdots(a+1)}\le\left(\frac{a+b-k-1}{a+b}\right)^b\le exp\left(-b\cdot\frac{k+1}{a+b}\right),\)

<tbc>where the last step uses the bound \(1+x\le exp(x)\). By a union bound and taking the complement,

\(\mathbb{P}[m_1,\dots,m_{b+1}\le k]\ge 1-(b+1)exp\left(-b\cdot\frac{k+1}{a+b}\right).\) (28)

If _k_ is such that the right-hand side of (28) is at least 3/4, we know that \(m^*\le k\). Solving for _k_ yields the stated bound on _m_<sup>∗</sup>.

For the lower bounds, \(m^*\ge 1\) because at least one of _m_<sub>1</sub>_,...,m_<sub>_b_+1</sub> is at least 1, and \(m^*\ge\frac{a}{b+1}\) because \(m_1+\cdots+m_{b+1}=a\), and _m_<sup>∗</sup> is greater than or equal to the average term in the sum.

The first part of Theorem 9 now comes from taking the logarithm of \(\mathrm{D}(\Pi_\mathrm{XInv})\) in Proposition 53 and using the bounds in Proposition 54.

_Proof of the first part of Theorem 9._ We mainly make use of the following approximation based on Stirling’s formula.

\(\mathrm{ln}(n!)=\left(n+\frac{1}{2}\right)\mathrm{ln}(n)-n+O(1).\) (29)

In order to estimate \(\mathrm{ln}\mathrm{D}(\Pi_\mathrm{XInv})\), we need to estimate \(\mathrm{ln}((a+b)!)-\frac{a}{m^*}\mathrm{ln}(m^*)-\frac{b}{n^*}\mathrm{ln}(n^*)\). By (29),

\(\mathrm{ln}((a+b)!)=\left(a+b+\frac{1}{2}\right)\mathrm{ln}(a+b)-(a+b)+O(1)\) (30)

\(\frac{a}{m^*}\mathrm{ln}((m^*)!)=\left(a+\frac{a}{2m^*}\right)\mathrm{ln}(m^*)-a+\frac{a}{m^*}O(1)\) (31)

\(\frac{b}{n^*}\mathrm{ln}((n^*)!)=\left(b+\frac{b}{2n^*}\right)\mathrm{ln}(n^*)-b+\frac{b}{n^*}O(1)\) (32)

We can use the lower bounds in Proposition 54, namely that \(m^*\ge 1\) and \(n^*\ge\frac{b}{a+1}\), to simplify the occurrences of _m_<sup>∗</sup> and _n_<sup>∗</sup> in the denominators of (31) and (32). Therefore,

\(\mathrm{ln}\mathrm{D}(\Pi_\mathrm{XInv})\ge a\mathrm{ln}\left(\frac{a+b}{m^*}\right)+b\mathrm{ln}\left(\frac{a+b}{n^*}\right)-\frac{a}{2}\mathrm{ln}(m^*)-\frac{a+1}{2}\mathrm{ln}(n^*)+\frac{1}{2}\mathrm{ln}(a+b)-O(a)\)<br>
\(=a\mathrm{ln}\left(\frac{a+b}{m^*\sqrt{m^*n^*}}\right)+\left(b+\frac{1}{2}\right)\mathrm{ln}\left(\frac{a+b}{n^*}\right)-O(a).\)

Using the upper bounds in Proposition 54, absorbing low-order terms, and using the condition that \(a\le b\), we get

\(\mathrm{log}\mathrm{D}(\Pi_\mathrm{XInv})\ge\Omega\left(a\mathrm{log}\left(\frac{b\sqrt{ab}}{a+b}\right)+b\mathrm{log}(a)\right)\ge\Omega(a\mathrm{log}(\sqrt{ab}/2)+b\mathrm{log}(a))=\Omega((a+b)\mathrm{log}(a)).\)

