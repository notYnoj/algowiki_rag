_Proof._ Since E<sup>(_i_)</sup>_S_ does not depend on _x<sub>i</sub>_,

\(D_iS(x)=\frac{(S-\mathbb{E}^{(i)}S)(x_1,\dots,x_i,\dots,x_n)-(S-\mathbb{E}^{(i)}S)(x_1,\dots,-x_i,\dots,x_n)}{2}\)<br>
\(=\frac{d_iS(x_1,\dots,x_i,\dots,x_n)-d_iS(x_1,\dots,-x_i,\dots,x_n)}{2}\)<br>
\(=d_iS(x),\)

where, above, the last equality follows _d<sub>i</sub>S(x_<sub>1</sub>_,...,_1_,...,x<sub>n</sub>_)=-_d<sub>i</sub>S(x_<sub>1</sub>_,...,_-1_,...,x<sub>n</sub>_) since E<sup>(_i_)</sup>(_d<sub>i</sub>S(X_))=0.

The above implies a slightly weaker \[18, Theorem 1.2\], i.e., with a different absolute constant, but the fact that Enflo type and Rademacher type coincide still follows from Theorem 2.1 just as it follows from \[18, Theorem 1.4\] with, as indicated there, a routine symmetrization argument.

To make the connection complete, recall the additional notations in \[18\]: the operator \(\Delta\) is defined by<tbc>

\(\Delta:=\sum_{i=1}^nD^i,\)

<tbc>and the semigroup _P<sub>t</sub>_ is defined as<tbc>

\(P_t:=\mathrm{e}^{-t\Delta}.\)

<tbc>When the _X<sub>i</sub>_’s are Rademacher random variables, the crucial observation in \[18\] is that (we denote by \(\xi'\), \(\delta'\) the variables \(\xi\), \(\delta\) introduced there, to avoid any confusion with \(\delta\) previously defined):

\(-\frac{\mathrm{d}P_tS}{\mathrm{d}t}=\frac{1}{\sqrt{\mathrm{e}^{2t}-1}}\mathbb{E}_{\xi^\prime(t)}\left(\sum_{i=1}^n\delta'_i(t)D_iS(\xi'(t)X)\right),\) (2.6)

where \(\xi'(t)X\) is defined as \((\xi'_1(t)X_1,\dots,\xi'_n(t)X_n)\).

Something similar holds in a more general framework (when the \(X'_is\) are random variables taking a finite number of values):

**Theorem 2.3.** _With the same assumptions as in Theorem 2.1,_

\(-\frac{\mathrm{d}\mathbb{E}_{X^\prime,US}(X^{(\alpha)})}{\mathrm{d}\alpha}=\frac{1}{\sqrt{\alpha(1-\alpha)}}\mathbb{E}_{X^\prime,U}\left(\sum_{i=1}^n\delta_i(\alpha)d_iS(X^{(\alpha)})\right).\)

_Proof._ This is essentially the same proof as the proof of Theorem 2.1.

We conclude this section with a remark on the Talagrand _L_<sub>1</sub>-_L_<sub>2</sub> inequality in Banach spaces of Rademacher type 2.

As noted in \[6\], it is natural, to try to understand for which Banach spaces \((E,\|\cdot\|_E)\) there exists _C=C(E)\>_0 such that for any function _S_ of i.i.d. Rademacher random variables _X_<sub>1</sub>_,...,X<sub>n</sub>_ taking values in _E_,

\(\|S-\mathbb{E}S\|_{E,2}^2\le C\sigma(S)\sum_{i=1}^n\frac{\|D_iS\|_{E,2}^2}{1+\mathrm{log}\left(\frac{\|D_iS\|_{E,2}}{\|D_iS\|_{E,1}}\right)},\) (2.7)

where \(\|\cdot\|_{E,k}=\left(\mathbb{E}\|\cdot\|_E^k\right)^{1/k}\), which is a generalization of Talagrand’s _L_<sub>1</sub>-_L_<sub>2</sub> inequality (see Theorem 3.7) to Banach spaces.

Clearly, if a Banach space satisfies (2.7), it must be of Rademacher type 2. It is still unknown whether or not the converse is true. To date, the best result is \[6, Theorem 1\]:

