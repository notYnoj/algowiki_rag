<tbc>The nightrider’s main complication comes from the non-unit slopes. We propose as worthy subjects the partial nightriders with only two moves, from Section 7:

(b) The lateral nightrider. We conjecture a period of 4 for \(q\ge 3\). We verified this for _q_=3,4.<tbc>

(c) The inclined nightrider. The period for _q_=3 is 12.<tbc>

(d) The orthogonal nightrider. The period for _q_=3 is 20.<tbc>

<tbc>We thank Arvind Mahankali for calculating these periods, using Mathematica. Note that the coefficient of _n_<sup>2_q_-6</sup> in Lemma 7.4 strongly suggests but does not prove these periods.

After we proposed these pieces, Hanusa and Mahankali \[10\] found their denominators, which we reproduce in  8.1. As upper bounds on periods, they also suggest but do not prove the true periods.

(e) A simple three-move rider would have moves (1,0),(0,1),(_c,d_). This should be investigated.<tbc>

(f) The partial nightrider N<sup>3</sup>. We discussed it briefly in Section 7, finding the counting formula and the period 2 for _q_=2. The period for three pieces appears to be 60. This period is the same as for the complete nightrider but we expect N<sup>3</sup> to have a smaller period than N when \(q\ge 4\).

## 8.2. Counting nonattacking combinatorial types.

It would be valuable to produce a conjectural expression for the number of combinatorial types of nonattacking configuration for the queen, a partial queen with three moves, or any other piece with more than two moves (one or two moves being easy; see Proposition I.5.6).

## 8.3. The problem of the recurrence relation.

Suppose we generate a sequence of numbers, say _u_<sub>1</sub>_,u_<sub>2</sub>_,..._, one at a time. Each time we generate a new _u<sub>n</sub>_ we look for a linear, homogeneous recurrence relation with constant coefficients that _u_<sub>1</sub>_,u_<sub>2</sub>_,...,u<sub>n</sub>_ satisfy. The recurrence may change at each _n_, but suppose there is an _N_ such that the (_N+k_)-th recurrence is identical to the _N_-th recurrence for _k_=1,2_,...,K_. Let us call this a _stable recurrence_ of strength _K_. If the stable recurrence is valid for all _n\>N_, it is the true recurrence satisfied by the sequence.

Kotˇcešovec’s method of finding formulas for a rider P and a number _q_ was to compute _u<sub>n</sub>=u_<sub>P</sub>(_q;n_) until he detected a stable recurrence of sufficient strength. Then he assumed the stable recurrence was the true recurrence and used it to obtain a rational generating function for _u_<sub>P</sub>(_q;n_), from which he could obtain a quasipolynomial formula. (Personal communication, 19 July 2018.) His stable relation is the true relation in all cases that we could verify. The first question is: Why?

We know there is a recurrence for _u_<sub>P</sub>(_q;n_), because that is implied by the quasipolynomial formula. What we do not know is whether there is an _N_ at which a stable recurrence appears<tbc>

\begin{tabular}{ccccc}
_Name_ & _q_=1 & _q_=2 & _q_=3 & \(q\ge 4\) \\
Lateral & 1 & 2 & 4 & 4 \\
Inclined & 1 & 2 & \(12=3\cdot 2^{q-1}\) & \(3\cdot 2^{q-1}\) \\
Orthogonal & 1 & 2 & \(20=5\cdot 2^{q-1}\) & \(15\cdot 2^{q-1}\) \\
\end{tabular}

8.1. The denominators of the two-move partial nightriders, from \[10, Section 6\].

