for various computational problems \[GO95, Her96, P ̆at10, AL13, VW13, AV14, JV16, KPP16\]. Moreover, its connection to other fine-grained conjectures has recently been established \[BKM<sup>+</sup>24, Lam26\].

### Quantum complexity of _k_-SUM.

For _k_=2, Ambainis \[Amb07\], based on the result of \[BDH<sup>+</sup>05\], gave an \(\widetilde{O}(n^{2/3})\) quantum algorithm. For all values of _k_, the upper bound \(\widetilde{O}(n^{k/3})\) can be obtained via the Claw Finding algorithm of Tani \[Tan09\]. For _k_=4, an algorithm for random instances running in time \(\widetilde{O}(n^{6/5})\) was obtained in \[BJLM13\]. A classical foundation for this line of work on random instances is Wagner’s merging-tree algorithm for the Generalized Birthday Problem \[Wag02\]. _Random instances_ of _k_-SUM were studied in \[GNS18, NS20, Sch21\]. For single-solution random instances, the best known _k_-SUM algorithm is due to Schrottenloher \[Sch21\]<sup>3</sup>.

**Theorem 1.1** (\[Sch21\])**.** _For every integer k\>_2_, single-solution random instances of k_-SUM _can be solved in quantum time_ \(\widetilde{O}(n^{\Phi_k})\)_, where_

\(\Phi_k=\frac{2k-\lfloor k/7\rfloor-\lfloor(k+3)/7\rfloor}{6}.\)

Here, _single-solution random instances_ are those for which the expected number of witnesses is one; see \[Sch21\] for the exact definition.

## Our Results

Our main result is the quantum algorithm for the _worst-case k_-SUM problem.

**Theorem 1.2.** _For every integer k\>_3_, worst-case k_-SUM _can be solved in quantum time_ \(\widetilde{O}(n^{\Psi_k})\)_, where_<sup>4</sup>

\(\Psi_k=\underbrace{\frac{2k-\lfloor k/7\rfloor-\lfloor(k+3)/7\rfloor}{6}}_{\Phi_k}-\frac{[k\equiv 3mod7]}{9}-\frac{[k\equiv 6mod7]}{18}.\)

This improves Tani’s \(\widetilde{O}(n^{k/3})\) algorithm for every value of _k\>_3, and, asymptotically, \(\Psi_k=\frac{2k}{7}+O(1)\).

A simple corollary of our _k_-SUM algorithm is a new upper bound for the Subset Sum problem, which improves the previous worst-case quantum bound _O_<sup>∗</sup>(2<sup>_n/_3</sup>) \[BJLM13, AHJ<sup>+</sup>22\].

**Corollary 1.3.** _The_ Subset Sum _problem can be solved in quantum time O_<sup>∗</sup>(2<sup>2_n/_7</sup>).

Beyond Subset Sum, our _k_-SUM algorithm also improves the quantum upper bound for a related variant. In Pigeonhole Equal Subset Sum, one seeks two subsets with equal sums; here, the _n_ input integers are promised to sum to less than 2_<sup>n</sup>_-1, so that two such subsets exist by the pigeonhole principle. An _O_<sup>∗</sup>(2<sup>_n/_2</sup>) classical algorithm for this problem \[AHJ<sup>+</sup>22\] was improved by Jin and Wu \[JW24\] to _O_<sup>∗</sup>(2<sup>0.4_n_</sup>), and subsequently by Jin, Williams, and Zhang to _O_<sup>∗</sup>(2<sup>_n/_3</sup>) \[JWZ25\]. No algorithm faster than _O_<sup>∗</sup>(2<sup>_n/_3</sup>) is known for the Pigeonhole Equal Subset Sum problem, even in the quantum setting. These works also raised the question of whether the _modular_ version of this problem can be solved faster than _O_<sup>∗</sup>(2<sup>0.5_n_</sup>). We give a positive answer in the quantum setting, showing that the Pigeonhole Modular Equal Subset Sum problem can be solved in quantum time _O_<sup>∗</sup>(2<sup>0.453_n_</sup>) by a simple reduction to the _k_-SUM problem and an application of Theorem 1.2. Formal definitions and proofs are provided in Theorem 4.2 of Section 4.

<sup>3</sup>Some of the bounds above were proven for the _k_-XOR problem, but they carry over to _k_-SUM. <sup>4</sup>\([\cdot]\) is the Iverson bracket: for a condition E, \[E\]=1 if E holds, and \[E\]=0 otherwise.

