<tbc>We now bound the query time, recall that _q_<sub>21</sub> is concave in \(g_\ell\), since entropy is concave and \(\theta=g\mathrm{ln}4/\mathrm{ln}(20/9)\) is linear in _g_. Our choice of \(\gamma\) satisfies<tbc>

\(q_{21}(\gamma)+10^{-6}q'_{21}(\gamma)+\gamma=0.49998460\dots<\frac{1}{2},\)<br>
\((1+\gamma)q'_{21}(\gamma)-q_{21}(\gamma)=5.24066398\dots<6.\)

<tbc>By concavity and our choice of \(g_\ell\), we have<tbc>

\(q_{21}(g_\ell)\le q_{21}(\gamma)+q'_{21}(\gamma)(g_\ell-\gamma)\le q_{21}(\gamma)+q'_{21}(\gamma)\left(\frac{(1+\gamma)\ell}{\varepsilon\mathrm{log}N-\ell}+10^{-6}\right).\)

<tbc>Multiplying by \((\varepsilon\mathrm{log}N-\ell)>0\) and using the two inequalities above gives

\((\varepsilon\mathrm{log}N-\ell)q_{21}(g_\ell)\le(\varepsilon\mathrm{log}N-\ell)q_{21}(\gamma)+(1+\gamma)\ell q'_{21}(\gamma)+10^{-6}q'_{21}(\gamma)(\varepsilon\mathrm{log}N-\ell)\)<br>
\(=(q_{21}(\gamma)+10^{-6}q'_{21}(\gamma))\varepsilon\mathrm{log}N+((1+\gamma)q'_{21}(\gamma)-q_{21}(\gamma)-10^{-6}q'_{21}(\gamma))\ell\)

Since _q_<sub>21</sub> is increasing, we have \(q'_{21}(\gamma)>0\) and we may drop the last term in the upper bound. Applying the two inequalities above, we have<tbc>

\((\varepsilon\mathrm{log}N-\ell)q_{21}(g_\ell)<\varepsilon\mathrm{log}N(0.5-\gamma)+6\ell\)

<tbc>so that the time to compute one level \(\ell\) query is \((B^{(\ell)}P)^{q_{21}(g_\ell)}=O\left(N^{\varepsilon(0.5-\gamma)}2^{6\ell}\right)\). Note that we also have \(q_{21}(g_\ell)\le q_{21}(0.075)<0.5\) since _q_<sub>21</sub> is increasing, so we may also upper bound \((B^{(\ell)}P)^{q_{21}(g_\ell)}<(BP)^{1/2}=\tilde{O}(N^{\varepsilon/2})\). From Lemma 3.13, the total time to compute all queries is

\(\tilde{O}\left(N^{2+\varepsilon/2}+\sum_\ell\frac{N^3}{B2^{\ell(t-1)}}N^{\varepsilon(0.5-\gamma)}2^{6\ell}\right)=\tilde{O}\left(N^{2+\varepsilon/2}+\sum_\ell\frac{N^{3-\varepsilon\gamma}}{2^{\ell(t-7)}}\right)\)<br>
\(=\tilde{O}\left(N^{2+\varepsilon/2}+N^{3-\varepsilon\gamma}\right)\)

by our choice of _t\>_7. The final scan at level _h_ requires time \(O\left(\frac{N^2B}{2^h}+\frac{N^3}{2^{h\tau}}\right)=\tilde{O}\left(N^{2+\varepsilon/2}+N^{3-\varepsilon\gamma}\right)=\tilde{O}\left(N^{3-\varepsilon\gamma}\right)\) as long as \(2+\varepsilon/2\le 3-\varepsilon\gamma\) or \(\gamma\le\frac{2-\varepsilon}{2\varepsilon}\) , which holds for our choices of \(\varepsilon,\gamma\). We conclude the proof by observing that Lemma 3.2 costs a logarithmic factor.

## References

