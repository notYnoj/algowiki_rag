We call the ratios \(\big|P_X^{(0)}\big|\big/M_X\), \(\big|P_Y^{(0)}\big|\big/M_Y\), \(\big|P_Z^{(0)}\big|\big/M_Z\) the _fraction of holes_ in the _X_-, _Y_ -, _Z_-dimension respectively.

We will show that we can degenerate sub-polynomially many broken copies of _T_ with small fraction of holes in all three dimensions into an unbroken copy of _T_ if _T_ satisfies the following property.

**Property 7.1.** There exists a subset \(\mathcal{G}\subseteq\mathcal{S}_{N_X}\times\mathcal{S}_{N_Y}\times\mathcal{S}_{N_Z}\) of permutations over the variables of _T_ where S_<sub>N</sub>_ denotes the symmetric group on \[_N_\], such that G satisfies the following:

1. Every \((\pi_X,\pi_Y,\pi_Z)\in\mathcal{G}\) _preserves the partitions_. Specifically, it permutes any part into some entire part, i.e., for every part \(X_t\in\mathcal{P}_X\), there exists \(X_{t^\prime}\in\mathcal{P}_X\) such that \(\pi_X(X_t):=\{\pi_X(x)|x\in X_t\}=X_{t^\prime}\). Similar conditions hold for _Y_ - and _Z_-parts. Hence, \(\pi_X,\pi_Y,\pi_Z\) also induce permutations on P_<sub>X</sub>,_P_<sub>Y</sub>,_P_<sub>Z</sub>_, respectively.<tbc>

2. Every \((\pi_X,\pi_Y,\pi_Z)\in\mathcal{G}\) _preserves the tensor structure of T_. Formally, the coefficient of \(x_i\cdot y_j\cdot z_k\) in _T_ equals the coefficient of \(\pi_X(x_i)\cdot\pi_Y(y_j)\cdot\pi_Z(z_k)\) in _T_, for all variables _x<sub>i</sub>,y<sub>j</sub>,z<sub>k</sub>_.<tbc>

3. A uniformly random element \((\pi_X,\pi_Y,\pi_Z)\in\mathcal{G}\) _permutes any given part to a uniform random part_. Formally, for any fixed \(X_t,X_{t^\prime}\in\mathcal{P}_X\), \(Y_t,Y_{t^\prime}\in\mathcal{P}_Y\), \(Z_t,Z_{t^\prime}\in\mathcal{P}_Z\), and for a uniformly random \((\pi_X,\pi_Y,\pi_Z)\in\mathcal{G}\), we have

\(Pr[\pi_X(X_t)=X_{t^\prime}]=\frac{1}{M_X},\)<br>
\(Pr[\pi_Y(Y_t)=Y_{t^\prime}]=\frac{1}{M_Y},\)<br>
\(Pr[\pi_Z(Z_t)=Z_{t^\prime}]=\frac{1}{M_Z}.\)

We show the following.

**Theorem 7.2.** _Let T be a partitioned tensor defined above; let T_<sub>1</sub>_,...,T<sub>r</sub> be broken copies of T, where in each T<sub>i</sub> for_ \(i\in[r]\)_, at most_ \(\frac{1}{4logM_X}\), \(\frac{1}{4logM_Y}\)_, and_ \(\frac{1}{4logM_Z}\) _fraction of X-, Y -, and Z-parts are holes, respectively. If T satisfies Property 7.1 with a set of permutations_ G_, then there exists a constant C_<sub>0</sub> _such that for_ \(r\ge C_0\cdot M^\frac{3}{loglogN}\) _where M_=max{_M<sub>X</sub>,M<sub>Y</sub>,M<sub>Z</sub>}, we have_

\(\oplus_{i=1}^rT_i\unknown T.\)

_In particular, M_<sup>_o_(1)</sup> _broken copies of T with fraction of holes_ \(O\big(\frac{1}{logM}\big)\) _can degenerate into an unbroken copy of T._

Before proving Theorem 7.2, we first show the following Lemma 7.3 that will explain why we need Item 3 in Property 7.1. The lemma essentially states that if _T_ satisfies Property 7.1, then we can find a set of permutations \(\pi_X,\pi_Y,\pi_Z\) on the partitions of _X_-, _Y_ -, _Z_-variables such that any set of parts can be permuted away from any set of positions that we specify. Specifically, one should think under the context of degenerating a broken copy of _T_ with holes into some subtensor \(T|_{X^\prime,Y^\prime,Z^\prime}\), the lemma states that we can find a set of permutations preserving the tensor structure of _T_ on the variable sets such that the holes are away from the terms in \(T|_{X^\prime,Y^\prime,Z^\prime}\). Then applying the permutation on the broken copy would give the subtensor \(T|_{X^\prime,Y^\prime,Z^\prime}\) without holes or with fewer amount of holes.

