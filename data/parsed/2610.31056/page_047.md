## 8 Conclusion and Future Directions

We study the complexity of the Pigeonhole Equal Subset Sum and make progress on two central open questions: whether one can achieve subexponential-time algorithms and whether the O_<sup>⋆</sup>(M_<sup>1/3</sup>) barrier can be improved. Our contributions are

(i) Deterministic \(\mathrm{poly}(n)\cdot M^{\mathcal{O}(1/\mathrm{log}\delta)}\)-time algorithm when \(\delta=n/\mathrm{log}M\) is the density of the instance (Theorem 1.1).<tbc>

(ii) Conditional lower bound showing that no \(M^{o(1/\mathrm{log}\delta)}\)-time algorithm exists assuming currently based algorithms for lattice problems are tight (Theorem 1.2).<tbc>

(iii) Average-case, O_<sup>⋆</sup>_(2<sup>_n/_4</sup>)-time algorithms when \(M=\Theta(2^n)\) (Theorem 1.3 and Theorem 1.4)

Figure 2 gives a pictorial view of our results. We also show that no 2<sup>_o(n/_log_n_)</sup>-time algorithm exists for Pigeonhole Equal Subset Sum (conditionally answering open question of Jin [Jin24] up to log_n_ factor in the exponent).

Several intriguing directions remain open. Most notably, closing the remaining gap to fully resolve whether Pigeonhole Equal Subset Sum admits a 2<sup>_o(n_)</sup>-time algorithm remains a major challenge. Our lower bound relies on a technique of Vafa and Vaikuntanathan [VV25], who showed that no polynomial-time algorithm solves Number Balancing Problem with \(\kappa(n)=2^{-\Omega(\mathrm{log}^{3+\varepsilon}(n))}\). Although our lower bound is tight, it is tight only in the setting of exponential running times and does not improve the lower bound of Vafa and Vaikuntanathan [VV25]. In fact, our reduction, when plugged in with their hypothesis and parameters, would also exclude \(\kappa(n)=2^{-\mathcal{O}(\mathrm{log}^{3+\varepsilon}(n))}\)- approximation in polynomial time, but it would be worse because the lower bound of [VV25] prohibits even average-case algorithms. Can one improve these lower bounds in the setting of polynomial-time algorithms for Pigeonhole Equal Subset Sum?

Finally, we ask whether average-case algorithms for Pigeonhole Equal Subset Sum in the regime \(\delta=1\) can be extended to the worst-case setting. We conjecture that the structural insights of Jin, Williams, and Zhang [JWZ25] and our analysis in the average-case setting can be combined to yield an O_<sup>⋆</sup>_(2<sup>_n/_4</sup>)-time worst-case algorithm. Also, can we improve the average-case running time exponent of O_<sup>⋆</sup>_(2<sup>_n/_4</sup>) below 1/4?

Time(n)
Theorem 1.1
MO(1)
2O(nc/logn)
Theorem 1.2
2O(log2 n)
[KK82]
poly(n)
[VV25]
2O(log2 n)
2O(log3+E n)
2O(nc)
M(n)

Figure 2: Overview of our results. Green lines depict the previous upper bounds for the problem. Blue lines depict Theorem 1.1. The result of Vafa and Vaikuntanathan [VV25] forbids a polynomial- time (even average case) algorithm for \(M=2^{\Omega(\mathrm{log}^{3+\varepsilon} n)}\). Theorem 1.2 shows a tight lowerbound in the setting when \(M(n)=2^{\Theta(n^c)}\) for constant \(c\in(0,1)\).

