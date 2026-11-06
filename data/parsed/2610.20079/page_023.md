**Lemma 8.1** (Partitioning by one bit group)**.** An array of length _n\>H_<sup>2</sup> can be partitioned by a bit group of at most _t_ bits into contiguous buckets in increasing bit-group order, using

\(O\big(\frac{n}{B}[1+(h/a)^\tau]\big)\)

block transfers. After local sorting, interval concatenation alone takes _O(n/B_) transfers.

_Proof._ Divide the current storage order into \(J=\lceil n/H^2\rceil\) contiguous subarrays, each with at most _H_<sup>2</sup> records. Apply Lemma 7.2 to sort each subarray by the current bit group. Since _J=O(n/H_<sup>2</sup>), the total sorting cost satisfies the stated bound.

After sorting, each value occupies at most one contiguous interval in a subarray. Scan the subarrays and store each interval’s start and length in an auxiliary array on disk, indexed by subarray number and bit-group value. Each entry occupies a constant number of words, and empty intervals have length zero. Read the corresponding intervals in increasing bit-group order, appending complete records to the output stream to form contiguous buckets.

The auxiliary array has _JK=O(n/H_) entries. Each entry access and interval boundary costs a constant number of transfers, while every record is copied exactly once. Concatenation therefore costs _O(n/B+n/H_)=_O(n/B_) transfers and uses a fixed number of block buffers. The buckets are ordered by the current bit group; later bit groups and local sorting determine the order within each bucket.

## 8.2 The Cost of High-Order Recursion

After partitioning, high-order bits determine the order between buckets, and the remaining work takes place within buckets. Put _p_=log(_N/M_).

**Proposition 8.2** (Sorting large inputs)**.** For \(N\ge M^2\), the _N_ input integers can be sorted in

\(O\big(\frac{N}{B}\big[1+\frac{p}{a^\tau h^\varepsilon}\big]\big)\)

block transfers, using at most _M_ words of memory and polynomial disk space.

_Proof._ All integers in a subproblem share the high-order bits already processed. If its length is at most _H_<sup>2</sup>, use Lemma 7.2 to sort by the complete integers. If no bit groups remain, all integers are equal and can be output directly. Otherwise, apply Lemma 8.1 and recursively process the nonempty buckets in increasing bucket order, advancing to the next bit group. High-order bits order the buckets, and recursion sorts each bucket, proving correctness.

Subproblems at one depth are disjoint and contain at most _N_ records in total. Those requiring further partitioning have length greater than _H_<sup>2</sup> and produce _O(N/H_<sup>2</sup>) subarrays altogether. Lemma 8.1 gives the per-level cost

\(O\big(\frac{N}{B}[1+(h/a)^\tau]\big).\) (20)

There are _O(N/H_) auxiliary entries, new buckets, and tasks at that depth. Newly formed short buckets have total length at most _N_; Lemma 7.2 bounds their sorting, startup, and final output by (20) as well. Long buckets with no remaining bit groups require only a scan to output.

