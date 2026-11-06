<tbc>_w<sub>i</sub> times over a sequence of W operations, then the depth of the leaf holding e<sub>i</sub> does not exceed_ min(log(_W/w<sub>i</sub>),_log_n_)+_O_(1).

The result of Lemma 4 can be further improved by bootstrapping. For any integer \(f\ge 1\) the following statement can be proved.

**Lemma 5** _Suppose there exists a binary search tree T<sup>f</sup>, such that (1) the depth of a leaf holding an element e<sub>i</sub> in T<sup>f</sup> does not exceed_ min(log(_W/w<sub>i</sub>),_log_n_)+_O_(1)+_O(f_) _(2) the amortized cost of updating T<sup>f</sup> after an element access or an insertion is O_((log<sup>(_f_)</sup>_n_)<sup>2</sup>)_. Then there is a binary search tree T_<sup>_f_+1</sup>_, such that (1) the depth of a leaf holding an element e<sub>i</sub> in T_<sup>_f_+1</sup> _does not exceed_ min(log(_W/w<sub>i</sub>),_log_n_)+_O_(1)+_O(f_+1) _(2) the amortized cost of updating T_<sup>_f_+1</sup> _after an element access or an insertion is O_((log<sup>(_f_+1)</sup>_n_)<sup>2</sup>).

_Proof_: We divide the tree _T_<sup>S</sup> into the macro-tree and mini-trees in the same way as in the proof of Lemma 4. Every mini-tree is implemented using the tree _T<sup>f</sup>_. Hence each mini-tree can be updated in _O_((log<sup>(_f_)</sup>(log_n_))<sup>2</sup>)=_O_((log<sup>(_f_+1)</sup>_n_)<sup>2</sup>) time. The amortized cost of maintaining the macro-tree is _O_(1). Hence the total amortized cost of updates is _O_((log<sup>(_f_+1)</sup>_n_)<sup>2</sup>).

Suppose that \(\varepsilon_i\) is stored in the macro-tree. The depth of a node \(\varepsilon_i\) in the macro-tree is bounded by \(\mathrm{log}(\mathrm{min}(W'/w'_i,n))+O(1)\). Now suppose that \(\varepsilon_i\) is stored in some mini-tree. The depth of \(\varepsilon_i\) in the mini-tree is bounded by \(\mathrm{log}(\mathrm{min}(W'_g/w'_i,n_i))+O(f)+O(1)\), where \(W'_g\) is the total sum of all quantized weights in the mini-tree and _n<sub>g</sub>_ is the total number of elements in the subtree. By the same argument as in Lemma 4, the depth of \(\varepsilon_i\) in _T_ is bounded by \(\mathrm{log}(\mathrm{min}(W'/w'_i,n))+O(f+1)+O(1)\).

Our main result is obtained when we apply Lemma 5 _f_+1 times for a parameter \(f\ge 0\).

**Theorem 1** _For any_ \(f\ge 1\) _there exists a binary search tree T<sup>f</sup>, such that the depth of a leaf holding an element e<sub>i</sub> in T<sup>f</sup> does not exceed_ min(log(_W/w<sub>i</sub>),_log_n_)+_O(f_) _and the amortized cost of updating T<sup>f</sup> after an element access or an insertion is O_(log<sup>(_f_)</sup>_n+f)._

We remark that when we insert a new element _e<sub>i</sub>_, we need to update the search path for one leaf. This may incur an additional cost of log_n+O_(1) operations.

Our data structure can also support two symmetric operations. We can decrement the weight of an element and delete an element of weight 1. These operations can be implemented in the same way as incrementing the weight of an element and an insertion of a new element.

## 7 Worst-Case Updates

Our construction can be modified to support updates with worst-case time guarantees. We start by showing how the data structure from Section 5 can be changed. We run several processes in the background; these processes adapt the tree structure to the changing value of the parameter \(\tau\) and maintain the correct number of pseudo-leaves for each element _e<sub>i</sub>_. The value of \(\tau\) is changed every time the total weight _W_ for the number of elements is changed by a constant factor (described below). Two background processes guarantee that the value of \(\tau\) used in _T_<sup>S</sup> is within a constant factor of its current value. Moreover pseudo-leaves are stored in a _k_-neighbor tree data structure, but the parameter \(k=\Theta(\mathrm{log}n)\) must be changed when the number of elements is increased or<tbc>

