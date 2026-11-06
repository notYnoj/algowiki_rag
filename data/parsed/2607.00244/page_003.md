color yields an _r_(1+ln_n_)-approximate minimum coloring, by the classic analysis of Set Cover’s greedy algorithm. Moreover, \(n^{\Theta(1)/(loglogn)^2}\cdot\mathcal{O}(logn)=n^{\Theta(1)/(loglogn)^2}\).

We keep both proofs because the proof of Theorem 1 implements the above outline without the extra technicalities needed for Min Coloring.

We then delineate the tractability boundary of _k_-Independent Set (_k_-IS for short) on graphs of bounded merge-width. Strictly speaking, merge-width is a _family_ of parameters. For every positive integer _r_, the radius-_r_ merge-width, denoted by mw<sub>_r_</sub>, must be bounded by a function of _r_, for the merge-width itself to be bounded. Low-radius merge-width, think mw<sub>1</sub>, mw<sub>2</sub>, or mw<sub>_c_</sub> for some constant _c_, is of independent interest. There are some properties that only require these parameters to be bounded. Notably, classes of bounded merge-width were proven \(\chi\)-bounded by showing the stronger statement that classes of bounded mw<sub>2</sub> are \(\chi\)-bounded [6] (and the \(\chi\)-boundedness of classes of bounded mw<sub>1</sub> remains open).

Given radius-2<sup>_ck_<sup>2</sup></sup> merge sequences of bounded width<sup>2</sup> for some appropriate constant _c\>_0, _k_-IS admits a fixed-parameter tractable (FPT) algorithm [17]. In fact, this is more generally the case for first-order model checking. Dreier and Toruńczyk ask whether a simpler and faster algorithm could exist for _k_-Independent Set (and _k_-Dominating Set).

A related question is whether these problems admit FPT algorithms given radius-_r_ merge sequences of bounded width already in the regime _r_=O(1). We rule this out for any radius _r=o(k_), with a reduction from the W[1]-hard Grid Tiling problem [24] to _k_-IS. We ensure that the produced graphs have bounded radius-_r_ merge-width by spacing the Grid Tiling cells out with "paths of co-matchings" of length \(\Theta(r)\).

\(\blacktriangleright\) **Theorem 3.** \(\forall r=o(k)\)_, k-Independent Set is W[1]-hard in graphs of bounded mw<sub>r</sub>._

We then adapt the previous reduction to get the same statement for _k_-Dominating Set.

\(\blacktriangleright\) **Theorem 4.** \(\forall r=o(k)\)_, k-Dominating Set is W[1]-hard in graphs of bounded mw<sub>r</sub>._

**Future work.** Our work naturally leads to the following questions. Combining Theorems 1 and 2 and [4], we now know that, unless the ETH fails, the best approximation factor for Max Independent Set and Min Coloring lies somewhere between \(n^{\Theta(1)/(loglogn)^2}\) and \(n^{\Theta(1)/loglogn}\). Can one obtain matching bounds, up to constants in the exponent?

Ruling out a PTAS for MIS on graphs of bounded twin-width under the weaker assumption that \(\mathrm{P}\neq\mathrm{NP}\) remains open. Let us also mention the question of obtaining nontrivial approximation algorithms for these problems when the contraction sequence is _not_ provided.

Theorems 3 and 4 and [17] raise the question of the smallest radius _r(k_) such that _k_-Independent Set (and _k_-Dominating Set) is FPT on graphs given with a radius-_r(k_) merge sequence of bounded width. We now know that this radius is between \(\Omega(k)\) and 2<sup>O(_k_<sup>2</sup>)</sup>.

**AI disclosure.** After we proved Theorem 1, we suspected that the same result should hold for Min Coloring, and could probably be proven in a similar fashion. We delegated this adaptation to ChatGPT Pro 5.5 Extended Thinking. We provided it with the proof of Theorem 1 with a concise prompt asking for a possible transfer to Min Coloring. Its first response, produced after 17 minutes, pinpointed the places where the same proof would break. We then clarified that the task was the adaptation. After another 50 minutes, it provided a complete proof of Theorem 2. Although it follows the proof of Theorem 1 at a high level, this proof contains several new elements, notably the initial hardness result [5,

<sup>2</sup> witnessing that the radius-2<sup>_ck_<sup>2</sup></sup> merge-width is bounded; see Section 2.3 for the relevant definitions.

