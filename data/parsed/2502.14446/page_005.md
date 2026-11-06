Input :D-dimensional time series T, subsequence length w, number of motifs k, K max allowed number of concatenations, L max number of repetitions, dimensionality of the motifs to find d, failure probability \(\delta\)<br>
Output:{Set of the top-k motifs}, with probability \(1-\delta\)<br>
// Initialization<br>
for \(\mathbf{T}_a\in\mathbf{T}^w\), \(f\leftarrow 1\) to D, \(j\leftarrow 1\) to L do<br>
   compute \(h_{K,j}(\mathbf{T}_a^f)\);<br>
   TOP = PriorityQueue();<br>
   for \(i\leftarrow K\) to 1 do<br>
   for \(j\leftarrow 1\) to L do<br>
   \(E\leftarrow\emptyset\);<br>
   for \(f\leftarrow 1\) to D do<br>
   for \((\mathbf{T}_a,\mathbf{T}_b)\in\mathbf{T}^w\times\mathbf{T}^w:h_{i,j}^f(\mathbf{T}_a^f)=h_{i,j}^f(\mathbf{T}_b^f)\) do<br>
   if \((\mathbf{T}_a,\mathbf{T}_b)\notin E\) then<br>
   \(E\leftarrow E\cup\{(a,b)\}\);<br>
   \(W(a,b)\leftarrow 1\);<br>
   else<br>
   \(W(a,b)\leftarrow W(a,b)+1\);<br>
   for \((a,b)\in E\) do<br>
   if \(W(a,b)\ge d\) then<br>
   TOP.insert<br>
(<br>
**T**<br>
_a_<br>
,<br>
**T**<br>
_b_<br>
)<br>
)<br>
;<br>
   if |TOP|>>k then<br>
TOP.pop<br>
()<br>
   if \(|\text{TOP}|=k\wedge\text{STOP}(\text{TOP.max}(),i,j,\delta)\) then<br>
return TOP<br>
return true top-k by computing all pairs;

## 4 ALGORITHM

We now describe our algorithm, named MOMENTI (for _MOtifs in MultidimEnsioNal Timeseries_), to find the top-_k_ motifs in a multi- dimensional time series. Our algorithm has a user-defined error probability \(\delta\). At a high level, our algorithm is comprised of two main phases. First, it builds a LSH-based index of the time series subsequences, where the dimensions of all subsequences are hashed independently. Then the index is traversed to discover candidate motif pairs, until a data-dependent stopping condition is met. The pseudocode of our algorithm is presented in Algorithm 1.

_Index construction._ As we have seen in the previous section, two critical parameters in an LSH setup are the number of concatenations _K_ and the number of repetitions _L_. Furthermore, the hash<tbc>

<tbc>function of Equation (4) requires a quantization parameter _r_ to be set as well. We shall see how to automatically set _r_ later in Section 6.

For a time series **T**, setting _K_ and _L_ so to minimize the number of distance computations requires the knowledge of the motif distance _before_ we construct the index. To work around the fact that we, of course, do not know this distance beforehand, our index instead sets the _maximum K_ and _L_ values to be used in the second phase.

To construct the index of the subsequence of length _w_ of a multivariate time series **T** we first sample multiple independent composite hash functions of length _K_: one for each dimension \(f\in[D]\) and repetition \(j\in[L]\). As described in the previous section, this is achieved by simply sampling a random vector _a_ and a random value _b_ for each function. We denote the composite hash function at repetition \(j\in[L]\) for dimension \(f\in[D]\) with \(h_{K,j}^f\).

Then, for each subsequence **T**_<sub>a</sub>_, we compute multiple independent hash values: for each dimension \(f\in[D]\) and for each repetition \(j\in[L]\), we compute the _composite_ hash value of length _K_ of the vector \(\mathbf{T}_a^f\) using the corresponding hash function, that is we compute \(h_{K,j}^f(\mathbf{T}_a^f)\).

Note that a composite hash value can be seen as a string of _K_ integer values. A fundamental operation in the next phase will be retrieving, for a given dimension \(f\in[D]\) and repetition \(j\in[L]\), all the subsequences whose hash share the prefix of a given length. To efficiently support this operation, we construct an index on hash values consisting of a family of ordered vectors. Specifically, for each dimension \(f\in[D]\) and each repetition \(j\in[L]\), each vector indexes the string of _K_ hash values of all subsequences. By doing so, hash values with the same prefix appear in contiguous ranges of the array, providing higher locality of reference. In the following, for \(0<i\le K\) we denote with \(h_{i,j}^f(\mathbf{T}_a^f)\) the prefix of length _i_ of the hash value for the subsequence dimension \(\mathbf{T}_a^f\) in repetition _j_.

_Index traversal._ A key property of the index introduced in the previous paragraph is that very similar subsequences are likely to share long prefixes of their hashes. At the same time, due to the probabilistic nature of LSH it is not certain that similar subsequences share a long prefix in the first repetition.

We first give the intuition behind the algorithm, and then give all the details. Starting from the longest possible hash prefix, _K_, the _L_ repetitions are considered, focusing on each one on all pairs of subsequences sharing the same hash prefix: for each such pair we can compute the distance, which is used to rank candidate motif pairs in a priority queue. Furthermore, from the distance we can derive the collision probability by means of Equation (5). We use this probability to define a stopping condition that allows to rule out the event that the true motif has _not_ been seen in the repetitions considered so far. If the probability of this negative event is less than a user defined threshold \(\delta\) and the priority queue contains at least _k_ elements then the algorithm stops, returning the top-_k_ pairs in the priority queue. Otherwise the next iteration is considered, with a caveat: if the last of the _L_ repetitions is reached with the stopping condition not satisfied, then it means that hashes of length _K_ are too selective for the dataset at hand. Therefore, the process is restarted considering prefixes of length _K_-1. This procedure continues, potentially considering shorter and shorter prefixes, until the stopping condition is met.

**Algorithm 1:** MOMENTI

**Algorithm 2:** Stopping condition

