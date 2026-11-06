## 6 Universal Problem Variants

We now consider the universal variants, i.e., checking whether all strings \(u\unknown w\) are in L(_A_).

**Theorem 6.1.** _The universal-variant of the matching problem can be solved in time O_(|_w|m_) _for the prefix relation and in time O_(|_w_|<sup>2</sup>_m_) _for the infix relation. It is PSPACE-complete for the extension and left-extension relation, coNP-complete for the subsequence relation, and PSPACE- complete for the supersequence relation._

_Proof._ We will prove the statements for the different relations separately.

• The prefix relation: We perform a state-set simulation and check in every step of the simulation whether there is at least one accepting state in the set of active states.<tbc>

• The infix relation: We can solve the problem by solving the prefix-case for every suffix of _w_, which yields a running time of _O_(|_w_|<sup>2</sup>_m_).<tbc>

• The extension and left-extension relation: To solve the extension-case in PSPACE, we can construct an \(\varepsilon\)NFA \(A'\) for \(\Lambda_{\prec_\text{ext}}(w)\) and then check whether \(\mathsf{L}(A')\subseteq\mathsf{L}(A)\), which can be done in PSPACE. The left-extension case is analogous: construct an \(\varepsilon\)NFA for \(\Lambda_{\prec_\text{ext}}(w)\).<tbc>

<tbc>The PSPACE-hardness follows from the fact that for \(w=\varepsilon\) the extension- and left-extension- case of the universal matching problem is the same as \(\varepsilon\)NFA universality, which is PSPACE- hard.<tbc>

• The subsequence relation: The problem is obviously in coNP, since we can just guess a subsequence of _w_ and check whether it is rejected by the \(\varepsilon\)NFA.<tbc>

<tbc>For the coNP-hardness, we reduce from the negation of the NP-hard Boolean satisfiability problem on conjunctive normal form (CNF) formulas with at most 3 literals per clause, i.e., we reduce from the coNP-hard problem of checking whether a 3-CNF formula _F_ is not satisfiable. Take a 3-CNF formula _F_ with _n_ variables. We build an \(\varepsilon\)NFA _A_ that accepts all {0,1}-strings of length at most _n_-1, accepts all {0,1}-strings of length between _n_+1 and 2_n_, and accepts all length-_n_ {0,1}-strings that represent non-satisfying assignments of _F_. Indeed, an \(\varepsilon\)NFA \(A'\) for the latter strings can easily be built by using for every clause a path that reads exactly the assignments that do not satisfy this particular clause, and taking the disjunction across the clauses of _F_. Now let _w_=(01)_<sup>n</sup>_ and note that \(\Lambda_{\prec_\text{sub}}(w)\) contains only {0,1}-strings of length at most 2_n_, and that it does contain every {0,1}-string of length _n_. Therefore, if the \(\varepsilon\)NFA _A_ accepts all strings from \(\Lambda_{\prec_\text{sub}}(w)\) then \(A'\) accepts every possible length-_n_ {0,1}-string, and every such string represents a non-satisfying assignment of _F_, so we know that _F_ is not satisfiable. If _F_ is not satisfiable, then every possible length-_n_ {0,1}-string must be accepted by the \(\varepsilon\)NFA \(A'\), which means that the \(\varepsilon\)NFA _A_ must accept all strings from \(\Lambda_{\prec_\text{sub}}(w)\).<tbc>

• The supersequence relation: To show the PSPACE upper bound, we can easily construct in PTIME an \(\varepsilon\)NFA _A_<sub>_w,_**sup**</sub> that accepts exactly the supersequences of the input string _w_ - note that this is an easy special case of \[BLS15, Lemma 8\] which we reviewed in Section 3. As _A_<sub>_w,_**sup**</sub> accepts \(\Lambda_{\prec_\text{sup}}(w)\), we can then check whether \(\mathsf{L}(A_{w,\text{\textbf{sup}}})\subseteq\mathsf{L}(A)\), which can be done in PSPACE.<tbc>

<tbc>The PSPACE-hardness follows again from the fact that for \(w=\varepsilon\) the supersequence-case of the universal matching problem is the same as \(\varepsilon\)NFA universality, which is PSPACE- hard.

## 7 Conditional Lower Bounds

We now present the conditional lower bounds that are stated in  2. These bounds apply to all problems for which we showed a time complexity higher than the optimal linear complexity<tbc>

