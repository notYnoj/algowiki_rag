As long as \(\eta\le 1/2\), it holds that either \(a_<\ge\eta a\) or \(a_>\ge\eta a\), and either \(b_<\ge\eta b\) or \(b_>\ge\eta b\). Distributing the "and" over the "or", we obtain the four cases we considered, which are therefore exhaustive. We conclude that (13) holds for \(C'=4^{3/2}C\) whenever \(a\doteq|A|\ge 1\) and \(b\doteq|B|\ge 1\).

In the case where _a_=0 and \(b\ge 1\), the right-hand side of (9) vanishes, as do |_A<sub>\<</sub>_| and |_A<sub>\></sub>_|, so (9) holds if and only if |_B<sub>\<</sub>_|=|_B<sub>\></sub>_|, or equivalently, the leaf \(\ell_\mathrm{hi}\) is ranked exactly in the middle of the leaf set _L_<sub>hi</sub>. As the ranking \(\rho\) is chosen uniformly at random, this happens with probability 1/(_b_+1) where \(b\doteq|B|=|L_\mathrm{hi}|-1\). The case where \(a\ge 1\) and _b_=0 is symmetric. The remaining case, _a=b_=0, is one we do not need to consider as the tree _T_ then only has two leaves. In all other cases we obtain a strong upper bound on the probability that (9) holds, and by complementation a strong lower bound on the root sensitivity. We capture the lower bound in the following single expression that holds for all cases under consideration.

**Lemma 35.** _There exists a constant c such that for every binary tree T with at leaves 3 leaves and a root of degree 2, the root sensitivity of T is at least_

\(1-\frac{c}{\sqrt{n_1n_2(n_1+n_2)}},\) (14)

_where n_<sub>1</sub> _and n_<sub>2</sub> _denote the number of leaves in the subtrees rooted by the two children of the root._

## 5.3 Average sensitivity

We are now ready to establish that, except for trivial cases, the average sensitivity of a binary tree is close to maximal. The trivial cases are those where the tree has at most two leaves, in which case the sensitivity is zero.

**Lemma 36.** _The average sensitivity of_ \(\Pi_T\) _for binary trees T with_ \(n\ge 2\) _leaves is n-O_(1).

_Proof._ We use the expression (10) for the average sensitivity of \(\Pi_T\), where _v_ ranges over all nodes of degree 2 such that _T<sub>v</sub>_ contains as least two leaves. Consider a node _v_ of degree 2 such that _T<sub>v</sub>_ contains _n_<sub>_v,_1</sub> leaves one one side and _n_<sub>_v,_2</sub> leaves on the other side, where \(n_{v,1}+n_{v,2}\ge 3\). If we choose the ranking \(\rho\) and the adjacent-rank transposition \(\tau\) uniformly at random, each of the \(\genfrac(){pt}{2}{n}{2}\) pairs of leaves are equally likely to be the affected pair. As there are \(n_{v,1}\cdot n_{v,2}\) choices that result in _v_ as their lowest common ancestor, we have that \(\mathbb{P}[v=\mathrm{LCA}(\ell_\mathrm{lo},\ell_\mathrm{hi})]=\frac{2n_{v,1}n_{v,2}}{n(n-1)}\) . Combining this with the root sensitivity lower bound given by (14), we have that

\(s(\Pi_T)\ge(n-1)\sum_v\frac{2n_{v,1}n_{v,2}}{n(n-1)}\cdot\left(1-\frac{c}{\sqrt{n_{v,1}n_{v,2}(n_{v,1}+n_{v,2})}}\right)\)<br>
\(=(n-1)-\frac{2c}{n}\sum_v\sqrt{\frac{n_{v,1}n_{v,2}}{n_{v,1}+n_{v,2}}}.\)

The following claim then completes the proof.

**Claim 37.** _There is a constant_ \(c'\) _such that for all binary trees T with n leaves_

\(\sum_v\sqrt{\frac{n_{v,1}n_{v,2}}{n_{v,1}+n_{v,2}}}\le c'n,\) (15)

_where the sum ranges over all nodes v of degree 2 such that T<sub>v</sub> contains at least 3 leaves._

