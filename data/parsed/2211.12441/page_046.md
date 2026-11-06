Because |sin(_t_)| is increasing here and |sin(2_t_)| is symmetric about \(\frac{\pi}{4}\) , the value of the integral on the interval \([\frac{\pi}{2n},\frac{\pi}{4}]\) exceeds the value on the interval \([\frac{\pi}{4},\frac{\pi}{2}-\frac{\pi}{2n}]\). Using Fact 66,<tbc>

\(\frac{2}{b^2}\int_{\frac{\pi}{2n}}^\frac{\pi}{4}\big|\frac{1}{sin(t)sin(2t)}\big|dt\le\frac{1}{b^2}\int_{\frac{\pi}{2n}}^\frac{\pi}{4}\big(\frac{\pi}{2}\big)^2\frac{1}{t^2}dt\le\frac{\pi^2}{4b^2}\cdot\frac{2n}{\pi}=\frac{\pi n}{2b^2}.\)

<tbc>We have now established that

\(\int_{\frac{\pi}{2n}}^{\frac{\pi}{2}-\frac{\pi}{2n}}|\varphi_{a,b}(2t)|dt\le\frac{\pi n}{b^2}.\)

### Region III.

Notice that |sin(_t_)| is increasing on the interval \([\frac{\pi}{2}-\frac{\pi}{2n},\frac{\pi}{2}]\), so we can bound |sin(_t_)| by \(|sin(\frac{\pi}{2}-\frac{\pi}{2n})|\). Similar to before, the first step follows from Lemma 65, this time applied to \(k\in\{2,\dots,a\}\).

\(\int_{\frac{\pi}{2}-\frac{\pi}{2n}}^\frac{\pi}{2}|\varphi_{a,b}(2t)|dt\le\int_{\frac{\pi}{2}-\frac{\pi}{2n}}^\frac{\pi}{2}\frac{1}{\beta_t(1)}\big|\frac{sin(\beta_1(t))}{sin(t)}\big|dt\le\int_{\frac{\pi}{2}-\frac{\pi}{2n}}^\frac{\pi}{2}\frac{1}{|bsin(t)|}dt\)<br>
\(\le\frac{\pi}{2n}\cdot\frac{1}{bsin(\frac{\pi}{2}-\frac{\pi}{2n})}\le\frac{\pi}{2n}\frac{1}{b(1-\frac{1}{n})}=\frac{\pi}{2b(n-1)}.\)

### Overall bound.

Summing the above bounds, we can deduce that

\(\int_{\frac{\pi}{a+b}}^\frac{\pi}{2}|\varphi_{a,b}(2t)|dt\le\frac{\pi}{b(n-1)}+\frac{\pi n}{b^2}.\)

By choosing \(n=\lceil\sqrt{a}\rceil\) (keeping in mind that \(b\ge a\ge 2\)), we can deduce Lemma 64.

## 9.4 Pole reduction

Finally, we prove the pole reduction lemma (Lemma 65). The essence is an interval matching strategy capture Lemma 67. Here is the intuition.

Recall that we want to upper bound factors of the form \(|\frac{sin(\ell t)}{\ell}|\) by rescaled versions \(|\frac{sin(kt)}{k}|\) of the same pattern, where \(\ell\in\{b+1,\dots,b+a\}\) and \(k\in\{1,\dots,a\}\) are matched. The matching definitely needs to avoid situations like in Figure 14a, where \(|\frac{sin(kt)}{k}|\) vanishes at the point _t_ while \(|\frac{sin(\ell t)}{\ell}|\) does not. Ideally, the period of the _k_-scaled version that contains the point _t_ encloses the period of the \(\ell\)-scaled version that contains _t_, like in Figure 14b. As long as the pattern is convex, this ensures that the _k_-scaled version is larger than the \(\ell\)-scaled version everywhere on the encompassed period. (We will formally prove this in Claim 74.) Thus, if at every point _t_, we can set up a matching such that the enclosing relationship holds for all matched pairs, we are home free. Lemma 67 below does exactly this.

Let us first introduce some notation. For every real number _t_ and positive integer _k_, there is a unique integer _n_ such that _t_ is contained in the half-open interval \[_n/k,(n_+1)_/k_). We call this interval the _k-interval_ of _t_. For positive integers \(k,\ell\), we can say that the _k_-interval of _t encloses_ the \(\ell\)-interval of _t_ if the \(\ell\)-interval of _t_ is a subset of the _k_-interval of _t_. We use the shorthand that _k_ encloses \(\ell\) at _t_.

