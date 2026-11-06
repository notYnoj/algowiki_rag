<tbc>Lemma 6.5 and (6.10) now give

\(|\mathrm{supp}(H_B)|\le c_\mathrm{BG}d\frac{\mathrm{log}_2^6(4\mathrm{max}\{W(J),1\})}{\eta_\ell^2}\)<br>
\(\le O_R\big(\frac{d}{\varepsilon^2}(\ell+1)^{10}\big),\)

which is (6.14).

There is at most one sparsifier in each of \(1+\lfloor\mathrm{log}_2\mathrm{max}\{m,1\}\rfloor\) levels. Summing (6.14) shows that the number of stored constraints across all sparsifiers is

\(O_R\big(\frac{d}{\varepsilon^2}\mathrm{log}^{11}(m+2)\big).\)

Each constraint stores an ordered _k_-tuple of variable indices and an integer weight. These use _O<sub>R</sub>_(log(_n_+2)+log(_m_+2)) bits by (6.16). The level counters and the error parameter use the remaining logarithmic term in (6.15).

Finally, using the above, we can prove the theorem.

_Proof of Theorem 6.1._ If _m_=0, output the empty instance. Otherwise, run the binary sparsify- merge-sparsify algorithm above and, after the last arrival, output the weighted union _H_ of the sparsifiers in the occupied levels. Every retained constraint descends from a constraint in the stream, so \(H\subseteq I\). Claim 6.11 gives, simultaneously for every assignment \(\alpha\),

\(\mathrm{unsatval}_H(\alpha)\in(1\pm\varepsilon)\mathrm{unsatval}_I(\alpha).\)

Claim 6.13 gives the explicit bound in (6.15), and hence the space claimed in the theorem. Lemma 6.5 makes every reduction deterministic. The input stream is read once. All later reductions operate only on stored sparsifiers. The algorithm need not know _m_ in advance because the error schedule depends only on the level.

_Proof of Corollary 6.2._ Let _R<sup>⋆</sup>_=core(_R_), with core domain _C_. If _R<sup>⋆</sup>_ is trivial, then, since it is nonempty, _R<sup>⋆</sup>=C<sup>k</sup>_. Every _R<sup>⋆</sup>_-instance has minimum unsatisfied value zero, and the same is true for the corresponding _R_-instance by Lemma 4.3. The upper bound is then immediate. Hence suppose that _R<sup>⋆</sup>_ is non-trivial.

For the upper bound, replace every arriving _R_-constraint by the _R<sup>⋆</sup>_-constraint on the same scope, as in Lemma 4.2. Set<tbc>

\(\delta=\frac{\varepsilon}{2+\varepsilon}\)

<tbc>and run Theorem 6.1 with error \(\delta\), obtaining a sparsifier _H_ of the resulting instance _I<sup>⋆</sup>_. Minimizing the pointwise sparsifier inequalities gives

\((1-\delta)\mathrm{OPT}_\mathrm{min}(I^\star)\le\mathrm{OPT}_\mathrm{min}(H)\le(1+\delta)\mathrm{OPT}_\mathrm{min}(I^\star).\) (6.18)

<tbc>Output<tbc>

\(Z=\frac{\mathrm{OPT}_\mathrm{min}(H)}{1-\delta}.\)

<tbc>Lemma 4.3 gives OPT<sub>min</sub>(_I<sup>⋆</sup>_)=OPT<sub>min</sub>(_I_), and therefore<tbc>

\(\mathrm{OPT}_\mathrm{min}(I)\le Z\le\frac{1+\delta}{1-\delta}\mathrm{OPT}_\mathrm{min}(I)=(1+\varepsilon)\mathrm{OPT}_\mathrm{min}(I).\)

