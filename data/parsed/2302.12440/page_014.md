Let us define \(m=\sum_{i\in[n-1]}\mathbb{E}[\tau_i|E]+n^{2/3}=O(nlogn)\).

If the number of random bits used in the _i_-th call to SafeBinarySearch is _r<sub>i</sub>_, then we can similarly show

\(\mathbb{P}\left[\sum_{i\in[n-1]}r_i\ge\sum_{i\in[n-1]}\mathbb{E}[r_i]+n^{2/3}|E\right]=o(1).\)

Let \(R=\sum_{i\in[n-1]}\mathbb{E}[r_i|E]+n^{2/3}=O(nlogn)\).

Consider the following algorithm (which is our SafeSimpleSort):

• Run A until it finishes, or it is about the make the (_m_+1)-th query, or it is about the use the (_R_+1)-th random bit.<tbc>

• If A finishes, then return the output of A; otherwise, output an arbitrary permutation.

Then SafeSimpleSort always makes at most _m=O(n_log_n_) queries, uses at most _R=O(n_log_n_) random bits, and has error probability P\[A errs\]+_o_(1)=_o_(1).

Finally, we give our main algorithm for noisy sorting. See Algorithm 3 for its description.

We first analyze its error probability.

**Lemma 21.** _Algorithm 3 has error probability o_(1).

_Proof._ Let _E_<sub>0</sub> be the event that the algorithm does not err because of lack of random bits at Line 7, Line 17, or Line 34. Let _E_<sub>1</sub> be the event that SafeSimpleSort successfully sorts _S_ at Line 5; _E_<sub>2</sub> be the event that all calls of SafeWeakSort at Line 17 are correct; _E_<sub>3</sub> be the event that all calls of SafeLessThan at Lines 20 and Lines 27 are correct; _E_<sub>4</sub> be the event that all calls of SafeBinarySearch at Line 34 are correct.

We show that if _E_<sub>0</sub>_,E_<sub>1</sub>_,E_<sub>2</sub>_,E_<sub>3</sub>_,E_<sub>4</sub> all happen, then Algorithm 3 is correct. First of all, under _E_<sub>1</sub>, _S_ is correctly sorted at Line 5. Secondly, under _E_<sub>2</sub> and _E_<sub>0</sub>, for each _l_, _B<sub>l</sub>_ is correctly sorted at Line 17. Under _E_<sub>3</sub> and _E_<sub>0</sub>, at Line 32, all elements remaining in _B<sub>l</sub>_ are indeed greater than _l_ and smaller than _r_, so adding _B<sub>l</sub>_ to A between _l_ and _r_ keeps all elements in A sorted. Therefore, before the for loop at Line 33, all elements in A are correctly sorted, and clearly these elements are exactly _A_\\_X_. Finally, under _E_<sub>4</sub> and _E_<sub>0</sub>, the insertions made at Line 34 are all correct, so the final result is correct.

For each call of SafeBinarySearch at Line 7, the probability that it requires more than _n_<sup>2/3</sup> random bits is \(O(\frac{polylogn}{n^{4/3}})\) by Corollary 19 Part 1 and Chebyshev’s inequality. By union bound, with probability 1-_o_(1), none of the calls of SafeBinarySearch at Line 7 causes the algorithm to err. We can similarly bound the probability the algorithm errs at Line 17 or Line 34. Overall, \(Pr[\neg E_0]\le o(1)\). Clearly, \(Pr[\neg E_1]\le o(1)\), \(Pr[\neg E_2]\le\frac{1}{nlogn}\cdot(|S|-1)\le\frac{1}{logn}\), \(Pr[\neg E_3]\le\frac{1}{nlogn}\cdot(2n)=\frac{2}{logn}\) and \(Pr[\neg E_4]\le\frac{1}{nlogn}\cdot n=\frac{1}{logn}\). Thus, by union bound, the overall success probability of Algorithm 3 is at least \(1-\frac{4}{logn}-o(1)=1-o(1)\).

Let a bucket be the set of elements that are between two adjacent elements in the sorted order of _S_. Then we have the following simple lemma.

**Lemma 22.** _With probability_ \(\ge 1-\frac{1}{n}\)_, all buckets have size at most_ 3log<sup>2</sup>_n._

