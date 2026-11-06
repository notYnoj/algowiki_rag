<tbc>By the final part of Lemma 4.6, Bob can construct \(H_{\alpha^S}\) from the public variable set, the assignment \(\alpha^S\), and the bounds _N<sup>d</sup>_ and _N_<sup>_d_-1</sup>. He does not need to know Alice’s string. The gadget uses _O<sub>R</sub>(N_) new variables, and \(P_b\cup H_{\alpha^S}\) is simple. When _R_ is symmetric, it has no repeated unordered scope.

Suppose now that the streaming algorithm uses _s(n_) bits of space. We first reduce its error so that each output is wrong with probability at most \(1/(10\cdot 2^d)\). This requires only _O<sub>R</sub>_(1) independent copies because _d_ depends only on _R_. Alice runs the amplified algorithm on _P<sub>b</sub>_ and sends its memory state to Bob. For each \(S\subseteq[d]\), Bob starts from a copy of this state, appends \(H_{\alpha^S}\), and obtains \(\mathrm{OPT}_\mathrm{max}(P_b\cup H_{\alpha^S})\). Subtracting the known number \(|H_{\alpha^S}|\) gives \(\mathrm{val}_{P_b}(\alpha^S)\). A union bound shows that all 2_<sup>d</sup>_ values are correct simultaneously with constant probability, after which Bob recovers _b<sub>q</sub>_ from the signed sum above.

There is a constant _A<sub>R</sub>_ such that every final instance uses at most _A<sub>R</sub>N_ variables. For any sufficiently large target value _n_, choose \(N=\lfloor n/A_R\rfloor\) and add unused variables so that the final instance has exactly _n_ variables. Then \(N=\Theta_R(n)\). We have obtained a randomized public-coin one-way protocol for INDEX_<sub>N<sup>d</sup></sub>_ with _O<sub>R</sub>(s(n_)) communication. By Lemma 3.7, \(s(n)=\Omega_R(N^d)=\Omega_R(n^d)\).

We have proved the required lower bound when _R_ is a core. It remains only to combine this with the reduction to the core and the upper bound proved above.

_Proof of Theorem 7.1._ Let _R<sup>⋆</sup>_=core(_R_). By Lemma 4.2, solving Exact-CSP(_R_) has the same streaming space complexity as solving Exact-CSP(_R<sup>⋆</sup>_). The deterministic upper bound follows from Lemma 7.2. If _d_=0, the indicator of _R<sup>⋆</sup>_ is constant, so _R<sup>⋆</sup>_ is either empty or equal to _C<sup>k</sup>_. This gives the last statement of the theorem. Suppose now that \(d\ge 1\). The randomized lower bound follows by applying Theorem 7.3 to _R<sup>⋆</sup>_. The reduction to the core preserves simple instances. If _R_ is symmetric, then _R<sup>⋆</sup>_ is symmetric and the reduction also preserves the unordered scopes. This proves all three parts of the theorem.

Thus the streaming complexity of Exact-CSP(_R_) on simple instances is governed, up to the logarithmic factor in the upper bound, by the degree of the core relation.

## 8 Conclusion and Open Questions

In this paper, we demonstrated that the core of a relation is vital for characterizing the streaming complexity of many optimization problems related to constraint satisfaction problems. We hope that this work encourages further exploration of the relationship between CSP cores and streaming complexity. We conclude with a handful of open questions.

• Can the algorithms presented in Theorem 5.1 and Theorem 6.1 be made efficient in terms of both space and time complexity? A key challenge in this regard is that there is no general technique for efficiently detecting if a CSP instance is non-redundant. If one could find such an algorithm, it would be a major milestone in the development of algorithms for CSP kernelization. See [CJP20; LW20; Car22; BG25] for further discussion.<tbc>

• In addition, our paper only considers _insertion-only_ streams. What if we allow both insertions and deletions?<tbc>

