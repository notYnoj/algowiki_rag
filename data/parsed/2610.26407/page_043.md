<tbc>For Poisson and Gamma observations, write _q=e<sup>z</sup>_. Then<tbc>

\(d_i(x_i,q)=\left\{\begin{array}{ c c }
x_i(e^\nu-1-v), & v=z-logx_i,\text{Poisson}, \\
\kappa_i(e^\nu-1-v), & v=logx_i-z,\text{Gamma}.
\end{array}\right.\)

<tbc>Since \(x_i,\kappa_i>0\) and \(dv/dz=\pm 1\), it suffices to show that 1/(_e<sup>v</sup>_-1-_v_) is strictly convex for \(v\neq 0\). Differentiating gives<tbc>

\(\frac{d^2}{dv^2}\frac{1}{e^\nu-1-v}=\frac{e^\nu(e^\nu+2e^{-v}+v-3)}{(e^\nu-1-v)^3}.\)

<tbc>The denominator is positive for \(v\neq 0\). To show that the numerator is positive, use _e<sup>v</sup>\>_1+_v_ and _e_<sup>-_v_</sup>_\>_1-_v_ to get

\(e^\nu+2e^{-v}+v-3>(1+v)+2(1-v)+v-3=0.\)

Thus the second derivative is positive, proving strict convexity in _z_ for both families. \(\square\)

_Proof of Lemma 4_ By Lemma 9 and the proof of Lemma 7, \(\unknown(t)\rightarrow\unknown^0\). Define

\(H_t(q):=\sum_i\frac{1}{d_i(\mu_i(t),q)},H(q):=\sum_i\frac{1}{d_i(\theta_i^0,q)}.\)

We will show that every limit of _q_<sup>†</sup>(_t_) belongs to \((\theta_{k+1}^0,\theta_k^0)\) and minimizes _H_. Uniqueness then gives convergence to _q_<sup>†</sup>.

Since \(\mu_{[k]}(t)\rightarrow\theta_k^0\) and \(\mu_{[k+1]}(t)\rightarrow\theta_{k+1}^0\), eventually \(\mu_{[k+1]}(t)<q^\dagger<\mu_{[k]}(t)\). Since _q_<sup>†</sup>(_t_) minimizes _H<sub>t</sub>_ on this interval,<tbc>

\(H_t(q^\dagger(t))\le H_t(q^\dagger)\longrightarrow H(q^\dagger)<\infty.\) (26)

<tbc>Let \(t_n\rightarrow\infty\) satisfy \(q^\dagger(t_n)\rightarrow\bar{q}\). Since \(\mu_{[k+1]}(t)\le q^\dagger(t)\le\mu_{[k]}(t)\), we have \(\bar{q}\in[\theta_{k+1}^0,\theta_k^0]\). If \(\bar{q}=\theta_k^0\) (and likewise \(\bar{q}=\theta_{k+1}^0\)), then<tbc>

\(H_{t_n}(q^\dagger(t_n))\ge\frac{1}{d_k(\mu_k(t_n),q^\dagger(t_n))}\longrightarrow\infty,\)

<tbc>contradicting (26). Therefore \(\bar{q}\in(\theta_{k+1}^0,\theta_k^0)\), and continuity gives

\(H(\bar{q})=lim_{n\rightarrow\infty} H_{t_n}(q^\dagger(t_n))\le H(q^\dagger).\)

Thus \(\bar{q}\) minimizes _H_, and Assumption 3 gives \(\bar{q}=q^\dagger\). Since _q_<sup>†</sup>(_t_) is eventually contained in a compact interval and every such limit equals _q_<sup>†</sup>, we conclude that \(q^\dagger(t)\rightarrow q^\dagger\). \(\square\)

_Proof of Theorem 2_ By Lemma 4 and Theorem 1(ii),<tbc>

\(-\frac{logEOC(\mathcal{H}_t)}{\sum_iN_i(t)}\longrightarrow\Gamma(w(q^\dagger);\unknown^0)\le\Gamma^*(\unknown^0).\)

<tbc>For the lower bound, write \(H(q):=\sum_i1/d_i(\theta_i^0,q)\). Part (iii) of Theorem 1 gives

\(\Gamma(w(q^\dagger);\unknown^0)\ge\frac{1}{H(q^\dagger)}.\)

It therefore remains to show \(\Gamma^*(\unknown^0)/2\le 1/H(q^\dagger)\).

