## 1 Introduction

The _edit distance (ED)_ between two strings _X_ and _Y_ , henceforth denoted ED(_X,Y_), is the minimum number of character insertions, deletions, and substitutions required to transform _X_ to _Y_ . The complexity of edit distance and its maximization counterpart<sup>1</sup>, _longest common subsequence (LCS)_, is a long-standing, central problem in algorithm design, with important applications, especially in bioinformatics. The simple quadratic-time dynamic programming solution is core material for undergraduate algorithms; this running time has been improved by one or two log factors (depending on the exact access model) \[MP80, Gra16\]. Despite extensive research for over half a century<sup>2</sup>, no better algorithms for exact ED or LCS are known.

Indeed, in one of the flagship successes of fine-grained complexity, \[BI18\] showed that there are no exact algorithms for Edit Distance running in "truly subquadratic" time, namely it is impossible to improve by \(n^\delta\) for any constant \(\delta>0\), assuming fine-grained complexity hypothesis SETH (see also e.g., \[AWW14, ABW15, BK15\]). Furthermore \[AHWW16, AB18\] showed that improving even by a few log factors would refute other fine-grained complexity assumptions and imply new circuit complexity lower bounds.

Given the limitations of exact algorithms, and especially in light of fine-grained hardness results, approximation algorithms for Edit Distance have been extensively studied: A sequence of earlier works gave super-constant-factor approximation factors in _n_<sup>1+_o_(1)</sup> time \[ADG<sup>+</sup>03, BEK<sup>+</sup>03, BJKK04, BES06, OR07, AK10, AN10, AKO10, AO12\]. More recently, constant-factor approximation algorithms times were obtained by \[CDG<sup>+</sup>20, BEG<sup>+</sup>21, And20, BR20, GRS20, KS20b, AN20\]. The current state of the art has several algorithms with different trade-offs between running time and approximation (see  1). While we cannot cover all the techniques used in previous work on approximate edit distance, at a high level we seem to have hit a fundamental obstacle: all known constant-factor approximation algorithms for ED rely on a triangle inequality technique that inherently incurs at least a 3-factor in the approximation \[Rub18\]. No better-than-3-approximation algorithms are known with any non-trivial running time.

Remarkably, good multiplicative approximations for LCS are even more scarce than ED: despite significant attention (e.g., \[HSSS19, RS20, AV21, RSSS25, BCD23, HL23\]), for worst-case instances the best previous known approximation factor is just barely sub-polynomial \[Nos21\]. Furthermore, \[CGL<sup>+</sup>19\] shows that obtaining such approximation-time tradeoffs for approximate LCS with _deterministic_ algorithms would imply new breakthrough circuit lower bounds<sup>3</sup>.

### Main result

We give approximation schemes for ED and LCS, i.e., for any constant \(\varepsilon>0\), we get a \((1+\varepsilon)\)-approximation for ED and a \((1-\varepsilon)\)-approximation for LCS. Our approximation schemes run in time

\(\frac{n^2}{2^{log^{\Omega(1)}(n)}},\)

for two strings with total length _n_. This running time represents a quasi-polynomial improvement over the classical quadratic-time algorithms.

### Why this is interesting

<sup>1</sup>Technically, LCS is the complement of a variant of ED where substitutions are not allowed (or rather counted as 1 deletion + 1 insertion). <sup>2</sup>Beating the quadratic time was proposed as an open problem as early as \[CKK72\]. <sup>3</sup>Specifically, Item 3 of Theorem 1.9 of \[CGL<sup>+</sup>19\] says that if a deterministic algorithm for LCS can obtain even a much weaker _O_(polylog(_N_))-approximation guarantee in \(N^2/2^{\omega(loglogN)^3}\) time, then NTIME\[2<sup>_O(n_)</sup>\] is not contained in non-uniform NC<sup>1</sup>.

