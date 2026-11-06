1. Trace the chord cycle of _D_ and form the visit sequence **w** of length 2_k_.<tbc>

2. The dual code is the RGS normalization **c**<sup>∗</sup> of **w**; let \(\mu\) be the relabeling that sends the labels of _D_ to the labels of **c**<sup>∗</sup>.<tbc>

3. The sign \(\sigma_{\mu(i)}^*\) is +1 if the cycle runs along chord _i_ in opposite directions (the two arrivals are at different endpoints), and -1 if it runs along _i_ in the same direction (both arrivals at the same endpoint).<tbc>

4. Replace the result by its canonical form (2).

Since **w** depends on the base point and the direction of the tracing, the dual is a well-defined _equivalence class_.

**Lemma 5.2.** _If D is a one-cycle diagram, then D_<sup>∗</sup> _is a one-cycle diagram,_ \(D^{**}\simeq D\)_, D and D_<sup>∗</sup> _have the same (non- )orientable genus, and the class of D_<sup>∗</sup> _depends only on the class of D. Consequently, if N is the number of equivalence classes, K the number of unordered pairs_ {\[_D_\],\[_D_<sup>∗</sup>\]} _and s the number of self-dual classes, then s_=2_K-N._

_Proof._ See Kybalko et al. (2018).

**Theorem 5.3.** _Two optimal Morse flows X,Y are topologically equivalent if and only if_ \(D_X\simeq D_Y\)_, and X is topologically equivalent to the inverse flow_ -_Y if and only if_ \(D_X\simeq D_Y^*\).

_Proof._ See Kybalko et al. (2018).

_Remark_ 5.4. If a one-cycle signed chord diagram _D_ is interpreted as a cellular embedding of a single-vertex graph (a bouquet of _k_ circles) on a closed surface _M_ with a single 2-cell, then the dual chord diagram _D_<sup>∗</sup> specifies the cellular embedding of the topological dual graph _G_<sup>∗</sup> on _M_; _G_<sup>∗</sup> is again a bouquet of _k_ circles with a single 2-cell.

## 6 Software Implementation and Enumeration Data

The enumeration algorithm has been fully implemented in Python and deposited in Zenodo Prishlyak (2026a). For the genus parameter _g_ the program takes _k_=2_g_ and \(\sigma\equiv(+1)^k\) if \(g\ge 0\) (orientable case), and _k_=-_g_ with all 2_<sup>k</sup>_-1 sign vectors different from (+1)_<sup>k</sup>_ if _g\<_0 (non-orientable case).

**Algorithm 2** Enumeration of one-cycle classes

