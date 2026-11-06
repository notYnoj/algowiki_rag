<tbc>intermediate abstractions -- all of these abstractions can be viewed in some way as a relaxation of (tight) compaction; but each relaxation is of an incomparable nature. We will first define all these intermediate abstractions, and then we explain our blueprint for getting an optimal tight compaction circuit.

**Intermediate abstractions.** We rely the following intermediate abstractions -- among them, the approximate splitter and the sparse loose compactor are new abstractions.

• _Lossy loose compaction_. Let \(\alpha\in(0,1)\). Given an array of length _n_ containing at most _n/_128 _real_ elements and all remaining elements are _fillers_, an \(\alpha\)-lossy loose compactor compresses the array by a half, losing at most \(\alpha n\) real elements in the process.<tbc>

• _Approximate splitter_. Let \(\beta\in(0,1/4]\) and let \(\alpha\in(0,1)\). An \((\alpha,\beta)\)-approximate splitter solves the following problem: we are given an input array containing _n_ elements each marked with a 1-bit label indicating whether the element is _distinguished_ or not. It is promised that at most \(\beta\cdot n\) elements in the input are distinguished. We want to output a permutation of the input array, such that at most \(\alpha n\) distinguished elements are not contained in the first \(\lfloor\beta n+n/64\rfloor\) positions of the output.<tbc>

• _Approximate tight compaction_. Let \(\alpha\in(0,1)\). Given an input array containing _n_ elements, each with a 1-bit key, an \(\alpha\)-approximate tight compactor outputs a permutation of the input array, such that at most \(\alpha\cdot n\) elements in the output are misplaced. Here, the _i_-th element in the output is said be misplaced iff its key disagrees with what the _i_-th smallest key in the input array.<tbc>

• _Sparse loose compactor_. Let \(\alpha\in(0,1)\). An array of length _n_ is said to be \(\alpha\)-sparse if there are<tbc>

ProposeAcceptFinalize, const-degree expander, log log iterations (Pippenger [Pip96])
1 -lossy loose compact (output size n/2)
[ALS'21]-style bootstrapping [ALS21] with new tricks using near-sort, $7
1 1
1 4)-approx sparse splitter
Final circuit size: nw . poly log* n depth: O(log0.1 n)
Pippenger-style recurse [Pip96] for log log iterations, $12
ProposeAcceptFinalize re-parameterized with (poly log n)-degree expander and log log iterations + (poly log)-depth tight compact [Pip96,ALS21], $13
1 -approx tight compact (output size n/ log n)
poly log n -sparse loose compact (output size n/ log n)
Circuit size: nw . poly log* n depth: O(log0.2 n)
AKS [AKS83]
Circuit size: O(nw) depth: O(logn)
Circuit variant of Asharov et al. [AKL+20b, Algorithm 5.2], $14
tight compact
Circuit size: nw . poly log* n depth: O(logn)
Figure 1: Blueprint of our tight compaction circuit. The light blue parts represent our new abstractions or constructions. Rounded boxes represent the intermediate abstractions.
Figure 1: Blueprint of our tight compaction circuit. The light blue parts represent our new abstractions or constructions. Rounded boxes represent the intermediate abstractions.

