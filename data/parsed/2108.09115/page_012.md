## 5 Large edit distance, \(7+\epsilon\)-approx

In this section we prove our result for the large edit distance regime. Our main result is a 7+_o_(1) approximation for ED(_A,B_) in \(n^{\frac{3}{2}+o(1)}\) query time. We are allowed to preprocess each _A_ and _B_ separately and spend ∼_n_<sup>2</sup> time in overall preprocessing.

_Remark_ (Estimating the distance vs computing an alignment). For simplicity of presentation, we write our algorithms as merely estimating the distance. It is straightforward with standard techniques to modify them to output the alignment as well in roughly the same running time.

### Organization of this section

In Subsection 5.1 we give a bird’s eye overview of the main technical elements of our algorithm. Subsection 5.2 formally describes the decomposition of the strings into windows, Subsection 5.3 is a standard dynamic programming for computing an optimal window-compatible matching from pairwise distances. Our main contribution is in Subsection 5.4 which describes the algorithm for learning the close-window graph.

### 5.1 High Level Description of the Algorithm

### The basic divide-and-conquer framework for approximate edit distance

The algorithm builds upon the recent progress on approximating edit distance in subquadratic time using divide-and-conquer algorithms [BEG<sup>+</sup>18, CDG<sup>+</sup>18, And19, BR19, KS19, RSSS19], along with our small-edit-distance algorithm from Section 3. We decompose the strings _A_ and _B_ into contiguous substrings called _windows_. These windows can be overlapping and have variable lengths. Up to an (1+_o_(1))-factor approximation, we can now wlog restrict our attention to matchings of _A_ to _B_ that are "window-compatible", i.e. they respect the partition to windows (see Lemma 10).

If we (approximately) knew all the pairwise distances between windows, a standard DP would find an (approximately) optimal window-compatible matching efficiently (Lemma 12). Computing the pairwise distances is further reduced to (approximately) learning the bipartite _close-window graph_, where a pair of _A_- and _B_-windows are neighbors if their pairwise edit distance is below an appropriate threshold \(\tau\).

The goal is now to approximately learn the close-window graph while computing as few window- window distances as possible. With this in mind, we classify the windows as either _dense_ (high- degree in the close window graph), or _sparse_. We use by-now-standard separate subroutines to handle each kind of windows.

### Further details of our algorithm

The density of a window can be estimated by computing its edit distance to a small sample of its potential neighbors. To obtain optimal tradeoff between parameters, we cannot afford even this small sample to classify windows as dense or sparse. Here we deviate from previous works and estimate the density on-the-fly. That is each window is assumed to be sparse by default, and only when it is selected as a special "seed" for the sparse subroutine, we estimate its degree and move it to the dense subroutine if necessary. (In fact, an originally dense window can lose many of its neighbors and become sparse by the time it is selected; this does not hurt our analysis.)

The main sparse subroutine proceeds by recursively narrowing down the set of relevant candidate neighbors. Even though sparse windows take part in multiple levels of recursion, the loss in approximation from each level of the sparse subroutine is negligible, so it continues to be negligible in aggregate. The dense subroutine incurs the main loss in approximation due to the use of triangle<tbc>

