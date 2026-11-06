However, since \(\mathrm{supp}(\mathbf{x}^\star)\nsubseteq S[z^\star]\), we know \(\mathrm{supp}(\mathbf{x}^\star+\bar{\mathbf{x}}_{V^\prime})\nsubseteq S[z^\star]\), and hence it violates the support containment condition in \(K|_{V\cup V^\prime}\), contradicting our assumption that all maximizers to index _i_ in instance \(K|_{V\cup V^\prime}\) satisfy the support containment condition.

Hence we have established that _r_\[_i<sub>V</sub>_\]=_r<sub>V</sub>_ must hold.

Now we look at the second instance, \(K^{(V\leftarrow Y_V)}|_{V^\prime}=\left(V',\{Q_w\}_{w\in V^\prime},S'[],q'[]\right)\). Note that we have \(q'[i_V]=r[i_V]=r_V\) by definition. Hence, \((\bar{\mathbf{x}}_{V^\prime},i_V,\bar{r})\) should be a valid solution for index _i_ in instance \(K^{(V\leftarrow Y_V)}|_{V^\prime}\), with objective value

\(q'[i_V]+\sum_{w\in V^\prime} Q_w(\bar{x}_w)=r_V+\sum_{w\in V^\prime} Q_w(\bar{x}_w)=\bar{r}.\)

Now we claim that \(r'[i]=\bar{r}\) (recall that \(r'[\cdot]\) denotes objective values achieved by the solution \(Y_{V^\prime}\)) must hold. Otherwise, by the definition of the HintedKnapsackExtend<sup>+</sup> instance \(K^{(V\leftarrow Y_V)}|_{V^\prime}\), there can only be two possibilities:

• Case 1: \((\bar{\mathbf{x}}_{V^\prime},i_V,\bar{r})\) is not a maximizer solution for index _i_ in \(K^{(V\leftarrow Y_V)}|_{V^\prime}\).<tbc>

<tbc>This means there is some solution (**_x_**<sup>∗</sup>_,z_<sup>∗</sup>_,r_<sup>∗</sup>) for index _i_ in \(K^{(V\leftarrow Y_V)}|_{V^\prime}\) that achieves a higher objective \(r^*>\bar{r}\). Then, in instance \(K|_{V\cup V^\prime}\), the solution \((\mathbf{x}^*+\mathbf{x}[z^*],z[z^*])\) has total weight \(z[z^*]+\sum_{w\in V}w\cdot x[z^*]_w+\sum_{w\in V^\prime} w\cdot x_w^*=z^*+\sum_{w\in V^\prime} w\cdot x_w^*=i\) and total objective value \(q[z[z^*]]+\sum_{w\in V}Q_w(x[z^*]_w)+\sum_{w\in V^\prime} Q_w(x_w^*)=r[z^*]+\sum_{w\in V^\prime} Q_w(x_w^*)=q'[z^*]+\sum_{w\in V^\prime} Q_w(x_w^*)=r^*>\bar{r}\), contradicting the assumption that \((\bar{\mathbf{x}},\bar{z})\) is a maximizer for _i_ in instance \(K|_{V\cup V^\prime}\).<tbc>

• Case 2: \((\bar{\mathbf{x}}_{V^\prime},i_V,\bar{r})\) is a maximizer solution for index _i_ in \(K^{(V\leftarrow Y_V)}|_{V^\prime}\), but there is another maximizer solution \((\mathbf{x}^*,z^*,\bar{r})\) for index _i_ in \(K^{(V\leftarrow Y_V)}|_{V^\prime}\) that does not satisfy the support containment condition \(\mathrm{supp}(\mathbf{x}^*)\subseteq S'[z^*]\).<tbc>

<tbc>Similar to Case 1, we again consider the solution (**_x_**<sup>∗</sup>+**_x_**\[_z_<sup>∗</sup>\]_,z_\[_z_<sup>∗</sup>\]) in instance \(K|_{V\cup V^\prime}\), which has total weight _i_ and total objective value \(\bar{r}\). So it is an alternative maximizer to index _i_ in instance \(K|_{V\cup V^\prime}\). Since \(S'[z^*]=S[z[z^*]]\backslash V\) by definition (Eq. (20)), we have \(\mathrm{supp}(\mathbf{x}^*)\nsubseteq S'[z^*]=S[z[z^*]]\backslash V\) , which means \(\mathrm{supp}(\mathbf{x}^*)\nsubseteq S[z[z^*]]\), and thus \(\mathrm{supp}(\mathbf{x}^*+\mathbf{x}[z^*])\nsubseteq S[z[z^*]]\). This contradicts our assumption that all maximizers to index _i_ in instance \(K|_{V\cup V^\prime}\) satisfy the support containment condition.

Hence, we must have \(r'[i]=\bar{r}\). This means that we indeed have found a maximizer to index _i_ after we compose the solutions _Y<sub>V</sub>_ and \(Y_{V^\prime}\). So our solution for index _i_ is actually correct for the instance \(K|_{V\cup V^\prime}\). This finishes the proof that \(Y_{V^\prime}\circ Y_V\) correctly solves \(K|_{V\cup V^\prime}\).

Lemma 4.5 allows us to decompose an instance by partitioning the set \(U\subseteq[w_\mathrm{max}]\). In addition to this, we also need another way to decompose an instance, which in some sense allows us to partition the array indices \[-_L...L_\]. First, we define the entry-wise maximum of two instances.

**Definition 4.6** (Entry-wise maximum)**.** Given HintedKnapsackExtend<sup>+</sup> instances \(K=\left(U,\{Q_w\}_{w\in U},S[],q[]\right)\) and \(K'=\left(U,\{Q_w\}_{w\in U},S'[],q'[]\right)\), we define the following instance,<tbc>

\(\left(U,\{Q_w\}_{w\in U},S''[],q''[]\right),\)

