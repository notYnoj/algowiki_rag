**Tightness.** \[21\] prove tight bounds and from their proof we can immediately obtain that the approximation algorithm of the two-for-one swap heuristic is exactly 2/(_k_+1). For _k_=1, every maximal independent set is optimum; assume \(k\ge 2\) below. Assume that _N_ consists of collection of subsets of _k_ points from some universe _U_, and \(f(A)=|\cup_{e\in A}e|\). It is well known (and easy to show) that _f_() is increasing submodular and so we do have a MISkP instance. In this setting, a set \(A\subseteq N\) is independent if and only if the elements of _A_ are disjoint. (this is the _k_-Set Packing problem \[21, 11, 18\]). Let _e_<sub>1</sub>_,e_<sub>2</sub>_,...,e_<sub>_k_+1</sub> be _k_+1 disjoint sets of _U_ with _k_ elements each, and let _e_<sub>_k_+2</sub> have one element from each of _e_<sub>1</sub>_,e_<sub>3</sub>_,e_<sub>4</sub>_,...,e_<sub>_k_+1</sub> and _e_<sub>_k_+3</sub> be disjoint from _e_<sub>_k_+2</sub> and have one element from each of _e_<sub>2</sub>_,e_<sub>3</sub>_,e_<sub>4</sub>_,...,e_<sub>_k_+1</sub>. The heuristic can stop with {_e_<sub>_k_+2</sub>_,e_<sub>_k_+3</sub>} as the output while a solution with _k_+1 elements of _N_ exists: {_e_<sub>1</sub>_,...,e_<sub>_k_+1</sub>}. This example for _k_=3 is given in Figure 3.

### Method Limitations

We are not able to construct this bipartite graph for larger swaps and general matroids (or linear matroids). The method does work for strongly base orderable matroids \[4, 22, 14, 39, 20\] and gives the better dependence of \[21\] of the approximation ratio as function of the size of the swap. Constructing such a bipartite graph for strongly base orderable matroids was done in Feldman, Naor, Schwartz, and Ward \[14\], but we could not find an explicit dependence of the approximation ratio as a function of the size of the swap in their paper. Note that the matroid being strongly base orderable or not does not affect the algorithm, just its proven performance guarantee.

### Acknowledgment

Adrian thanks Chandra Chekuri for providing useful references. Gruia thanks Bahareh Kudarzi for discussions regarding \[21\]. ChatGPT was used to identify the minor errors that we repair here.

## References



Figure 3: An example where the two-for-one swap heuristic has approximation ratio of exactly 2/(_k_+1), for _k_=3. The heuristic’s output may consists of the two rounded rectangles, while the four sharp cornered rectangles make an optimum solution.

