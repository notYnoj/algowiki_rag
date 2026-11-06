Consequently, for every fixed \(S\subseteq V\) and every \(i\ge\alpha\),

\(Pr[A_i(1)\cap S=\emptyset|R]\le\frac{Pr[A_i(1)\cap S=\emptyset]}{Pr[R]}\)<br>
\(\le 2\left(1-\frac{1}{2^{2i}}\right)^{|S|}\)<br>
\(\le 2exp\left(-\frac{|S|}{2^{2i}}\right).\)

Thus, if \(|S|=\tilde{O}(2^{2i})\), then A<sub>i</sub>(1), and hence A<sub>i</sub>, intersects S with high probability.

## C Proof of Theorem 3.4

For our context \(i\ge\alpha\). Let us now prove the bounds in the lemma.

1. Ball size bound<tbc>

<tbc>The proof follows the same structure as that of Theorem 3.7; we highlight only the necessary modifications here. Let S be the set of the \(\tilde{O}(2^{2i})\) vertices closest to s in G. Applying the same probabilistic argument used in Theorem 3.7, we can show that with high probability, at least one vertex from S is sampled into A<sub>i</sub>. Consequently, the size of the ball is bounded, that is, \(|ball_i(s)|\le|S|=\tilde{O}(2^{2i})\).<tbc>

2. Running time and the exact distance property for vertices in the ball and to pivots<tbc>

<tbc>We run FINDBALLS&CLUSTERS(A<sub>i</sub>,i) for all \(\alpha\le i\le loglogn-1\). Using an argument similar to Theorem A.2, the running time of FINDBALLS&CLUSTERS(A<sub>i</sub>,i) is \(\tilde{O}(n^2)\) for a fixed \(i\le loglogn-1\). Over all i, the running time remains \(\tilde{O}(n^2)\).<tbc>

<tbc>We first run a multisource BFS from all vertices in A<sub>i</sub> in FINDBALLS&CLUSTERS(A<sub>i</sub>,i). This computes, for every vertex, its pivot and its distance to that pivot. Next, for each \(s\in V\) , we run a BFS up to distance |s pivot<sub>i</sub>(s)|-1. This step computes the exact distance from s to every vertex in ball<sub>i</sub>(s). Consequently, after executing FINDBALLS&CLUSTERS(A<sub>i</sub>,i), we obtain est(s,v)=|sv| for every \(v\in ball_i(s)\).

This completes the proof of Theorem 3.4.

## D Proof of Theorem 3.9

The lemma follows directly from Theorem 3.7. We prove the claim for the sa<sub>i</sub> path; the argument for the tb<sub>i</sub> path is symmetric.

Assume that no vertex on the sa<sub>i</sub> path (except may be a<sub>i</sub>) lies in A<sub>i</sub>, since otherwise it would serve as a candidate for a<sub>i</sub> or u<sub>i</sub>. Suppose, for contradiction, that there exists a vertex \(z\neq a_i\) on the sa<sub>i</sub> path with degree \(>\tilde{O}(2^{2i})\). By Theorem 3.7, z has a neighbor in A<sub>i</sub> with high probability. Since z lies on the sa<sub>i</sub> path, we have |sz|\<|sa<sub>i</sub>|. Hence, z is closer to s than a<sub>i</sub> and satisfies \(|zpivot_i(z)|\le 1\). This contradicts Theorem 3.8, which defines a<sub>i</sub> as the closest such vertex.

Therefore, every vertex on the sa<sub>i</sub> path, except possibly a<sub>i</sub>, has degree at most \(\tilde{O}(2^{2i})\). Conse quently, every edge on the sa<sub>i</sub> path has degree \(\tilde{O}(2^{2i})\). This proves Theorem 3.9.

## AI Disclosure

AI Disclosure: We used an AI language model (e.g., Gemini/ChatGPT/Claude) to assist with proofreading, improving clarity, and checking the logical correctness of claims/equations. The authors verified the correctness and originality of all content including references.

