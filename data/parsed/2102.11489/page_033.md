**Proposition 8.3** (Pippenger \[Pip96\] and Asharov et al. \[AKL<sup>+</sup>20b\])**.** _There exists an appropriate constant_ \(\epsilon\in(0,1)\) _and a bipartite expander graph family_ \(\{G_{\epsilon,m}\}_{m\in\mathbb{N}}\) _where each vertex has d edges for a constant_ \(d:=d(\epsilon)\)_, such that for any perfect square m and n=md/_2_, the above lossy loose compaction algorithm, when instantiated with this family of bipartite expander graph, can correctly compress any input array of length n to a half its original size losing at most n/_log_<sup>c</sup>n real elements, as long as the input array has at most n/_128 _real elements._

**Remark 3.** In the above, we assumed that _n_ is divisible by _d/_2. If _n=dm/_2 where _m_ is a perfect square. In case this is not the case, we can always round _n_ up to the next integer that satisfies this requirement; this blows up _n_ by at most a 1+_o_(1) factor. This is why in our definition of lossy loose compactor, the output size is allowed to be \(\lfloor n/1.9\rfloor\) rather than \(\lfloor n/2\rfloor\), assuming that _n_ is sufficiently large.

**Implementing the algorithm in a low-depth circuit.** Since our lossy loose compactor algorithm is almost the same as Asharov et al.’s loose compactor \[ALS21\], we can implement the algorithm as a circuit in almost the same way as described by Asharov et al. \[ALS21\], except that we run fewer iterations. It is not hard to check that the resulting circuit has _O(n_loglog_n_) generalized boolean gates, _O(n_) number of _w_-selector gates, and has depth _O_(loglog_n_).

\begin{tabular}{cc}
\multicolumn{2}{c}{\(\bullet\) **The algorithm:**} \\
1. & Divide **I** into _m_ chunks of size _d/_2. If a chunk contains at most _d/_8 real elements (i.e., at most a quarter loaded), it is said to be _sparse_; otherwise it is said to be _dense_. It is not hard to see that the number of dense chunks must be at most _m/_32. \\
2. & Now imagine that each chunk is a vertex in _L_ of \(G_{\epsilon,m}\), and \(D\subset L\) is a set of dense vertices (i.e., corresponding to the dense chunks). Let edges(_D,R_) denote all the edges in \(G_{\epsilon,m}\) between \(D\subset L\) and _R_. \\
 & Let _D_ be the subset of productive factories, and run the ProposeAcceptFinalize subroutine for _c_loglog_n_ iterations. The outcome is a subset of edges \(M\subseteq\mathsf{edges}(D,R)\) that satisfy Fact 8.2, where the fraction of unsatisfied chunks is 1/log_<sup>c</sup>n_. \\
3. & Now, every dense chunk _u_ in _D_ does the following: for each of an arbitrary subset of \(\mathsf{load}(u)\le d/2\) outgoing edges of _u_ in _M_, send one element over the edge to a corresponding neighbor in _R_; for all remaining out edges of _u_, send a filler element on the edge. \\
 & Every vertex in _R_ receives no more than _d/_8 real elements. Henceforth we may consider every vertex in _R_ as a sparse chunk, i.e., an array of capacity _d/_2 but containing only _d/_8 real elements. \\
4. & At this moment, for each dense chunk in _L_, replace the entire chunk with _d/_2 filler elements. \\
5. & Now, all chunks in _L_ and in _R_ must be sparse, that is, each chunk contains at most _d/_8 real elements, while its size is _d/_2. We now compress each chunk in _L_ and _R_ to a quarter of its original size (i.e., to size _d/_8 in length), losing few elements in the process (we will bound the number of lost elements later). \\
 & Output the compressed array **O**, containing of \(2m\cdot\frac{d}{8}=2\cdot\frac{2n}{d}\cdot\frac{d}{8}=n/2\) elements. \\
\end{tabular}

