When \(|s-s^*|<2^{k_\ell}\) we give a lower bound on \(\left|\mathcal{A}_I^{s-2^{k_\ell}}\right|\left|\mathcal{A}_I^{s+2^{k_\ell}}\right|/\left|\mathcal{A}_I^s\right|^2\) and then use the arithmetic geometric mean equality to deduce that \(\left|\mathcal{A}_I^{s-2^{k_\ell}}\right|+\left|\mathcal{A}_I^{s+2^{k_\ell}}\right|\ge(2/\alpha)\left|\mathcal{A}_I^s\right|\). Using a telescoping product, we have that:<tbc>

\(\frac{\left|\mathcal{A}_I^{s-2^{k_\ell}}\right|\left|\mathcal{A}_I^{s+2^{k_\ell}}\right|}{\left|\mathcal{A}_I^s\right|^2}=\prod_{j=1}^{2^{k_\ell}}\frac{\left|\mathcal{A}_I^{s-j}\right|}{\left|\mathcal{A}_I^{s-j+1}\right|}\frac{\left|\mathcal{A}_I^{s+j}\right|}{\left|\mathcal{A}_I^{s+j-1}\right|}.\)

<tbc>We first show that the telescoping product is well-defined, i.e., that all terms \(\left|\mathcal{A}_I^w\right|\), \(s-2^{k_\ell}\le w\le s+2^{k_\ell}\), are positive. The left binomial term of Eq. (8) for \(\left|\mathcal{A}_I^w\right|\) is \(\genfrac(){pt}{2}{x_\mathrm{min}}{w}\). From Eq. (7) we have that \(x_\mathrm{min}=\Theta(n)\). Also, \(|w-s^*|\le|w-s|+|s-s^*|\le 2\sqrt{n}\) and so, since \(s^*=x_\mathrm{min}/2+O(\sqrt{n})\) by Eq. (9), we have

\(w=x_\mathrm{min}/2\pm O(\sqrt{n}).\)

Therefore for sufficiently large _n_, since \(x_\mathrm{min}=\Theta(n)\), _w_ is positive and less than the upper index, _x_<sub>min</sub>, so the first binomial term, \(\genfrac(){pt}{2}{x_\mathrm{min}}{w}\), is positive.

Now consider the right binomial term of Eq. (8) for \(\left|\mathcal{A}_I^w\right|\), which is \(\genfrac(){pt}{2}{n-x_\mathrm{max}-1}{n/2-|I|-w}\). We have that \(x_\mathrm{max}\le 5n/8+O(\sqrt{n})\), so the upper index of the binomial is at least \(3n/8-O(\sqrt{n})\). Using the expression for _w_ above, as well as the fact that \(|I|\le x_\mathrm{max}-x_\mathrm{min}+1=O(\sqrt{n})\), Eq. (6), we can bound the lower index as follows:

\(n/2-|I|-w=n/2-x_\mathrm{min}/2\pm O(\sqrt{n})\ge n/2-x_\mathrm{max}/2\pm O(\sqrt{n}),\)

which again is positive and is less than the upper index for sufficiently large _n_.

We now expand the telescoping product above:

\(\frac{\left|\mathcal{A}_I^{s-2^{k_\ell}}\right|\left|\mathcal{A}_I^{s+2^{k_\ell}}\right|}{\left|\mathcal{A}_I^s\right|^2}=\prod_{j=1}^{2^{k_\ell}}\frac{\left|\mathcal{A}_I^{s-j}\right|}{\left|\mathcal{A}_I^{s-j+1}\right|}\frac{\left|\mathcal{A}_I^{s+j}\right|}{\left|\mathcal{A}_I^{s+j-1}\right|}=\prod_{j=1}^{2^{k_\ell}}\frac{\left(s-j+1\right)(n/2-x_\mathrm{max}+|I|+s-j)}{(x_\mathrm{min}-s+j)(n/2-|I|-s+j)}\frac{\left|\mathcal{A}_I^{s+j}\right|}{\left|\mathcal{A}_I^{s+j-1}\right|}=\prod_{j=1}^{2^{k_\ell}}\frac{\left(s-j+1\right)(n/2-x_\mathrm{max}+|I|+s-j)}{(x_\mathrm{min}-s+j)(n/2-|I|-s+j)}\frac{(x_\mathrm{min}-s-j+1)(n/2-|I|-s-j+1)}{(s+j)(n/2-x_\mathrm{max}+|I|+s+j-1)}=\prod_{j=1}^{2^{k_\ell}}\big(\frac{s-j+1}{s+j}\big)\big(\frac{x_\mathrm{min}-s-j+1}{x_\mathrm{min}-s+j}\big)\big(\frac{n/2-|I|-s-j+1}{n/2-|I|-s+j}\big)\big(\frac{n/2-x_\mathrm{max}-1+|I|+s-j+1}{n/2-x_\mathrm{max}-1+|I|+s+j}\big).\)

In the last line, inside the product there are four terms, each of the form \(\frac{z-j+1}{z+j}\) , where, from our previous derivations, \(z=\Theta(n)\) and \(j\le\sqrt{n}\). Therefore for some positive constant _c_, each of these terms is at least \(1-c/\sqrt{n}\). Therefore, since \(k_\ell\le\sqrt{n}\),<tbc>

\(\frac{\left|\mathcal{A}_I^{s-2^{k_\ell}}\right|\left|\mathcal{A}_I^{s+2^{k_\ell}}\right|}{\left|\mathcal{A}_I^s\right|^2}\ge(1-c/\sqrt{n})^{4\sqrt{n}}\ge(1/4)^{4c},\)

