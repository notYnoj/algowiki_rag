**Lemma 7.3.** _Let T be a tensor satisfying the assumptions of Theorem 7.2 with_ G_. Then there exists_ \((\pi_X,\pi_Y,\pi_Z)\in\mathcal{G}\) _such that for any sets of parts_ \(P_X,P'_X\subseteq\mathcal{P}_X\), \(P_Y,P'_Y\subseteq\mathcal{P}_Y\), \(P_Z,P'_Z\subseteq\mathcal{P}_Z\) _we have_

\(\big|P_X\cap\pi_X(P'_X)\big|\le\frac{4|P_X|\cdot|P'_X|}{|\mathcal{P}_X|},\big|P_Y\cap\pi_Y(P'_Y)\big|\le\frac{4|P_Y|\cdot|P'_Y|}{|\mathcal{P}_Y|},\big|P_Z\cap\pi_Z(P'_Z)\big|\le\frac{4|P_Z|\cdot|P'_Z|}{|\mathcal{P}_Z|}.\) (25)

_Proof._ We prove the lemma using a probabilistic argument. Consider a uniformly random element \((\pi_X,\pi_Y,\pi_Z)\in\mathcal{G}\). By Item 3 in Property 7.1, for any \(X_t\in\mathcal{P}_X\), we have<tbc>

\(Pr[\pi_X(X_t)\in P_X]=\frac{|P_X|}{|\mathcal{P}_X|}.\)

<tbc>By linearity of expectation<tbc>

\(\mathbb{E}\big[\big|P_X\cap\pi_X(P'_X)\big|\big]=\sum_{X_t\in P_X^\prime} Pr[\pi_X(X_t)\in P_X]=\frac{|P_X|\cdot|P'_X|}{|\mathcal{P}_X|}.\)

<tbc>Thus by Markov’s inequality, have

\(Pr\big[|\pi_X(X_t)\in P_X|>\frac{4|P_X|\cdot|P'_X|}{|\mathcal{P}_X|}\big]\le\frac{1}{4}.\)

The argument works similarly for _Y_ and _Z_, so by union bound over _X,Y,Z_, with probability \(\ge\frac{1}{4}\), a random \((\pi_X,\pi_Y,\pi_Z)\in\mathcal{G}\) satisfies Eq. (25). Therefore, we can conclude that there exists such a \((\pi_X,\pi_Y,\pi_Z)\in\mathcal{G}\) satisfying Eq. (25).

We now proceed to prove Theorem 7.2. The main idea is to first take a broken copy of _T_ that covers most of the terms in the tensor, then write the missing terms as a sum of 7 smaller subtensors which we treat as 7 subproblems, and finally recurse on each of the subproblems with smaller sizes.

_Proof of Theorem 7.2._ Assume _P<sub>X</sub>,P<sub>Y</sub>,P<sub>Z</sub>_ are sets of _h<sub>X</sub>,h<sub>Y</sub>,h<sub>Z</sub>_ parts of _X_-, _Y_-, _Z_-dimension respectively, and assume that we need to produce _T_∥<sub>_P<sub>X</sub>,P<sub>Y</sub>,P<sub>Z</sub>_</sub>. The number of broken copies of _T_ required for this purpose is denoted as _f(h<sub>X</sub>,h<sub>Y</sub>,h<sub>Z</sub>_). Clearly, _f(h<sub>X</sub>,h<sub>Y</sub>,h<sub>Z</sub>_)=0 when one of _h<sub>X</sub>,h<sub>Y</sub>,h<sub>Z</sub>_ equals zero (because _T_∥<sub>_P<sub>X</sub>,P<sub>Y</sub>,P<sub>Z</sub>_</sub> would be an empty tensor), and we need to upper bound _f(M<sub>X</sub>,M<sub>Y</sub>,M<sub>Z</sub>_), which is the number of broken copies required to produce a complete copy of _T_.

Take a broken copy of _T_, namely \(T_\mathrm{hole}=T\|_{\mathcal{P}_X\backslash P_X^{(0)},\mathcal{P}_Y\backslash P_Y^{(0)},\mathcal{P}_Z\backslash P_Z^{(0)}}\), where \(P_X^{(0)}\), \(P_Y^{(0)}\), \(P_Z^{(0)}\) are the set of holes. Then, applying Lemma 7.3 on \(P_X,P_X^{(0)},P_Y,P_Y^{(0)},P_Z,P_Z^{(0)}\) gives \((\pi_X,\pi_Y,\pi_Z)\in\mathcal{S}_{N_X}\times\mathcal{S}_{N_Y}\times\mathcal{S}_{N_Z}\) such that

\(\big|P_X^{(0)^\prime}\big|:=\big|P_X\cap\pi_X\big(P_X^{(0)}\big)\big|\le 4\cdot\frac{|P_X|\cdot|P_X^{(0)}|}{M_X}\le\frac{1}{\mathrm{log}M_X}\cdot|P_X|,\big|P_Y^{(0)^\prime}\big|:=\big|P_Y\cap\pi_Y\big(P_Y^{(0)}\big)\big|\le\frac{1}{\mathrm{log}M_Y}\cdot|P_Y|,\big|P_Z^{(0)^\prime}\big|:=\big|P_Z\cap\pi_X\big(P_Z^{(0)}\big)\big|\le\frac{1}{\mathrm{log}M_Z}\cdot|P_Z|.\) (26)

