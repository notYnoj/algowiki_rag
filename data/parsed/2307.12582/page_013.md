_Proof._ If \(|W|\unknown 4c_Aw_\mathrm{max}^{1/2}\mathrm{log}w_\mathrm{max}\), our \(\widetilde{O}(n+|W|w_\mathrm{max})\) algorithm in the previous subsection already runs in \(\widetilde{O}(n+w_\mathrm{max}^{3/2})\) time. It remains to consider the case when \(|W|\unknown 4c_Aw_\mathrm{max}^{1/2}\mathrm{log}w_\mathrm{max}\).

If \(t\unknown\Sigma_\mathcal{I}/2\), we let \(t'=\Sigma_\mathcal{I}-t\). It is straightforward that the instance (I_,t_) is equivalent to the instance \((\mathcal{I},t')\) and that \(t'\unknown\Sigma_\mathcal{I}/2\). If \(t<2c_Aw_\mathrm{max}^{3/2}\mathrm{log}w_\mathrm{max}\), the \(\widetilde{O}(n+t)\)-time algorithm already runs in \(\widetilde{O}(n+w_\mathrm{max}^{3/2})\) time.

We will use our technique developed for Knapsack to deal with Subset Sum. Like Knapsack, this whole subsection is divided into two parts: the structural part and the algorithm part. In the structural part, we will conceptually take the given instance as a special Knapsack instance, and transform it into a 0-1 Subset Sum instance. This allows us to carry over the proximity results from Knapsack. In the algorithm part, we take the original instance and show that it is possible to leverage the proximity results to design our algorithm without involving the instance transformation.

## 6.2.1 The structural part

In this part, we conceptually view Bounded Subset Sum as a 0-1 Knapsack. Recall that our Knapsack algorithm starts with a greedy solution. For Subset Sum, every item has the same efficiency, which means we may construct a greedy solution with respect to any order of items. For technical reasons, however, we need to start with a special greedy solution **g**. Towards this, we will first define item sets I<sub>2</sub> and I<sub>3</sub>, use them to define **g**, and then use **g** to further define item sets I<sub>1</sub> and I<sub>4</sub>. These four sets will be treated in a similar way as we treat I<sub>1</sub> to I<sub>4</sub> in Knapsack.

Let _W_ be the set of all item weights. Let

• _W_<sub>2</sub> be the set of the largest \(2c_Aw_\mathrm{max}^{1/2}\mathrm{log}w_\mathrm{max}\) weights in _W_;<tbc>

• _W_<sub>3</sub> be the set of the smallest \(2c_Aw_\mathrm{max}^{1/2}\mathrm{log}w_\mathrm{max}\) weights in _W_.

Clearly, \(W_2\cap W_3=\emptyset\). For each _w_ in _W_<sub>2</sub>, we put an arbitrary item of weight _w_ into I<sub>2</sub>. For each _w_ in _W_<sub>3</sub>, we put an arbitrary item of weight _w_ into I<sub>3</sub>. The following statements hold.

(i) the total weight of items in I<sub>2</sub> is at most \(2c_Aw_\mathrm{max}^{3/2}\mathrm{log}w_\mathrm{max}\unknown t\).<tbc>

(ii) the total weight of items not in I<sub>3</sub> is at least \(\Sigma_\mathcal{I}/2\unknown t\).

Let **g** be an arbitrary maximal solution such that **g** selects every item in I<sub>2</sub> but no item in I<sub>3</sub>. In the algorithm part, we shall construct such a solution **g**.

Assuming **g**, let I<sub>1</sub>=**g**(I)\\I<sub>2</sub>, and let I<sub>4</sub>=<o>**g**</o>(I)\\I<sub>3</sub>. We relabel the items so that for any _i\<j_, every item in I_<sub>i</sub>_ has smaller index than any item in I_<sub>j</sub>_.

Recall that Subset Sum is a decision problem. Since we treat it as a special Knapsack problem, we define its optimal solution as the solution that returns a subset-sum \(t^*\unknown t\) and is closest to _t_. In particular, if the answer to Subset Sum is "yes", then _t_<sup>∗</sup>=_t_. Let **z** be the optimal solution with the largest lexicographical order. That is, **z** always prefers items with smaller indices. We have the following fine-grained proximity between **g** and **z**.

Lemma 6.4. \(\Delta(\mathcal{I})=\sum_{i\in\mathcal{I}}w_i|g_i-z_i|\unknown(4c_A+2c_B)w_\mathrm{max}^{3/2}\mathrm{log}w_\mathrm{max}\).

_Proof._ Note that \(\Delta(\mathcal{I})=\sum_{i=1}^4\Delta(\mathcal{I}_i)\). It is obvious that \(\Delta(\mathcal{I}_2)+\Delta(\mathcal{I}_3)\) is at most \(4c_Aw_\mathrm{max}^{3/2}\mathrm{log}w_\mathrm{max}\) since the total weight of items in \(\mathcal{I}_2\cup\mathcal{I}_3\) is bounded by this amount. Next we show that \(\Delta(\mathcal{I}_1)\unknown c_Bw_\mathrm{max}^{3/2}\). \(\Delta(\mathcal{I}_4)\) can be proved similarly due to symmetry.

Suppose, for the sake of contradiction, that \(\Delta(\mathcal{I}_1)>c_Bw_\mathrm{max}^{3/2}\). As in the proof of Lemma 4.1, we can show that either there is a subset D of <o>**z**</o>(I<sub>1</sub>) and a subset Z of **z**(I<sub>2</sub>) such that D and Z have the same total weight, or there is a subset D of <o>**z**</o>(I<sub>2</sub>) and a subset A of \(\mathbf{z}(\mathcal{I}_3\cup\mathcal{I}_4)\) such that D and A have the same total weight. Note that in Subset Sum, every item has the same efficiency of 1. In the former case, \(\hat{\mathbf{z}}=(\mathbf{z}\backslash\mathcal{Z})\cup\mathcal{D}\) is an optimal solution whose lexicographical order is larger than **z**. In the latter case, \(\hat{\mathbf{z}}=(\mathbf{z}\backslash\mathcal{A})\cup\mathcal{D}\) is an optimal solution whose lexicographical order is larger than **z**. Both contradict our choice of **z**.

