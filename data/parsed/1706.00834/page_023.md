<tbc>set \(M_{(i,j)}^{(\mathrm{out})}\) consists of (_j-i_) many multiedges. The _k_th multiedge leaving (_i,j_) is comprised of 2 edges going from the node (_i,j_) to the nodes (_i,k_) and (_k_+1_,j_). The loss of the _k_th multiedge is _d_<sub>_i_-1</sub>_d<sub>k</sub>d<sub>j</sub>_. Figure 5 illustrates the multi-DAG and multipaths associated with matrix chain multiplications.

Since the above recurrence relation correctly solves the offline optimization problem, every multipath in the multi-DAG represents a full parenthesization, and every possible full parenthesization can be represented by a multipath of the multi-DAG. We have |_M_|=_O(n_<sup>3</sup>) multiedges which are the components of our new representation. Assuming that all dimensions _d<sub>i</sub>_ are bounded as _d<sub>i</sub>\<d_<sub>max</sub> for some _d_<sub>max</sub>, the loss associated with each multiedge is upper-bounded by (_d_<sub>max</sub>)<sup>3</sup>. Most crucially, the original number of scalar multiplications in the matrix-chain product is linear in the losses of the multiedges and the unit-flow polytope has _O(n_<sup>3</sup>) facets.

## Regret Bounds.

It is well-known that the number of full parenthesizations of a sequence of _n_ matrices is the _n_th Catalan number (Cormen et al., 2009). Therefore \(\mathcal{N}=\frac{(2n)!}{n!(n+1)!}\in(2^n,4^n)\). Also note that each multipath representing a full parenthesization consists of exactly _D=n_-1 multiedges. Thus, incorporating (_d_<sub>max</sub>)<sup>3</sup> as the loss range for each com ponent and using Theorem 10, EH achieves a regret bound of \(\mathcal{O}(n\left(d_\mathrm{max}\right)^\frac{3}{2}\sqrt{L^*})\). Moreover, since |_M_|=_O(n_<sup>3</sup>), using Theorem 14 and considering (_d_<sub>max</sub>)<sup>3</sup> as the loss range for each component , CH achieves a regret bound of \(\mathcal{O}(n^\frac{1}{2}\left(\mathrm{log}n\right)^\frac{1}{2}\left(d_\mathrm{max}\right)^\frac{3}{2}\sqrt{L^*})\).

## 5.3 Knapsack

Consider the online version of the _knapsack_ problem (Kleinberg and Tardos, 2006): We are given a set of _n_ items along with the _capacity_ of the knapsack \(C\in\mathbb{N}\). For each item \(i\in\{1..n\}\), a _heaviness_ \(h_i\in\mathbb{N}\) is associated. In each trial, the algorithm predicts with a _packing_ which is a subset of items whose total heaviness is at most the capacity of the knapsack. After the prediction of the algorithm, the adversary reveals the profit of each<tbc>

S
(1,4)
(2,4)
(3,4)
(4,4)
(1,3)
(2,3)
(3,3)
(1,2)
(2,2)
T
(1,1)

Figure 5: Given a chain of _n_=4 matrices, the multipath associated with the full parenthesization (_A_<sub>1</sub>((_A_<sub>2</sub>_A_<sub>3</sub>)_A_<sub>4</sub>)) is depicted in blue.

