computing an inner product modulo 2 is _not_ an AC0 operation. We sidestep this issue as follows: note that all of our hashing is done in the preprocessing step, and that we are only hashing _O(n_<sup>1.5</sup>) values. So although the hashes technically cannot be computed in AC0, we do not need to use word-level parallelism here: we can afford an extra _w_ factor in the running time of preprocessing. Note we also need at most _O_(poly(log_n_)) bits of randomness to specify the hash function.

So for every vertex \(i\in I\cup J\) and every color class _S<sub>v</sub>_, we can hash the elements of \(N(u)\cap S_v\), put them in sorted order, and write them down in compressed form using \(k\ell/w\) words. Note that we can have collisions here, so we will store a mapping from the hashes in the image to the vertices in the preimage (written down in sorted order), which requires \(O(n^{1+\delta} w)\) time. Again, we require _O_(poly(log_n_)) bits of randomness, all of which is used to build our word-packed lists in preprocessing.

When we receive an edge query (_i,j_), we need to determine for every color class _S<sub>v</sub>_ whether the associated sets \(N(i)\cap S_v\) and \(N(j)\cap S_v\) have nonempty intersection. If we fix a color class _v_ and look at the associated packed lists, by Claim 17, we can produce an indicator mask corresponding to their intersection in time _O_(log_w_). However, since we have hashed the vertex names, it is possible that items in the intersection are false positives. Thus, we need extract the values in the intersection, look them up in the preimage, and verify that the original entries match as well.

We first bound the probability of false positives. The probability that any two entries collide is 1_/k_<sup>3</sup>, and there are \(\genfrac(){pt}{2}{k}{2}\) pairs of entries, so we get at most 1/2_k_ collisions per color class per query in expectation. We then look up the true vertex names in the preimage. To do this, we can think of these as being written down in sorted order, where each value takes up one word. We then merge the two lists and compute the true intersection in time linear in the size of the preimage, which in expectation, is _O_(1_/k_<sup>2</sup>). We can also think of this cost as the number of collisions within the neighborhoods of _i_ and _j_. So the expected cost of checking all of these collisions for a particular color class is _O_(1_/k_), or linear in their number.

Recall that we have \(n^\delta/w\) color classes, so computing the indicator masks over all of them requires time \(O(n^\delta logw/w)\) per query. As a result, we can afford to spend asymptotically that same amount of time checking false positives. Let _P_ be the number of collisions we have to check. By construction, we have \(\mathbb{E}[P]=\frac{1}{2k}\cdot\frac{n^\delta}{w}=\frac{n^\delta}{2(1+\delta^\prime)w^2}\). By a Markov bound,

\(Pr\left[P\ge n^\delta logw/w\right]\le\frac{1}{2(1+\delta')wlogw}\le\frac{1}{2}.\)

Thus, as in the All-Edges Equality algorithm in Theorem 21, if we see more than \(n^\delta logw/w\) collisions, we rerun the query in a subsequent round of the algorithm. The number of queries required is upper bounded by \(n^{1+\delta}\cdot\sum_{i=0}^\infty 2^{-i}\le 2n^{1+\delta}\). Thus, we require a total of \(O(n^{1+\delta})\) queries, each of which takes \(O(n^\delta logw/w)\) time. As a result, we can compute All-Edges Sparse Triangle in expected time \(O(n^{1+2\delta} logw/w)\). \(\blacktriangleleft\)

## 5 Solving Other Triangle Problems Faster

We now look at other triangle problems whose algorithms can be improved using the techniques from above. We begin by looking at all-edges monochromatic triangle.

### 5.1 All-Edges Monochromatic Triangle Detection

Vassilevska, Williams, and Yuster gave a \(O(n^{(3+\omega)/2})\) time algorithm for the detection version of the problem [36]. Thus, in the dense case, it seems to be meaningfully harder than triangle

