<tbc>_X(i_+1)-_X(i_), we have that _X_ is a supermartingale if \(\mathbb{E}'(\Delta X(i))\le 0\) and a submartingale if \(\mathbb{E}'(\Delta X(i))\ge X(i)\). Thus referring back to our vertex degree setting and letting \(S_{j,v}=[s_{j,v},T_{s_{j,v}}^-]\) for all _j_ for which _s<sub>j,v</sub>_ is defined, it suffices to show that \(\mathbb{E}'(\Delta d_v^-(i))\ge 0\) for all \(i\in S_{j,v}\) and _j_ for which _s<sub>j,v</sub>_ is defined. Once this is done, we may use the following concentration inequalities to prove that with high probability the random variables do not jump outside of their error bounds before time \(t=(1-n^{-\alpha_\mathrm{gr}})n\). It will then be clear that still with high probability this holds for all relevant random variables simultaneously via a union bound.

All inequalities are variations of the Hoeffding-Azuma inequality. The first two results are used for the variables tracking the number of edges in the process.

Lemma 5.1. _Let X(i_) _be a submartingale such that_ \(|\Delta X(i)|\le c_i\) _for all i. Then_<tbc>

\(\mathbb{P}(X(m)-X(0)\le-a)\le\mathrm{exp}\left(-\frac{a^2}{2\sum_{i\in[m]}c_i^2}\right).\)

<tbc>Lemma 5.2. _Let X(i_) _be a supermartingale such that_ \(|\Delta X(i)|\le c_i\) _for all i. Then_

\(\mathbb{P}(X(m)-X(0)\ge a)\le\mathrm{exp}\left(-\frac{a^2}{2\sum_{i\in[m]}c_i^2}\right).\)

The next two are used for all remaining variables we wish to track in the process.

Lemma 5.3. \[9\] _Let X(i_) _be a submartingale such that_ \(-\Theta\le\Delta X(i)\le\theta\) _for all i and_ \(\theta\le\Theta/2\)_. Then for any_ \(a<\theta m\) _we have_<tbc>

\(\mathbb{P}(X(m)-X(0)\le-a)\le\mathrm{exp}\left(-\frac{a^2}{3\theta\Theta m}\right).\)

<tbc>Lemma 5.4. \[9\] _Let X(i_) _be a supermartingale such that_ \(-\Theta\le\Delta X(i)\le\theta\) _for all i and_ \(\theta\le\Theta/10\)_. Then for any_ \(a<\theta m\) _we have_

\(\mathbb{P}(X(m)-X(0)\ge a)\le\mathrm{exp}\left(-\frac{a^2}{3\theta\Theta m}\right).\)

Turning again to the setting of vertex degrees, using the latter two results with _f<sub>d</sub>_(1-_o_(1)) in place of _a_ if the hypotheses are satisfied and (_f<sub>d</sub>_(1-_o_(1)))<sup>2</sup> is sufficiently large, we get that with high probability \(d_v^-(T_{s_{j,v}}^-)-d_v^-(s_{j,v})>-f_d(1-o(1))\). Thus, since, \(d_v^-(s_{j,v})=np^3-e_d+f_d(1-o(1))\) we get that \(d_v^-(T_{s_{j,v}}^-)>np^3-e_d\) and since \(d_v^-(T_{s_{j,v}}^-)\) is not in the lower critical interval by definition, and \(T_{s_{j,v}}^-\) is the first time after _s<sub>j,v</sub>_ for which this is true, it follows that with high probability \(d_v^-(T_{s_{j,v}}^-)\in[np^3-e_d+f_d,np^3-e_d+f_d(1+o(1))]\). The required _o(f<sub>d</sub>_) term is determined by the maximum of \(|\Delta d_v^-(i)|\) which we’ll see below is indeed _o(f<sub>d</sub>_).

Given the above discussion and results, we can reduce the problem to considering the following _trend hypotheses_, which yield the necessary supermartingale and submartingale properties of \(X^\pm\), and _boundedness hypotheses_ which are the necessary constraints to successfully apply the relevant martingale concentration inequalities as required. In particular,

**Trend hypotheses:**

_Supermartingale conditions:_

If \(Q^+(i)\ge-bn^2\) then \(\mathbb{E}'(\Delta Q^+(i))\le 0\).

If \(d_v^+(i)\ge-b^{2/3}n\) then \(\mathbb{E}'(\Delta d_v^+(i))\le 0\).

