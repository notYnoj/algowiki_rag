**Lemma 3.6.** _Consider running PartialVoteCover on the set cover instance corresponding with source s, and let_ FreqOf _be as defined in Section 2.4 for that instance, i.e. for a given element v,_ FreqOf(_v_) _is the number of sets in the instance which contain v. Then PartialVoteCover runs in time_ \(O(\sum_{v\in K}\mathrm{FreqOf}(v))\)_, where K is the random sample chosen in the algorithm._

This is sufficient to meet the desired _O(n_log_n_) bound if we can show that each element is contained in few sets; this will be addressed in Lemma 3.9.

_Proof._ The runtime bottlenecks in PartialVoteCover are Lines 6 and 10. Recall from Section 2.4 that we can answer in constant time any of the following queries: (1) MemberOf, which answers whether a given set contains a given element; (2) FreqOf, which returns the number of sets containing a given element; and (3) SetOf, which returns the _i_th (according to some arbitrary order) set containing a given element. We will just assume we have access to these primitives, but we refer back to Section 2.4 for a description of how these primitives can be supported in the set cover instances of a sparsest \(\alpha\)-navigable graph instance.

## Line 6: check if an element has been covered.

We maintain C in a hash table. To check if element _v_ is covered by C, we scan over all possible sets that contain _v_ (by finding the number of sets with FreqOf and iterating over them with SetOf) and, for each one, check if it is contained in the hash table representing C. We return **true** if any such set is in C. We do one constant-time membership query per set containing _v_, so \(\le\mathrm{FreqOf}(v)\) per sample _v_, and \(\le\sum_{v\in K}\mathrm{FreqOf}(v)\) in total.

## Line 9: find the set with the most votes.

For each \(S\in\mathcal{S}\), we maintain the intersection \(V\cap S\) in a hash table. We update all of these hash tables any time _V_ is modified. _V_ is modified on Lines 8 and 12.

Line 8 adds _v_ to _V_ . The only intersections \(V\cap S\) that change are those where \(v\in S\). We can find these by calling SetOf operations on _v_. For each such set _S_, we do a single constant-time insertion into its \(V\cap S\) hash table, for a maximum of \(\sum_{v\in K}\mathrm{FreqOf}(v)\) across all voters.

Line 12 runs after a set _S_<sup>∗</sup> has been added to C. It subtracts _S_<sup>∗</sup> from _V_ . The elements we must remove from _V_ are exactly those in the hash table for \(V\cap S^*\). Thus, we iterate over \(V\cap S^*\), and for each element _v_ in it, we must remove _v_ from all \(V\cap S\) hash tables. But note that the sets _S_ where \(v\in V\cap S\) are exactly those where \(v\in S\). We can iterate through these by calling SetOf operations on _v_. For each of these, we do a single constant-time hash table deletion. We can bound the total number of deletions by observing that any _v_ can only be removed from _V_ once. Since each such _v_ is removed from FreqOf(_v_) hash tables, we perform a maximum of \(\sum_{v\in K}\mathrm{FreqOf}(v)\) deletions over the course of PartialVoteCover.

Having bounded the cost of maintaining the hash tables, how do we efficiently identify the largest (Line 9) in order to evaluate the condition on Line 10? We first note that it is only necessary to identify the most voted set if the condition passes. We know from Observation 3.3 that at the start of each loop iteration, the condition must be false. Thus, it can only become true when a hash table grows. It follows that it is sufficient to check, whenever a hash table grows due to Line 8, whether it now has size _c_ln_n_, and set _S_<sup>∗</sup> to that set if so. Therefore, we can satisfy Lines 9 and 10 in time proportional to the number of hash table insertions, which is no more than \(\sum_{v\in K}\mathrm{FreqOf}(v)\).

It follows that PartialVoteCover runs in \(O(\sum_{v\in K}\mathrm{FreqOf}(v))\) time.

