## A Column-wise Enumerator: Full Details

### Algorithm Description

#### Column-wise expansion.

We organize the search by _columns_ of increasing subset size. The state space consists of canonical partial sums \(\sigma\) paired with their current prefix (bitmask) _R_. At column _k_ we extend each canonical state of size _k_-1 by adding one unused element \(a_i\notin R\), producing \(\sigma'=\sigma+a_i\) with prefix \(R'=R\cup\{a_i\}\). If \(\sigma'\) is new, or if \(R'\) is lexicographically smaller than the current representative, we update the representative of \(\sigma'\). This yields at most \(O(U\cdot n)\) total _extension attempts_ from canonical states. As established in Section 4.1, the overall complexity is governed by the cost of canonicality checks during collisions.

#### High-density handling.

To guarantee correctness in high-collision regimes, we impose a deterministic canonicalization based on lexicographic order of index bitmasks: scan indices \(1\rightarrow n\) and prefer 0_\<_1 at the first differing position. Each numeric sum \(\sigma\) keeps exactly one _canonical_ representative (lex-minimal mask), which prevents non-deterministic pruning and ensures a single expansion path per sum.

### 4-Column Litmus Test.

The real-time collision checks enable a quick hardness probe. By running only the first _k_ columns (e.g., _k_=4) in **polynomial** time _O(n<sup>k</sup>_), we empirically estimate the early collision rate. High early collision typically predicts small _U_, signaling an "easy" instance; low early collision predicts a large _U_, signaling a harder, unstructured input. This offers a lightweight pre-check before any full exponential exploration.

### Reader’s Guide (what to look for).

• _Separation of concerns:_ (i) enumeration of prefixes, (ii) canonical tie-breaking, (iii) suppression- on-overwrite. Any scheduler (BFS/DFS/priority) that respects these yields the same canonical set.<tbc>

• _Spec vs. implementation:_ We first give a _minimal recursive_ specification that makes the logic transparent; the column-wise iterative code that follows is the optimized implementation used in our analysis.<tbc>

• _Where the_ \(O(U\cdot n^2)\) _comes from:_ \(O(U\cdot n)\) extension attempts times _O(n_) lex-compare cost on collisions, with suppression ensuring each canonical state expands at most once.<tbc>

