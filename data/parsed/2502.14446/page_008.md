### 5.3 Index construction and size

We now consider the contribution to the running time of Algorithm 1 given by the hash index and derive its space complexity.

Lemma 5.6. _The hash construction at line 1 of Algorithm 1 takes time_ \(O(D\cdot K\cdot L\cdot nlogn)\).

Proof. For each multidimensional subsequence we have to evaluate \(D\cdot K\cdot L\) hashes. For a fixed hash function we can compute all the dot products in _O(n_log_n_) time, using the cyclical convolution theorem. The result follows. □

Given that for each of the _n_ subsequences we have to store, in each of the _L_ repetitions, a total of _D_ hashes of length _K_ we have the following.

Theorem 5.7. _Algorithm 1 has space complexity proportional to_ \(O(K\cdot L\cdot D\cdot n)\).

## 6 IMPLEMENTATION DETAILS

In this section, we describe the key aspects of the implementation that impact the algorithm’s running time and its motif discovery capabilities. Namely, the number of hash evaluations and comparisons and the challenge of not knowing the dimensionality of the motifs to discover.

### 6.1 Index building

_Setting the quantization width r._ Recall from Equation 4 the formulation of the hash function we use. Even though the choice of the parameter _r_ does not compromise the correctness of the algorithm, it is fundamental since it influences the performance. A value that is too high will group many subsequences together at long indices, mitigating the filtering effect of LSH, a value that is too low will separate even the smallest perturbation between subsequences, forcing the algorithm to visit shorter prefixes. To deal with this parameter automatically, the algorithm adopts an estimation-based heuristic.

First we sample a number of random vectors from ∼N(0,1), computing their dot product with a random sample of subsequences from the time series. This produces an estimate of the distribution of the values that are discretized by Equation 4.

Then, we discretize this empirical distribution into 256 equal- width buckets. The width of these buckets will be used as the parameter _r_ in the hash function. The rationale is that by doing so we will be able to represent each hash value with a single byte.

Note that this heuristic can be implemented efficiently by leveraging on the _cyclical convolution theorem_, the same method used by MASS for the _Distance Profile_ \[43\]. We can obtain, with one convolution between one of the random vectors and the sample of the time series, all the dot products for that vector.

_Tensoring._ Tensoring is a technique to reduce the number of evaluations for the hash functions \[12\]. Let H be a LSH family and \(K,L\ge 1\) integers. For \(m=\sqrt{L}\), we define H_<sub>l</sub>_ as a set of _m_ hash functions sampled from \(\mathcal{H}^\frac{K}{2}\) and similarly for H_<sub>r</sub>_. Then \((h_a,h_b)\in\mathcal{H}_l\times\mathcal{H}_r,1\le a,b\le m\) provides _m_<sup>2</sup> repetitions with _Km_ evaluations. Furthermore, let us define for \(1\le j\le L\):

\(h_{K,j}=\left(h_{\frac{K}{2},l},h_{\frac{K}{2},r}\right)\in\mathcal{H}_l\times\mathcal{H}_r\text{where}\left\{\begin{array}{ c c }
l=j\div\sqrt{L} &  \\
r=jmod\sqrt{L}
\end{array}\right..\) (10)

The resulting hash is obtained from interleaving values from the selected left and right hash. This reduces the hash evaluations from \(K\cdot L\) to \(K\cdot\sqrt{L}\) at the cost of losing independence between repetitions. To accommodate this change we give this alternative formulation of Lemma 5.2, omitting the proof for the sake of space.

Lemma 6.1. _Under the same conditions of Lemma 5.2, using the tensoring approach, the probability that W(a,b)\<d in all previous iterations is upper bounded by_

\(\left\{\begin{array}{ c c }
P_t(i/2,j) &  \\
P_t(i/2,j)\cdot P_t((i+1)/2,L-j) & 
\end{array}\right.\)

_where_ \(P_t(i',j')=(1-p^{\lceil i^\prime\rceil})^{j^\prime\div\sqrt{L}}\cdot(1-p^{\lfloor i^\prime\rfloor})^{j^\prime mod\sqrt{L}}\).

Using Lemma 6.1 in the stopping condition of Algorithm 1 maintains the correctness guarantees of Lemmas 5.3 and 5.4.

_Corollary_ 5.6.1. With the tensoring approach the index construction takes time proportional to \(O(D\cdot K\cdot\sqrt{L}\cdot nlogn)\).

### 6.2 Index traversal

_Comparisons on the fly._ In Algorithm 1, maintaining the structure of line 4 at runtime is very expensive, since it would require quadratic space to store the weights for, potentially, each pair of subsequences. To deal with this problem, while maintaining the same theoretical approach, we just scan the index over each dimension and every time a unidimensional collision is seen we immediately compute _W(a,b_), if greater or equal than the searched motif dimensionality _d_, we perform the insertion of the pair in the priority queue. This approach does not require any additional space at the cost of a slightly higher number of hash comparisons, since we may evaluate a colliding pair up to _D_ times.

_Duplicate collisions within the same repetition._ Our approach dynamically chooses the length of the composite hashes by progressively iterating on the prefixes of the full ones, this results in looking into prefixes of decreasing size. Consequently, collisions at level _i_ are a _superset_ of the collisions at level _i_+1, in order to avoid unnecessary distance computations, the algorithm will check if the colliding hashes appear at the level _i_+1, skipping the pair in the positive case.

### 6.3 Finding motifs of multiple dimensionalities

One of the critical points up to now is the fact that at input we require the number of dimensions _d_ that span the motif. In many real scenarios, it is possible to know only approximately the expected dimensionality of the pattern in a certain domain.

Our method can be easily extended to discover motifs spanning different dimensions, allowing the user to specify a range of dimensionalities _d<sub>low</sub>,d<sub>high</sub>_ of the motifs they want to discover. The data structure at line 3 of Algorithm 1 becomes a set of _d<sub>high</sub>-d<sub>low</sub>_+1 priority queues, which are independently updated during the discovery process. This allows the algorithm to reuse information from a single distance computation across the different requested dimensionalities. Since evaluating dist_<sub>d</sub>_ (**T**_<sub>a</sub>,_**T**_<sub>b</sub>_) for a pair of sub sequences requires computing \(dist\left(\mathbf{T}_a^f,\mathbf{T}_b^f\right)\forall f\in[D]\), we can

