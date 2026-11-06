_ACM Symposium on Theory of Computing, May 13-17, 1990, Baltimore, Maryland, USA,_ pages 438-445. ACM, 1990. `doi:10.1145/100216.100274`.

**18** Robert W Rosenthal. A class of games possessing pure-strategy Nash equilibria. _International Journal of Game Theory_, 2(1):65-67, 1973.

**19** Alejandro A. Schäffer and Mihalis Yannakakis. Simple local search problems that are hard to solve. _SIAM J. Comput._, 20(1):56-87, 1991. `doi:10.1137/0220004`.

**20** Dominik Scheder and Johannes Tantow. PLS-completeness of string permutations. In Anne Benoit, Haim Kaplan, Sebastian Wild, and Grzegorz Herman, editors, _33rd Annual European Symposium on Algorithms, ESA 2025, September 15-17, 2025, Warsaw, Poland_, volume 351 of _LIPIcs_, pages 56:1-56:14. Schloss Dagstuhl - Leibniz-Zentrum für Informatik, 2025. URL: `https://doi.org/10.4230/LIPIcs.ESA.2025.56`, `doi:10.4230/LIPICS.ESA.2025.56`.

**21** Alexander Skopalik and Berthold Vöcking. Inapproximability of pure nash equilibria. In Cynthia Dwork, editor, _Proceedings of the 40th Annual ACM Symposium on Theory of Computing, Victoria, British Columbia, Canada, May 17-20, 2008_, pages 355-364. ACM, 2008. `doi:10.1145/1374376.1374428`.

**22** Vipin Ravindran Vijayakshmi and Alexander Skopalik. Improving approximate pure nash equilibria in congestion games. In Xujin Chen, Nikolai Gravin, Martin Hoefer, and Ruta Mehta, editors, _Web and Internet Economics - 16th International Conference, WINE 2020, Beijing, China, December 7-11, 2020, Proceedings_, volume 12495 of _Lecture Notes in Computer Science_, pages 280-294. Springer, 2020. `doi:10.1007/978-3-030-64946-3\\\_20`.

**23** Clara Waldmann. _Congestion Games: Equilibria, Networks, and Complexity_. PhD thesis, Technische Universität München, 2022.

## A Remaining proofs for Max-4-SAT

In this section, we give the remaining proofs for Section 4.3. The reduction given above transforms a circuit _C_ (an instance of Flip) into a 4-CNF-formula _F=F(C_) (an instance of LocalMax-4-SAT). One step was to augment the circuit _C_ to not only output the _m_-bit vector representing the _value_ of its input **x**, but also the best neighbor of **x**. We denote by \(C_V(\mathbf{x})\in\{0,1\}^m\) the value and by _C<sub>N</sub>_(**x**) the best neighbor. Let \(\alpha\) be a truth assignment to the variables of _F_ and _f_ the _flip variable_. Recall that we call the TOP circuit _active_ if \(\alpha(f)=1\); we call BOTTOM active if \(\alpha(f)=0\). We call the other circuit _inactive_. We define a function _g_ that maps assignments \(\alpha\) of _F_ to circuits input for _C_ as follows:

\(g(\alpha)=\left\{\begin{array}{ c c }
\alpha(x^B) & ,\text{if}\alpha(f)=0 \\
\alpha(x^T) & ,\text{if}\alpha(f)=1
\end{array}\right.\)

\(\blacktriangleright\) **Theorem 9.** _Let_ \(\alpha\) _be a locally optimal assignment to the variables of F. Then_ \(g(\alpha)\) _is a solution to the flip instance C._

**Proof.** We will assume without loss of generality that \(\alpha(f)=1\), i.e., the TOP circuit is active.

\(\blacktriangleright\) **Lemma 10.** \(\alpha\) _maps all shadow variables of the active circuit TOP to_ 0.

**Proof.** Suppose, for the sake of contradiction, that \(\alpha(s_i^T)=1\) for some \(1\le i\le m\). What happens when we change \(\alpha(s_i^T)\) to 0? Clause groups 0, 1, 3 and 4 do not contain shadow variables. Clauses of groups 1b and 6 contain only the negative literal \(\neg s_i^T\), so the change can only improve. In group 2, \(s_i^T\) occurs in \(C_i^B:=\neg f\rightarrow(o_i\le v_i^B)\vee s_i^T\) (4.14) and \((o_i\wedge s_i^T)\rightarrow f\) (4.17), and in group 5 only in \((\neg f\wedge v_i^T\wedge\neg v_i^B)\rightarrow s_i^T\) (4.18). All three clauses are and stay satisfied by \(\alpha(f)=1\). Group 6 contains \((\neg s_i^T)\) (4.19), so the satisfied weight improves, meaning that \(\alpha\) was no local optimum. \(\blacktriangleleft\)

