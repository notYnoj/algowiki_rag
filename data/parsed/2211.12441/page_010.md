<tbc>to all pairs (_a,b_), which is what we need for Theorem 6. We establish such a bound in Section 9. The counts of the rankings \(\rho\) with a particular value for \(\text{XInv}_\rho(A,B)\) appear as the coefficients of the _Gaussian polynomials_. Our bound can be stated equivalently as a bound on those coefficients.

### Organization.

We have organized the material so as to provide a shortest route to a full proof of Theorem 5. Here are the sections needed for the different main results:

\(\circ\) Theorem 5 (lower bound for general trees): 3, 4.<tbc>

\(\circ\) Theorem 6 (lower bound for binary trees): 3, 5, 9.<tbc>

\(\circ\) Theorem 8 (lower bound for restricted classes): 7, 8 up to 8.3 inclusive.<tbc>

\(\circ\) Theorem 9 (lower bound for counting cross inversions): 7, 8 but not 8.2 nor 8.3.

In Section 2, we provide some background on known lower bounds in the comparison-query model, several of which are unified by the Sensitivity Lemma and Connectivity Lemma. In Section 6, we present our lower bounds against randomized algorithms with bounded error. The tight bound on maximum probability of the cross-inversion distribution is covered in Section 9. For completeness, we end in Section 10 with proofs of the results we stated on the Turing complexity of inversion minimization on trees.

## 2 The Comparison-Query Model

In this section we provide an overview of known results and techniques for lower bounds in the comparison-query model. This section can be skipped without a significant loss in continuity.

Tight bounds have been established for problems like sorting, selection, and heap construction.

\(\circ\) We already discussed the central problem of sorting in Section 1.<tbc>

\(\circ\) In _selection_ we are told a rank _r_, and must identify the item with rank _r_. The query complexity is known to be \(\Theta(n)\) \[BFP<sup>+</sup>73, DZ99, DZ01\]. There is also _multiple selection_, in which one is given multiple ranks _r_<sub>1</sub>_,...,r<sub>k</sub>_, and must identify each of the corresponding items. The query complexity of multiple selection is likewise known up to a \(\Theta(n)\) gap between the upper and lower bounds \[KMMS05\].<tbc>

\(\circ\) In _heap construction_ we must arrange the items as nodes in a complete binary tree such that every node has a rank no larger than its children. The query complexity is known to be \(\Theta(n)\) \[CC92, GM86\].

All the problems above can be cast as instantiations of a general framework known as _partial order production_ \[Sch76\]. Here, in addition to query access to the ranking \(\rho\) of the items, we are given _n slots_ and regular access to a partial order _\<_slot on the slots. The objective is to put each item into a slot, one item per slot, so that whenever two slots, _s_<sub>1</sub> and _s_<sub>2</sub>, are related by _s_<sub>1</sub>_\<_slot _s_<sub>2</sub>, we also have \(\rho(s_1)<\rho(s_2)\). Sorting coincides with the case where _\<_slot is a total order. In selection of rank _r_, there is a designated slot _s_<sup>∗</sup>, and there are exactly _r_-1 slots _s_ with _s\<_slot _s_<sup>∗</sup> and exactly _n-r_ slots _s_ with _s_<sup>∗</sup>_\<_slot _s_; there are no other relations in _\<_slot (see the example at the end of Section 7 for more details). Multiple selection is similar. For heap construction, _\<_slot matches the complete binary tree arrangement.

