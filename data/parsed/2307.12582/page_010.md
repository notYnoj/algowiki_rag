strictly higher average efficiency than Z, or -- if the efficiency is the same -- strictly smaller average weight than Z. In the former case, \(\hat{\mathbf{z}}\) has a larger profit than **z**. In the latter case, |D|_\>_|Z|. Since **g** selects all items in D and Z, it follows that \(\hat{\mathbf{z}}\) is an optimal solution with \(\|\hat{\mathbf{z}}-\mathbf{g}\|_1<\|\mathbf{z}-\mathbf{g}\|_1\). Both cases contradict our choice of **z**.

**Case (ii).** <o>**z**</o>(I<sub>2</sub>) has at least \(c_Aw_\mathrm{max}^{1/2}\mathrm{log}w_\mathrm{max}\) distinct weights. When obtaining **z** from **g**, the total weight of items that are added is exactly \(\Delta(\mathcal{I}_{\unknown b})\), while the total weight of items that are deleted is at least \(\Delta(\mathcal{I}_1^{\overline{W^*}})\). Since the total weight of **z** and **g** differ by at most _w_<sub>max</sub> (they are both maximal solutions), we have the following.

\(\Delta(\mathcal{I}_{\unknown b})\unknown\Delta(\mathcal{I}_1^{\overline{W^*}})-w_\mathrm{max}\unknown(2c_B-1)w_\mathrm{max}^{3/2}\unknown c_Bw_\mathrm{max}^{3/2}.\)

Also note that \(\Delta(\mathcal{I}_{\unknown b})\) is exactly the total weight of items in \(z(\mathcal{I}_{\unknown b})\). Again, the weight multisets of <o>**z**</o>(I<sub>2</sub>) and \(\mathbf{z}(\mathcal{I}_{\unknown b})\) satisfies the conditions of Lemma 3.1. By Lemma 3.1, there is a non-empty subset D of <o>**z**</o>(I<sub>2</sub>) and a non-empty subset Z of \(\mathbf{z}(\mathcal{I}_{\unknown b})\) such that D and Z have the same total weight. Moreover, D is to the left of Z. By an argument similar to that in case (i), we can obtain a solution \(\hat{\mathbf{z}}=(\mathbf{z}\backslash\mathcal{Z})\cup\mathcal{D}\) that is better than **z**, which contradicts with our choice of **z**. This completes the proof.

## 4.2 Algorithmic Part

Lemma 4.2. _In_ \(\widetilde{O}(n)\) _time, we can compute the partition_ (_W_<sup>∗</sup>_,<o>W</o>_<sup>∗</sup>) _of W in Lemma 4.1._

It is easy to see that the process of identifying _W_<sup>∗</sup> in the proof of Lemma 4.1 can be generalized to Bounded Knapsack and can be done in \(\widetilde{O}(n)\) time.

The following theorem directly follows by Lemma 4.2 and Lemma 2.2.

Theorem 4.1. _There is an_ \(\widetilde{O}(n+w_\mathrm{max}^{5/2})\)_-time algorithm for Bounded Knapsack._

## 5 An \(\widetilde{O}(n+w^{12/5})\)-time Algorithm for Knapsack

In the structural part of the \(\widetilde{O}(n+w_\mathrm{max}^{5/2})\)-time algorithm, in order to make the weight multiset of **z**(I<sub>2</sub>) (or <o>**z**</o>(I<sub>2</sub>)) dense, we require that items in it have \(\Theta(w_\mathrm{max}^{1/2}\mathrm{log}w_\mathrm{max})\) distinct weights. The multiplicities of these weights are not considered. In this section, we develop a better proximity result by exploiting the multiplicities of weights, and therefore obtain an algorithm with improved running time. As before, this section is divided into the structural part and the algorithmic part.

### 5.1 Structural Part - Fine-Grained Proximity

As in Subsection 4.1, it suffices to consider 0-1 Knapsack, and the notations defined at the beginning of that subsection will be used.

Lemma 5.1. _There exists a partition of W into W_<sup>∗</sup> _and <o>W</o>_<sup>∗</sup> _such that_

(i) \(|W^*|\unknown 4c_Aw_\mathrm{max}^{3/5}\mathrm{log}w_\mathrm{max}\),<tbc>

(ii) \(\Delta(\mathcal{I}^{\overline{W^*}})\unknown 4c_Bw_\mathrm{max}^{7/5}\),

_where c<sub>A</sub> and c<sub>B</sub> are two large constants used in Lemma 3.1._

Lemma 5.1 does not exploit the multiplicities of weights, and can be proved in exactly the same way as Lemma 4.1. The trade-off between |_W_<sup>∗</sup>| and \(\Delta(\mathcal{I}^{\overline{W^*}})\) essentially results from Lemma 3.1. When |_W_<sup>∗</sup>| is \(\widetilde{\Theta}(w_\mathrm{max}^p)\) for some \(p\unknown 1/2\), \(\Delta(\mathcal{I}^{\overline{W^*}})\) is \(O(w_\mathrm{max}^{2-p})\).

<o>_W_<sup>∗</sup></o> already meets the requirement since \(|\overline{W^*}|\Delta(\mathcal{I}^{\overline{W^*}})\unknown c_Bw_\mathrm{max}^{12/5}\). _W_<sup>∗</sup>, however, may be problematic since \(\Delta(\mathcal{I}^{\overline{W^*}})\) can be as large as \(O(w_\mathrm{max}^2)\). We further partition _W_<sup>∗</sup> into two sets and prove a similar result as before. But this time, we will take advantage of the multiplicities of weights and use Lemma 3.2 instead of Lemma 3.1.

Lemma 5.2. _There exits a partition of W_<sup>∗</sup> _into W_<sup>+</sup> _and <o>W</o>_<sup>+</sup>=_W_<sup>∗</sup>\\_W_<sup>+</sup> _such that_

(i) \(|W^+|\unknown 4c_Aw_\mathrm{max}^{2/5}\mathrm{log}^2w_\mathrm{max}\),<tbc>

(ii) \(\Delta(\mathcal{I}^{\overline{W^+}})\unknown 8c_Bw_\mathrm{max}^{9/5}\),

_where c<sub>A</sub> and c<sub>B</sub> are two large constants used in Lemma 3.2._

