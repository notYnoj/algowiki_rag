# Optimal search trees with 2-way comparisons<sup>⋆</sup>

**Abstract.** In 1971, Knuth gave an _O(n_<sup>2</sup>)-time algorithm for the classic problem of finding an optimal binary search tree. Knuth’s algorithm works only for search trees based on 3-way comparisons, but most modern computers support only 2-way comparisons (\(<,\le,=,\ge,\) and _\>_). Until this paper, the problem of finding an optimal search tree using 2-way comparisons remained open -- poly-time algorithms were known only for restricted variants. We solve the general case, giving (i) an _O(n_<sup>4</sup>)-time algorithm and (ii) an _O(n_log_n_)-time additive-3 approximation algorithm. For finding optimal _binary split trees_, we (iii) obtain a linear speedup and (iv) prove some previous work incorrect.

### 0 _Erratum (March 2021)_

_The proof of Theorem 3 here (and in the conference version of this paper [2], and in versions 1-4 on arxiv.org) is incorrect. For details of the error in the proof of Theorem 3, see the comments at the end of Section 3.1._

_The remaining results are correct and have full proofs here, but some of the results have been updated substantially and now appear in updated manuscripts, as follows:_

- _For an update of Theorem 1, with a simpler algorithm for 2WCST, see [5]._

- _For a result related to (but not supplanting) Theorem 2, see [4]._

- _For an update of Theorem 4, with additional counterexamples for Spuler’s dynamic program, see [3]._

### 1 Background and statement of results

In 1971, Knuth [13] gave an _O(n_<sup>2</sup>)-time dynamic-programming algorithm for a classic problem: _given a set_ K _of keys and a probability distribution on queries, find an optimal binary-search tree T._ As shown in Fig.1, a search in such a tree for a given value _v_ compares _v_ to the root key, then (i) recurses left if _v_ is smaller,

<sup>⋆</sup> This is the full version of an extended abstract that appeared in ISAAC [2]. <sup>⋆⋆</sup> Research funded by NSF grants CCF-1217314 and CCF-1536026. <sup>⋆⋆⋆</sup> Research funded by HKUST/RGC grant FSGRF14EG28. <sup>†</sup> Research funded by NSERC and the Canada Research Chairs Programme.

Marek Chrobak<sup>1**_⋆⋆_**</sup>, Mordecai Golin<sup>2**_⋆⋆⋆⋆_**</sup>, J. Ian Munro<sup>3†</sup>, and Neal E. Young<sup>1</sup>

<sup>1</sup> University of California -- Riverside, Riverside, California, USA <sup>2</sup> Hong Kong University of Science and Technology, Hong Kong, China <sup>3</sup> University of Waterloo, Waterloo, Canada

arXiv:1505.00357v5 [cs.DS] 9 Mar 2021

