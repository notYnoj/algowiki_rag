<tbc>For \(q\le 4\) these were rigorously proved by Dudeney and Fabel (see Kotˇcešovec \[12, p. 234\] for these attributions and citations). The formulas for _q_=2,3 are special cases of our Theorems III.4.1 and III.4.2, thereby reinforcing the correctness of those theorems. Kotˇcešovec found the formulas for _q_=5,6 heuristically, by calculating the values _u_<sub>B</sub>(_q;n_) for many values of _n_, looking for an empirical recurrence relation, deducing a generating function, and from that getting the quasipolynomial. (See Section 8.3 for more about his method.) His approach, while excellent for finding formulas, does not prove their validity because it does not bound the period--even though period 2 is plausible since one could guess that odd and even board sizes would have separate polynomials.

We have proved that 2 is the complete story on the period. In Theorem VI.1.1 \[7\] we provide the missing upper bound that rigorously establishes period 2 for every _q\>_2 and hence the correctness of Kotˇcešovec’s quasipolynomial formulas.2 Together with the fact that we know the degree 2_q_ and the leading coefficient 1_/q_! of the constituent polynomials, this implies that, if the first 4_q_ values of a candidate quasipolynomial are correct, then we have _u_<sub>B</sub>(_q;n_). Since Kotˇcešovec did check those values for \(q\le 6\) \[13\], his formulas are proved.

**Theorem 4.1.** _All the formulas in Equations_ (4.1) _are correct._

Despite the overall period 2, in Kotˇcešovec’s formulas (4.1) the six leading coefficients do not vary with the parity of _n_. Kotˇcešovec conjectured expressions for \(\gamma_1\), \(\gamma_2\), and \(\gamma_3\) in terms of _q_ alone; we proved them in Theorem III.3.1 (and see s III.3.1 and III.3.2) since the bishop is the partial queen Q<sup>02</sup>. That theorem also gives the periods of \(\gamma_4\) and \(\gamma_5\).

**Corollary 4.2** (of Theorem III.3.1)**.** _In u_<sub>B</sub>(_q;n_) _the coefficients_ \(\gamma_i\) _for_ \(i\le 5\) _are constant as functions of n._

As the number of combinatorial types of nonattacking configuration of _q_ unlabelled bishops is _q_! by Theorem I.5.8, we know this is the value of _u_<sub>B</sub>(_q_;-1) even though we do not know the general formula for _u_<sub>B</sub>(_q;n_).

A surprising development during our work on this project was Kotˇcešovec’s discovery that, in 1936, Arshon had solved the _n_-bishops problem, the number of ways to place _n_ nonattacking bishops on an \(n\times n\) board \[1\]. His method was to count independently the number of ways to place _i_ nonattacking bishops on the black squares and on the white squares. This work was forgotten until Kotˇcešovec rediscovered it. It was an easy step for him to write down an explicit formula for the number of placements of _q_ nonattacking bishops \[12, fourth ed., p. 140\]. Kotˇcešovec then restated the Arshon equations with no subtractive terms by using Stirling numbers of the second kind \[12, fourth ed., p. 142\]. His formula for _q_ bishops is

(4.2) \(u_\mathbb{B}(q;n)=\sum_{i=0}^q\sum_{j=0}^{\left\lfloor\frac{n+1}{2}\right\rfloor}\genfrac(){pt}{2}{\left\lfloor\frac{n+1}{2}\right\rfloor}{j}S\big(j+\left\lfloor\frac{n}{2}\right\rfloor,n-i\big)\cdot\sum_{h=0}^{\left\lfloor\frac{n}{2}\right\rfloor}\genfrac(){pt}{2}{\left\lfloor\frac{n}{2}\right\rfloor}{h}S\big(h+\left\lfloor\frac{n+1}{2}\right\rfloor,n-(q-i)\big).\)

For us this is not entirely satisfactory. Since the number of terms depends on _n_, (4.2) does not give the quasipolynomial form of _u_<sub>B</sub>(_q;n_) and does not allow us to substitute _n_=-1 to obtain the number of combinatorial types of nonattacking configuration (though for the

2Stanley in \[16, Solution to Exercise 4.42\] says that both quasipolynomiality and the period follow directly from Arshon’s formulas; however, we believe such a derivation would be difficult.

