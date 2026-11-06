Then, the rebuild process first uses _z_ comparisons and _z_ representative exchanges to move all active representatives to _D_. After which, they are replaced back into the library. This process exchanges all _z_ representatives back into the library in their calculated positions using one exchange. By the standard analysis of traversing a binary tree in in-order, the move procedures are called _O(z_) times, and each use requires _O_(1) arithmetic operations, totaling _O(z_) arithmetic operations. Summing up, dynamic rebalancing makes _O(z_lg_m_) comparisons, _O(z_lg_m_) moves, and _O(z_lg_m_) arithmetic operations.

As the traversal phase does not make any moves, it cannot change the order of active representatives, and as rebuilds do not change the order of active representatives, active representatives remain in sorted order after dynamic rebalancing.

## A.5 Amortized Analysis

Although individual instances of dynamic rebalancing can cost up to _O(s_#lg_m_) when the root is rebuilt, as large rebuilds are rare, the amortized cost of dynamic rebalancing is small. While the main text provides an intuitive bound using a simplified accounting method, here we formalize this proof via a potential argument.

For an internal node _n<sub>k</sub>_, let the imbalance of _n<sub>k</sub>_ be defined as

\(\psi\left(n_k\right)=max\left(0,\left|size\left(n_{2k}\right)-size\left(n_{2k+1}\right)\right|-1\right)\) (A.5)

This allows us to define our non-negative potential function for some scaling constant _c_:

\(\Phi=\sum_{i=1}^{s_\#^{-1}}c\cdot\psi(n_i)lg^2s'_\#.\) (A.6)

When a new active representative is inserted into a gap _L<sub>i</sub>_, the size of that leaf node and all its ancestors increases by 1. For each of the \(lgs'_\#\) ancestors of _L<sub>i</sub>_, exactly one child’s size increases by 1, which may cause its imbalance to increase by 1. This, in turn may increase potential by \(clgs'_\#lg^2s'_\#=clg^3s'_\#\). Recall previously that the baseline actual cost of insertion, i.e. excluding dynamic rebalancing is _O_(lg_m_). By definition, the amortized cost is given by the actual cost of the operation plus the change in the potential function (\(\Delta\Phi\)). Thus, the aggregate cost of insertion prior to the rebuild is given by:

\(O(lgm)+clg^3s'_\#=O(lg^3m).\)

When a rebuild occurs, the found scapegoat node _n<sub>j</sub>_ has \(\psi\left(n_j\right)=\Omega(z/logs'_\#)\) by condition (A.4). After rebuilding the subtree rooted in _n<sub>j</sub>_, all internal nodes _n<sub>k</sub>_ within the rebuilt topology obey \(\left|size\left(n_{2k}\right)-size\left(n_{2k+1}\right)\right|\le 1\), strictly reducing the internal potential of the subtree to 0. Because the total size of the subtree rooted at _n<sub>j</sub>_ is strictly conserved during the local structural change, the sizes and imbalances of all ancestors of _n<sub>j</sub>_ remain completely unaffected. Since all node potentials are non-negative, the total drop in the global potential \(\Phi\) is bounded below by the drop at _n<sub>j</sub>_ itself, which is \(c\cdot\psi\left(n_j\right)lg^2s'_\#=c\cdot\Omega(zlogs'_\#)=c\cdot\Omega(zlgm)\). By selecting the scaling constant _c_ to be sufficiently large, the net decrease in \(\Phi\) absorbs the _O(z_lg_m_) actual cost of the rebuild. Thus, the rebuild step contributes nothing (or a negative amount) to the aggregate amortized cost. This means the total amortized cost of insertion, including any dynamic rebalancing it may trigger, is strictly bounded by the baseline cost.

Resizes cannot increase potential as they re-initialize all gaps uniformly with 1 active representative per gap which represents a perfectly balanced state where potential is 0. Thus, the aggregate cost stands.

\(\blacktriangleright\) **Lemma A.2.** _R.insert(x_) _requires O_(lg<sup>3</sup>_m_) _comparisons and O_(lg<sup>3</sup>_m_) _moves amortized._

