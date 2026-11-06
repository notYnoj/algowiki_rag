detection. However, in the sparse setting, we give an algorithm that runs in the same slightly subquadratic runtime as we get from Theorem 1 for All-Edges Sparse Triangle. We define the problem in the usual way, but require the additional stipulation of bounded degree.

\(\blacktriangleright\) **Definition 23** (All-Edges Sparse Monochromatic Triangle)**.** _Let G be a tripartite graph whose vertex set is_ \(I\cup J\cup K\) _and_ |_I_|=|_J_|=|_K_|=_n. Let the maximum degree in the graph be_ \(O(n^\delta)\)_. The graph has colors along the edges; that is, there is a function_ \(c:E\rightarrow[n^2]\)_. For every edge_ \(e\in E\cap(I\times J)\)_, decide whether e participates in a monochromatic triangle._

**Reminder of Theorem 2.** There is a Las Vegas algorithm for the All-Edges Sparse Monochromatic Triangle problem that runs in expected time \(O(n^{1+2^\delta} logw)/w\).

**Proof of Theorem 2.** We will follow the proof of Theorem 1 fairly closely. We run the following slightly modified algorithm. For clarity, we will refer to the edge colors prescribed by _c_ as labels.

**1.** Randomly partition _K_ into \(n^\delta/logn\) color classes using a _O_(log_n_)-wise independent hash function.

**2.** Compress the name of each vertex in _K_ using a linear hash function: \(h:[n]\rightarrow[\mathsf{poly}(\ell)]\). Compress the names of the edge colors using another linear hash function \(h_c:[n]\rightarrow[\mathsf{poly}(\ell)]\).

**3.** For each vertex _i_ in \(I\cup J\), for every color class _S<sub>v</sub>_ in \([n^\delta/logn]\), write down a compressed list that describes every node _x_ in \(N(i)\cap S_v\). For every _x_, we will store its hash concatenated with the hash of the label _c(i,x_).

**4.** To respond to an edge query (_i,j_), for every color class, compute the set intersection of the compressed lists associated with _i_ and _j_’s neighbors with that color. If the intersection is non-empty and the label of the two neighbors matches the label of (_i,j_), we have found a monochromatic triangle.

Let _k_ be \(max_{v\in[n^\delta/w],u\in(I\cup J)}|N(u)\cap S_v|\), the maximum number of neighbors in _K_ a given vertex in \(I\cup J\) has in a particular color class. By the same argument as in the All-Edges setting, we have that after color-coding as in Step 1, _k=O(w_) with high probability. As before, our goal is to write down matrices _A_ and _B_ of dimension \(n\times\sqrt{n}\) and \(\sqrt{n}\times n\) that capture _I_ and _J_’s edges to _K_, respectively. We now choose two linear hash functions \(h_v:[n]\rightarrow[k^3]\) as before, and \(h_c:[n^2]\rightarrow[k^3]\) for hashing the edge labels. Suppose vertex _i_ in _I_ has an edge with label _c<sub>i</sub>_ to the _v_th vertex in the _k_th color class of _K_. The associated hash value is _h<sub>v</sub>(v_)||_h<sub>c</sub>(c<sub>i</sub>_). We compute these hashes for all (at most) _k_ such vertices in \(N(i)\cap S_v\), put them in sorted order, and word-pack them into \(k\ell/w\) words. Again, we will have hash collisions, so we can store a mapping from the hashes in the image to the vertices in the preimage. This preprocessing (across all vertices and color classes) takes _O(n_<sup>1.5</sup>log_n_) time and _O_(poly(log_n_)) random bits.

Thus, for a given edge query (_i,j,c(i,j_)), our task is to decide whether there exists a _v_ such that the associated sets \(N(i)\cap S_v\) and \(N(j)\cap S_v\) have nonzero intersection and all three labels match. We can use our compressed list operations to solve this problem slightly faster than brute force. The chunk length is \(2\ell\), since we have concatenated the hashed color class indices with hashed labels. As before, if we fix a color class and look at the associated packed lists \((N(i)\cap S_v\) and \(N(j)\cap S_v)\), by Claim 17, we can produce an indicator mask that conveys their intersection in time _O_(loglog_n_). However, we need to exclude triangles that are not monochromatic.

