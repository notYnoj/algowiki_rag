## 4 LCS Step 0: Window-compatible Solutions

The goal of this section is to show that window-compatible solutions provide very accurate estimates for LCS. Roughly speaking, in this section, we construct a set of windows for _A_ and a set of windows for _B_ and we show that it suffices to only compute the LCS of pairs of windows. If that information is available, then we can estimate the LCS of the original two strings very accurately.

We use the same definition of window-compatible transformation as \[BEG<sup>+</sup>18\], but we will use slightly different sets of windows. Every window is a (contiguous) substring of each string. Notice that windows may not have the same length. We use _W<sub>A</sub>_ to denote the set of windows constructed for _A_ and _W<sub>B</sub>_ for the set of the windows that we construct for _B_.

Let us first state our definition of window-compatible solutions for LCS.

**Definition 4.1** (Window-compatible common subsequence)**.**<tbc>

• Let \(S=\langle w_1,\cdots,w_\alpha\rangle\) and \(S'=\langle w'_1,\cdots w'_\alpha\rangle\) be two sequences of non-overlapping windows from _W<sub>A</sub>_ and _W<sub>B</sub>_, respectively. We call a common subsequence of (_A,B_) _window-compatible with respect to S and_ \(S'\), if it is a union of _k_ common subsequences of \((w_1,w'_1),\dots,(w_\alpha,w'_\alpha)\)<tbc>

• We call a common subsequence _window-compatible_, if it is window-compatible with respect to some pair of sequences of non-overlapping windows from _W<sub>A</sub>_ and _W<sub>B</sub>_, ordered by their respective starting indices.

_W<sub>A</sub>_ will simply be a partitioning of _A_ into disjoint windows of length _d_ (for parameter _d_ to be finalized later). Setting _d=n<sup>x</sup>_ leads to a truly subquadratic time solution for any 0_\<x\<_1, however, one can play with the value of _d_ to optimize the running time. Below we consider two constructions of windows _W<sub>B</sub>_ for string _B_.

### 4.1 Window construction for constant \(\lambda\) (Step 0 of Theorem 2.2)

For clarity, we use _B_<sup>(_j,l_)</sup> to denote a length-_l_ substring of _B_ which starts at index _j_ and ends at index _j+l_-1. Our construction has multiple layers, where each layer contains windows with equal lengths. For parameter \(\epsilon_0\in(0,1)\) to be defined later, let

\(f:=\lceil log_{1+\epsilon_0}(1/\epsilon_0)\rceil+1=\Theta\left(\frac{1}{\epsilon_0}log(\frac{1}{\epsilon_0})\right).\)

For each \(i\in\{-f,\cdots,f\}\), we define \(d_i=d(1+\epsilon_0)^i\), \(g_i=\epsilon_0d_i\), and _t<sub>i</sub>=n/d<sub>i</sub>_. For each _i_, let \(W_B^i\) denote the set of all the windows in this layer. In the _i_-th layer, all the windows have the same size which is _d<sub>i</sub>_. _g<sub>i</sub>_ is the shift size, i.e. for each window (except the leftmost and rightmost windows), if we shift by \(\pm g_i\) we get another window in \(W_B^i\). _t<sub>i</sub>_ is the number of windows in the _i_-th layer.

**Definition 4.2** (Window construction for constant \(\lambda\))**.**

\(W_B^i:=\big\{B^{(left,len)}\big|\text{left}=x\cdot g_i+y\cdot d_i,\text{len}=d_i,\forall x\in\{0,1,\cdots,d_i/g_i-1\},\forall y\in\{0,1,\cdots,t_i-1\}\big\}\)

where we use _B_<sup>(left,len)</sup> denotes a (contiguous) substring of string _B_ that starts at left and has length len. Finally _W<sub>B</sub>_ is \(\cup_{i\in\{-f,\cdots,f\}}W_B^i\).

**Fact 4.3** (Parameters for constant \(\lambda\) (Theorem 2.2))**.**

_Recall that_ \(\epsilon\) _is a small constant and_ \(\lambda\) _is the relative length of the true LCS between A and B. In order to make sure the loss in the approximation is negligible, we use_<tbc>

\(\epsilon_0:=\epsilon\lambda.\)

