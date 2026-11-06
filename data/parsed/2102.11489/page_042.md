**LC**<sub>2</sub>: Due to Theorem 10.1, we build a \(((8\cdot 1.74)^2/\mathrm{log}^{C_0}n,n,w)\)-lossy loose compaction circuit **LC**<sub>2</sub> from **SP**<sub>2</sub>. **LC**<sub>2</sub>’s size is upper bounded by the expressions:

\(\text{generalized boolean gates :}2.07\cdot 2.1\cdot(5.1)^2Cn\mathrm{log}^{(4)}n+O_4(n)\le(2.1\cdot 5.1)^2Cn\mathrm{log}^{(4)}n\)<br>
\(\text{selector gates :}2.07\cdot 2.1\cdot(5.1)^2Cn\le(2.1\cdot 5.1)^2Cn\)<br>
\(\text{depth :}2.07\cdot 2.1\cdot(2.5C_0\mathrm{loglog}n)^2\cdot(C\mathrm{loglog}n)+O_5(\mathrm{log}^{(3)}(n))\)<br>
\(\le(2.1\cdot 2.5C_0\mathrm{loglog}n)^2\cdot(C\mathrm{loglog}n)\)

Let \(d\in\mathbb{N}\) be the smallest integer such that \(\mathrm{log}^{(2^d)}n\le w\), i.e., \(d=\lceil\mathrm{log}(\mathrm{log}^*n-\mathrm{log}^*w)\rceil\le\mathrm{log}(\mathrm{log}^*n-\mathrm{log}^*w)+1\). Continuing for _d_ iterations, we get:

**LC**_<sub>d</sub>_: **LC**_<sub>d</sub>_ is a \(((8\cdot 1.74)^d/\mathrm{log}^{C_0}n,n,w)\)-lossy loose compactor, and **LC**_<sub>d</sub>_’s size is upper bounded by the expressions:

\(\text{generalized boolean gates :}(2.1\cdot 5.1)^dCn\mathrm{log}^{(2^d)}n=O(nw)\cdot\mathsf{poly}(\mathrm{log}^*n-\mathrm{log}^*w)\)<br>
\(\text{selector gates :}(2.1\cdot 5.1)^dCn=O(n)\cdot\mathsf{poly}(\mathrm{log}^*n-\mathrm{log}^*w)\)<br>
\(\text{depth :}(2.1\cdot 2.5C_0\mathrm{loglog}n)^d\cdot(C\mathrm{loglog}n)\le O(\mathrm{log}^{0.5}n)\)

This gives rise to Theorem 11.1.

## 12 Approximate Tight Compaction

**Definition.** Let \(\alpha\in(0,1)\). An \((\alpha,n,w)\)-approximate tight compactor (also written as \(\alpha\)-approximate tight compactor when _n_ and _w_ are clear from the context) solves the following problem: given an input array **I** containing _n_ elements, each containing a 1-bit key and a _w_-bit payload, we want to output a permutation (denoted **O**) of the input array **I**, such that at most \(\alpha\cdot n\) elements in **O** are misplaced -- here, an element **O**\[_i_\] is said be misplaced iff **O**\[_i_\] is marked with the key \(b\in\{0,1\}\); however, the sorted array sorted(**I**) wants the key 1-_b_ in position _i_.

**Theorem 12.1** (Approximate tight compaction)**.** _Fix an arbitrary constant_ \(\widetilde{C}>1\)_. There is an_ \((1/(\mathrm{log}n)\widetilde{C},n,w)\)_-approximate tight compaction circuit that has_ \(O(n\cdot w)\cdot\mathrm{max}\left(1,\mathsf{poly}(\mathrm{log}^*n-\mathrm{log}^*w)\right)\) _generalized boolean gates,_ \(O(n)\cdot\mathrm{max}\left(1,\mathsf{poly}(\mathrm{log}^*n-\mathrm{log}^*w)\right)\) _number of w-selector gates, and with depth at most O_(log_n)._

**Proof of Theorem 12.1:** Given an \((\alpha,n,w)\)-lossy loose compactor, we can obtain a \((8\alpha,n,w)\)- approximate tight compactor using an algorithm that is similar to the one described in the proof of Theorem 9.3. For convenience, below we shall refer to the elements with the 0-key in the input array **I** as _distinguished_.

**Approximate tight compaction from lossy loose compaction**

1. _Count._ Compute the total number (denoted `cnt`) of distinguished elements in the input array **I**.<tbc>

2. _Color._ For any \(i\le\mathtt{cnt}\), if **I**\[_i_\] is not distinguished, mark the element `red`; for any _i\>_`cnt`, if **I**\[_i_\] is distinguished, mark the element `blue`; every other element is marked \(\perp\). Let the outcome be **X**.<tbc>

<tbc>Note that at this moment, each element is labeled with 3 bits of metadata, one bit of distinguished indicator and two bits of color-indicator (indicating whether the element is colored, and if so, which color).<tbc>

