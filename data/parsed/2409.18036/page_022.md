<tbc>where the last inequality is by the fact that _T_ is non-empty with probability at least \(\frac{1}{2}\). □

Therefore, the running time of the Insertion Sort over all the _N_ iterations is bounded by _O(N_) in expectation. This completes the proof of Lemma 5.3. □

Putting together all of the above analyses, the total expected running time of the algorithm is \(O(N)+tp(N)+O(N\cdot(t_q(N)+t_{del}(N)))+O(N)\), which is \(tp(N)+O(N\cdot(t_q(N)+t_{del}(N)))\).

Theorem 1.2 thus follows.

## 6 Conclusion

In this paper, we study the Dynamic Parameterized Subset Sampling (DPSS) problem in the Word RAM model. Our first main result is an optimal DPSS algorithm. We propose our novel data structure HALT that achieves the optimal bounds. Our second main result showing that if the item weights in the DPSS problem are allowed to be float numbers, then an deletion-only optimal DPSS algorithm can be used to solve Integer Sorting over the whole range of bit-length in _O(N_) expected time, where _N_ is the number of integers to sort. Finally, our third main result is a new efficient method for sampling variates from the Truncated Geometric distribution in _O_(1) expected time in the Word RAM model. We expect considerable application of this technique for efficient random variate realization.

## Acknowledgements

In this work, Junhao Gan is supported in part by Australian Research Council (ARC) Discovery Early Career Research Award (DECRA) DE190101118. Seeun William Umboh is partially supported by ARC Training Centre in Optimisation Technologies, Integrated Methodologies, and Applications (OPTIMA). Hanzhi Wang is supported by the VILLUM Foundation grant 54451.

