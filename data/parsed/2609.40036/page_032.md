**Lemma 4** (Pairwise bound and syndrome budget)**.** _For_ 0_\<p\<_1/2 _and a fixed nonzero flow of weight w,_<tbc>

\(Pr\{|E-f|\le|E|\}\le B_\Theta(p)^w.\) (126)

<tbc>_Let u=Dp\>_0_. Uniformly over simple D-regular graphs, outside an event of probability at most_<tbc>

\(\eta_n=e^{-u^2n/D}+e^{-u^4n/(4D)},\) (127)

<tbc>_every favorable connected flow support has w edges and w-t vertices with_

\(w\le 2un,t\le 2u^2n.\) (128)

_Proof._ On an edge where \(f_e\neq 0\), the score increment is

\(S_e=\unknown_{\{E_e=f_e\}}-\unknown_{\{E_e=0\}}.\) (129)

Its probabilities at 1 and -1 are \(p\theta_e(f_e)\) and 1-_p_. Set

\(t_\Theta=\frac{1}{2}log\frac{1-p}{p\Theta}>0.\) (130)

For every edge in the support of _f_,

\(\unknown e^{t_\Theta S_e}=(1-p)e^{-t_\Theta}+p\theta_e(f_e)e^{t_\Theta}+p(1-\theta_e(f_e))\le B_\Theta(p).\) (131)

The same tilt works for all flow values, so independence and Markov’s inequality prove (126).

For a deterministic error _e_, put D(_e_)=2|_e_|-|_B<sup>T</sup>e_|. Let \(e'=e-f\), and write

\(R(x):=2|x|-|V(suppx)|=\sum_v(deg_{suppx}(v)-1)_+.\) (132)

A nonzero flow support has minimum degree at least two. Since its edges are contained in \(suppe\cup suppe'\), a vertexwise comparison gives

\(2t=\sum_v(deg_{suppf}(v)-2)_+\le R(e)+R(e').\) (133)

Every nonzero syndrome coordinate is incident to both error supports, and favorability gives \(|e'|\le|e|\). Hence \(R(e),R(e')\le\mathcal{D}(e)\), so \(t\le\mathcal{D}(e)\).

A vertex incident to exactly one corrupted edge has nonzero syndrome. Consequently, its probability _s_ of a nonzero syndrome satisfies

\(s\ge Dp(1-p)^{D-1},Dp-s\le Dp\big[1-(1-p)^{D-1}\big]\le D(D-1)p^2\le u^2.\) (134)

Therefore \(\unknown\mathcal{D}(E)\le u^2n\), for every replacement distribution. Changing one error symbol changes D by at most four. The bounded-differences inequality gives the second exponential in (127); applied to |_E_|, it gives \(Pr(|E|>un)\le e^{-u^2n/D}\). Finally \(|f|\le|E|+|E-f|\le 2|E|\).

