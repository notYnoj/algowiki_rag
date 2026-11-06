When necessary we further denote by \(w_\ell^{(j)}\) the number of accesses to \(\ell\) during the first _j_ accesses. Thus \(W^{(t)}=\sum_\ell w_\ell^{(t)}=t\).

## Relation Between Static and Dynamic Optimal Trees.

Consider an optimal static binary search tree for a sequence of _W_ accesses to _n_ elements. As previously noted, the average cost of such a tree is at most _H_+2 where _H_ is the entropy of the access sequence.

**Lemma 1** _Let_ \(a_1,a_2,\dots,a_W\) _with_ \(a_i\in\{1,2,\dots,n\}\) _be a length W_ access sequence _on the elements, i.e., element e<sub>a<sub>t</sub></sub> is accessed at time t. Let H be the entropy corresponding to the full access sequence. Then_

\(\sum_{t=1}^Wlog\frac{t}{max\left(w_{a_t}^{(t-1)},1\right)}\le W\cdot H+2W.\)

The proof of this Lemma is straightforward and is therefore deferred to the Appendix.

Suppose that we could build a tree _T_<sup>(_t_)</sup> such that the depth of _e<sub>i</sub> after_ access _t_ is \(d_i^{(t)}\le log\frac{t}{w_i^{(t)}}+c\). The access of _a<sub>t</sub>_ at time _t_ would be in the previous tree _T_<sup>(_t_-1)</sup> with cost \(d_{a_t}^{(t-1)}\). The only exception to the above is if time _t_ is the first access to _e<sub>a<sub>t</sub></sub>_, so it was not already in _T_<sup>(_t_-1)</sup>. In that case the access cost would be \(d_{a_t}^{(t)}\), the depth of the location into which \(a_i^t\) would be inserted. Thus define \(d_{a_t}^{(t-1)}=d_{a_t}^{(t)}\). Since \(w_{a_t}^{(t-1)}=0\) and \(w_{a_t}^{(t)}=1\), \(d_{a_t}^{(t-1)}=d_{a_t}^{(t)}\le logt+c=log\frac{t}{max\left(w_{a_t}^{(t-1)},1\right)}+c\). The total cost of the accesses would then, from Lemma 1, be

\(\sum_id_{a_t}^{(t-1)}\le W\cdot H+(2+c)W,\)

i.e, within a constant additive error of optimal per access, where optimal defined as the cost with the static optimal tree, is lower-bounded by \(W\cdot H\).

Our approach to building almost optimal trees is therefore to maintain such trees _T_<sup>(_t_)</sup> over the access sequences.

## Our Results.

Let \(f\ge 1\) be any fixed integer. In this paper we describe a dynamic tree structure that can be maintained under access operations and insertions. The depth of the leaf that holds _e<sub>i</sub>_ is bounded by min(log(_W/w<sub>i</sub>),_log_n_)+_O(f_) where _w<sub>i</sub>_ is the number of times _e<sub>i</sub>_ was accessed so far and _W_ is the total length of the access sequence. Hence we can access any element _e<sub>i</sub>_ using at most min(log_n,_log(_W/w<sub>i</sub>_))+_O_(1) comparisons. We can also insert new elements into the tree. When an element is accessed (resp. when a new element is inserted), only _O_(log<sup>(_f_)</sup>_n_) worst-case time will be needed to update the tree; this update procedure does not require any comparisons. Thus our data structure enjoys the advantages of both the weighted alphabetic tree and the perfect binary tree. At the same time, the cost of maintaining the data structure is low.

This result is obtained by a combination of two ideas. First, our construction is based on approximate weights of elements instead of exact weights. Second, we maintain an unweighted binary tree _T_<sup>S</sup> with leaves "representing" approximate weights. Our dynamic tree is a subtree of _T_<sup>S</sup>. We define the approximate weights in Section 3 and describe the tree _T_<sup>S</sup> in Section 4. Next, we show how updates of our data structure can be implemented by leaf insertions in _T_<sup>S</sup> in Section 5. We reduce the update cost and make all time bounds worst-case in Sections 6 and 7 respectively.

