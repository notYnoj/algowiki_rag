In the implementation<sup>1</sup>, every pair of strings (_u,v_) is manipulated as the corresponding number _uv_ written in base _k_ (every considered pair is stored in a 64 bits integers). We also use the fact that a permutation of the alphabet does not change the result. That is, for every function _f_ that permutes the letters of the alphabet and for all strings _u,v_ of length _h,V<sub>n</sub>(u,v_)=_V<sub>n</sub>(f(u),f(v_)). For every pair _u,v_, we consider the _f_ that minimizes the string _uv_ for the lexicographic order (and we call _f(uv_) the _normalization_ of _uv_). This allows us to divide the size of the considered vector by ∼_k_!. However, it can be costly to recompute the renaming of the strings, so we provide three different versions of the code that provide different optimizations that are better for different values of _k_.

## The binary case.

A first version was written specifically for the binary alphabet. In this case, exchanging the letters of the string for the normalization is simply taking the bitwise negation of the string, and we can use bit-shifts and other bit manipulation to produce a faster code. In this code, the transformation _T_ is computed on the fly for every iteration, and we only store the vectors. The results obtained with this program are given in  2. The source code is in the file `EditDistance\_binary\_alphabet.cpp` from the GIT repository. This is the only version that uses parallelization (the optimal number of cores seems to be 2 as using more cores seems to increase considerably the number of cache misses).

We obtain \(\alpha_2\le 0.315514\). In \[14\], the author uses other symmetries that one might be able to adapt here to push the computations to _h_=18 instead of _h_=17 with the same machine (which, based on the difference between _h_=16 and _h_=17, would not improve the bound by much). Let us mention that the results obtained by Lueker have been very recently improved by optimizing the implementation and some of the techniques used might be applicable in our case as well \[11\].

## The general case.

The second version of the code precomputes the transformation _T_ and stores it. In the general setting of an alphabet of size _k_ the normalization is more costly to compute, so we only compute it once for every pair of strings. Storing _T_ increases the memory consumption (by a factor of order _k_), but saves a lot of computation time. The results obtained with this program are given in  3, and the source code is in the file `EditDistance\_general\_case.cpp` from the GIT repository.

<sup>1</sup>The code is available on `https://gite.lirmm.fr/mrosenfeld/expected-edit-distance`.

\begin{tabular}{cccc}
h & Upper bound & Memory consumption & Computation time \\
14 & 0.319052 & 1.6Gb & 1m19s \\
15 & 0.317752 & 6.2Gb & 6m \\
16 & 0.31658 & 25Gb & 17m \\
17 & 0.315514 & 100Gb & 1h32m \\
\end{tabular}

2: Our results for the binary case. The number of iterations of _T_ before choosing \(\vec{v}=w_n\) is _n_=150. We used a laptop for \(h\le 15\) and a more powerful computer for _h\>_15. All the times here (and in futur tables) are purely indicative and do not constitute a proper benchmarking.

