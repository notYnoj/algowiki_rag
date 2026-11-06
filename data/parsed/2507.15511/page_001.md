Certificate-Sensitive Subset Sum: Realizing Instance Complexity

Jesus Salas<sup>∗</sup>

**Abstract**

The Subset Sum problem is a classical NP-complete problem with a long-standing _O_<sup>∗</sup>(2<sup>_n/_2</sup>) deterministic bound due to Horowitz and Sahni. We present results at two distinct levels of generality.

**First (instance-sensitive bound)**, we introduce, to our knowledge, the first deterministic algorithm whose runtime provably scales with the _certificate size_ \(U=|\Sigma(S)|\), the number of distinct subset sums. Our enumerator constructs all such sums in time \(O(U\cdot n^2)\), with a randomized variant achieving expected time \(O(U\cdot n)\). This provides a constructive link to Instance Complexity by tying runtime to the size of an information-theoretically minimal certificate.

**Second (unconditional worst-case bound)**, by combining this enumerator with a double meet-in-the-middle strategy and a _Controlled Aliasing_ technique that enforces a simple canonical- normal-form (CNF) expansion policy on aliased states, we obtain a deterministic solver running in \(O^*(2^{n/2-\varepsilon})\) time with \(\varepsilon=log_2(\frac{4}{3})\)--the first unconditional deterministic improvement over the classical _O_<sup>∗</sup>(2<sup>_n/_2</sup>) bound for _all_ sufficiently large _n_.

**Finally**, we refine fine-grained hardness for Subset Sum by making explicit the structural regime (high collision entropy / near collision-free) implicitly assumed by SETH-based reductions, i.e., instances with near-maximal _U_.

## 1 Motivation

This work offers four primary contributions, three of which are structural in nature.

\(\bullet\) **Instance-sensitive bound via certificate size** _U_: To our knowledge, this is the first deterministic algorithm for a canonical NP-complete problem whose runtime provably adapts to a _minimal_ constructive certificate, namely \(\Sigma(S)\). The algorithm constructs this certificate online from scratch, in deterministic time \(O(U\cdot n^2)\) (expected \(O(U\cdot n)\) randomized), rather than merely deciding feasibility.

\(\bullet\) **Unconditional worst-case improvement:** By combining the enumerator with a double meet-in-the-middle strategy and _Controlled Aliasing under Canonical Normal Form (CNF)_--i.e., a simple _count-based expansion policy_ at the alias indices (§5.2, App. E)--IC- SubsetSum achieves a worst-case runtime \(O^*(2^{n/2-\varepsilon})\) with \(\varepsilon=log_2\left(\frac{4}{3}\right)\) for _all_ inputs, the first deterministic improvement over the classical _O_<sup>∗</sup>(2<sup>_n/_2</sup>) Horowitz–Sahni bound in nearly 50 years.

<sup>∗</sup>Research conducted independently. **jesus.salas@gmail.com** — ORCID: 0009-0007-6411-2270 A version of this paper will be submitted to a major theoretical computer science conference.

arXiv:2507.15511v6 [cs.CC] 28 Aug 2025

