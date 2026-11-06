**Fact 1** _Consider a node u of height_ \(h\ge\lfloor\mathrm{log}r\rfloor\) _for some_ \(r\ge 1\)_. Suppose that r leftmost (rightmost) pseudo-leaves in the subtree of u are pseudo-leaves of e<sub>i</sub>. Then there is at least one node v of height_ \(\lfloor\mathrm{log}r\rfloor\) _such that all pseudo-leaves in the subtree of v are pseudo-leaves of e<sub>i</sub>.<br>
Consequentially, if_ 2_x entries are assigned to some element e<sub>i</sub>, then there is at least one node v of height_ \(\lfloor\mathrm{log}x\rfloor\)_, such that all pseudo-leaves in the subtree of v are assigned to e<sub>i</sub>._

We define an almost-optimal tree _T_ as a subtree of _T_<sup>S</sup>. Let \(\varepsilon_i\) denote an arbitrary node of height \(\lfloor\mathrm{log}(w'_i)\rfloor\) such that all leaves in the subtree rooted at \(\varepsilon_i\) are _i_-nodes. Since we assigned \(2w'_i\) pseudoleaves to _e<sub>i</sub>_, such a node \(\varepsilon_i\) always exists. All pseudoleaves below \(\varepsilon_i\) correspond to some array entries in _B_\[_l<sub>i</sub>..r<sub>i</sub>_\]. The tree _T_ is a subtree of _T_<sup>S</sup> pruned at nodes \(\varepsilon_i\). That is, the nodes \(\varepsilon_i\) are the leaves of _T_ and all proper ancestors of all \(\varepsilon_i\) are internal nodes of _T_. We keep keys in the internal nodes of _T_ that can be used for routing.

The depth of the leaf \(\varepsilon_i\) does not exceed \(\mathrm{log}\frac{W'}{w'_i}\) by more than a constant: every leaf of _T_<sup>S</sup> has depth at most \(\mathrm{log}W'+1\). The depth of \(\varepsilon_i\) is then at most

\(\mathrm{log}(W')+1-(\mathrm{log}(w'_i)+1)=\mathrm{log}\frac{W'}{w'_i}+2\le\mathrm{log}\frac{W}{w_i}+3.\)

Hence each \(\varepsilon_i\) has an almost-optimal depth in _T_. In addition _T_<sup>S</sup> is a perfectly balanced tree with 2_n_ nodes and the depth of any node in _T_<sup>S</sup> does not exceed log_n_+1. Summing up, the depth of any leaf \(\varepsilon_i\) that holds the element _e<sub>i</sub>_ does not exceed min(log(_W/w<sub>i</sub>),_log_n_)+3.

An example tree _T_<sup>S</sup> and the corresponding almost-optimal tree _T_ are shown on Fig. 1. An interesting property of our method is that the tree _T_ is not necessarily a full tree: it is possible that some internal nodes have only one child. In the following sections we will show how the tree _T_<sup>S</sup> can be dynamized.

## 5 Almost-Optimal Dynamic Trees

Our dynamic data structure maintains a balanced tree _T_<sup>S</sup> on a dynamic set _B_ of pseudo-leaves.

This first version of the algorithm will work in phases. A phase will end when the total weight _W_ is increased by a factor of 2 or when the total number of elements is increased by a factor of 2.

Unlike in the previous section, these pseudo leaves are not kept in an array. Instead, _T_<sup>S</sup> is maintained as a _k_-neighbor tree data structure with _k_=log_n_\[22\] as described in Section 2. This method guarantees that all leaves of _T_<sup>S</sup> have the same depth and , since the total number of pseudoleaves can at most double within a phase, the height of the tree is bounded by \(\mathrm{log}(4W')+1\le\mathrm{log}n+4\). An update of _T_<sup>S</sup> takes _O_(log<sup>2</sup>_n_) time.

Each phase starts with a correct _T_<sup>S</sup> that had just been built from scratch using the approach of Section 4. Set \(\bar{\tau}=\tau=\frac{W}{n}\). This value stays constant within the phase.

During a phase, for every element _e<sub>i</sub>_ we keep track of its weight _w<sub>i</sub>_ and its approximate weight \(w'_i=\lceil w_i/\bar{\tau}\rceil\). Note that this implies that during a phase \(w'_i\) can be increased (incremented by 1 at a step) but not decreased.

When \(w'_i\) is incremented by 1, the tree _T_<sup>S</sup> is updated: we identify the rightmost pseudo-leaf \(\ell_i\) associated to _e<sub>i</sub>_ and insert two new pseudo-leaves, \(\ell_n\) and \(\ell_{n+1}\), immediately after \(\ell_i\). When a new element _e<sub>f</sub>_ is inserted into a tree, we insert two new pseudo-leaves, \(\ell_f\) and \(\ell_{f+1}\), into _T_<sup>S</sup>. The leaf \(\ell_f\) is inserted after the leaf \(\ell_p\), where _e<sub>p</sub>_ is the largest element satisfying _e<sub>p</sub>\<e<sub>f</sub>_ and \(\ell_p\) is the<tbc>

