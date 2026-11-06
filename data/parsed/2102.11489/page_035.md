3. Reverse route the resulting array by reversing the decisions made by the AKS network in Step 1, and output the result.

Since the AKS sorting network performs comparisons on labels that are at most 2-bits long, the entire algorithm can be implemented as a circuit with _O(n_log_n_) generalized boolean gates, _O(n_log_n_) number of _w_-selector gates, and of depth _O_(log_n_).

## 9.2 Approximate Splitter from Lossy Loose Compaction

**Approximate splitter.** Let \(\beta\in(0,1/4]\) and let \(\alpha\in(0,1)\). An \((\alpha,\beta,n,w)\)-approximate splitter (also written as \((\alpha,\beta)\)-approximate splitter when _n_ and _w_ are clear from the context) solves the following problem: suppose we are given an input array **I** containing _n_ elements where each element has a _w_-bit payload and a 1-bit label indicating whether the element is _distinguished_ or not. It is promised that at most \(\beta\cdot n\) elements in **I** are distinguished. We want to output a permutation (denoted **O**) of the input array **I**, such that at most \(\alpha n\) distinguished elements are not contained in the first \(\lfloor\beta n+n/64\rfloor\) positions of **O**.

**Theorem 9.3** (Approximate splitter from lossy loose compaction)**.** _Suppose that there is an_ \((\alpha,n,w)\)_-lossy loose compaction circuit with B_lc(_n_) _generalized boolean gates and S_lc(_n_) _w-selector gates, and of depth D_lc(_n). Suppose also that there is an O_(1)_-depth approximate swapper circuit with B_sw(_n_) _generalized boolean gates and S_sw(_n_) _w-selector gates for an input array containing n element each of bit-width w._

_For any constant_ \(\beta\in(0,1/4]\)_, there is a_ \((8\alpha,\beta,n,w)\)_-approximate splitter circuit with at most_ 2.5_S_sw(_n_)+5_S_lc(_n_)+_O(n_) _number of w-selector gates,_ 2.5_S_sw(_n_)+2.5_B_sw(_n_)+2.5_B_lc(_n_)+10_S_lc(_n_)+_O(n_) _generalized boolean gates, and has depth at most_ \(2.4log\frac{1}{\alpha}\cdot(D_\mathrm{lc}(n)+O(1))\).

**Proof of Theorem 9.3:** Consider the following algorithm.

We now describe the \(\text{\textbf{Swap}}^n(\cdot)\) subroutine.

• **Input:** An array **X** of \(m\le n\) elements, each has a _w_-bit payload<sup>7</sup> and a 2-bit label indicating whether the element is colored, and if so, whether the element is `blue` or `red`. _n_ is the size of the original problem when **Swap** is first called; the same _n_ will be passed into all recursive calls since it is used to decide when the recursion stops. It is promised that<tbc>

\begin{tabular}{cc}
\multicolumn{2}{c}{**Approximate splitter from lossy loose compaction**} \\
1. & _Color._ Any distinguished element _not_ contained in the first \(\lfloor\beta n+n/64\rfloor\) positions of **X** are colored `blue`. Any non-distinguished element contained in the first \(\lfloor\beta n+n/64\rfloor\) positions of **X** are colored `red`. Observe that \(n_\mathrm{red}\ge n_\mathrm{blue}+n/64\), where _n_<sub>red</sub> and _n_<sub>blue</sub> denote the number of `red` and `blue` elements, respectively. \\
 & Note that at this moment, each element in **X** is labeled with 3 bits of metadata, one bit of distinguished indicator and two bits of color-indicator (indicating whether the element is colored or uncolored, and if so, which color). \\
2. & _Swap._ Call **Swap**_<sup>n</sup>_(**X**) defined below to swap the `blue` elements with `red` elements except for a small residual fraction (here we use a payload of size _w_+1 and not _w_ as we also include the distinguished-indicator as part of the payload). Return the outcome. \\
\end{tabular}

