The result follows by taking \(s\ge log(n/\eta)/log(c^{-1})\).

The almost regular variant of **ASM** only requires a subroutine that we finds matchings which are almost maximal.

**Definition A.3.** Let _G_=(_V,E_) be a communication graph and \(M\subset E\) a matching in _G_. For \(0<\eta\le 1\), we say that _M_ is \((1-\eta)\)**_-maximal_** if the set \(V'\) of vertices not satisfying conditions 1 or 2 in Definition 2.6 satisfies \(|V'|\le\eta|V|\).

We can apply Lemma A.1 to give a constant round algorithm which finds almost maximal matchings.

**Corollary A.4.** There exists a randomized distributed algorithm \(\mathbf{AMM}(G,\eta,\delta)\) which finds a \((1-\eta)\)-maximal matching with probability at least \((1-\delta)\). \(\mathbf{AMM}(G,\eta,\delta)\) runs in \(O(log(\eta^{-1}\delta^{-1}))\) rounds.

_Proof._ Consider the algorithm which iterates **MatchingRound** _s_ times. We apply Lemma A.1 and Markov’s inequality to obtain

\(Pr(|V_s|\ge\eta n)\le\frac{c^sn}{\eta n}=\eta^{-1}c^s.\)

Choosing \(s=O(log(\delta^{-1}\eta^{-1}))\), we have \(\eta^{-1}c^s\le\delta\), which gives the desired result.

