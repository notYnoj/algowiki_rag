The ordered _v_-part of a retained description must consist of distinct vertices of _C_\\_A_<sub>0</sub>: in the _v_-positions of the sample we have placed vertices that avoid the true missing set _V(G_)\\_C_, and no vertex may appear in both the _u_-part and the _v_-part. Since \(A_0\subseteq C\), there are exactly _n-a-h_ available vertices, and hence at most \(P_{n-a-h}^b\) choices for the ordered _v_-part.

For fixed _t,W,_**i**, the block-size estimate gives

\(a\le t\left\lceil\frac{q}{2t}\right\rceil\le\frac{q}{2}+t,b=q-a\ge\frac{q}{2}-t\ge\frac{q}{4},\) (15)

where \(q\ge 4T\ge 4t\). We first give a common upper bound. For fixed _t,W,_**i**, the numbers _a_ and _b_ are fixed, but the replayed cap and its missing-set size may depend on the ordered _u_-tuple. Let U_<sub>t,W,_**i**</sub> be the set of ordered tuples **u**=(_u_<sub>1</sub>_,...,u<sub>a</sub>_) of distinct vertices for which replaying the process on _A_<sub>0</sub>={_u_<sub>1</sub>_,...,u<sub>a</sub>_} with color string **i** completes _t_ rounds and yields a cap _C=U(P<sup>t</sup>_) satisfying \(A_0\subseteq C\) and \(|V(G)\backslash C|\ge\alpha tn\). For \(\mathbf{u}\in\mathcal{U}_{t,W,\mathbf{i}}\), write _h_(**u**):=|_V(G_)\\_C_| for the missing-set size of its replayed cap.

Conditioned on a particular ordered _u_-tuple, the remaining positions are filled uniformly by an ordered _b_-tuple from _V(G_)\\_A_<sub>0</sub>. Thus, writing _h=h_(**u**) temporarily, the fraction of these completions that avoid the missing set is

\(\frac{P_{n-a-h}^b}{P_{n-a}^b}=\prod_{j=0}^{b-1}\frac{n-a-h-j}{n-a-j}=\prod_{j=0}^{b-1}\left(1-\frac{h}{n-a-j}\right)\le\left(1-\frac{h}{n-a}\right)^b\le exp\left(-\frac{hb}{n-a}\right)\le exp\left(-\frac{hb}{n}\right)\le e^{-\alpha tb}\le e^{-\alpha tq/4}.\text{(16)}\)

The displayed product is used only when \(b\le n-a-h\); otherwise the fraction is zero and the same bound holds. The condition \(A_0\subseteq C\) ensures that the entire missing set lies in _V(G_)\\_A_<sub>0</sub>. The penultimate inequality uses \(h\ge\alpha tn\) and \(n-a\le n\).

For fixed _t,W,_**i**, let _N_<sub>_t,W,_**i**</sub> denote the number of retained descriptions. Summing separately over the ordered _u_-tuples, rather than treating _h_ as a constant, gives

\(\frac{N_{t,W,\mathbf{i}}}{P_n^q}=\frac{1}{P_n^a}\sum_{\mathbf{u}\in\mathcal{U}_{t,W,\mathbf{i}}}\frac{P_{n-a-h(\mathbf{u})}^b}{P_{n-a}^b}\le\frac{|\mathcal{U}_{t,W,\mathbf{i}}|}{P_n^a}e^{-\alpha tq/4}\le e^{-\alpha tq/4}.\)

Here we used \(P_n^q=P_n^aP_{n-a}^b\) and \(|\mathcal{U}_{t,W,\mathbf{i}}|\le P_n^a\).

There are at most \(\genfrac(){pt}{2}{2t}{t}\le 4^t\) choices for _W_ and _k<sup>t</sup>_ choices for the color string. Every colorable sample yields at least one retained description, even though its proper coloring may depend on the<tbc>

