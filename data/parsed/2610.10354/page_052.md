By the pigeonhole principle at least one part \(1\le\ell\le L\) satisfies<tbc>

\(\sum_{x\in D_\ell}\tilde{r}(x)\ge\frac{\alpha|A|^2}{2L};\)

<tbc>take that part and report \(D'=D_\ell\). Indeed, each \(x\in D_\ell\) satisfies

\(r_{A-A}(x)\ge\frac{\tilde{r}(x)}{2}\ge\frac{|A|}{2^{\ell+1}}\ge\frac{\sum_{x\in D_\ell}\tilde{r}(x)}{4|D_\ell|}\ge\frac{\alpha|A|^2}{8L|D_\ell|},\)

which is as claimed, recalling that \(L\le 1+log\frac{1}{\alpha}+log(1+\frac{|D|}{|A|})\).

Finally, consider the running time. Lemma 2.5 takes time \(\widetilde{O}(|A|/\epsilon+|D|)=\widetilde{O}(|A|+|D|/\alpha)\). All subsequent steps, including the construction of _D_<sup>∗</sup>, its partitioning, and selecting the relevant part \(D_\ell\), run in linear time _O_(|_D_|).

We also rely on the following lemma, which is a combination of \[TV06, Lemma 2.33\] and \[TV06, Lemma 2.34\].

**Lemma 7.3.** _Let_ \(0<\alpha\le 1\) _and let A,S be sets with_ \(S\subseteq Sym(A;\alpha)\)_. Then:_<tbc>

\(|\{(s_1,s_2)\in S^2:s_1-s_2\in Sym(A;\alpha^2/2)\}|\ge\frac{\alpha^2|S|^2}{2}.\)

<tbc>**Proof.** Supposing otherwise,

\(E(A,S)=\sum_{s_1,s_2\in S}r_{A-A}(s_1-s_2)\)<br>
\(<\frac{\alpha^2|S|^2}{2}\cdot|A|+|S|^2\cdot\frac{\alpha^2|A|}{2}\)<br>
\(=\alpha^2|S|^2|A|.\)

But at the same time, by Cauchy-Schwarz,

\(E(A,S)\ge\sum_{a\in A}r_{A+S}(a)^2\)<br>
\(\ge\frac{\left(\sum_{a\in A}r_{A+S}(a)\right)^2}{|A|}\)<br>
\(=\frac{\left(\sum_{s\in S}r_{A-A}(s)\right)^2}{|A|}\)<br>
\(\ge\frac{(|S|\cdot\alpha|A|)^2}{|A|}\)<br>
\(=\alpha^2|S|^2|A|,\)

which shows the desired contradiction.

