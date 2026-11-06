## 6 Hardness Amplification for Dynamic Binary Search Trees

was _accessed most recently_. Since each "preferred path" has length \(|p|\le\mathrm{depth}(\mathcal{T})\le\mathrm{log}n\), every _path_ can itself be stored in a BST, so assuming these paths can be dynamically maintained (under split and joins), searching for the predecessor of a key _x<sub>i</sub> inside_ each path only takes _O_(loglog_n_) time, until the search "falls-off" the current preferred path and switches to a different one. The key observation is that this "switch" can be charged to Alt<sub>T</sub>(_X_), as it certifies a new alternation in Wilber’s lower bound, hence OPT must pay for this move as well. This elegant argument directly leads to the aforementioned \(O(\mathrm{loglog}n)\cdot\mathsf{OPT}(X)\) search time.

The analysis of Tango trees relies on charging the algorithm’s cost to the Alternation bound. One may ask if the bound can be improved using a clever algorithm (not necessarily Tango trees) so that we can charge _o_(loglog_n_) factor to the Alternation bound. Unfortunately, the answer is no as there are known examples of access sequences \(\tilde{X}\) with \(\mathsf{Alt}(\tilde{X})=O(m)\) but \(\mathsf{OPT}(\tilde{X})=\Theta(m\mathrm{loglog}n)\) [27, 6]. In light of this, Tango trees are indeed off by a factor \(\Theta(\mathrm{loglog}n)\) from \(\mathsf{Alt}(\tilde{X})\). Interestingly, when \(\mathsf{OPT}(X)\unknown m\frac{\mathrm{log}n}{2^{o(\mathrm{loglog}n)}}\) , one can do somewhat better. Let <o>OPT</o>(_X_):=OPT(_X)/|X_|. The Tango tree, presented by [16] (see the discussion in their Section 1.5), has a competitive ratio of

\(O\big(1+\mathrm{log}\frac{\mathrm{log}n}{\mathsf{OPT}(X)}\big)=o(\mathrm{loglog}n).\) (3)

The condition that allows _o_(loglog_n_)-competitiveness is rather narrow: the amortized optimal cost <o>OPT</o>(_X_) must be very close to log_n_ to achieve _o_(loglog_n_)-competitiveness. Can we achieve _o_(loglog_n_)-competitiveness with a wider range of <o>OPT</o>(_X_) using Alt(_X_)?

Unfortunately, the answer is no. More generally, we prove a matching lower bound: the competitive ratio of any BST algorithm based on the Alternation bound must be at least \(\Omega(\mathrm{log}\frac{\mathrm{log}n}{\mathsf{OPT}(X)})\), matching to the upper bound of the Tango tree by Equation (3). More precisely, we prove the following theorem whose proof is a small modification of the proof in Theorem 3.

\(\blacktriangleright\) **Theorem 5.** _Let_ \(\alpha:\mathbb{N}\times\mathbb{R}_{\ge 1}\rightarrow\mathbb{R}_{\ge 1}\) _be any function such that some BST algorithm achieves an amortized cost of_ \(\alpha\big(n,\overline{\mathsf{OPT}}(X)\big)\cdot\big(\overline{\mathsf{Alt}}(X)+1\big)\) _for all access sequences X over n keys. Then_ \(\alpha(n,s)\ge\Omega\big(\mathrm{log}\big(\frac{\mathrm{log}n}{s}\big)\big)\).

As a corollary of Theorem 5,<sup>4</sup> the lower bound of \(\Omega(\mathrm{log}\frac{\mathrm{log}n}{\mathsf{OPT}(X)})\) follows by setting _s_ to be within constant factor of <o>OPT</o>(_X_). This holds for every BST algorithm based on the Alternation bound. With the matching upper bound by Equation (3), Tango tree optimally utilizes the Alternation bound.

### 1.2 Further Related Work

Splay trees and GreedyFuture are prime candidates for the dynamic optimality conjecture since they both satisfy many important properties of dynamic trees including static optimality [40], working-set property [40, 19], dynamic finger property [14, 12], and more (see the surveys [22, 25] for an overview of the results in the field). Although they are not yet known

<sup>4</sup> We remark that we cannot set \(\beta(n)=\overline{\mathsf{OPT}}(X)\) in Theorem 3 because \(\beta(n)\) does not depend on _X_ and, even if <o>OPT</o>(_X_) is a function of _n_, the construction of the sequence _X_ depends on \(\beta(n)\). We need the lower bound of Theorem 5.

