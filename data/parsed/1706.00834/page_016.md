<tbc>this is true since \(\widehat{f}_\mathrm{in}(s)=f_\mathrm{in}(s)=1\). For _i\>_1:

\(\widehat{f}_\mathrm{in}(v_i)=\sum_{m=(v,U)\in M_{v_i}^{(\mathrm{in})}}w_m\widehat{f}_\mathrm{in}(v)\)<br>
\(=\sum_{m=(v,U)\in M_{v_i}^{(\mathrm{in})}}w_mf_\mathrm{in}(v)\text{(Inductive hypothesis)}\)<br>
\(=\sum_{m=(v,U)\in M_{v_i}^{(\mathrm{in})}}\frac{f_m}{f_\mathrm{in}(v)}f_\mathrm{in}(v)\text{(Definition of}w_m\text{)}\)<br>
\(=\sum_{m=(v,U)\in M_{v_i}^{(\mathrm{in})}}f_m=f_\mathrm{in}(v_i)\)

and that completes the induction. Now for each multiedge \(m=(v,U)\in M\) we have:

\(\widehat{f}_m=\widehat{f}_\mathrm{in}(v)w_m=\widehat{f}_\mathrm{in}(v)\frac{f_m}{f_\mathrm{in}(v)}=f_m\)

Thus \(f=\widehat{f}\).

To construct D, we must find all the weights _w<sub>m</sub>_. To do so, we will have two passes over the set of multiedges _M_. In the first pass, we compute all incoming flows _f_<sub>in</sub>(_v_) for all \(v\in V\) in _O(c|M_|) time. Then in the second pass we find all the weights \(w_m=\frac{f_m}{f_\mathrm{in}(v)}\) in _O_(|_M_|) time. Having constructed D, we can efficiently sample a multipath with the right expectation.

## Regret Bound.

The regret bound for CH depends on a good choice of the initial weight vector **_f_**<sup>init</sup> in the unit-flow polytope. We use an initialization technique similar to the one discussed in Rahmanian et al. (2018). Instead of explicitly selecting **_f_**<sup>init</sup> in the unit-flow polytope, the initial weight is obtained by projecting a point \(\widehat{f}^\mathrm{init}\) outside of the polytope to its inside. This yields the following regret bounds.

**Theorem 14** _Given a multi-DAG_ H=(_V,M), let D be an upper-bound on the_ 1_-norm of the count vectors of the multipaths (i.e._ \(\|\unknown\|_1\le D\) _for all multipaths_ \(\unknown\)_). Also denote the total loss of the best multipath by L_<sup>∗</sup>_. Then with proper tuning of the learning rate_ \(\eta\) _over the trials, CH guarantees:_<tbc>

\(\mathcal{R}_{CH}\le\sqrt{2L^*D\left(\mathrm{log}|M|+\mathrm{log}D\right)}+D\mathrm{log}|M|+D\mathrm{log}D.\)

<tbc>_Moreover, when the multipaths are bit vectors, then:_<tbc>

\(\mathcal{R}_{CH}\le\sqrt{2L^*D\mathrm{log}|M|}+D\mathrm{log}|M|.\)

<tbc>**Proof.** According to Koolen et al. (2010), with proper tuning of the learning rate \(\eta\), the regret bound of CH is:

\(\mathcal{R}_\mathrm{CH}\le\sqrt{2L^*\Delta(\unknown||f^\mathrm{init})}+\Delta(\unknown||f^\mathrm{init}),\) (10)

