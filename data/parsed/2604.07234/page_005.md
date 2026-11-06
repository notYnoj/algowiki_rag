<tbc>i.e., with the expectation _inside_ the log. This is in contrast to the default, _quenched_ free energy

\(\frac{1}{N}\mathbb{E}[logZ],\)

where the expectation is outside the log.

**Theorem 1.1** (Quenched-annealed gaps)**.** _Fix_ \(\alpha\in(0,1)\)_. Let_ \(X,X'\in\{0,1\}^N\) _be independent uniform random strings and let_ \(Y\in\{0,1\}^M\) _be a uniform random length-M subsequence of X (with_ \(M=\lfloor\alpha N\rfloor\)_). Defining_<tbc>

\(f_\mathrm{null}^\mathrm{ann}(\alpha):=\mathrm{lim}_{N\rightarrow\infty}\frac{1}{N}log\mathbb{E}\left[Z_{X^\prime,Y}\right],\)

<tbc>_there exists a constant_ \(f_\mathrm{pl}(\alpha)>0\) _such that_

(1.6) \(\frac{1}{N}logZ_{X,Y}-\rightarrow^pf_\mathrm{pl}(\alpha)>f_\mathrm{null}^\mathrm{ann}(\alpha),\)

_where_ \(-\rightarrow^p\) _denotes convergence in probability. Moreover, if_ \(\alpha\in(0,1/2)\)_, then there exists a constant_ \(f_\mathrm{null}(\alpha)>0\) _such that_

(1.7) \(\frac{1}{N}logZ_{X^\prime,Y}-\rightarrow^pf_\mathrm{null}(\alpha)\)

_and this constant satisfies_

(1.8) \(h(2\alpha)/2\le f_\mathrm{null}(\alpha)<f_\mathrm{null}^\mathrm{ann}(\alpha).\)

The threshold \(\alpha=1/2\) is the natural boundary for the weak limit (1.7) to hold under the null model. Indeed, as discussed at the beginning of Section 2, it is easy to show that \(Z_{X^\prime,Y}=0\) with high probability for \(\alpha>1/2\) and that at the boundary \(\alpha=1/2\), there does not exist a weak limit of the form (1.7) for the null model. Additionally, the main quantitative result in Section 3 which separates the exponential behavior of \(Z_{X^\prime,Y}\) from the annealed free energy of the null model, namely (3.34), holds for all \(\alpha\in(0,1)\) (though with implicit constants depending on the choice of \(\alpha\)). Together with Theorem 1.1, these observations give strict exponential-scale bounds for the Random Subsequence Model throughout the entire dense regime \(\alpha\in(0,1)\). We record in Appendix B a combinatorial consequence of (1.8), showing in particular that there is no further transition in the relation between \(f_\mathrm{null}(\alpha)\) and \(f_\mathrm{null}^\mathrm{ann}(\alpha)\) within the range \(\alpha<1/2\).

We now connect Theorem 1.1 to channel coding over the binary deletion channel with uniform random codes; see [PIW24] for a more complete discussion of this viewpoint. For \(p\in[0,1]\), we let \(C_\mathrm{unif}(p)\in[0,1]\) denote the maximum rate achievable through the deletion channel with deletion probability _p_ using uniform random codes, i.e., the quantity that was introduced in (1.2).

**Corollary 1.2** (Positive rate for uniform codes; [PIW24, Conjecture 3])**.** _It holds for all deletion probabilities_ \(p\in[0,1)\) _that C_<sub>unif</sub>(_p)\>_0.

Corollary 1.2 confirms [PIW24, Conjecture 3] and resolves [PIW24, Question 1] by showing that uniformly random codes achieve a strictly positive rate even when \(p\ge 1/2\), i.e., in the regime where each bit is more likely to be deleted than retained. This is the first such positive-rate result for uniform codebooks in this regime, and it strengthens (in a qualitative sense) the earlier lower bounds of [Gal61; Zig69; DG01; DM06; RD13; HOS16], all of which were only able to address the _p\<_1/2 setting.

In fact, the proof of Theorem 1.1 yields a quantitative version of Corollary 1.2 in the likely deletion regime. Specifically, there exists \(k\in\mathbb{N}\) (the crude explicit bound of Theorem 3.13 gives _k_=362, which we expect to be far from sharp) such that as \(p\rightarrow 1\),<tbc>

\(C_\mathrm{unif}(p)=\Omega\big((1-p)^k\big).\)

<tbc>On the other hand, as \(p\rightarrow 1\), [DSV12] gives the upper bound

\(C_\mathrm{unif}(p)=O\left((1-p)^{4/3}log\frac{1}{1-p}\right).\)

