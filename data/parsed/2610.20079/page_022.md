**Lemma 7.2** (Local sorting)**.** For \(1\le n\le M^2\), an array of _n_ records can be sorted in

\(O\big(1+\frac{n}{B}[1+(logM/a)^\tau]\big)\) (19)

block transfers, using at most _M_ words of memory and polynomial disk space.

_Proof._ First suppose \(n\le H^2\). For a call on _z_ records, sort in memory if \(z\le 512H\). Otherwise, take \(t=\lceil logz/4\rceil\), _s_=2_<sup>t</sup>_, and _r=s_<sup>3</sup>, pad to _rs_ records with positive sentinels, and apply Proposition 7.1, recursively sorting each column. Remove the new padding after the call, retaining the original _z_ records. Increasing the fixed memory threshold ensures \(s\ge 8\) in every nonterminal call.

After padding, _rs\<_16_z_ and each column has length _r\<_8_z_<sup>3/4</sup>. Each level reduces size to its 3/4 power. Starting from \(n\le H^2\), three levels give column length less than \(128H^{27/32}\le 128H\), below the stopping threshold. The four rounds of column sorting in a call have total input length (4_s_+1)_r=O(z_). Thus the recursion has constant depth and processes _O(n_) records in total, including padding and repeated sorts.

Each interchange acts on _O(zw_) bits with field width _O_(log_M_). Lemma 6.1 bounds its cost by \(O(1+(z/B)[1+(logM/a)^\tau])\). Short columns that fit in memory share sequential input and output streams: read and sort one column at a time, appending the results. A round processing _L_ records costs only _O_(1+_L/B_) transfers. Nonterminal calls have length \(\Omega(M)\), so their scan cost absorbs startup. Summing over the levels proves (19).

For \(H^2<n\le M^2\), sort a constant number of subarrays and perform a constant number of two-way merge rounds, each costing a scan. Execute depth first and reuse memory; each parent retains only a constant number of descriptor words, and temporary disk arrays have polynomial size. Corollary A.3 restores the original parameters. If _M_ is bounded, then \(n\le M^2\) is also bounded and direct comparison sorting suffices.

## 8 Sorting Arbitrary Input Sizes

The local algorithm sorts individual subarrays but does not determine their order relative to one another. We use most-significant-digit radix sorting: partition by the highest bit group, then process the next group within each bucket, sorting a bucket directly once it is small enough for the local algorithm. A _bit group_ is a consecutive group of binary digits, and a _bucket_ contains records sharing the current bit-group value.

Keep \(H=\lfloor M/C\rfloor\) and _a_=log(_M/B_), and write _h_=log_M_. Each bit group has \(t=\lfloor logH\rfloor=\Theta(h)\) bits and at most \(K=2^t\le H\) values; a shorter highest group uses its actual width. We first work with the simulated parameters supplied by Lemma A.2, whose memory-to-block ratio can be made larger than any fixed constant. Increase that ratio threshold _R_<sub>0</sub> so that \(H\ge B\). Corollary A.3 restores the original parameters.

### 8.1 The Cost of One Partition

Processing \(\Theta(logM)\) bits per round may create \(\Theta(M)\) buckets. Reserving one block buffer per bucket would require \(\Theta(MB)\) words and need not fit in memory. Instead, sort each subarray by the current bit group so that each bucket occupies a contiguous interval, then read and concatenate these intervals one at a time. This uses a fixed number of block buffers, at the cost of boundary transfers for each interval. We show that these transfers still fit within scan cost.

