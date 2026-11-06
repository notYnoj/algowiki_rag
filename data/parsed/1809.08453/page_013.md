\- The non-increasing weights of the GGI are defined as follows:

\(\lambda=\underbrace{(n_c^{n_c+1},n_c^{n_c},n_c^{n_c},n_c^{n_c-1},\dots,n_c^3,n_c^2,n_c^2,n_c^1}_{2n_c\text{weights}},\underbrace{0,\dots,0}_{6n_c\text{weights}}).\)

We recall that the 2_n<sub>c</sub>_ agents with the highest disutility values are the decisive agents (the two decisive agents of clause _c<sub>j</sub>_ are matched with an agent of rank 2_j_+1 or 2_j_+2) and the 6_n<sub>c</sub>_ agents with the lowest disutility values are the _non_-decisive agents (who are matched to one of their two first choices). Consequently, the weight vector \(\lambda\) attributes a weight 0 in the GGI operator to the 6_n<sub>c</sub>_ non-decisive agents while, for each clause _c<sub>j</sub>_, it attributes a weight \(n_c^j\) (resp. \(n_c^{j+1}\)) to the most satisfied (resp. least satisfied) of the two decisive agents of _c<sub>j</sub>_.

An upper bound on the GGI value is given by \(\Delta_u=\sum_{j=1}^{n_c}(n_c^j+n_c^{j+1})d(2j+2)\). This would correspond to a stable marriage, where for each _c<sub>j</sub>_, the two decisive agents of _c<sub>j</sub>_ are both matched to their choice of rank 2_j_+2. Similarly, a lower bound on the GGI value is given by \(\Delta_l=\sum_{j=1}^{n_c}(n_c^j+n_c^{j+1})d(2j+1)\) (if the two decisive agents of _c<sub>j</sub>_ are both matched to their choice of rank 2_j_+1). Simple calculations show that \(\Delta_l=\Delta_u-n_c(1+n_c)\).

These bounds are useful for establishing Lemma 1 below, that makes it possible to infer the number of unsatisfied clauses from the GGI value. The lower the GGI value, the higher the number of unsatisfied clauses. Hence, minimizing the GGI value amounts to maximizing the number of unsatisfied clauses, which concludes the proof.

**Lemma 1** _For the GGI stable marriage instance obtained by the method described above, a stable marriage_ **x** _corresponds to a truth assignment on V for which the number of unsatisfied clauses is:_

\(\big\lfloor\frac{\Delta_u-\text{\texttt{GGI}}_\lambda(\mathbf{d}(\mathbf{x}))}{n_c+1}\big\rfloor\)

_Proof of Lemma 1._ We wish to show that if a stable marriage **x** corresponds to a truth assignment on _V_ with exactly _k_ unsatisfied clauses then:

\(\Delta_u-(k+1)(n_c+1)<\text{\texttt{GGI}}_\lambda(\mathbf{d}(\mathbf{x}))\le\Delta_u-k(n_c+1),\)

from which the lemma straightforwardly follows.

Assume that _k_ clauses {_c_<sub>_j_<sub>1</sub></sub>_,...,c<sub>j<sub>k</sub></sub>_} are unsatisfied for the truth assignment induced by **x**. Then for each _c<sub>j<sub>l</sub></sub>_, the two decisive agents of _c<sub>j<sub>l</sub></sub>_ are both matched to their choice of rank 2_j<sub>l</sub>_+1. Hence:

\(\text{\texttt{GGI}}_\lambda(\mathbf{d}(\mathbf{x}))\le\Delta_u-\sum_{l=1}^k(n_c^{j_l}+n_c^{j_l+1})(d(2j_l+2)-d(2j_l+1))\)<br>
\(=\Delta_u-\sum_{l=1}^k(n_c^{j_l}+n_c^{j_l+1})n_c^{-j_l}=\Delta_u-k(n_c+1)\)

because each decisive agent of clause _c<sub>j<sub>l</sub></sub>_, for \(l\in\{1,\dots,k\}\), has a disutility of _d_(2_j<sub>l</sub>_+1) and not _d_(2_j<sub>l</sub>_+2).

Now, let {_c_<sub>_j_<sub>1</sub></sub>_,...,c_<sub>_j<sub>n<sub>c</sub>-k_</sub></sub>} denote the satisfied clauses for the truth assignment induced by **x**. Then for each _c<sub>j<sub>l</sub></sub>_, at least one of the two decisive agents of _c<sub>j<sub>l</sub></sub>_ is matched to his/her choice of rank 2_j<sub>l</sub>_+2. In the best case (w.r.t. the GGI value), only one of the two is matched

