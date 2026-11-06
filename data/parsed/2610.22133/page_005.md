<tbc>Here MM(_k,m,n_) denotes the running time of multiplying a \(k\times m\) Boolean matrix by an \(m\times n\) Boolean matrix.

**Lemma 4.2.** _Given two Boolean matrices A and B of size_ \(s\times n\) _and_ \(n\times n\)_, one can construct in time_ O(_n_<sup>2</sup>+_ns_) _an instance of the induced subgraph connected component problem on a_ 2_n-node graph with a set of size s_=|S|_, such that solving this instance yields the product AB._

As a corollary to Main Theorem 1, we obtain algorithms for the following problems (for details on how the preceding algorithm implies these results, we refer the reader to [KS06, Corollaries 3.2, 3.3, and 3.4]).

**Corollary 1.1.** _The following problems have a deterministic_ \(\tilde{\mathcal{O}}(n^\omega)\)_-time algorithm on an n-node input graph: computing neighborhood-deleted components in a graph, listing all extremities in a graph and determining whether the graph has a star cut-set, determining whether two fixed vertices x, y are a two-pair._

We also obtain an \(\tilde{\mathcal{O}}(n^\omega)\)-time algorithm for recognizing AT-free graphs (a related result was previously known only for claw-free AT-free graphs in matrix multiplication time [HK02]), as well as for listing all dominating pairs and two-pairs.

**Main Theorem 2.** _There is a deterministic_ \(\tilde{\mathcal{O}}(n^\omega)\)_-time algorithm that determines if a graph is AT-free._

Previously, the fastest time algorithm for recognizing AT-free graphs ran in O(_n_<sup>2.82</sup>) time [KS06].

**Main Theorem 3.** _There is a deterministic_ \(\tilde{\mathcal{O}}(n^\omega)\)_-time algorithm for listing all dominating pairs._

This improves upon Spinrad and Kratsch’s O(_n_<sup>2.79</sup>) running time.

**Main Theorem 4.** _There is a deterministic_ \(\tilde{\mathcal{O}}(n^\omega)\)_-time algorithm for listing all two-pairs._

The previous best running time was Spinrad and Kratsch’s O(_n_<sup>2.79</sup>).

We remark that all our algorithms are deterministic, and the underlying algorithms are remarkably simple. Although the algorithms themselves are straightforward, the proofs establishing their correctness are occasionally more complex (e.g., recognition of AT-free graphs); in such cases, the more involved proofs reveal new structural insights into the problems.

Finally, we study two related problems not addressed in the work of [KS06]. While we only achieve partial progress on these, we suspect their time complexity may strictly exceed \(\mathcal{O}(n^\omega)\). Their fine-grained complexity offers an interesting direction for future study, so we leave both problems open to the community.

**Induced Non-shortest Paths.** The first problem we propose is a generalization of verifying whether two vertices form a _two-pair_. More generally, given two vertices _u,v_ at distance _d(u,v_)=_k_, one can ask whether there exists an induced (equivalently, chordless) path between them that is not a shortest path (note that every shortest path is necessarily induced). Following previous work, we call such a path a _uv-trail_. In this terminology, the problem of listing two-pairs is the all-pairs version of this problem restricted to vertex pairs with _k_=2.

This problem is not new: it was recently introduced by Berger, Seymour, and Spirkl [BSS21], who gave an O(_n_<sup>18</sup>)-time algorithm for a single fixed pair. This was very recently improved by Chiu and Lu [CL24] to \(\mathcal{O}(n^{2\omega})\), i.e., the time required to multiply two \(n^2\times n^2\) matrices. No lower bound was provided, nor any evidence that matrix multiplication is necessary. We show that matrix multiplication seems necessary, even for a single pair with _k_=3, by giving a reduction from triangle detection.

**Lemma 4.16.** _For any_ \(k\ge 3\)_, suppose there exists an algorithm that, in time_ \(\mathsf{T}=\Omega(n^2)\)_, determines whether an n-node graph_ **G** _contains a uv-trail for two vertices u,v with d(u,v_)=_k. Then there is an algorithm solving triangle detection in time_ O(T).



