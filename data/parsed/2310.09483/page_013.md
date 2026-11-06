_Proof._ Let _U_ be the set of the smallest _n/_8 elements of _X_. Consider some iteration of the loop on line 25 where _x<sub>i</sub>\<x<sub>L</sub>_-1. Let _A<sub>i</sub>_ be a random variable that takes value 1 if the _i_th random element is \(\in U\) and 0 otherwise. Note that if _A<sub>i</sub>_ is 0, we cannot increment _C_ in the _i_th iteration. Thus, \(C\le A=\sum_iA_i\). Let \(\mu=\mathbb{E}[A]=8c_2logN\frac{|U|}{n}=c_2logN\), we have:

\(Pr[C\ge 2c_2logN]\le Pr[A\ge 2c_2logN]\)<br>
\(=Pr[A\ge(1+\delta)\mu]\)

Where \(\delta=1\)

\(\le e^{-\frac{\delta^2\mu}{2+\delta}}\)<br>
\(=e^{-\frac{\mu}{3}}\)<br>
\(=e^{-logN\frac{c_2}{3}}\)<br>
\(=N^{-\frac{c_2}{3}}\)

Thus, choosing \(c_2\ge 3(r+1)\), we get<tbc>

\(Pr[C\ge 2c_2logN]\le\frac{1}{N^{r+1}}\)

<tbc>By a union bound:

\(Pr[\exists x_i<x_L-1:C\ge 2c_2logN]\le\#\{x_i<x_L-1\}\frac{1}{N^{r+1}}\)<br>
\(<\frac{1}{N^r}.\)

**Lemma 4.4.** _If_ \(|X_L|\ge\frac{3n}{8}\) _, for any constant r\>_0 _we can choose c_<sub>2</sub> _sufficiently large such that_

\(Pr[\exists x_i>x_L+2:C<2c_2logN]<\frac{1}{N^r}.\)

_Proof._ Similar to the previous Lemma, using the fact that \(|X_L|\ge\frac{3n}{8}\Longrightarrow\#\{x_i\le x_L+1\}\ge\frac{3n}{8}\).

**Corollary 4.5.** _If_ \(|X_L|\ge\frac{3n}{8}\) _, for any constant r\>_0 _we can choose c_<sub>2</sub> _sufficiently large such that after the sample phase,_ \(Pr[max(Y)>x_L+2]<\frac{1}{N^r}\).

_Proof._ If max(_Y)\>x<sub>L</sub>_+2 then we must have had _C\<_2_c_<sub>2</sub>log_N_ for some _x<sub>i</sub>\>x<sub>L</sub>_+2, which happens with probability \(<\frac{1}{N^r}\) by the previous Lemma.

**Corollary 4.6.** _If_ \(|X_L|\ge\frac{3n}{8}\) _, for any constant r\>_0 _we can choose c_<sub>2</sub> _sufficiently large such that after the sample phase,_ \(Pr[min(X\backslash Y)<x_L-1]<\frac{1}{N^r}\).

