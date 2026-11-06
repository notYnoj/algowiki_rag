then<tbc>

\(|\partial\mathcal{F}|\ge\genfrac(){pt}{2}{n-1}{\lfloor(n-1)/2\rfloor}.\)

<tbc>From this, we can conclude that<tbc>

\(\#\left\{t_i:\frac{T}{2}-t_i<a_{n-1}\right\}\ge\genfrac(){pt}{2}{n-1}{\lfloor(n-1)/2\rfloor}.\)

<tbc>As _t<sub>i</sub>_-s are symmetric with respect to \(\frac{T}{2}\) and _a<sub>n</sub>\>a_<sub>_n_-1</sub>, we can conclude<tbc>

\(\#\left\{t_i:\left|t_i-\frac{T}{2}\right|<a_n\right\}\ge\#\left\{t_i:\left|t_i-\frac{T}{2}\right|<a_{n-1}\right\}\ge 2\genfrac(){pt}{2}{n-1}{\lfloor(n-1)/2\rfloor}.\)

<tbc>**Lemma 3.**<tbc>

\(a_n\ge\#\left\{t_i:\left|t_i-\frac{T}{2}\right|<a_n\right\}.\)

<tbc>_Proof._ Consider the interval

\(J=\left(\frac{T}{2}-a_n,\frac{T}{2}+a_n\right),\)

whose length is 2_a<sub>n</sub>_.

If _J_ contained _a<sub>n</sub>_+1 consecutive subset sums<tbc>

\(t_i,t_{i+1},\dots,t_{i+a_n},\)

<tbc>then

\(t_{i+a_n}-t_i<2a_n,\)

contradicting the first lemma. Therefore _J_ contains at most _a<sub>n</sub>_ subset sums.

Hence, we can conclude from those lemmas that

\(a_n\ge 2\genfrac(){pt}{2}{n-1}{\lfloor(n-1)/2\rfloor},\)

which is exactly the statement of the theorem.

**Asymptotic consequence.**

Using the central-binomial-coefficient estimate<tbc>

\(\genfrac(){pt}{2}{m}{\lfloor m/2\rfloor}=\left(\sqrt{\frac{2}{\pi}}-o(1)\right)\frac{2^m}{\sqrt{m}},\)

<tbc>the conditional bound in the theorem yields

\(a_n\ge\left(\sqrt{\frac{2}{\pi}}-o(1)\right)\frac{2^n}{\sqrt{n-1}}\ge\left(\sqrt{\frac{2}{\pi}}-o(1)\right)\frac{2^n}{\sqrt{n}}.\)

This is of the same asymptotic order as the established lower bound discussed by Dubroff, Fox, and Xu \[4\]. It is also worth mentioning that this lower bound is better for odd _n_, since if _n_ is odd, then \(2\genfrac(){pt}{2}{n-1}{\lfloor(n-1)/2\rfloor}>\genfrac(){pt}{2}{n}{\lfloor n/2\rfloor}\), as \(2\genfrac(){pt}{2}{n-1}{\lfloor(n-1)/2\rfloor}-\genfrac(){pt}{2}{n}{\lfloor n/2\rfloor}=C_{\frac{n-1}{2}}\) , where \(C_{\frac{n-1}{2}}\) is the \(\frac{n-1}{2}\) -th Catalan number.

