**Claim 5.5.** For any node _v_ in any catalytic branching program, if we choose _L_ uniformly at random from \[_n\]<sup>n</sup>_, we have \(Pr_L[(v,L)\text{is good}]\le(1-\Omega(1))^{n^2/T}\).

_Proof._ We can imagine randomly choosing values of _L_ one-at-a-time as the branching program queries them. Once _n/_2 steps have been taken, there would then remain at least _n/_2 indices of _L_ which have yet to be determined, all of which will be chosen uniformly and independently from \[_n_\]. So, for any value \(y\in[n]\) that has been output after these steps, there is at least a \(1-(1-1/n)^{n/2}\ge\Omega(1)\) chance that _y_ appears at least twice in _L_. These events are anti-correlated, so if we output more than _n_<sup>2</sup>/400_T_ values, then there is at most a \((1-\Omega(1))^{n^2/400T}\) probability that none of them appear more than once in the list.

**Claim 5.6.** Suppose a given catalytic branching program, with _x_ start vertices, correctly solves unique elements on a given list \(L\in[n]^n\), and _L_ contains at least _n/_100 unique elements. Then, the branching program must contain at least _x_ vertices _v_ such that (_v,L_) is good.

_Proof._ In order for a given computation path in the branching program to output _n/_100 correct values, it must pass through at least one vertex _v_ such that (_v,L_) is good. If it didn’t, then either some node along the path outputs an incorrect value, or else we can divide the computation path into 2_T/n_ segments of length _n/_2, each of which outputs at most _n_<sup>2</sup>/400_T_ values, meaning at most _n/_200 outputs in total.

Now, note that, none of the computation paths from any of the start nodes can intersect each other, because otherwise one of them would fail to end up at the correct end node. Thus, in order for all _x_ of them to correctly solve unique elements on _L_, there must be at least _x_ good vertices.

These two claims together imply the overall result. By Claim 5.5, we have<tbc>

\(\mathbb{E}_{L\sim[n]^n}[\#\text{good vertices}]\le x2^S(1-\Omega(1))^{n^2/T}=x2^{S-\Omega(n^2/T)},\)

<tbc>meaning by Markov’s inequality that<tbc>

\(Pr_{L\sim[n]^n}[\#\text{good vertices}\ge x2^{S-\Omega(n^2/T)}]<1/2.\)

<tbc>But, observe that

\(Pr_{L\sim[n]^n}[L\text{has at least}n/100\text{unique elements}]>1/2.\)

So, there exists at least one value of _L_ such that the branching program has both fewer than \(x2^{S-\Omega(n^2/T)}\) good vertices and greater than _n/_100 unique elements. If we have \(ST\le o(n^2)\) (so \(S\le o(n^2/T)\)), then this would mean strictly fewer than _x_ good vertices, so Claim 5.6 would imply that the catalytic branching program is incorrect on _L_.

## References

[AAV26] Aryan Agarwala, Yaroslav Alekseev, and Antoine Vinciguerra. "Linear Matroid Intersection Is in Catalytic Logspace". In: _17th Innovations in Theoretical Computer Science Conference, ITCS 2026, Bocconi University, Milan, Italy, January 27-30, 2026_. Ed. by Shubhangi Saraf. LIPIcs. Schloss Dagstuhl - Leibniz-Zentrum für Informatik, 2026, 3:1–3:23. doi: `10.4230/ LIPICS.ITCS.2026.3`. url: `https://doi.org/10.4230/LIPIcs.ITCS.2026.3`.

[AB09] Sanjeev Arora and Boaz Barak. _Computational Complexity: A Modern Approach_. 1st. USA: Cambridge University Press, 2009. isbn: 0521424267.

[Abr91] Karl R. Abrahamson. "Time-Space Tradeoffs for Algebraic Problems on General Sequential Machines". In: _J. Comput. Syst. Sci._ 43.2 (1991), pp. 269–289. doi: `10.1016/0022-0000(91) 90014-V`. url: `https://doi.org/10.1016/0022-0000(91)90014-V`.

