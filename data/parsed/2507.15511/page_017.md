<tbc>\(O(U\cdot n)\), e.g., via a deterministic canonicality test that avoids the _O(n_) lexicographic comparison cost while preserving the local model in Conjecture 1?

### Improving the Controlled Aliasing Bound.

Our worst-case speedup \(\varepsilon=log_2(\frac{4}{3})\) arises from a single alias pair per half under the 2-lane canonicalization keyed by \((\tilde{\sigma},\chi)\) (CNF). Straightforward pattern-based generalizations for alias groups of size _g_ induce 2_<sup>g</sup>_ lanes and exponential overhead, keeping \(\varepsilon\) constant. We conjecture that a _count-based_ scheme--tracking only the number of chosen elements from each alias group (yielding (_g_+1) buckets) with polynomial overhead--could permit \(g=\Theta(logn)\), improving the multiplicative reduction from 2_<sup>g</sup>_ to (_g_+1). In principle, this could yield \(\varepsilon=\Theta(logn)\), i.e., a worst-case runtime of 2<sup>_n/_2</sup>_/n<sup>c</sup>_ for some constant _c\>_0. Making this rigorous requires (i) a safety proof for count-only canonicalization (lane invariant and merge completeness), and (ii) a certified reconstruction path from counts to witnesses without reintroducing exponential blowup.

### Structure-Sensitive Runtimes in NP.

Which other NP-complete problems admit certificate- sensitive runtimes? Collision entropy provides a structural knob complementary to solution density. For Partition, Knapsack, and Bin Packing, one may aim to construct compressed summaries of feasible configurations whose _construction time_ is proportional to summary size. Formalizing such certificates and proving instance-sensitive enumeration bounds are promising directions.

### Derandomization of Local Canonicality.

The randomized \(O(U\cdot n)\) bound uses 2-universal hashing to filter collisions so that lexicographic comparisons are needed only rarely (expected _O_(1) per check). Is there a deterministic analogue achieving sublinear-time canonicality tests in the local deduplicating model? Such a result would match the conjectured optimal runtime (Conjecture 1) and yield a practical local derandomization.

### Constructive Instance Complexity Beyond Subset Sum.

We showed that the certificate \(\Sigma(S)\) can be constructed in deterministic \(O(U\cdot n^2)\) time (or expected \(O(U\cdot n)\)). Can analogous online certifiers be built for problems such as 3SAT or Clique under appropriate entropy/compressibility assumptions? A broader theory of _algorithmic IC_--tracking both information content and construction cost--remains to be developed.

### Toward a Complexity Class for Certificate-Sensitive Problems.

Our solver runs in time polynomial in the input size _n_ and in the size of an intrinsic instance-specific certificate (\(U=|\Sigma(S)|\)). This suggests a class we tentatively call **P-IC** (_Polynomial in Instance Certificate_): problems for which a natural instance certificate can be constructed and then used to solve the instance in time polynomial in the certificate size and input size. Pinning down robust certificate notions (e.g., sets of satisfying assignments for SAT, achievable value/weight pairs for Knapsack) and charting the boundaries of P-IC is an intriguing direction for future work.

## 10 Conclusion

### Theoretical Advance.

This paper develops a framework for structure-aware enumeration in NP-complete problems, using Subset Sum as a case study. We introduce the certificate-sensitive parameter \(U:=|\Sigma(S)|\) and show that it aligns with both per-instance difficulty and observed<tbc>

