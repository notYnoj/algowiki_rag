<tbc>to one common automorphism and will be used for satisfiability. The second makes the same idea strong enough for exact optimization.

We will repeatedly use the fact that applying one automorphism to every assigned value changes nothing. We state it in the following observation.

**Observation 4.1.** _Let_ \(R\subseteq D^k\)_, let I be an R-instance, and let_ \(\sigma\in\mathrm{Aut}(R)\)_. For every assignment_ \(\alpha\)_, we have_ \(\mathrm{val}_I(\sigma\circ\alpha)=\mathrm{val}_I(\alpha)\)_. Therefore,_ \(\mathrm{unsatval}_I(\sigma\circ\alpha)=\mathrm{unsatval}_I(\alpha)\).

_Proof._ Consider a constraint _R(x_<sub>1</sub>_,...,x<sub>k</sub>_) of _I_. Since \(\sigma\) is an automorphism, the constraint is satisfied by \(\alpha\) if and only if it is satisfied by \(\sigma\circ\alpha\). This holds for every constraint, which proves both equalities.

## 4.1 Reduction to the core

The first goal is to reduce all three streaming problems from _R_ to its core _R<sup>⋆</sup>_. The reduction keeps every constraint on the same scope. It only replaces the relation _R_ by _R<sup>⋆</sup>_. The next lemma states that this preserves the streaming space exactly.

**Lemma 4.2.** _Let R<sup>⋆</sup>_=core(_R). The following statements hold._

(_i)_ SPACE(SAT(_R_))=SPACE(SAT(_R<sup>⋆</sup>_)).<tbc>

(_ii)_ _for every_ \(\gamma\ge 1\), \(\mathsf{SPACE}(\mathsf{Min}\mathsf{CSP}_\gamma(R))=\mathsf{SPACE}(\mathsf{Min}\mathsf{CSP}_\gamma(R^\star))\).<tbc>

_(iii)_ SPACE(Exact-CSP(_R_))=SPACE(Exact-CSP(_R<sup>⋆</sup>_)).

_The reductions preserve the number of variables and constraints, the scope of each corresponding constraint, stream order, and simplicity. If R is symmetric, then R<sup>⋆</sup> is symmetric as well._

To prove Lemma 4.2, we first prove that the same replacement preserves the two optimum values of every instance.

**Lemma 4.3.** _Let_ \(R\subseteq D^k\)_, let_ \(\sigma:D\rightarrow C\) _be an idempotent endomorphism of minimum image, and let_ \(R^\star=\mathrm{core}(R)=\sigma(R)=R\cap C^k\)_. Given an R-instance I, let I<sup>⋆</sup> be the R<sup>⋆</sup>-instance obtained by replacing every constraint R(x_<sub>1</sub>_,...,x<sub>k</sub>_) _by R<sup>⋆</sup>(x_<sub>1</sub>_,...,x<sub>k</sub>_) _on the same scope. Then_ OPT<sub>max</sub>(_I_)=OPT<sub>max</sub>(_I<sup>⋆</sup>_) _and_ OPT<sub>min</sub>(_I_)=OPT<sub>min</sub>(_I<sup>⋆</sup>). In particular, I is satisfiable if and only if I<sup>⋆</sup> is satisfiable._

_Proof._ Let \(\alpha\) be any assignment for _I_. If _R(x_<sub>1</sub>_,...,x<sub>k</sub>_) is satisfied by \(\alpha\), then \((\alpha(x_1),\dots,\alpha(x_k))\in R\), and applying the endomorphism \(\sigma\) gives \((\sigma(\alpha(x_1)),\dots,\sigma(\alpha(x_k)))\in\sigma(R)=R^\star\). Hence \(\mathrm{val}_{I^\star}(\sigma\circ\alpha)\ge\mathrm{val}_I(\alpha)\) and \(\mathrm{unsatval}_{I^\star}(\sigma\circ\alpha)\le\mathrm{unsatval}_I(\alpha)\). Taking an assignment that is optimal for the relevant objective gives \(\mathrm{OPT}_\mathrm{max}(I^\star)\ge\mathrm{OPT}_\mathrm{max}(I)\) and \(\mathrm{OPT}_\mathrm{min}(I^\star)\le\mathrm{OPT}_\mathrm{min}(I)\).

For the reverse direction, consider any assignment \(\beta\) taking values in _C_. Since \(R^\star=R\cap C^k\), every constraint is satisfied by \(\beta\) as an _R_-constraint if and only if it is satisfied by \(\beta\) as an _R<sup>⋆</sup>_-constraint. In particular, an assignment attaining either optimum for _I<sup>⋆</sup>_ is also an assignment for _I_ with the same value. Therefore \(\mathrm{OPT}_\mathrm{max}(I)\ge\mathrm{OPT}_\mathrm{max}(I^\star)\) and \(\mathrm{OPT}_\mathrm{min}(I)\le\mathrm{OPT}_\mathrm{min}(I^\star)\). Combining the two directions proves both equalities, and the satisfiability claim follows from OPT<sub>min</sub>=0.

We can now prove the streaming reduction. The point is that the instance level argument did not change any scope.

