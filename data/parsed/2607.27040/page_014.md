\(\blacktriangleright\) **Theorem 3.2.** _The input array_ A_, consisting of n elements, can be sorted in-place using no more than n_lg_n+O(n_lg<sup>(_t_)</sup>_n_) _comparisons, O(tn_) _moves, and O(n_lg_n_) _arithmetic operations._

**Proof.** When performing the in-place conversion across varying block sizes _m_, small instances may violate the parameter constraint \(2\le\lceil lg^{(t)}m\rceil\le lglgm+1\). To ensure the deterministic scheme remains valid for every subproblem, we set _g_<sub>1</sub>=2<sup>max(2,\(\lceil lg^{(t)}m\rceil\))</sup> for each instance sorting _m_ active elements. This adjustment adds at most a linear number of comparisons per subproblem, preserving the asymptotic performance of Theorem 2.7.

Mirroring Theorem 3.1, substituting \(C'(m)=mlgm+O(mlg^{(t)}m)\) and \(M'(m)=O(tm)\) from Theorem 2.7 into (11) yields _n_lg_n+O(n_lg<sup>(_t_)</sup>_n_) comparisons and _O(tn_) moves. Similarly, arithmetic operations are also bounded by _O(n_lg_n_). These upper bounds hold unconditionally as Theorem 2.7 provides worst-case bounds.

## 4 Concluding Remarks

In this paper, we have addressed the exact operational complexity of in-place sorting, establishing that the fundamental lower bound of \(nlgn+\Omega(n)\) total operations is tight for in-place randomized algorithms (with exponentially high probability). By resolving the previous inefficiencies present in [4] via introducing a novel ordered set, optimized cache structures, and an optimal small sort, we have achieved the ultimate goal stated in [4, 10] with exponentially high probability: sorting in-place using only _n_lg_n+O(n_) comparisons and _O(n_) moves.

We leave as an open problem the task of retaining the bound of _n_lg_n+O(n_) total operations in the worst case. The deterministic cache line stands as the only remaining obstacle to optimality, limiting the deterministic approach at _n_lg_n+O(n_lg<sup>(_t_)</sup>_n_) comparisons and _O(tn_) moves (where _t_ is an integer parameter satisfying \(2\le t\le lg*n-1\)), which results in a slightly looser total operation bound of _n_lg_n+O(n_lg<sup>∗</sup>_n_) when _t_≈lg<sup>∗</sup>_n_. However, this is sufficient to answer the open problem from [4] for improvements on their upper bound of _n_lg_n+O(n_lg_n_) comparisons and _O(n_) moves.

All in-place algorithms are unstable as the buffer elements are permuted arbitrarily. Whilst the deterministic additional memory algorithm is stable on active elements, it requires a completely distinct buffer to operate stably and in-place. As existing methods of collecting such a distinct buffer incur \(\Omega(nlgn)\) comparisons of overhead [1], we have not yet achieved a stable, in-place sorting algorithm that makes _n_lg_n+o(n_lg_n_) comparisons and _O(n_) moves (i.e. _n_lg_n+o(n_lg_n_) total operations). That problem remains open. The best known stable bound stands at _O(n_lg_n_) comparisons and _O(n_) moves [1].

## AI Disclosure

AI tools were used exclusively for: (i) standard copy-editing tasks, including language refinement of the authors’ own text (Gemini, Perplexity), and (ii) to assist in converting the authors’ hand-drawn diagrams into TikZ code (Gemini). No additional diagrammatic details were introduced by the AI. The technical aspects, including all algorithms and proofs, were formulated entirely by the authors, who assume responsibility for the entire content.

