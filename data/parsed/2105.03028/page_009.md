We now combine these results to improve LCS approximation on all alphabets.

**Proof of Theorem 8.** Let \(\rho\) and \(\rho'\) be positive parameters whose values will be specified later. If either of the strings _A_ or _B_ are \(\rho s\)-balanced, we are done by Lemma 10 (by taking \(\rho\) to be small enough so that the lemma applies). If the LCS of _A_ and _B_ is not \(\rho'\)-balanced we are done by Lemma 11. So, we may assume that neither _A_ nor _B_ are \(\rho s\)-balanced and that their LCS is \(\rho'\)-balanced.

By Lemma 12 we can find binary alphabet restrictions _X_ and _Y_ of _A_ and _B_ respectively with the property that neither _X_ nor _Y_ are \(\rho\)-balanced. Informally, since the LCS of _A_ and _B_ is balanced, a better than 1/2 approximation for the LCS of _X_ and _Y_ acts as a better than 1_/s_ approximation for LCS(_A,B_). More precisely, since LCS(_A,B_) is \(\rho'\)-balanced, each of its characters occurs at least \((1/s-\rho')\mathrm{LCS}(A,B)\) times in the LCS. By construction, we also know that LCS(_X,Y_) is at least as large as a binary alphabet restriction of LCS(_A,B_). Thus, it follows that given a positive constant \(\epsilon'\), a \(1/2+\epsilon'\) approximation of LCS(_X,Y_) has length at least

\((1/2+\epsilon')\cdot 2\left(1/s-\rho'\right)\mathrm{LCS}(A,B)=(1/s+2\epsilon'/s-\rho'-2\epsilon'\rho')\mathrm{LCS}(A,B).\)

By setting \(\epsilon=\epsilon'/s\) (for example) and \(\rho'\) sufficiently small in terms of \(\epsilon'\), the above calculation shows that a \(1/2+\epsilon'\) approximation for the LCS of _X_ and _Y_ acts as a \(1/s+\epsilon\) approximation for LCS(_A,B_). Hence to complete the proof, it suffices to get a better than 1/2 approximation for LCS(_X,Y_). We may assume that

\(min\left(0(X),0(Y)\right)\le(1+\delta)min\left(1(X),1(Y)\right)\) (5)

and

\(min\left(1(X),1(Y)\right)\le(1+\delta)min\left(0(X),0(Y)\right)\) (6)

for some constant \(\delta\) since otherwise Lemma 14 yields a better than 1/2 approximation.

As mentioned previously, [21] gives a better than 1/2 approximation for the LCS when _X_ and _Y_ have equal length. If _X_ and _Y_ have different lengths, without loss of generality we assume that |_X|\>|Y_| and \(0(Y)\le 1(Y)\). We do casework on frequencies in _X_, relative to the frequencies in _Y_.

Since _X_ is longer than _Y_, we cannot have both \(1(X)\le 1(Y)\) and \(0(X)\le 0(Y)\).

If 1(_X)\>_1(_Y_) and 0(_X)\>_0(_Y_) simultaneously, then Equation (6) implies that

\(1(Y)\le(1+\delta)\cdot 0(Y)\)

which contradicts the fact that _Y_ is not \(\rho\)-balanced as long as we take \(\delta\le 2\rho\).

If instead \(1(X)\le 1(Y)\) and \(0(X)\le 0(Y)\), by Equation (6) we similarly have

\(0(X)\le 0(Y)\le 1(Y)\le(1+\delta)\cdot 0(X)\)

which again contradicts the fact that _Y_ is not \(\rho\)-balanced for the same choice of \(\delta\).

Thus, the only possibility is that \(1(X)\le 1(Y)\) and 0(_X)\>_0(_Y_). Let _m_=|_Y_| be the length of string _Y_. Then Equation (5) implies that

\(0(Y)\le(1+\delta)\cdot 1(X)\le 1(X)+\delta m\)

while Equation (6) implies that

\(1(X)\le(1+\delta)\cdot 0(Y)\le 0(Y)+\delta m.\)

