<tbc>_sorting any input array containing n elements each with a key from the domain_ {0,1,2} _and a payload of w bits._

**Slow sorter and slow alignment.** We now discuss how to implement the earlier **SlowSort**\(^K(\cdot)\) and **SlowAlign**\(^{K,K^\prime}(\cdot)\) algorithms in circuit.

**Fact 15.2** \((\text{\textbf{SlowSort}}^K(\cdot)\text{circuit})\)**.** _Let n be the length of the input array and w be the length of each element’s payload. Recall that each element has a key from the domain_ \[0_,K_-1\]_, and let k_:=log_K. The_ \(\text{\textbf{SlowSort}}^K(\cdot)\) _algorithm of Theorem 5.1 can be implemented as a circuit with_ \(O(nK\cdot(w+k))\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) _generalized boolean gates,_ \(O(nK)\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) _number of_ (_w+k_)_-selector gates, and of depth O_(log_n+k_).

_Proof._ Recall the **SlowSort**\(^K(\cdot)\) algorithm of Theorem 5.1 where _K_:=2_<sup>k</sup>_:

1. Step 1 can be implemented using _K_ parallel instances of the counting circuit of Fact 6.3 on arrays of length _n_, and then using the all-prefix-sum circuit of Fact 6.4 on an array of length _K_ where the entire sum is promised to be at most _O_(log_n_) bits long. In total, Step 1 requires a circuit with _O(nK+K_log_n_)=_O(nK_) generalized boolean gates and of depth _O_(log_K_+log_n_)=_O(k_+log_n_).<tbc>

2. Step 2 can be implemented by broadcast each element of _A_ over a binary tree of _K_ leaves, and then having all _nK_ elements perform a comparison in parallel using Fact 6.2. This requires _O(nK_) number of (_w+k_)-selector gates, _O(nK_) generalized boolean gates, and at most _O(k_) depth.<tbc>

3. Step 3 invokes _K_ parallel instances of the generalized binary-to-unary conversion circuit on arrays of length _n_, and _K_ parallel instances of the ternary-key sorting circuit. This requires \(O(nK(w+k))\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) generalized boolean gates, \(O(nK)\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) number of (_w+k_)-selector gates, and has depth _O_(log_n_).<tbc>

4. Step 4 can be accomplished in a circuit with _O(nK_) number of generalized boolean gates, _O(nK_) number of (_w+k_)-selector gates and of depth _O_(log_K_)=_O(k_). Note that we can use a single bit to mark whether each element in each of \(B'_0,B'_1,\dots,B'_{K-1}\) has a real key in the range \[0_,K_-1\] or not.

Summarizing the above, we have that the entire **SlowSort**\(^K(\cdot)\) algorithm can be implemented as a circuit with \(O(nK(w+k))\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) generalized boolean gates, \(O(nK)\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) number of (_w+k_)-selector gates, and of depth _O_(log_n_).

We now discuss the circuit implementation of the **SlowAlign**\(^{K,K^\prime}(\cdot)\) algorithm of Theorem 5.2.

**Fact 15.3** \((\text{\textbf{SlowAlign}}^{K,K^\prime}(\cdot)\text{circuit})\)**.** _Let n be the length of the input array and w be the length of each element’s payload. Recall that each element has a key from the domain_ \[0_,K_-1\]_, and an index from the domain_ \([0,K'-1]\)_. Let k_=log_K and_ \(k'=logK'\)_. The_ \(\text{\textbf{SlowAlign}}^{K,K^\prime}(\cdot)\) _algorithm of Theorem 5.1 can be implemented as a circuit with_ \(O(n\cdot(K+K')\cdot(w+k+k'))\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k+k')))\) _generalized boolean gates,_ \(O(n(K+K'))\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k+k')))\) _number of_ \((w+k+k')\)_-selector gates, and of depth_ \(O(logn+k+k')\).

_Proof._ Recall that **SlowAlign**\(^{K,K^\prime}\) invokes one instance of **SlowSort**_<sup>K</sup>_ on an array of length _n_ containing \((w+k')\)-bit payloads, and one instance of **SlowSort**\(^{K^\prime}\) on an array of length _n_ containing (_w+k_)-bit payloads and its reverse routing circuit. Therefore, the fact follows from Fact 15.2.

