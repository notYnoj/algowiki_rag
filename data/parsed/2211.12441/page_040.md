probability of the outcome _k_.<sup>2</sup>  (33) then follows because

\(\int_{-\pi}^\pi z^de^{-ikt}dt=\int_{-\pi}^\pi e^{i(d-k)t}dt=\left\{\begin{array}{ c c }
2\pi & d=k \\
0 & d\neq k
\end{array}\right.\)

The following lemma then represents the essence of the proof of Lemma 34.

**Lemma 55.** _Then there exists a constant C such that for all integers a, b with_ \(b\ge a\ge 2\)

\(\int_{-\pi}^\pi|\varphi_{a,b}(t)|dt\le\frac{C}{b\sqrt{a}}.\) (34)

_where_ \(\varphi_{a,b}(t)\doteq\mathbb{E}(e^{itX_{a,b}})\).

_Proof of Lemma 34._ By symmetry, it suffices to consider the case where \(a\le b\). In the case where _a_=1, the distribution of _X<sub>a,b</sub>_ is uniform over {0_,...,b_}, so the maximum probability is \(\frac{1}{b+1}\le C/\sqrt{ab(a+b)}\) for any constant \(C\ge\sqrt{2}/2\). Otherwise, we have

\(\mathbb{P}[X_{a,b}=k]=\frac{1}{2\pi}\int_{-\pi}^\pi\varphi_{a,b}(t)e^{-itk}dt\le\frac{1}{2\pi}\int_{-\pi}^\pi|\varphi_{a,b}(t)|dt\le\frac{C}{2\pi b\sqrt{a}}\le\frac{C}{\sqrt{ab(b+1)}}\)

by (33) and Lemma 55.

To establish Lemma 55, as \(|\varphi_{a,b}(t)|\) is an even function, it suffices to take the integral (34) over the domain \([0,\pi]\) and multiply by two:

\(\int_{-\pi}^\pi|\varphi_{a,b}(t)|dt=2\int_0^\pi|\varphi_{a,b}(t)|dt\) (35)

We divide the domain of integration on the right-hand side of (35) into two regions: one close to zero, and the rest. The integrand is well-behaved in the center near zero, with it being approximated accurately by a normal curve. It is harder to analyze the behavior of the function away from zero. In this region, a pole reduction lemma (captured by Lemma 65) that hinges on a combinatorial matching result (Lemma 67), plays a crucial role in eliminating most of the messy behavior of the function and still providing an effective bound.

We first derive an expression for the characteristic function of _X<sub>a,b</sub>_ in Section 9.1, bound the central part of the integral in Section 9.2, the peripheral part in Section 9.3, and conclude with the pole reduction lemma in Section 9.4.

## 9.1 Characteristic function

The characteristic function of a generic random variable _X_ is defined as \(\varphi_X(t):\mathbb{R}\rightarrow\mathbb{C}:t\mapsto\mathbb{E}(e^{itX})\). It always exists and has the following interesting property (among others):

**Fact 56.** _For independent random variables X,Y,_

\(\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t).\)

<sup>2</sup>In the case at hand, after multiplication by \(\genfrac(){pt}{2}{a+b}{a}\), the resulting polynomial is known as the Gaussian polynomial with parameter (_a,b_).

