### 5.2 Almost-regular preferences

For \(\alpha\ge 1\), We call preferences \(\mathcal{P}\alpha\)**_-almost-regular_** if \(max_{m\in Y}degm\le\alpha min_{m\in Y}degm\). For example, complete preferences (where all men rank all women) are 1-almost-regular, while uniformly bounded preferences are \(\alpha\)-almost-regular for \(\alpha=max_{m\in Y}degm\). From an algorithmic standpoint, \(\alpha\)-almost-regular preferences are advantageous because in order to bound the proportion of blocking edges from bad men, it suffices only to bound the number of bad men. By Lemma 4.5, to obtain such a guarantee, one need only iterate **QuantileMatch** _O_(1) rounds (instead of _O_(log_n_) times as required by **ASM**).

Further, for \(\alpha\)-almost-regular preferences, we can relax our requirement that **MaximalMatching** actually find a maximal matching. We say that a player _v_ is **_unmatched_** in _G_<sub>0</sub> if _v_ does not satisfy property 1 or 2 in Definition 2.6. We call a subroutine \(\mathbf{AMM}(\eta,\delta)\) which finds a matching in which only an \(\eta\)-fraction of players are left unmatched with probability at least \(1-\delta\) (see Appendix A for details). These unmatched players are immediately removed from play. With these simplifications, we obtain the following result.

**Theorem 5.2.** There exists a randomized distributed algorithm **AlmostRegularASM**\((P,\varepsilon,\delta,\alpha)\) which for \(\alpha\)-almost-regular preferences _P_ finds a \((1-\varepsilon)\)-stable matching with probability at least \(1-\delta\). The run-time of **AlmostRegularASM**\((P,\varepsilon,\delta,\alpha)\) is \(O(\alpha\varepsilon^3log(\alpha/\delta\varepsilon))\) rounds.

_Proof sketch._ **AlmostRegularASM**\((P,\varepsilon,\delta,\alpha)\) works by iterating **QuantileMatch** \(O(\alpha\varepsilon^{-2})\) times, which by Lemma 4.5 implies that only \(\varepsilon/4\alpha\) fraction of men are bad.

We modify **ProposalRound** to call \(\mathbf{AMM}(\eta,\delta')\) instead of **MaximalMatching**. **AMM** runs in \(O(log((\eta\delta')^{-1}))\) and finds a \((1-\eta)\)-maximal matching with probability \((1-\delta')\). Since **AMM** is called \(O(\alpha\varepsilon^{-3})\) times, choosing \(\eta=O(\varepsilon^4/\alpha)\) and \(\delta'=O(\delta\varepsilon^3/\alpha)\), **AMM** will leave at most an \(\varepsilon/4\alpha\) fraction of men unmatched in any call **AMM** with probability at least \(1-\delta\), by the union bound. Such unmatched men are immediately removed from play.

By the preceding two paragraphs, **AlmostRegularASM** produces a matching in which at most an \(\varepsilon/2\alpha\) fraction of men are either bad or unmatched. By \(\alpha\)-almost-regularity, these men can contribute at most \(\frac{\varepsilon}{2}|E|\) blocking pairs. The remaining men are good, and therefore by Lemmas 4.2 and 4.3<sup>2</sup> contribute at most \(\frac{\varepsilon}{2}|E|\) blocking pairs.

## References

<sup>2</sup>Although these lemmas were proven assuming that **MaximalMatching** found a maximal matching (not an almost maximal matching) the proofs remain valid as long as the small fraction of unmatched players immediately remove themselves from play.

