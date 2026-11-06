\(\mathsf{poly}(\mathrm{log}^*n-\mathrm{log}^*w)\cdot\alpha\), where \(\alpha=1/\mathsf{poly}\mathrm{log}(n)\) denotes the lossy factor of the initial lossy loose compactor we started out with.

## 8 Inefficient Lossy Loose Compaction Circuit

In this section, we will prove the following theorem.

**Theorem 8.1.** _Let c\>_1 _be an arbitrary constant. There is a circuit in the indivisible model with O(n_loglog_n_) _generalized boolean gates, O(n_) _number of w-selector gates, and of depth O_(loglog_n_) _that realizes an_ \((\frac{1}{\mathrm{log}^{\epsilon n}},n,w)\)_-lossy loose compactor._

To prove the above theorem, we describe how to implement lossy loose compaction as a low- depth circuit. Our construction is almost the same as the loose compactor circuit described by Asharov et al. \[ALS21\], except that we now run the algorithm for fewer (i.e., _c_loglog_n_) iterations rather than _O_(log_n_) iterations). Because we omit some iterations, we end up losing a small fraction of elements during the loose compaction. We describe the algorithm below.

**Expander graphs.** The construction will rely on a suitable family of bipartite expander graphs denoted \(\{G_{\epsilon,m}\}_{m\in\mathsf{SQ}}\) where \(\mathsf{SQ}\subseteq\mathbb{N}\) is the set of perfect squares. The parameter \(\epsilon\in(0,1)\) is a suitable constant referred to as the _spectral expansion_. The graph \(G_{\epsilon,m}\) has _m_ vertices on the left henceforth denoted _L_, and _m_ vertices on the right henceforth denoted _R_, and each vertex has \(d:=d(\epsilon)\) number of edges where _d_ is a constant that depends on \(\epsilon\). We give additional preliminaries on expander graphs in Appendix A.

Without loss of generality, we may assume that _d_ is a multiple of 8 since we can always consider the graph that duplicates each edge 8 times.

**Construction.** The input array is grouped into chunks of _d/_2 size. Chunks that have at most _d/_8 elements (i.e., a quarter loaded) are said to be _sparse_ and chunks that have more than _d/_8 elements are said to be _dense_. The idea is to first distribute the dense chunks such that there are only very few dense chunks after this step. Then, we can easily compact each chunk separately. When the remaining dense chunks are compressed, we end up losing some elements.

The challenge is how to distribute the dense chunks. We can consider the chunks to be left- vertices in the bipartite expander graph \(G_{\epsilon,m}\). Each dense chunk wants to distribute its real elements to its neighbors on the right, such that each right vertex receives no more than _d/_8 elements, i.e., each vertex on the right is a sparse chunk too. At this moment, we can replace dense chunks on the left with filler elements -- for almost all of these dense chunks, their real elements have moved to the right. For the remaining dense chunks, replacing them with filler causes some elements to be lost. Now that all chunks are sparse, and we can compress each chunk on the left and the right to a quarter its original size. All compressed chunks are concatenated and output, and the output array is a half the length of the input.

The distribution of the real elements to its neighbors on the right requires some care, as we have to guarantee that no node on the right will become dense. We will have to compute on which subset of edges we will route the real elements. This is done via the procedure ProposeAcceptFinalize described below.

**ProposeAcceptFinalize subroutine.** We now describe the ProposeAcceptFinalize subroutine which is the key step to achieve the aforementioned distribution of dense chunks. To make the description more intuitive, henceforth we call each vertex in _L_ a _factory_ and each vertex in _R_ a _facility_. Initially, imagine that the dense vertices correspond to factories that manufacture at most _d/_2 products, and the sparse vertices are factories that are unproductive. There are at most _m/_32 productive<tbc>

