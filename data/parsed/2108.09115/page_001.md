# Does Preprocessing help in Fast Sequence Comparisons?

**Abstract**

We study edit distance computation with preprocessing: the preprocessing algorithm acts on each string separately, and then the query algorithm takes as input the two preprocessed strings. This model is inspired by scenarios where we would like to compute edit distance between many pairs in the same pool of strings.

Our results include:

**Permutation-LCS** If the LCS between two permutations has length _n-k_, we can compute it _exactly_ with _O(n_log(_n_)) preprocessing and _O(k_log(_n_)) query time.

**Small edit distance** For general strings, if their edit distance is at most _k_, we can compute it _exactly_ with _O(n_log(_n_)) preprocessing and _O(k_<sup>2</sup>log(_n_)) query time.

**Approximate edit distance** For the most general input, we can approximate the edit distance to within factor (7+_o_(1)) with preprocessing time \(\tilde{O}(n^2)\) and query time \(\tilde{O}(n^{1.5+o(1)})\).

All of these results significantly improve over the state of the art in edit distance computation without preprocessing. Interestingly, by combining ideas from our algorithms with preprocessing, we provide new improved results for approximating edit distance without preprocessing in subquadratic time.

<sup>∗</sup>The Academic College of Tel Aviv-Yaffo. Email: `elazargo@mta.ac.il` †Stanford University. Email: `aviad@cs.stanford.edu` ‡University of California Berkeley. Work partially supported by an NSF CAREER Award 1652303, NSF HDR TRIPODS Grant 1934846 and an Alfred P. Sloan Fellowship. Email: `barnas@berkeley.edu`

Elazar Goldberg<sup>∗</sup> Aviad Rubinstein<sup>†</sup> Barna Saha<sup>‡</sup>

