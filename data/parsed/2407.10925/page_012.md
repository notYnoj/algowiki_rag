## Appendix A Program  and Additional Material

All program code is open source and available at `https://github.com/ Statistics-of-Subsequences/PaperMaterials`.<br>
This link also contains instructions on how to run the code.

The files hosted at this domain also include explanations of additional optimizations we implemented which were too lengthy to include in this paper. These optimizations focus on the Binary Feasible Triplet Algorithm (Algorithm 2.3), though we also note how it is possible to efficiently ‘pre-compute’ the **b** vector in the general case. In particular, by intelligently combining _L_<sub>0,1</sub> and _L_<sub>1,0</sub>, computing _L_<sub>0,0</sub> in a slightly less straightforward manner, reusing partial computations, and performing `max` operations locally wherever possible, these optimizations significantly reduce either A: the amount of memory I/O required each iteration, or B: the amount of computation performed each iteration, depending on the implementation.

## Appendix B Alternate Lower Bound Algorithm

We also developed a separate algorithm based on the implementation Lueker provided (see [20] for Lueker’s implementation). This algorithm was a preliminary implementation of our modified Binary Feasible Triplet algorithm and obtained the same results up to \(\ell=18\), supporting the results given in  2.

## Appendix C Complete Results for General \(\gamma_{\sigma,d}\) Constants

Here we list out all of our results for the Feasible Triplet algorithm for all \(\sigma\), _d_ values, even for smaller values of \(\ell\) which did not result in better lower bounds. These results can be cross-checked with  2 of [16] to demonstrate that our implementation of Algorithm 2.2 results in the exact same numbers for the values of \(\ell\) reported by Kiwi and Soto.

