<tbc>The value of **I**_<sub>n</sub>(R_) is _R_. Applying Lemma 5.10 yields \(2^{n^2/4}\le R\). Taking base-two logarithms proves the first assertion. Under the hypotheses of the second assertion, the same lemma gives<tbc>

\(2^{Nn^2/4}\mathcal{V}_n(Z_N)\le R_Nh_N\mathcal{V}_n(Z_N)\)

<tbc>for every sufficiently large _N_. The catalyst value is positive, so it cancels. Taking base-two logarithms and dividing by _N_ yields

\(\frac{\mathrm{log}_2R_N}{N}\ge\frac{n^2}{4}-\frac{\mathrm{log}_2h_N}{N}.\)

The final term tends to zero, proving the claimed lower bound on the limit inferior.

For odd _n_, the threshold exceeds MaxCut(_K<sub>n</sub>_) by 1/4. Thus the permitted polynomial ingredients cannot close the remaining gap in Theorem 1.1 by rearranging their combinations, taking tensor powers, adding subexponential overhead, or using catalysts. The conclusion concerns these formal derivations. It is not a lower bound of _n_<sup>2</sup>/4 on the true asymptotic-rank exponent. A new tensor relation can go beyond this obstruction only if its inclusion defeats the certificate or if it uses expressions or combination rules outside the specified system. On the diagonal, the certificate’s comparison function has growth exponent 2(_n_-1)_/n_ by Lemma 5.8, the same exponent used in Subsection 4.4.

## Open Problems

We conclude this paper with two open problems motivated by our findings.

• Can we determine the asymptotic rank of odd complete graphs? For each odd integer \(n\ge 3\), Theorem 1.1 leaves three possibilities: the value \(\mathrm{log}_2\widetilde{\mathsf{R}}(\mathsf{GT}_2(K_n))\) equals \(\lfloor n^2/4\rfloor\), equals _n_<sup>2</sup>/4, or lies strictly between them. Which occurs, and can different odd orders behave differently? In particular, does any odd complete graph satisfy<tbc>

<tbc>\(\left|\frac{n^2}{4}\right|<\mathrm{log}_2\widetilde{\mathsf{R}}\big(\mathsf{GT}_2(K_n)\big)<\frac{n^2}{4}?\)<tbc>

<tbc>At _n_=3, the two endpoint equalities would give \(\omega=2\) and \(\omega=9/4\), respectively; the strict intermediate case would give \(2<\omega<9/4\). Proving the lower endpoint requires improving the current upper bound. Within the polynomial system of Theorem 1.2, this requires a new ingredient beyond its listed rules. Proving the upper endpoint requires a lower bound beyond the maximum-cut bound, and hence information beyond flattening ranks. A strict intermediate value requires progress on both sides.<tbc>

• For a simple undirected graph _G_ with at least two vertices, can we obtain tighter upper bounds on \(\mathrm{log}_2\widetilde{\mathsf{R}}(\mathsf{GT}_2(G))\)? In particular, is<tbc>

<tbc>\(\mathrm{log}_2\widetilde{\mathsf{R}}\big(\mathsf{GT}_2(G)\big)=\mathrm{MaxCut}(G)\)<tbc>

<tbc>always true, as asked by Christandl, Vrana, and Zuiddam \[CVZ19, Question 1.3.2\]? Can we prove this equality for more families of graphs, or find a counterexample? It holds for bipartite graphs by Proposition A.4, and Theorem 1.1 proves it for even complete graphs. The identity \(\mathrm{log}_2\widetilde{\mathsf{Q}}(\mathsf{GT}_2(G))=\mathrm{MinCut}(G)\) shows that the analogous problem for asymptotic subrank already has a purely graph-theoretic answer.<tbc>

