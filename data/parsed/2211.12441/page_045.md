A basic bound can be found by applying Lemma 65 on \(|\varphi_{a,b}(2t)|\) for _k_=2_,...,a_, resulting in an upper bound of 1_/b_sin(_t_). This bound is usable, but is weak on points closer to 0. To remedy this, we can divide the domain of integration into multiple parts, where the points closer to 0 can safely include more terms in the denominator.

Let \(2\le n\le a\) be an integer. We split the domain of integration into three intervals: \([\frac{\pi}{a+b},\frac{\pi}{2n}]\), \([\frac{\pi}{2n},\frac{\pi}{2}-\frac{\pi}{2n}]\), and \([\frac{\pi}{2}-\frac{\pi}{2n},\frac{\pi}{2}]\). By selecting a good value of _n_, we can get a reasonable upper bound on this region. Here, we will make use of Lemma 65 and the following linear approximation to sine:

**Fact 66.** _For a positive integer k and_ \(t\in[0,\pi/2k]\),

\(\mathrm{sin}(kt)\ge\frac{2kt}{\pi}.\)

_Proof._ Notice that \(\mathrm{sin}(kt)=\frac{2kt}{\pi}\) when _t_=0 and \(t=\frac{\pi}{2k}\). This fact then follows since sine is concave on this interval.

**Region I.** The first region of integration is \([\pi/(a+b),\pi/(2n)]\).

\(\int_{\frac{\pi}{a+b}}^{\frac{\pi}{2n}}|\varphi_{a,b}(2t)|dt\le\int_{\frac{\pi}{a+b}}^{\frac{\pi}{2n}}\frac{n!}{\beta_t(1)\cdots\beta_t(n)}\left|\frac{\mathrm{sin}(\beta_t(1)t)\cdots\mathrm{sin}(\beta_t(n)t)}{\mathrm{sin}(t)\cdots\mathrm{sin}(nt)}\right|dt\)<br>
\(\le\frac{n!}{b^n}\int_{\frac{\pi}{a+b}}^{\frac{\pi}{2n}}\left|\frac{1}{\mathrm{sin}(t)\cdots\mathrm{sin}(nt)}\right|dt\)<br>
\(\le\frac{1}{b^n}\int_{\frac{\pi}{a+b}}^{\frac{\pi}{2n}}\left(\frac{\pi}{2}\right)^n\frac{1}{t^n}dt\)<br>
\(\le\frac{1}{b^n}\cdot\left(\frac{\pi}{2}\right)^n\cdot\frac{1}{n-1}\cdot\left(\frac{a+b}{\pi}\right)^{n-1}\)<br>
\(\le\frac{1}{b^n}\cdot\left(\frac{\pi}{2}\right)^n\cdot\frac{1}{n-1}\cdot\left(\frac{2b}{\pi}\right)^{n-1}\)<br>
\(\le\frac{\pi}{2b(n-1)}.\)

The first two steps involve applying Lemma 65 on all \(k\in\{n+1,\dots,a\}\), and then using the fact that \(|\mathrm{sin}(x)|\le 1\) and \(\beta_t(k)\ge b\). The third step uses Fact 66 for \(k\in\{1,\dots,n\}\), which applies on the interval \([\pi/(a+b),\pi/(2n)]\) for these values of _k_. From there, we bound with the left limit of integration.

**Region II.** We now bound \(|\varphi_{a,b}(2t)|\) on the interval \([\frac{\pi}{2n},\frac{\pi}{2}-\frac{\pi}{2n}]\). We can use Lemma 65 to eliminate all terms except \(k\in\{1,2\}\) this time.

\(\int_{\frac{\pi}{2n}}^{\frac{\pi}{2}-\frac{\pi}{2n}}|\varphi_{a,b}(2t)|dt\le\int_{\frac{\pi}{2n}}^{\frac{\pi}{2}-\frac{\pi}{2n}}\frac{2}{\beta_t(1)\beta_t(2)}\left|\frac{\mathrm{sin}(\beta_t(1)t)\mathrm{sin}(\beta_t(2)t)}{\mathrm{sin}(t)\mathrm{sin}(2t)}\right|dt\)<br>
\(\le\frac{2}{b^2}\int_{\frac{\pi}{2n}}^{\frac{\pi}{2}-\frac{\pi}{2n}}\left|\frac{1}{\mathrm{sin}(t)\mathrm{sin}(2t)}\right|dt.\)

