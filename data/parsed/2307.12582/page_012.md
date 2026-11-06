Now we compute \(\hat{S}_1:=\frac{1}{k}(\bar{S}_0-r_0)+S_1\) via FFT, which takes \(c_2\sigma_2log\sigma_2\) time for some constant _c_<sub>2</sub> and \(\sigma_2\le\mathfrak{m}_{S_0}/k+\mathfrak{m}_{S_1}\). It thus remains to determine whether

\(\frac{t-r_0}{k}\in\hat{S}_1+kS_2+\cdots+k^{h-1}S_h.\)

By the induction hypothesis, this takes \(c_1(h-1)\sigma'log\sigma'\) time where \(\sigma'=\mathfrak{m}_{\hat{S}_1}+\mathfrak{m}_{S_2}+\cdots+\mathfrak{m}_{S_h}\le\mathfrak{m}_{S_0}/k+\mathfrak{m}_{S_1}+\cdots+\mathfrak{m}_{S_h}\). Therefore, it is easy to verify that the overall running time is bounded by \(c_2\sigma_2log\sigma_2+c_1(h-1)\sigma'log\sigma'\le c_1h\sigma log\sigma\) when \(c_1\ge c_2\).

## 6.1.2 Item Grouping

We follow a standard idea to bundle item copies into groups. A solution to the grouped instance will take item copies within a group as a whole. Thus, the key point is to show that, after grouping, we do not lose any solution, and thus the optimal solution.

Recall that _u<sub>j</sub>_ refers to the copy number of item _j_. It is obvious that _u<sub>j</sub>_ can be represented as \(u_j[0]+u_j[1]\cdot 2^1+\cdots+u_j[l_j]\cdot 2^{l_j}\) where \(2\le u_j[i]<4\) for all \(0\le i\le\ell_j-1\) and \(u_j[\ell_j]<4\). This can be easily achieved recursively: let _r_ be the residue of _u<sub>j</sub>_ modulo 2; set _u<sub>j</sub>_\[0\]=2+_r_, \(u_j\leftarrow\frac{u_j-(2+r)}{2}\) and repeat the above procedure.

As \(u_j\le 4w_{max}\) for all \(1\le j\le n\), \(\ell_j\le 2+logw_{max}\). For ease of discussion, we let _u<sub>j</sub>_\[_i_\]=0 for \(i>\ell_j\) and \(\ell=max_j\ell_j\). Now we define _X<sub>i</sub>_ as a multiset that consists of exactly _u<sub>j</sub>_\[_i_\] copies of weight _w<sub>j</sub>_ for every _j_, and note that by 2_<sup>i</sup>X<sub>i</sub>_ we mean the multiset that consists of exact _u<sub>j</sub>_\[_i_\] copies of weight 2_<sup>i</sup>w<sub>j</sub>_, which represents a multiset of groups (where each group contains 2_<sup>i</sup>_ copies of weight _w<sub>j</sub>_ but has to be selected as a whole).

Let _X_ denote the multiset where every _w<sub>j</sub>_ occurs _u<sub>j</sub>_ times. Recall that S(_X_) denotes the set of all possible subset-sums of multiset _X_. We show the following in the appendix.

Lemma 6.3.

\(\mathcal{S}(X)=\sum_{i=0}^\ell 2^i\mathcal{S}(X_i)=2^0\mathcal{S}(X_0)+\cdots+2^\ell\mathcal{S}(X_\ell).\)

_That is, for any_ \(t\in\mathcal{S}(X)\)_, there exist_ \(t_i\in\mathcal{S}(X_i)\) _such that_ \(t=\sum_{i=0}^\ell 2^it_i\).

Polak et al. \[26\] derived a similar lemma for \(\ell=2\).

## 6.1.3 Finalizing the \(\widetilde{O}(nw_{max})\)-time algorithm

Now we are ready to present our \(\widetilde{O}(nw_{max})\)-time algorithm. By Observation 6.1, we have \(u_j\le 4w_{max}\). Consequently, for \(\ell=O(logw_{max})\), the given instance can be grouped as \(\cup_{i=0}^\ell 2^iX_i\). Note that _X<sub>i</sub>_ contains at most 4_n_ elements as there are _n_ item weights, and each item has _u<sub>j</sub>_\[_i_\]_\<_4 copies. Our goal is to determine whether \(t\in\mathcal{S}(\cup_{i=0}^\ell 2^iX_i)\) for an arbitrary target value _t_. By Lemma 6.3, it suffices to determine whether \(t\in\sum_{i=0}^\ell 2^i\mathcal{S}(X_i)\). We first compute each S(_X<sub>i</sub>_). This is equivalent to computing sumset \(\sum_{e\in X}\{0,e\}\). According to Lemma 6.1, this can be achieved in \(\widetilde{O}(\sigma_1)\) time, where \(\sigma_1\le 4nw_{max}\). Next, we apply Lemma 6.2 to determine whether \(t\in\sum_{i=0}^\ell 2^i\mathcal{S}(X_i)\), which takes \(\widetilde{O}(\sigma\ell)\) time, where \(\sigma=\sum_{i=0}^\ell\mathfrak{m}_{\mathcal{S}(X_i)}\), where m<sub>S(_X<sub>i</sub>_)</sub> refers to the largest integer in S(_X<sub>i</sub>_), which is bounded by 4_nw_<sub>max</sub>. Consequently, the overall running time is \(\widetilde{O}(\ell^2nw_{max})=\widetilde{O}(nw_{max})\).

Remark 6.1. _We do not require that in the input instance, item weights are distinct. If, however, there are items of the same weight, we can simply merge them and update u<sub>j</sub>’s. After preprocessing, we apply our algorithm. Hence, the running time of our algorithm can also be bounded by_ \(\widetilde{O}(n+|W|w_{max})\) _where W stands for the set of distinct weights._

## 6.2 An \(\widetilde{O}(n+w_{max}^{3/2})\)-time Algorithm for Subset Sum

We present an alternative algorithm for Bounded Subset Sum of running time \(\widetilde{O}(n+w_{max}^{3/2})\). We start with the following observation. Recall that _W_ is the set of all distinct weights.

Observation 6.2. _We may assume without loss of generality that_ \(|W|\ge 4c_Aw_{max}^{1/2}logw_{max}\)_, and_ \(2c_Aw_{max}^{3/2}logw_{max}\le t\le\Sigma_\mathcal{I}/2\).

