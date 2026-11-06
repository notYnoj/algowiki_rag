Using this pipelining technique, we can first compute all the generalized boolean gates which will populate the flags of all selector gates. This step takes _O(k_) depth and _O(nk_<sup>2</sup>) generalized boolean gates. Next, we can evaluate all _O(nk_) number of (_w+k_)-selector gates in a topological order; this can be accomplished in _O(k_) depth.

**Sorting a nearly orderly array.** We now describe how to implement the algorithm of Theorem 5.4 in circuit.

• Step 1 calls the **FindDominant** circuit of Fact 15.4, and then for each segment, invokes one copy of the counting circuit of Fact 6.3 and the generalized binary-to-unary conversion circuit of Fact 6.5. Therefore, this step can be accomplished with a circuit containing \(O(n\cdot(w+k))\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) generalized boolean gates, \(O(n)\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) number of (_w+k_)-selector gates, and of depth _O_(log_n+k_).<tbc>

• For Step 2: to mark each element with its segment index, we can simply hard-wire the segment indices in the circuit. Then, we invoke the oblivious compaction circuit of Theorem 14.1 which requires \(O(n(w+k))\cdot max(\mathsf{poly}(log^*n-log^*(w+k)),1)\) generalized boolean gates, \(O(n)\cdot max(\mathsf{poly}(log^*n-log^*(w+k)),1)\) number of (_w+k_)-selector gates, and _O_(log_n_) depth.<tbc>

• Step 3 invokes the **SlowAlign**<sup>_K,K_<sup>2</sup></sup> circuit of Fact 15.3 on 3_n/K_<sup>2</sup> elements. This requires \(O(n\cdot(w+k))\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) generalized boolean gates, \(O(n)\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) number of (_w_+3_k_)-selector gates, and has depth _O_(log_n+k_).<tbc>

• Step 4 is a reverse routing step whose costs are absorbed by Step 2.<tbc>

• Step 5 invokes _K_<sup>2</sup> instances of the counting circuit of Fact 6.3 each on an array of length _n/K_<sup>2</sup>. This takes _O(n_) generalized boolean gates.<tbc>

• Step 6 invokes the compaction circuit of Theorem 14.1 on an array containing _K_<sup>2</sup> elements, where each element is of length _W_:=_O(n(k+w)/K_<sup>2</sup>). Since \(K^2\cdot n(k+w)/K^2=O(n(k+w))\), this step requires \(O(n(k+w))\cdot max(\mathsf{poly}(log^*n-log^*(w+k)),1)\) generalized boolean gates, \(O(K)\cdot max(\mathsf{poly}(log^*n-log^*(w+k)),1)\) number of _W_-selector gates, and of depth _O_(log_K_).<tbc>

• Step 7 invokes _K_ instances the **SlowSort**<sup>_K_</sup> circuit of Fact 15.2 each on an array of length _n/K_<sup>2</sup>. This cost of this step is dominated by that of Step 3.<tbc>

• Step 8 is a reverse routing step whose costs are dominated by Step 6.

Due to Lemma 6.1, the above can be implemented as a constant fan-in, constant fan-out a boolean circuit of size \(O(n(w+k))\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) and depth _O_(log_n_+log_w_), assuming that _n\>_2<sup>4_k_+7</sup>.

**Fact 15.6** (Sorting a (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)-orderly array in circuit)**.** _Suppose that n\>_2<sup>4_k_+7</sup>_. There is a constant fan-in, constant fan-out boolean circuit that fully sorts an_ (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)_-orderly array containing n elements each with a k-bit key and a w-bit payloads, whose size is_ \(O(n(w+k))\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) _and whose depth is O_(log_n_+log_w)._

**Sorting short keys in the circuit model.** Summarizing the above, we get the following theorem:

**Theorem 15.7** (Restatement of Theorem 1.1)**.** _Suppose that n\>_2<sup>4_k_+7</sup>_. There is a constant fan- in, constant fan-out boolean circuit that correctly sorts any array containing n elements each with a k-bit key and a w-bit payloads, whose size is_ \(O(nk(w+k))\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) _and whose depth is O_(log_n_+log_w)._

