_Moreover, the hard family is local inside the ordinary SAT input space: for every_ \(m\in\{0,1\}^k\) _and_ \(i\in[k]\),

\(d_\mathrm{H}\big(\mathrm{Enc}_{n,M}(\Phi(m)),\mathrm{Enc}_{n,M}(\Phi(m^{\oplus i}))\big)\le\Delta,\)

_and each adjacent pair_ \(\Psi_{t-1}^{m,i},\Psi_t^{m,i}\) _in item 2 differs in at most three input bits under_ Enc<sub>_n,M_</sub>_. In particular, the second statement is_ one-sided: _only the endpoint formulas_ \(\Phi(m)\) _and_ \(\Phi(m^{\oplus i})\) _are required to be satisfiable; the intermediate formulas_ \(\Psi_t^{m,i}\) _may be arbitrary._

_Proof._ Let \(\{I(m)\}_{m\in\{0,1\}^k}\) be the satisfiable Max E3LIN2 family from Lemma 6.1. For each _m_, define \(\Phi(m)\) by replacing every equation of _I(m_) with the corresponding four-clause gadget. Order the clauses of \(\Phi(m)\) by first fixing the order of the E3LIN2 constraints and then, inside each gadget, fixing the order of its four clauses. The key point is that this ordered list of equation scopes is independent of _m_; only the right-hand-side bits vary with the message. Because the reduction is local and each variable appears in only constantly many equations in the E3LIN2 family, the resulting formulas are explicit, satisfiable, and bounded-occurrence, with _M=O(n_) clauses.

Set \(\eta:=\eta_\mathrm{lin}/4\), and let _A_ be a randomized one-sided \((1-\eta)\)-approximate algorithm for Max E3SAT. Define<tbc>

\(B(I(m)):=A(\Phi(m)).\)

<tbc>Let _Y_ be a random assignment drawn from \(A(\Phi(m))\), and let _s(Y_) denote the number of E3LIN2 equations of _I(m_) satisfied by _Y_ . Since each satisfied equation contributes 4 satisfied clauses and each unsatisfied equation contributes exactly 3, we have<tbc>

\(\#\text{clauses of}\Phi(m)\text{satisfied by}Y=3|I(m)|+s(Y).\)

<tbc>Therefore

\(\mathbb{E}[s(Y)]\ge(1-\eta)4|I(m)|-3|I(m)|=(1-4\eta)|I(m)|=(1-\eta_\mathrm{lin})|I(m)|.\)

Thus _B_ satisfies the hypothesis of Lemma 6.1, and item 1 follows immediately with _c_:=_c_<sub>lin</sub>.

It remains to justify the locality claims in the standard SAT input encoding. By construction of the LTC-induced E3LIN2 family, the two instances _I(m_) and \(I(m^{\oplus i})\) differ only on those local tests that read the _i_th message coordinate, hence on at most \(\theta\) equations, where \(\theta=O(1)\) is the variable degree of the tester. For every fixed equation slot, the three variables appearing in that equation are independent of _m_; only the right-hand-side bit may change with _m_. Consequently, when such an equation is replaced by the corresponding E3SAT gadget, all variable-index bits in the standard clause-listing encoding remain fixed, and only the sign bits of the literals may change. Each changed equation slot affects four clauses, each clause contributes three sign bits, and therefore

\(d_\mathrm{H}\big(\mathrm{Enc}_{n,M}(\Phi(m)),\mathrm{Enc}_{n,M}(\Phi(m^{\oplus i}))\big)\le\Delta:=12\theta.\)

This proves the bounded-difference claim for the endpoints.

For item 2, fix _m_ and _i_. Changing one E3LIN2 equation changes one four-clause gadget, and that gadget change can be implemented by four single-clause replacements. Since the source and target clauses in each such replacement use the same variable triple, their standard encodings differ only in the three sign bits of that clause. Therefore there is a sequence

\(\Phi(m)=\Psi_0^{m,i},\Psi_1^{m,i},\dots,\Psi_L^{m,i}=\Phi(m^{\oplus i})\)

of length at most \(L:=4\theta\) in which each step replaces a single clause by another clause on the same variable triple. (If a shorter path exists, pad it with repeated endpoint formulas.) By the triangle<tbc>

