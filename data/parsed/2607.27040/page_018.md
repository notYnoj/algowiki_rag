formula for the range covered by a node _n<sub>k</sub>_ is \(L_\ell\dots L_r\) where \(l=\left(k-2^{\lfloor lgk\rfloor}\right)2^{logs^\prime_\#-\lfloor lgk\rfloor}+1\) and \(r=l+2^{logs^\prime_\#-\lfloor lgk\rfloor}-1\). For a node _n<sub>k</sub>_ covering the range \(L_\ell\dots L_r\), we define size(_n<sub>k</sub>_) as the number of active representatives in the range covered by the node, that is the number of active representatives in \(L_\ell\dots L_r\), and span(_n<sub>k</sub>_) as the length of the range covered by the node, which is given by _r-l_+1 or \(2^{logs^\prime_\#-\lfloor lgk\rfloor}\) from the general formulas of _l_ and _r_. As a parent covers the union of the ranges of its children, size(_n<sub>k</sub>_)=size(_n_<sub>2_k_</sub>)+size(_n_<sub>2_k_+1</sub>) and span(_n<sub>k</sub>_)=span(_n_<sub>2_k_</sub>)+span(_n_<sub>2_k_+1</sub>). Additionally, since each gap contains at least 1 active representative by the gap invariant, \(size(n_k)\ge span(n_k)\). This structure is not explicitly stored by the algorithm, but we logically traverse the tree during dynamic rebalancing.

The key realization is that density-based balancing, e.g. in [2] are inherently limited to logarithmic slack, incurring an \(O(lglogs'_\#)\) comparisons overhead per search. Instead, we lazily keep nodes weight balanced, like scapegoat trees in [3]. For our structure, the invariant for some internal node _n<sub>k</sub>_ is

\(|size(n_{2k})-size(n_{2k+1})|\le max\left(1,size(n_k)/logs'_\#\right)\) (A.1)

We let _n_<sub>leaf</sub> be some leaf node in the tree whose ancestors all satisfy (A.1), and _n<sub>i</sub>_ be the shallowest ancestor of _n_<sub>leaf</sub> such that \(size(n_i)<logs'_\#\). Using size(_n_<sub>2_k_</sub>)+size(_n_<sub>2_k_+1</sub>)=size(_n<sub>k</sub>_), we bound the size of the children of a node _n<sub>k</sub>_ that follows (A.1) when \(size(n_k)\ge lgs'_\#\)

\(max\left(size(n_{2k}),size(n_{2k+1})\right)\le\left(1+1/logs'_\#\right)size(n_k)/2\)

By the above relationship, the size of a node reduces by a factor of at least \(\left(1+1/logs'_\#\right)/2\) per level of the tree given the size of the parent exceeds \(logs'_\#\), which is true for all \(\lfloor lgi\rfloor\) ancestors of _n<sub>i</sub>_ as sizes of nodes moving up the tree are monotone increasing. Thus, we bound size(_n<sub>i</sub>_)

\(size(n_i)\le\left((1+1/logs'_\#)/2\right)^{\lfloor lgi\rfloor} s_\#\)<br> \(\le(1+1/logs'_\#)^{\lfloor lgi\rfloor} s_\#/2^{\lfloor lgi\rfloor}\)

The expression (1+1_/u)<sup>u</sup>_ approaches _e_ from below, and since \(i\le 2s'_\#-1\) by the definition of the node indexes and \(s'_\#\) is a power of 2, we can deduce \(\lfloor lgi\rfloor\le lgs_\#\); thus \(\left(1+1/logs'_\#\right)^{\lfloor lgi\rfloor}\le\left(1+1/logs'_\#\right)^{logs^\prime_\#}\le e\), giving

\(size(n_i)\le es_\#/2^{\lfloor lgi\rfloor}\) (A.2)

For nodes _n<sub>k</sub>_ following (A.1) where \(size(n_k)<logs'_\#\), \(nt|size(n_{2k})-size(n_{2k+1})|\le 1\) is enforced by the invaria, and as size(_n<sub>k</sub>_)=size(_n_<sub>2_k_</sub>)+size(_n_<sub>2_k_+1</sub>), this implies

\(max\left(size(n_{2k}),size(n_{2k+1})\right)\le\left(size(n_k)+1\right)/2\)

Repeating this linear recurrence from _n<sub>i</sub>_ for the remaining \(logs'_\#-\lfloor lgi\rfloor\) layers of the tree until we reach _n_<sub>leaf</sub> yields by induction

\(size(n_\text{leaf})\le\left(size(n_i)+\left(2^{logs^\prime_\#-\lfloor lgi\rfloor}-1\right)\right)/2^{logs^\prime_\#-\lfloor lgi\rfloor}\)<br> \(\le size(n_i)/2^{logs^\prime_\#-\lfloor lgi\rfloor}+1\)

Applying the size bounds for _n<sub>i</sub>_ in (A.2), we obtain

\(size(n_\text{leaf})\le\left(es_\#/2^{\lfloor lgi\rfloor}\right)/2^{logs^\prime_\#-\lfloor lgi\rfloor}+1\)<br> \(\le es_\#/2^{logs^\prime_\#}+1\)

