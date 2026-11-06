better than any STT (Section 2.1). Then we generalize the discussion to elaborate further on our technique for finding this specific example and multiple others (Section 2.2), and study the integrality gap of the LP (Section 2.3). Finally, in Section 2.4 we disprove Conjecture 2 and show that the proposed rounding scheme may result in a sub-optimal STT. There, we also give a lower bound on the approximation-ratio for this specific rounding scheme.

## 2.1 Specific Counter Example: Strictly Better Fractional Vertex

In this section we provide an explicit example for a topology and frequencies such that the LP solution for it is strictly better than any solution induced by a search tree. The topology and frequencies were found using computer search (Appendix B), more details follow in Section 2.2. In this section we provide a proof that the solution we found is a non-integer feasible solution to the LP, such that any other integer solution that is induced by a search tree is strictly worse.

**Definition 2.1** (Terminology)**.** For ease of reference, we define the following terminology. Let _U_ be a tree over _n_=7 nodes such that nodes 1 to 5 form a path in the natural order, with additional edges (3,6) and (6,7). This is also the tree in Figure 1, and _U_<sub>(7,3)</sub> in Figure 6. We refer to _U_ as a _long star_, with three _legs_. We refer to 3 as its center, to 1,5,7 as leaves, and to 2,4,6 as mid-nodes.

**Theorem 2.2.** Let _U_ be a long-star (Definition 2.1). Let \(f=\frac{1}{23}[3,2,0,2,3,3,10]\) be the frequencies vector, i.e., such that _f<sub>i</sub>_ is the frequency of querying node _i_. Then there is a feasible solution _P_ with depth coordinates _P<sub>D</sub>_=\[2,2,4.5,2,2,1.5,0.5\] that is strictly better for the LP with weights _f_ compared to any feasible point induced by an STT over _U_.

We note before the proof:

1. Theorem 2.2 holds even when we require a vector of strictly positive frequencies. Indeed, we can perturb _f_<sub>3</sub> by some \(\epsilon>0\) and still maintain a strictly-better feasible solution.<tbc>

2. _P_ is in fact a vertex, as determined by our LP-solver code. That being said, Theorem 2.2 does not require _P_ to be a vertex, just that its value is strictly better than any STT.

_Proof._ For convenience, we scale the frequencies back to integer weights and use the vector \(w=23\cdot f=[3,2,0,2,3,3,10]\). We divide the proof to two parts. First we describe all the coordinates of _P_ and verify its feasibility. Then we case-analyze the best possible value of a search tree, to show that it is strictly worse than the value of _P_.

**The solution** _P_**:** We present the values of the variables of _P_ in Figure 3, where the _X<sub>ij</sub>_ variables form a matrix _X_ (note that the variables _X<sub>ii</sub>_ do not exist, so these entries are marked by ’.’). The _D<sub>i</sub>_’s are written below _X_, as they are the sums of the columns of _X_, and _Z<sub>kij</sub>_ are to the side of _X_. The figure also verifies feasibility for each of the (in)equalities. The weighted depth of _P_ is: \(P_D\cdot w=[2,2,4.5,2,2,1.5,0.5]\cdot[3,2,0,2,3,3,10]=6+4+0+4+6+4.5+5=29.5\).

**Case analysis of all search trees:** The number of STTs over _U_ is too large for hand verification. There are 662 in total, but _U_ is symmetric, and _w_ is also mostly symmetric. This enables us to reduce the analysis to a handful of cases. We emphasize that in the following discussion, the quality of an STT is considered with respect to _w_=\[3,2,0,2,3,3,10\], and that the depths start from 0 (root) (see Remark 1.5).

Before the case analysis itself, we determine the best BST over the nodes 1 to 5, which is used later in two different cases. A best BST only on the subgraph of _U_ that contains nodes 1 to 5 has<tbc>

