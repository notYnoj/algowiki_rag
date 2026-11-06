# Near-Optimal In-Place Sorting

**Alex Z. Xu**<sup>1</sup> \(\unknown\)<br> Independent Researcher, Hong Kong

**Stephen J. Chick** \(\unknown\)<br> Independent Researcher, Commerce City, CO, USA

**Abstract**

We present an in-place comparison-based sorting algorithm that sorts an array of _n_ elements using _n_lg_n+O(n_) comparisons with exponentially high probability and always _O(n_) moves. This serves as the first in-place sorting algorithm to match the fundamental \(nlgn+\Omega(n)\) lower bound on total operations (i.e. sum of comparisons and moves). For the worst-case, we present an algorithm that makes _n_lg_n+O(n_lg<sup>(_t_)</sup>_n_) comparisons and _O(tn_) data moves, where _t_ is an integer parameter satisfying \(2\le t\le lg^*n-1\) and lg<sup>(_t_)</sup>_n_ denotes the _t_-time iterated logarithm, improving over the previous upper bound of _n_lg_n+O(n_lggl_n_) comparisons and _O(n_) moves when using constant _t\>_2. When _t_≈lg<sup>∗</sup>_n_, this yields a worst-case upper bound on total operations of _n_lg_n+O(n_lg<sup>∗</sup>_n_). We thus achieve the ultimate goal of efficient in-place sorting via randomization whilst narrowing the gap to this goal in the worst-case. This advance involves a novel ordered set structure that supports searches in an optimal lg_n+O_(1) comparisons for _n_ elements. Note that both algorithms are unstable.

**2012 ACM Subject Classification** Theory of computation \(\rightarrow\) Sorting and searching

**Keywords and phrases** sorting, in-place algorithms, data structures, computational complexity

<sup>1</sup> Corresponding author



