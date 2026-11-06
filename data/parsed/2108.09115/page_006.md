_Proof._ The shared common string can be partitioned into at most _k_+1 blocks that are contiguous for _X_, and similarly for _Y_ . The coarsest refinement of both partitions is contiguous on both _X_ and _Y_ and uses at most 2_k_+1 blocks.

## Algorithm description

The preprocessing algorithm (Algorithm 1) constructs log(_n_)+1 hash tables. The \(\ell\)-th hash table corresponds to window size \(2^\ell\); we use a rolling hash function (e.g. Rabin fingerprint) to construct a hash table of all contiguous substrings of _X_ of length \(2^\ell\) in time _O(n_).

Algorithm 2 finds the partition into blocks guaranteed in Claim 2. At each iteration of the algorithm, it finds the longest contiguous substring of _X_, starting from XStart that has an identical contiguous substring in _Y_ . Using the prestored hashes, this is done in time _O_(log(_n_)).

Finally, given the partition into blocks, we just have to solve a heaviest increasing substring problem on the _O(k_) blocks (with weights corresponding to block lengths). This can be done in time _O(k_log(_k_)) using a standard generalization of the classic LIS algorithm (e.g. \[JV92\]). We provide pseudocode in Algorithm 3 for completeness.

In the pseudocode below we sometimes abuse notation and think of X,Y as functions from indices to characters, and similarly, we use Y<sup>-1</sup> to denote the inverse of this function (i.e. given a character it returns its index in _Y_ .

\(n\leftarrow\text{length}(X)\)<br>
\(\text{for}\ell=0\dots\text{log}(n)\text{\textbf{do}}\)<br>
\(H[\ell]\leftarrow\text{Rolling hash of}X\text{with window of length}2^\ell\)<br>
return H

**Algorithm 1:** Preprocess(_X_)

