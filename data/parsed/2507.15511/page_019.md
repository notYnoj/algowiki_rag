## Appendix Overview

This appendix expands on the enumeration logic, correctness conditions, and structural optimizations introduced in Sections 4-6. It is organized as follows:

• Appendix A details the column-wise subset-sum enumerator, including the _suppression-on- overwrite_ invariant and the lex-minimal canonicalization rule, with full pseudocode.<tbc>

• Appendix B presents the interleaved double-meet-in-the-middle framework, the real-time Check/CheckAliased procedures (including the \(2\times 2\) compensatory merge under aliasing), and the work accounting used in the certificate-sensitive bounds.<tbc>

• Appendix C states the algebraic combination lemmas used by the solver (direct, complement, and mixed cases) and the associated correctness checks for sum recombination that power the real-time Check routines.<tbc>

• Appendix D provides additional experimental data, including plots of runtime scaling versus _U_ and measured collision entropy.<tbc>

• Appendix E gives the full _Controlled Aliasing_ framework: the 2-lane \((\tilde{\sigma},\chi)\) memoization with affine correction, the count-based canonical normalization (CNF) at the alias indices, and the expansion policy. It includes the key lemmas--Lemma 8, Lemma 6, Lemma 7, Lemma 9, Lemma 10--and the proof of Theorem 6.<tbc>

