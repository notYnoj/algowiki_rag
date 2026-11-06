This construction is illustrated in Figure 3 (where symbols \(\succ\) are omitted for readability reasons) for the Minimum 2-Satisfiability instance defined by Equations 7 and 8. The preference lists of the agents are only partially given but note that they can be completed in any consistent way that would lead to complete and transitive orders.

We now explain how to define the disutility values attributed to each rank, as well as the weights of the GGI operator, so that the number of unsatisfied clauses can be inferred from the GGI value of the stable marriage.

## Disutility values and weights of the GGI.

We first recall that each clause _c<sub>j</sub>_ induces 6 agents that are matched either with their first or second choices and 2 agents (the decisive ones) that are matched with their choices of rank 2_j_+1 or 2_j_+2. By construction of the preference lists, note that no agent can be matched with a partner that is ranked strictly beyond 2_n<sub>c</sub>_+2 in his/her preference list. Therefore the values of _d(i_) for _i\>_2_n<sub>c</sub>_+2 play no role, and can be fixed arbitrarily as long as they are increasing with _i_ and strictly greater than _d_(2_n<sub>c</sub>_+2). - The increasing disutility values for ranks 1 to 2_n<sub>c</sub>_+2 are defined as follows (assuming that \(n_c\ge 2\)):

\(d(1)=0\)<br>
\(d(2)=1\)<br>
\(d(2j+1)=j+1,\forall j\in\{1,\dots,n_c\}\)<br>
\(d(2j+2)=j+1+n_c^{-j},\forall j\in\{1,\dots,n_c\}\)

m1 : w1 ... w1 : m1 ... m'1 : w'1 ... w'1 : m'1 ... : : m5 : w5 ... w5 : m5 ... m'5 : w'5 ... w'5 : m'5 ... m11 : w1 w'1 w11 w13 ... w11 : m13 m11 ... m13 : w1 w'1 w2 w2 w3 w3 w13 w11 ... w13 : m11 m13 ... m21 : w1 w'1 w21 w22 ... w21 : m25 m21 ... m22 : w22 w25 ... w22 : m1 m'1 m2 m2 m21 m22 ... m25 : w1 w'1 w2 w2 w3 w3 w4 w'4 w5 w'5 w25 w25 ... w25 : m22 m25 ... m25 : w1 w'1 w2 w2 w3 w3 w4 w'4 w5 w'5 w25 w21 ... w25 : m25 m'25 ... m33 : w1 w'1 w2 w2 w3 w3 w3 w33 w34 ... w33 : m34 m33 ... m34 : w1 w'1 w2 w2 w3 w3 w4 w'4 w34 w33 ... w34 : m33 m34 ... m42 : w42 w44 ... w42 : m1 m'1 m2 m'2 m44 m42 ... m44 : w44 w42 ... w43 : m1 m'1 m2 m'2 m3 m3 m4 m4 m4 m42 m44 ...

Fig. 3: Preference lists obtained for the min 2-SAT instance of Equations 7 and 8.

