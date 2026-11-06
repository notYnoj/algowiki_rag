## Total running time.

The preprocessing time is O(_n_log_k_), as desired.

Consider one search-and-split step. Let \(\mathcal{T}'_\mathrm{r}\) be the input tree, let T<sub>r</sub> be the input super-tree, let _R_ be the set of vertices removed in the splitting step, and let F<sub>r</sub> be the super-forest produced after splitting. The time required to execute the step is

\(\mathcal{O}\left((|V(\mathfrak{T}_\mathrm{r})|+|E(\mathfrak{T}_\mathrm{r})|)\mathrm{log}k+|V(\mathfrak{F}_\mathrm{r})|+\sum_{v\in R}\mathrm{deg}_{\mathcal{T}_\mathrm{r}^\prime}(v)\mathrm{log}k\right).\)

Since each vertex is removed only once, the third term sums up to O(_n_log_k_) over all vertices. The second term can be charged to recursive calls (for each component of F<sub>r</sub> with more than one normal vertex) or single vertices (for each component of F<sub>r</sub> consists of only one normal vertex). It remains to bound the first term.

If T<sub>r</sub> consists of only one super-vertex _A_, then we charge the O(log_k_) cost to the centroid of \(\mathcal{T}'_\mathrm{r}[A]\), for a total of O(_n_log_k_) over the course of the algorithm.

We analyze the other recursive calls in rounds. Assume that in each round, we execute one step on each remaining super-tree, thereby finding all centroids on a certain level of the centroid tree. Let F<sub>0</sub> be the initial super-tree, and let F_<sub>i</sub>_ be the forest of super-trees after round _i_. Note that the number of _edges_ cannot grow by splitting, so each F_<sub>i</sub>_ contains at most \(\mathcal{O}(\frac{n}{k})\) edges, and therefore at most \(\mathcal{O}(\frac{n}{k})\) non-isolated vertices, so the round requires \(\mathcal{O}(\frac{n}{k}\mathrm{log}k)\) time in total.

If the height of the tree is _h_, then we have precisely _h_ rounds. Thus, the running time of the algorithm is \(\mathcal{O}((\frac{h}{k}+1)n\mathrm{log}k)\).

In particular, if we know _h_ and set _k=h_, then the running time is O(_n_log_h_). If we do not know _h_, we start with _k_=2 and run the algorithm for _k_ rounds. If it stops, then \(h\le k\) and we are done. Otherwise, try again with \(k\leftarrow k^2\). The last run of the algorithm, where \(h\le k\le h^2\), dominates the running time with O(_n_log_h_). Thus, we have

**Theorem 5.3.** _Let_ T _be a tree on n vertices and w be a positive weight function. We can compute a centroid tree of_ (T_,w_) _in time_ O(_n_log_h), where h is the height of the computed centroid tree._



Figure 7: A splitting step. (_Left._) The super-tree before splitting. The large black circles are super-vertices. The small dots are is the set of vertices _R_ to be removed. The gray circles and ellipses are components obtained after removing _R_. (_Right._) The ten super-vertices within eight super-trees obtained after splitting.

