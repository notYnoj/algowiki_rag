When the fields have shrunk to \(\Theta(log(M/B))\) bits, the buffers for grouping by field values fit in memory, and scans complete the interchange directly. Only these buffer blocks must fit; the full stream may remain on disk. If the prefix is too short to supply enough segments, borrow a few high-order digits from the fields, process the remaining digits, and then move the borrowed digits to their destinations. Section 6 and the appendices handle these arrangements, general field widths and segment counts, and the buffering and recursion overhead.

### 4.4 From rearrangement to sorting

For an array of at most _M_<sup>2</sup> integers, use the Columnsort procedure introduced above. Column sorts recursively handle shorter columns until they fit in memory, while fixed intercolumn rearrangements invoke the coded address interchange. A suitable table shape gives constant recursion depth. Section 7 proves correctness and the local sorting bound

\(O\left(1+\frac{n}{B}\left[1+\left(\frac{logM}{log(M/B)}\right)^{1-\varepsilon}\right]\right),n\le M^2.\)

For larger inputs, use most-significant-digit radix sorting: partition by the highest bit group, then process the next bit group within each bucket. High-order bits already determine the order between buckets. Once a bucket is small enough, sort it with the local algorithm. If every bit group has been processed, all its integers are equal and recursion can also stop.

One partition first divides the input into subarrays of size \(\Theta(M^2)\) and sorts each by the current bit group. Each group value then occupies at most one contiguous interval per subarray. Store the start and length of each interval, then concatenate intervals having the same bit-group value to form a bucket. Choosing \(\Theta(logM)\) bits per round keeps the number of intervals small enough that concatenation and boundary handling cost only a scan.

Buckets at the same recursion depth are disjoint and contain at most _N_ integers altogether. The local sorting bound controls each level’s cost. Since each integer has \(\Theta(logN)\) bits, there are _O_(log_N/_log_M_) levels. Combining these bounds yields

\(O\left(\frac{N}{B}\left[1+\frac{logN}{(log(M/B))^{1-\varepsilon}(logM)^\varepsilon}\right]\right)\)

block transfers. For \(N\le M^2\), the local bound also implies this bound. Section 8 supplies the partition and recursion analysis and combines it with direct sorting for bounded memory parameters to complete the main proof.

## 5 A Counterexample to the Multiple-Unicast Conjecture

This section proves Theorem 3.2. We first construct a linear circuit that exchanges two collections of inputs and interpret its connections as an undirected communication network. We then assign matrix labels to the network to show that every routing scheme has a common rate strictly below an achievable coding rate. The same matrix relations will accelerate address interchange in the next section. The starting point is an explicit finite list of XOR operations, together with subspace labels used to analyze it. We combine copies of this circuit so that auxiliary registers can be reused. The labels then specify how arrays are reordered during the I/O algorithm. The next subsections give the finite circuit, explain how its copies are combined, and derive the routing bound; Section 6 gives the address permutations.

