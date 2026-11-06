# Beating Trivial Time for Tricky Triangle Tasks

**Abstract**

For several well-studied triangle detection problems in the literature, the trivial enumeration algorithms are known to be optimal (up to the exponent) assuming popular fine-grained conjectures. For example, All-Edges Sparse Triangle and Sparse Monochromatic Triangle where each node has degree \(n^\delta\) for some \(\delta<1\), and the Exact Triangle where edges have arbitrary weights, all have this property under the 3SUM Conjecture. However, as there are slightly nontrivial algorithms for 3SUM, it is natural to wonder if the trivial algorithm for these tricky triangle tasks might also be improved.

Applying a variety of techniques from randomized algorithms, circuit complexity, and communication complexity, we present the first improvements over the trivial algorithms for each of these problems in the Word RAM model. Moreover, our algorithms can be implemented with _only_ polysize AC0 operations on words. Extending our techniques, we also show how to solve the notorious 4-cycle detection problem on _n_-node graphs in _o(n_<sup>2</sup>) time, in a Word-RAM model with word size \(w>\omega(log^2n)\). Along the way, we show how to sort _n_ items over a universe of size 2_<sup>u</sup>_ using only AC0 word operations in _O(nu_log_n)/w_ time.

**2012 ACM Subject Classification** graph algorithms analysis

**Keywords and phrases** sparse graph algorithms, triangle, Word RAM, 4-cycle

**Digital Object Identifier** 10.4230/LIPIcs.MFCS.2026.8

Funding Parts of this work were completed while R.W. was visiting the Institute for Advanced Study, Princeton, NJ. This material is based upon work supported by the National Science Foundation under grants DMS-2424441 (at IAS) and CCF-2420092 (at MIT).

**_Note: This is the full version of a paper that will appear in MFCS 2026._**

Neha Pant \(\boxtimes\) MIT Ryan Williams \(\boxtimes\) MIT

