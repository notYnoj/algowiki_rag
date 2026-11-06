**Implementing Steps 1 and 2 in circuit.** Due to Fact 6.3, Step 1 can be accomplished with _O(n_) generalized boolean gates and in depth _O_(log_n_). When the count `cnt` is computed from Step 1, we can implement Step 2 as follows. Recall that \(\mathtt{cnt}\in\{0,1,\dots,n\}\) is a ((log<sub>2</sub>_n_)+1)-bit number. Imagine that there are _n_ receivers numbered 1,2_,...,n_. Each receiver is waiting to receive either "\(\le\)" or "_\>_". Those with indices 1_,...,_`cnt` should receive "\(\le\)" and those with indices `cnt`+1_,...,n_ should receive "_\>_". We can accomplish this using the binary-to-unary conversion circuit of Fact 6.5, i.e., convert `cnt` into an _n_-bit string so that the head `cnt` bits are 0 and the tail _n_-`cnt` bits are 1. Due to Fact 6.5, Step 2 can be implemented as a circuit consisting of at most _O(n_) generalized boolean gates and in depth _O_(log_n_). Once each of the _n_ receivers receive either "\(\le\)" or "_\>_", it takes a single generalized boolean gate per receiver to write down either `blue`, `red`, or uncolored.

**Implementing Steps 3 in circuit.** The approach and analysis are similar to the **Swap**_<sup>n</sup>_ circuit in the proof of Theorem 9.3.

Summarizing the above, and plugging in a \((1/8log^\widetilde{C}n,n,w)\)-lossy loose compactor as stated in Theorem 11.1, we will get Theorem 12.1.

## 13 Sparse Loose Compactor

### 13.1 Building Blocks: Slow Tight Compaction and Distribution

**Lemma 13.1** (Slow tight compaction circuit **SlowTC**)**.** _There is an_ (_n,w)-tight compaction circuit of depth O_(log<sup>2</sup>_n), and requiring O(nw+n_log_n_) _generalized boolean gates and O(n_) _number of w-selector gates. Henceforth we will use_ **SlowTC** _to denote this circuit._

_Proof._ We can use the tight compactor circuit constructed in Asharov et al. \[ALS21, Theorems 4.8 and 5.1\]. In particular, wherever they employ an approximate swapper (called a loose swapper in their paper \[ALS21\]), we replace its implementation with a constant-depth one as described in Theorem 9.1. Asharov et al. \[ALS21\] did not analyze the depth of the circuit; however, with this modification, it is not hard to show that the resulting circuit has depth upper bounded by _O_(log<sup>2</sup>_n_).

Recall that in Section 4, we showed how to construct an algorithm that accomplishes distribution from tight compaction. The same algorithm applies in the circuit model. This gives rise to the following corollary:

**Corollary 13.2** (Slow distribution circuit **SlowDistr**)**.** _There is a circuit that solves the aforementioned distribution problem, henceforth denoted_ **SlowDistr**_; further, the number of generalized boolean gates, w-selector gates, and depth asymptotically match the_ **SlowTC** _circuit of Theorem 13.1._

_Proof._ Use the above algorithm where tight compaction is instantiated with **SlowTC**.

### 13.2 Sparse Loose Compactor

**Sparsity of an array.** Let _A_ be an array in which each element has a _w_-bit payload, and is tagged with a bit denoting whether the element is _real_ or a _filler_. Let \(\alpha\in(0,1)\). An array _A_ of length _n_ is said to be \(\alpha\)-sparse if there are at most \(\alpha n\) real elements in it.

