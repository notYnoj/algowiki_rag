words. This process repeats until the entire block \(A'\) is a contiguous sorted run. This requires \(k_\#=\lceil lgm'/lgk\rceil-1\) passes of merging. The use of table sort in the first phase is to avoid the overhead of constructing the selection tree in the second merging phase. For the formal step-by-step procedure and extended analysis, see [App. B].

\(\blacktriangleright\) **Lemma 2.3.** _For any constant c, a sequence of_ \(m'=O(lg^cm)\) _active elements can be sorted using no more than_ \(m'lgm'+o(m')\) _comparisons and_ \(O(m')\) _movies if given a merge buffer of_ \(m'\) _buffer elements._

**Proof.** Each merge pass requires at most \(m'lgk+O(m')\) comparisons. In the final pass, there are only \(k'=\left\lceil m'/k^{k_\#}\right\rceil\) runs, so it needs only \(m'\left\lceil lgk'\right\rceil+O(m')\) comparisons. Summing over the initial run sorting and all merge passes, the total comparison cost satisfies

