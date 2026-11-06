We can now iteratively generate a sequence of relaxations \(\{DCMCF_{env}^n\}_{n\in\mathbb{N}}\) as follows. Given the relaxation \(DCMCF_{env}^n\), with upper bounds \(u_a^n\) for each arc \(a\in A\) and optimal objective value \(\gamma_n^*\), either one of the two following conditions is met:

1. _Direct Success_: The relaxation immediately satisfies the desired property: for every arc \(a\in A\), the optimal objective value of \(DCMCF_{env}^n\) and the upper bound of every arc _a_ satisfy \(u_a^n\le\alpha(\sum_{k\in K}b^k)\gamma_n^*\).<tbc>

2. _Bounds Improvement_: The relaxation does not satisfy the desired property, but bounds can be improved: a new problem \(DCMCF_{env}^{n+1}\) with, for every arc \(a\in A\), a new upper bound \(u_a^{n+1}=\mathrm{min}\left(u_a^n,(\sum_{k\in K}b^k)\gamma_n^*\right)\) is created and solved.

The new problem \(DCMCF_{env}^{n+1}\) constructed in the latter case remains a relaxation of DCMF, since \((\sum_{k\in K}b^k)\gamma_n^*\) is a valid upper bound on the load of each arc \(a\in A\).

If this process is run for 1+|_A_| iterations and the condition is still not satisfied (i.e., no direct success), then there exists at least one arc _a_ for which the upper bound has been updated twice. In other words, we have \(u_a^n>\alpha(\sum_{k\in K}b^k)\gamma_n^*\) and \(u_a^{n+l}>\alpha(\sum_{k\in K}b^k)\gamma_{n+l}^*\) for some \(a\in A\), and some \(l\le 1+|A|\). Hence, the following inequalities hold: \(\alpha(\sum_{k\in K}b^k)\gamma_{n+l}^*<u_a^{n+l}\le u_a^{n+1}\le(\sum_{k\in K}b^k)\gamma_n^*\), implying that \(\frac{\gamma_{n+l}^*}{\gamma_n^*}\le\frac{1}{\alpha}\). Since the \(\gamma_n^*\) values cannot fall below the lower bound \(\gamma_{low}\) defined in (35), the iterative process must terminate and generate a relaxation of DCMF<sub>env</sub> that satisfies the required conditions within a maximum of \((|A|+1)\left\lceil\mathrm{log}_\alpha\left(\frac{\gamma_0^*}{\gamma_{low}}\right)\right\rceil\) iterations. Since \(\gamma_0^*\) is less than the trivial upper bound \(\frac{\sum_{a\in A}c_a}{\sum_{k\in K}b^k}\), the number of iterations is polynomially bounded in the size of the instance, ending the proof.

## B.5 Proof of Theorem 5.2

_Proof._ Given a DCMF instance and any constant \(\alpha>1\), Lemma 5.4 ensures that one can construct a relaxation DCMF<sub>env</sub> with optimal value \(\gamma^*\) such that, for every \(a\in A\), \(u_a\le\alpha(\sum_{k\in K}b^k)\gamma^*\).

