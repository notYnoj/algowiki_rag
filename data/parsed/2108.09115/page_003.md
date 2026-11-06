<tbc>distance between two long strings; and (ii) works on approximate closest pair or nearest neighbor among a large number of short strings \[ADG<sup>+</sup>03, Ind04, CK06, OR07, LDHO14, ARW17, Rub18b, CGL<sup>+</sup>19\]. Our preprocessing algorithms are most appealing when both the length and number of strings are large.

Preprocessing is also closely related to sketching \[BZ16, BJKK04\]. With an efficient sketching algorithm, we can preprocess a string to compute a small-sized sketch and then only compare the sketches during querying. The state of the art result in edit distance sketching has a preprocessing time of \(\tilde{O}(nk^2)\) and query time of _poly(k_log_n_) \[BZ16\]. Our algorithms get significantly better trade- offs. There are numerous works on related but different models such as computing embedding of edit distance \[ADG<sup>+</sup>03, OR07, CK06, CGK16\], document exchange protocols \[Jow12, BZ16, Hae19\] and error-correcting codes for insertions and deletions \[BGZ16, HRS19, Hae19\].

## Contributions.

In the preprocessing model we provide much faster and simpleralgorithms that output much better alignments:

**Permutation-LCS** If the LCS between two permutations has length _n-k_, we can compute it _exactly_ with _O(n_log(_n_)) preprocessing and _O(k_log(_n_)) query time. Contrast this result with \[AN10\] where in \(\tilde{O}(\frac{n}{k}+\sqrt{n})\), the ulam distance can be approximated to within a large constant factor.

**Small edit distance** For general strings, if their edit distance is at most _k_, we can compute it _exactly_ with _O(n_log(_n_)) preprocessing and _O(k_<sup>2</sup>log(_n_)) query time. Contrast this result with \[GKS19\] where in \(\tilde{O}(\frac{n}{k}+k^3)\) time, one can distinguish if edit distance is below _k_ or above \(\Theta(k^2)\).

**Approximate edit distance** For the most general input, we can approximate the edit distance to within factor (7+_o_(1)) with preprocessing time _O(n_<sup>2</sup>log(_n_)) and query time _O(n_<sup>1.5+_o_(1)</sup>). Contrast this result with \[And19\] where a \(f(\epsilon)\)-approximation for edit distance can be computed in time \(O(n^{1.5+\epsilon})\) (\(f(\epsilon)\) goes to infinity as \(\epsilon\) decreases).

**What if we only preprocess one string?** This setting is much harder, but we can still beat state of the art without preprocessing, namely distinguish _k_ vs 3_k_<sup>2</sup> with \(\tilde{O}(n)\) preprocessing and \(\tilde{O}(n/k+k^2)\) query time.

These strong improvements run contrary to the fine-grained complexity rule of thumb that preprocessing inputs does not help \[WW18\]. We also formalize a few conditional hardness results establishing limitations of preprocessing for fast string alignment:

**Exact alignment** We show that assuming (BP)-SETH, even after arbitrary polynomial-time preprocessing, computing edit distance or LCS exactly requires near-quadratic query time.

**Approximate edit-distance** We show that if we can \(\alpha\)-approximate edit distance in truly-subquadratic query time with arbitrary polynomial preprocessing, then we can also \((\alpha+o(1))\)-approximate it in truly-subquadratic time without preprocessing (currently not known for any \(\alpha<3\)).

We remark that another related hardness result is known for the case where we only preprocess one string: Abboud and Vassilevska-Williams show that, assuming a nonuniform variant of SETH, even polynomial _space_ (exponential time) preprocessing doesn’t help to break the near-quadratic time barrier \[AW19\].

