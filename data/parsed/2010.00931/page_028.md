Recall that in phase 1 we splay the branching nodes _x<sub>k</sub>,...,x_<sub>1</sub> on the search path in bottom-to-top order. Each branching node _x<sub>i</sub>_ is splayed up until it becomes a child of _x_<sub>_i_-1</sub>, or, in case of _x_<sub>1</sub>, until it becomes the root. After phase 1, the search path of _x_ consists of (_x_<sub>1</sub>_,...,x<sub>k</sub>_) possibly followed by a number of nodes (that were initially between _x<sub>k</sub>_ and _x_). Let us now denote by _N<sub>y</sub>_, resp. \(N'_y\), the set of nodes in the subtree rooted at node _y_ before, resp. after phase 1. We have \(N'_{x_i}\subseteq N_{x_{i-1}}\), for all _i=k,...,_2, so \(\phi(x_{i-1})\ge\phi'(x_i)\). By Lemma 17(i)(iii), \(\phi(x_k)\ge\phi(x)\ge-\mathtt{depth}_R(x)\), and \(\phi'(\cdot)<0\).

It follows that the total potential increase during phase 1 is at most

\(\Delta\phi^{(1)}\le d\big(-z_1+3\sum_{i=1}^k\big(\phi'(x_i)-\phi(x_i)\big)\big)\)<br>
\(\le 3d\big(\phi'(x_1)-\phi(x_k)\big)-dz_1\)<br>
\(\le 3d\cdot\mathtt{depth}_R(x)-dz_1,\triangleright\text{by Lemma 17(i)(iii)}\)

where _z_<sub>1</sub> is the number of ZIG-ZIG and ZIG-ZAG steps in this phase.

In phase 2 we splay _x_ to become the root, so the total potential increase in this phase is at most

\(\Delta\phi^{(2)}\le 3d\big(\phi'(x)-\phi(x)\big)-dz_2\)<br>
\(\le 3d\cdot\mathtt{depth}_R(x)-dz_2,\triangleright\text{by Lemma 17(i)}\)

where _z_<sub>2</sub> is the number of ZIG-ZIG and ZIG-ZAG steps in this phase.

Denoting _z=z_<sub>1</sub>+_z_<sub>2</sub>, the total increase in potential during the two phases is therefore at most \(6d\cdot\mathtt{depth}_R(x)-dz\). Intuitively, we save constant potential on every ZIG-ZIG and ZIG-ZAG step, which we need to offset the actual cost of O(`depth`_<sub>T</sub>(x_)). In the first phase we may have the unfavorable situation that there are many branching nodes, with short _odd-length_ gaps between them, in which case we lose potential due to the many ZIG-steps. But then, since the branching nodes stay on the search path for the second phase, they form a long contiguous splaying path on which we make up for the loss.

For _i_=2_,...,k_, let _h<sub>i</sub>_ denote the number of non-branching nodes between _x_<sub>_i_-1</sub> and _x<sub>i</sub>_ at the beginning of phase 1, let _h_<sub>1</sub> denote the non-branching nodes above _x_<sub>1</sub> on the path to the root, and let _h_<sub>_k_+1</sub> denote the number of nodes between _x_ and _x<sub>k</sub>_. In the first phase, The number of ZIG-ZIG and ZIG-ZAG operations that _x<sub>i</sub>_ participates in is \(\lfloor h_i/2\rfloor\), for all _i_.

Observe that \(\mathtt{depth}_T(x)=k+1+\sum_{i=1}^{k+1}h_i\). We thus have:<tbc>

\(z_1=\sum_{i=1}^k\left\lfloor\frac{h_i}{2}\right\rfloor\ge\sum_{i=1}^k\frac{h_i-1}{2}=\frac{\mathtt{depth}_T(x)-h_{k+1}-1}{2}-k.\)

<tbc>In the second phase, _x_<sub>1</sub>_,...,x<sub>k</sub>_ are still ancestors of _x_ but no longer branching. In addition, the original nodes on the search path between _x<sub>k</sub>_ and _x_ are still the ancestors of _x_. Thus, at the beginning of the phase _x_ has at least _k+h_<sub>_k_+1</sub> ancestors, and therefore:<tbc>

\(z_2\ge\left\lfloor\frac{k+h_{k+1}}{2}\right\rfloor\ge\frac{k+h_{k+1}-1}{2}.\)

