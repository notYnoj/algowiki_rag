**Definition 2.8** (Min-Plus Convolution Listing)**.** Given two sequences \(A,B\in\mathbb{Z}^{[0,n]}\), and an integer threshold _t_, list _t_ witnesses (_i,j_) where _A_\[_i_\]+_B_\[_j_\]=(_A∗B_)\[_k_\] for every _k_. If there are fewer than _t_ witnesses for certain indices _k_, list all the witnesses for these indices.

Similar as before, we use MPConvList(_n,t_) and \(\text{MPConvList}(n,t|u\le U)\) to denote the running times. A subinstance of Min-Plus Convolution (and all sequence problems considered in this paper) can be obtained by setting some entries to \(\perp\), a value that cannot be involved in any solution.

**Definition 2.9** (Bounded-Monotone Min-Plus Convolution)**.** Given two sequences \(A,B\in\mathbb{Z}^{[0,n]}\) where _B_ is monotonically nondecreasing and has entries in \[_O(n_)\], compute _A∗B_.

**Definition 2.10** (Min-Max Convolution)**.** Given two sequences \(A,B\in\mathbb{Z}^{[0,n]}\), compute a sequence \(C=\text{Min-Max}(A,B)\in\mathbb{Z}^{[0,2n]}\), where _C_\[_k_\]=min<sub>_i+j=k_</sub>max{_A_\[_i_\]_,B_\[_j_\]}.

**Definition 2.11** (Min-Equality Convolution)**.** Given two sequences \(A,B\in\mathbb{Z}^{[0,n]}\), compute a sequence \(C=\text{Min-Equal}(A,B)\in\mathbb{Z}^{[0,2n]}\), where _C_\[_k_\]=min<sub>_i+j=k,A_\[_i_\]=_B_\[_j_\]</sub>_A_\[_i_\].

**Definition 2.12** (Min-Witness Convolution)**.** Given two Boolean sequences \(A,B\in\{0,1\}^{[0,n]}\), compute a sequence \(C=\text{Min-Witness}(A,B)\in(\mathbb{Z}\cup\{\perp\})^{[0,2n]}\), where \(C[k]=min\{i\in[0,n]:k-i\in[0,n]\wedge A[i]=B[k-i]=1\}\) (if no such _i_ exists, define \(C[k]=\perp\)).

We now define the index set of a sequence. We will frequently use this notion to convert Min-Plus Convolution instances to 3SUM instances.

**Definition 2.13** (Index set \(\mathcal{I}(\cdot)\))**.** For a sequence \(A\in\mathbb{Z}^{[0,n]}\) indexed by integers in \[0_,n_\], the _index set_ of _A_ is \(\mathcal{I}(A)=\{(i,A[i]):i\in[0,n]\}\).

More generally, for a sequence \(A\in(\mathbb{Z}\cup\{\perp\})^{[0,n]}\), the index set of _A_ is \(\mathcal{I}(A)=\{(i,A[i]):i\in[0,n],A[i]\neq\perp\}\).

## 2.3 Reduction from Listing to Non-Listing Problems

For most problems considered in this paper, one can use an algorithm for the non-listing version of a problem to list witnesses, via a standard approach based on sampling and parallel binary search (e.g., \[AGMN92, Sei95\]). This is summarized in the following lemma.

**Lemma 2.14** (Listing Witnesses for Convolution Problems)**.** _Any Min-Plus Convolution Listing instance_ (_A,B_) _with threshold t can be reduced to t_(log_n_)<sup>_O_(1)</sup> _Min-Plus Convolution (non-Listing) subinstances. The reduction runs in time_ \(\widetilde{O}(nt)\)_. In particular,_

\(\text{MPConvList}(n,t|u)\le\widetilde{O}(t\cdot\text{MPConv}(n|u)).\)

_Moreover, for any_ \(t_1,t_2\ge 1\),

\(\text{MPConvList}(n,t_1t_2|u)\le\widetilde{O}(t_1\cdot\text{MPConvList}(n,t_2|u)).\)

_The same statements also hold with "Min-Plus" replaced by "Min-Max" and "Min-Equality"._

