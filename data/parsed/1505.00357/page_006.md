<tbc><u>Case 2.2</u>: \(K_a\prec K_c\). By Lemma 3(i), \(\omega(T_0)\ge\omega(T_{11})\). By Fact A, \(\omega(K_a)\ge\omega(T_{11})\).

If \(\langle v=K_z\rangle\) is in _T_<sub>11</sub>, then \(\omega(T_{11})\ge\omega(K_z)\) and transitively we are done.

In the remaining case, \(\langle v=K_z\rangle\) is in _T_<sub>10</sub>. _T_’s irreducibility implies \(K_z\prec K_c\). Since \(K_a\prec K_c\) also (Case 2.2), grandchild \(\langle v\prec K_c\rangle\) does not separate _K<sub>a</sub>_ from _K<sub>z</sub>_, and by Assumption 1 the root of subtree _T_<sub>10</sub> does an inequality comparison. Hence, the subtree rooted at \(\langle v\prec K_b\rangle\) is as in Fig.5(a):

**Lemma 4.** \(\omega(T_0)\ge\omega(T_{10})\).

(Because replacing (a) by (b) preserves correctness; proof in Appendix 7.2.)

Since descendant \(\langle v=K_z\rangle\) is in _T_<sub>10</sub>, Lemma 4 implies \(\omega(T_0)\ge\omega(T_{10})\ge\omega(K_z)\). This and Fact A imply \(\omega(K_a)\ge\omega(K_z)\). This proves Lemma 1. □

**Proposition 1.** _If any leaf node_ \(\langle K_\ell\rangle\)_’s parent P does not do an equality comparison against key_ \(K_\ell\)_, then changing P so that it does so gives an irreducible_ \(2\mathrm{WCST}T'\) _of the same cost._

_Proof._ Since \(\mathcal{Q}_{\langle K_\ell\rangle}=\{K_\ell\}\) and _P_’s comparison operator is in \(\mathcal{C}\subseteq\{<,\le,=\}\), it must be that \(K_\ell=\mathrm{max}\mathcal{Q}_P\) or \(K_\ell=\mathrm{min}\mathcal{Q}_P\). So changing _P_ to \(\langle v=K_\ell\rangle\) (with \(\langle K_\ell\rangle\) as the “yes” child and the other child the “no” child) maintains correctness, cost, and irreducibility. □

