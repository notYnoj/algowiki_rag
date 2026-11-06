\(w'_i=\left\lceil w_i/\tau\right\rceil\) for \(\tau=\frac{W}{n}\). Thus all approximate weights are integers between 1 and _n_. Note that \(\sum\frac{w_i}{\tau}=\frac{n}{W}\sum_iw_i=n\). Hence \(W'=\sum\left\lceil\frac{w_i}{\tau}\right\rceil\le\sum_i\frac{w_i}{\tau}+n=2n\le 2W\).

**Lemma 2** _Suppose that the depth of a leaf_ \(\ell_i\) _in a tree_ \(T'\) _does not exceed_ \(\mathrm{log}(W'/w'_i)+c\)_. Then the depth of_ \(\ell_i\) _in_ \(T'\) _does not exceed_ min(log(_W/w<sub>i</sub>),_log_n_)+_c_+1.

_Proof_: Since \(w'_i\ge 1\) for all _i_, \(\mathrm{log}(W'/w'_i)\le\mathrm{log}W'\le\mathrm{log}n+1\). Furthermore \(W'\cdot\tau\le 2W\) and \(w'_i\cdot\tau\ge w_i\). Hence \(\frac{W'}{w'_i}=\frac{W'\cdot\tau}{w'_i\cdot\tau}\le\frac{2W}{w_i}\) and \(\mathrm{log}\frac{W'}{w'_i}\le\mathrm{log}\frac{W}{w_i}+1\).

In summary \(\mathrm{log}\frac{W'}{w'_i}\le\mathrm{min}(\mathrm{log}\frac{W}{w_i},\mathrm{log}n)+1\).

Thus the problem of maintaining an almost-optimal tree \(T'\) for quantized weights \(\{w'_1,\dots,w'_n\}\) is equivalent to the problem of maintaining an almost-optimal tree for exact weights {_w_<sub>1</sub>_,...,w<sub>n</sub>_}. The tree \(T'\) has another important property: the depths of all leaves in \(T'\) are bounded by \(\lceil\mathrm{log}n\rceil+O(1)\).

## 4 Warm-Up: Almost-Optimal Static Trees

In this section we introduce our approach and basic notions that will be used in the following sections. By way of introduction we describe a method that produces an almost-optimal tree for a static set of elements with fixed weights.

We keep weights of elements as entries in an array _B_ of size \(m=2W'\le 2n\) so that there are two entries for each unit of weight. The first \(2w'_1\) entries of _B_ are assigned to _e_<sub>1</sub>, the following \(2w'_2\) entries are assigned to _e_<sub>2</sub>, and so on. In general we assign entries _B_\[_l<sub>i</sub>_\]_,...,B_\[_r<sub>i</sub>_\] to the element _e<sub>i</sub>_ where \(l_i=(2\sum_{j=1}^{i-1}w'_i)+1\) and \(r_i=2\sum_{j=1}^iw'_i\). Let _T_<sup>S</sup> denote a conceptual perfectly balanced tree on _B_. The _i_-th leaf of _T_<sup>S</sup> corresponds to the entry _B_\[_i_\] of _B_, every internal node has two children, and the height of _T_ is log_m_=log_n_+1<sup>4</sup>. The leaves of _T_<sup>S</sup> will be called _pseudo-leaves_. Leaves corresponding to entries in _B_\[_l<sub>i</sub>..r<sub>i</sub>_\] will be called _pseudo-leaves of the element e<sub>i</sub>_ (or pseudo-leaves associated to _e<sub>i</sub>_).

<sup>4</sup>To avoid tedious details, we assume in this section that _m_ and _n_ are powers of 2.

E3
E3
E2
E2
E4
E1
E1
E2
E2
E3
E3
E3
E3
E3
E4
E1
E4

Figure 1: Left: Balanced tree of approximate weights \(w'_1=1\), \(w'_2=2\), \(w'_3=4\), and \(w'_4=1\). Elements _e_<sub>1</sub>_,...,e_<sub>4</sub> are stored in nodes \(\varepsilon_1\), ..., \(\varepsilon_4\) respectively. Pseudo-leaves are shown with dashed lines. Internal nodes of _T_<sup>S</sup> that are not nodes of _T_ are also drawn with dashed lines. Leaves of _T_ are shown with solid lines and internal nodes of _T_ are depicted by filled circles. Right: Almost-optimal tree corresponding to the tree on Fig. 1

