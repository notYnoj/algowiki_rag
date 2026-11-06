with an edge of weight 0. Then, we do a BFS from X. Using this process, we can find \(pivot_\alpha(s)\) and \(|spivot_\alpha(s)|\) for every \(s\in V\). The time taken by this multi-source BFS is \(\tilde{O}(m)=\tilde{O}(n^2)\).

Subsequently, for each \(s\in V\), a BFS is performed up to distance \(|spivot_\alpha(s)|-1\) from s, covering precisely \(ball_\alpha(s)\) and recording exact distances, so est(s,v)=|sv| for each \(v\in ball_\alpha(s)\). Clusters are maintained alongside the balls.

We now bound the number of edges explored in the BFS for a single vertex s. To compute this BFS, we only need to process vertices strictly inside the \(ball_\alpha(s)\) or at a distance \(\le|spivot_\alpha(s)|-2\) from s. Every vertex strictly inside \(ball_\alpha(s)\) has degree at most \(\tilde{O}(2^{2^\alpha})\) as otherwise \(|ball_\alpha(s)|\ge\tilde{O}(2^{2^\alpha})\) contradicting Theorem A.1. Thus, the BFS from s processes at most \(\tilde{O}(2^{2^\alpha})\) vertices each having degree \(\tilde{O}(2^{2^\alpha})\). Thus, the BFS of s takes \(\tilde{O}(2^{2^{\alpha+1}})\) time. Summing over all vertices, the overall time taken by \(\text{FINDBALLS&CLUSTERS}(A_\alpha,\alpha)\) is \(\tilde{O}(n\cdot 2^{2^{\alpha+1}})=O(n^2)\) time (since \(\alpha\le loglogn-1\)).

We now state a lemma from Thorup and Zwick \[TZ01\] that bounds the maximum cluster size and the number of iterations required by FINDCENTERS. We refer the reader to \[TZ01\] for the complete proof.

**Lemma A.3** (Proof of Theorem 3.1, \[TZ01\])**.** _For every vertex_ \(w\in V\), \(|cluster_{A_\alpha}(w)|=O(2^{2^\alpha})\) _deterministically. Furthermore,_ FINDCENTERS _runs for an expected_ \(\tilde{O}(1)\) _iterations._

We now discuss the guarantees given by FINDCENTERS

(B1) Size of \(A_\alpha\)<br>
In each iteration of FINDCENTERS, we sample a set of size \(\tilde{O}\left(\frac{n}{2^{2^\alpha}}\right)\) from W. Using Theorem A.3, since FINDCENTERS runs an expected \(\tilde{O}(1)\) times, the total number of vertices added to \(A_\alpha\) is \(\tilde{O}\left(\frac{n}{2^{2^\alpha}}\right)\) in expectation. Therefore, the preceding lemma bounds the size of \(A_\alpha\) only in expecta tion. For our purposes, however, we need to bound the size of \(A_\alpha\) with high probability.<tbc>

(B2) Size of \(ball_\alpha(\cdot)\) and \(cluster_\alpha(\cdot)\)<br>
Using Theorem A.1, ball size is bounded with high probability. And by Theorem A.3, cluster size is bounded deterministically.<tbc>

(B3) Running time of FINDCENTERS<br>
In a single iteration of the while loop in FINDCENTERS, we perform three main operations:<br>
(a) Sample vertices from W. This takes O(n) time.<br>
(b) Execute FINDBALLS&CLUSTERS\((A_\alpha,\alpha)\). Using Theorem A.2, this step takes \(\tilde{O}(n^2)\) time.<br>
(c) Recompute the set W. Since the clusters have already been computed, this step requires only O(n) time.<br>
Overall, a single iteration takes \(\tilde{O}(n^2)\) time. By Theorem A.3, the loop in FINDCENTERS runs for an expected \(\tilde{O}(1)\) iterations. Therefore, the total running time of FINDCENTERS is \(\tilde{O}(n^2)\) in expectation.

At this stage, we nearly satisfy the conditions of Theorem 3.5. However, (B1) and (B3) currently hold only in expectation, whereas we require both the size of \(A_\alpha\) and the overall running time to be bounded with high probability. We now present a modified procedure, MODIFIEDFINDCENTERS, designed to achieve these high-probability guarantees.

**Algorithm 11:** MODIFIEDFINDCENTERS

**while** _true_ **do**

**2** Run FINDCENTERS, terminating early if it runs more than \(\tilde{O}(1)\) iterations

**3 if** FINDCENTERS _completes within_ \(\tilde{O}(1)\) _iterations_ **then**

**4** \(A_\alpha\leftarrow\) the set returned by the above invocation of FINDCENTERS

**5 return** \(A_\alpha\)

