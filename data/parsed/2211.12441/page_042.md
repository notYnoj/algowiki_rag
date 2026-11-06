Consider a random permutation of \[_a+b_\], let _A_ be the array consisting of the first _a_ elements, and _B_ the array consisting of the remaining _b_. Then Inv(_A_) has distribution _X<sub>a</sub>_, Inv(_B_) distribution _X<sub>b</sub>_, Inv(_AB_) distribution _X_<sub>_a+b_</sub>, and XInv(_A,B_) distribution _X<sub>a,b</sub>_. By Fact 57, we have:<tbc>

\(X_{a+b}=X_a+X_b+X_{a,b}.\)

<tbc>Moreover, the values of Inv(_A_), Inv(_B_), and XInv(_A,B_) are independent. Hence, by Fact 56<tbc>

\(\varphi_{a+b}(t)=\varphi_a(t)\varphi_b(t)\varphi_{a,b}(t),\)

<tbc>or

\(\varphi_{a,b}(t)=\frac{\varphi_{a+b}(t)}{\varphi_a(t)\varphi_b(t)}.\)

By (36) we conclude:

**Proposition 59.** _For integers_ \(n\ge 0\)_, let_ \(s_n(t)=\prod_{k=1}^n\frac{sin(kt)}{k}\) _. Then_

\(\varphi_{a,b}(t)=e^{itab/2}\frac{s_{a+b}(t/2)}{s_a(t/2)s_b(t/2)}\text{\textit{and}}|\varphi_{a,b}(t)|=\left|\frac{s_{a+b}(t/2)}{s_a(t/2)s_b(t/2)}\right|.\)

## 9.2 Center bound

For the first piece of the integral on the right-hand side of (35), we integrate \(|\varphi_{a,b}(t)|\) over the interval \([0,2\pi/(a+b)]\). For the sake of convenience, we substitute _t_ with 2_t_ in order to avoid the denominator of 2 in the sine terms of the integrand.

**Lemma 60 (center bound).** _For integers_ \(b\ge a\ge 2\),<tbc>

\(\int_0^\frac{2\pi}{a+b}|\varphi_{a,b}(t)|dt=2\int_0^\frac{\pi}{a+b}|\varphi_{a,b}(2t)|dt=O\left(\frac{1}{b\sqrt{a}}\right).\)

<tbc>We can write

\(|\varphi_{a,b}(2t)|=\prod_{k=1}^a\frac{k}{b+k}\cdot\frac{sin((b+k)t)}{sin(kt)}\)

as every term in the product on the right-hand side is nonnegative on this interval. We start with the following estimates.

**Claim 61.** _For positive integers_ \(k\le b\) _and_ \(x\in[0,\pi/(b+k)]\),

\(\frac{k}{b+k}\cdot\frac{sin((b+k)x)}{sin(kx)}\le 1-\frac{b^2}{2\pi^2}x^2.\)

To prove this claim, we first prove two trigonometric bounds. Refer to Fig. 13 for a plot of the functions and bounds.

**Claim 62.** _For positive integers k, and_ \(x\in[0,\pi/k]\),

\(sin(kx)\le kx-\frac{(kx)^3}{\pi^2}.\)

