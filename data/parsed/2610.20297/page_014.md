## Putting it Together: Choosing the Parameters.

We instantiate our algorithm with parameters<tbc>

\(c=21,\varepsilon=0.056,\gamma=0.0653,t=8.\)

<tbc>where \(c,\varepsilon,\gamma\) are chosen to match Theorem 1.1 and _t_ is a constant whose choice we justify later. Choose

\(B=\Theta\left(\frac{N^{\varepsilon/2}}{\sqrt{logU}}\right),P=\Theta(BlogU),h=\left\lceil\frac{\varepsilon\gamma}{t}logN\right\rceil.\)

Round _B_ down to a power of two. Choose the constant in _P_ sufficiently large, and then the constant in _B_ sufficiently small that \(2BP\unknown N^\varepsilon\). Thus \(BP=\Theta(N^\varepsilon)\).

Next, we aim to choose \(g_\ell\) so that the parameters of Lemma 3.12 are satisfied and we may apply Lemma 3.13. Before choosing \(g_\ell\) at level \(\ell\), we give a quick discussion on how this choice might affect the performance of Lemma 3.12. The constants in Theorem 3.11 may depend on parameters \(c,\varepsilon,\theta_\ell\) and therefore \(g_\ell\). To make these constants uniform over all levels and input sizes, we round each chosen \(g_\ell\) upward to the nearest multiple of 10<sup>-6</sup> (or any arbitrarily small fixed constant). Since \(g_\ell\) lies in a bounded range, there are _O_(1) total choices of \(g_\ell\) and the _O_() term of Theorem 3.11 can indeed be bounded by an absolute constant.

Following the above discussion, at level \(\ell\), choose \(g_\ell\) by rounding

\(\frac{\varepsilon\gamma logN+\ell}{\varepsilon logN-\ell}\)

upward to the nearest multiple of 10<sup>-6</sup>, and set \(q_\ell=q_c(g_\ell)\). Note that our choice of \(\gamma,t\) ensure \(h<\varepsilon logN\). Intuitively, since we make fewer queries at higher levels \(\ell\), we are willing to trade off slower queries in exchange for faster preprocessing.

We first check the hypotheses of Lemma 3.12. Note \(h\unknown logB\) by our choice of \(t,\gamma\). For every \(0\unknown\ell\unknown h\), we compute<tbc>

\(\gamma\unknown g_\ell\unknown g_h\unknown\frac{\varepsilon\gamma+\frac{h}{logN}}{\varepsilon-\frac{h}{logN}}+10^{-6}\unknown\frac{\varepsilon\gamma(t+1)+O(\frac{1}{logN})}{\varepsilon(t-\gamma)+O(\frac{1}{logN})}+10^{-6}\unknown\frac{\gamma(t+1)}{t-\gamma}+10^{-6}+O\left(\frac{1}{logN}\right)<0.075\)

<tbc>for sufficiently large _N_. Therefore, since _c_=21, we have<tbc>

\(0<\theta_\ell=\frac{g_\ell ln4}{ln(20/9)}<0.131<0.9.\)

<tbc>Next, observe that _R<sub>c</sub>_ is decreasing in _g_, so that

\(\varepsilon=0.056<R_c(0.075)\unknown R_c(g_\ell),\)

where _R_<sub>21</sub>(0.075)=0.05663927_..._. We have already ensured \(2B^{(\ell)}P\unknown 2BP\unknown N^\varepsilon\) so that Lemma 3.12 applies at every level.

By our choice of _B,P_ and \(\varepsilon\), we can bound the time required for Lemma 3.7 as \(\tilde{O}\left(N^{\omega+t\varepsilon}\right)=\tilde{O}\left(N^{3-\varepsilon\gamma}\right)\) as long as \(\omega+t\varepsilon\unknown 3-\varepsilon\gamma\) or \(t\unknown\frac{3-\omega-\varepsilon\gamma}{\varepsilon}\) , which our choices satisfy. Note that our choice of _P_ ensures that every prime in Q is smaller than _P_ for sufficiently large _N_. Note that this also bounds the time required by the \(\tilde{O}(N^2P^2)\) preprocessing term.

We next bound the preprocessing time required by Lemma 3.12. Since \(B^{(\ell)}P=\Theta(N^\varepsilon/2^\ell)\), we have<tbc>

\((B^{(\ell)}P)^{g_\ell}=\Theta\left(\left(N^\varepsilon/2^\ell\right)^{g_\ell}\right)=\Theta\left(2^{(\varepsilon logN-\ell)g_\ell}\right)=\Omega\left(N^{\varepsilon\gamma} 2^\ell\right).\)

<tbc>Using \(P/B^{(\ell)}=\Theta(2^\ell logU)\), the preprocessing term at each level is consequently<tbc>

\(\tilde{O}\left(\frac{N^3P}{B^{(\ell)}(B^{(\ell)}P)^{g_\ell}}\right)=\tilde{O}\left(N^{3-\varepsilon\gamma}\right).\)

