**Finding the dominant key.** We now analyze the complexity of the **FindDominant** algorithm (Theorem 5.3) when implemented in circuit. Note that the **FindDominant** algorithm need not look at the elements’ payload strings. Therefore, we may plug in an arbitrary \(w\ge 0\) as the fake payload length.

1. Step 1, i.e., the base case calls the **SlowSort**_<sup>K</sup>_ algorithm on an array of length at most _n/K_ where _K_:=2_<sup>k</sup>_. Therefore, this step requires \(O(n\cdot(w+k))\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) generalized boolean gates, \(O(n)\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) number of (_w+k_)-selector gates, and of depth _O_(log_n+k_).<tbc>

2. In each of the _O(k_) recursive calls to **FindDominant**, the array length would reduce by a factor of 4, and during each recursive call, we divide the array into groups of 8 and run an AKS circuit on each group. In total over all levels of recursion, this requires _O(n_) number of (_w+k_)-selector gates, _O(n_) generalized boolean gates, and _O(k_) depth.

Therefore, we have the following fact.

**Fact 15.4** (**FindDominant** circuit)**.** _Suppose that n\>_2<sup>_k_+7</sup> _and moreover n is a power of_ 2_. Let A be an array containing n elements each with a k-bit key, and suppose that A is_ (1-2<sup>-8_k_</sup>)_- uniform. Fix some arbitrary_ \(w\ge 0\) _(which need not be the element’s payload length_<sup>11</sup>_). Then, there is a circuit that can correctly identify the dominant key given any such A; and moreover, the circuit contains_ \(O(n\cdot(w+k))\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) _generalized boolean gates,_ \(O(n)\cdot max(1,\mathsf{poly}(log^*n-log^*(w+k)))\) _number of_ (_w+k)-selector gates, and of depth O_(log_n+k_).

## 15.2 Putting Everything Together: Sorting Short Keys in the Circuit Model

We now finish it off and discuss how to implement the algorithm of Theorem 5.5 in the circuit model. To do this, it suffices to describe how to implement a nearly orderly segmenter in circuit, and how to sort a nearly orderly array in circuit.

**Nearly orderly segmenter.** Recall that for \(k\le logn\), the algorithm of Theorem 3.2 is a comparator-based circuit with _O(nk_) comparators and of _O(k_) depth. We would like to convert this comparator-based circuit to a circuit with generalized boolean gates and _w_-selector gates.

**Fact 15.5** ((2<sup>-8_k_</sup>,2<sup>3_k_</sup>)-orderly segmenter circuit)**.** _Suppose that_ \(k\le logn\)_. There exists a_ (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)_-orderly-segmenter circuit with O(nk_<sup>2</sup>) _generalized boolean gates, O(nk_) _number of_ (_w+k)-selector gates, and of depth O(k)._

_Proof._ If we used a naive method for converting the comparator-based circuit in Theorem 3.2 to a circuit with generalized boolean gates and _w_-selector gates, the resulting circuit depth would have depth _O(k_log_k_) because every comparator can be implemented as an _O(k_)-sized and _O_(log_k_)-depth boolean circuit due to Fact 6.2.

Fortunately, we can rely on a _pipelining_ technique to make the depth smaller.

• In the beginning, all input bits of the input layer are "ready". All other comparators not in the input layer see all bits of their inputs as "not ready".<tbc>

• Whenever a comparator detects a new \(i\in[k]\) such that both of its inputs have the _i_-th bit ready, it can compare the _i_-th bits of the two inputs, and as a result, the _i_-th bits of the two outputs of the gate will be ready.<tbc>

<sup>11</sup>Note that the algorithm need not look at the elements’ payload strings.

