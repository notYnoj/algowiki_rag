<tbc>must be that in a fully sorted array, at most _K_ out of the _p_=2<sup>3_k_</sup>=_K_<sup>3</sup> segments have multiple keys, all remaining segments must have a single key. Since the input array is (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)-orderly, it means that in the input array, all but _K_ segments must be \((1-\eta)\)-uniform.

For any \((1-\eta)\)-uniform segment in the input array, if we extract from it all elements whose keys differ from the dominant key, as well as at least \(\lceil\eta m\rceil\) number of elements with the dominant key, then all remaining elements must belong to this segment if the array were fully sorted. In Step 1c, we label all such elements as "`misplaced`"; as well as all elements in segments that are not \((1-\eta)\)-uniform. The total number of elements marked as "`misplaced`" is upper bounded by

\(K\cdot m+2\eta m(K^3-K)\le n/K^2+2\eta n=n/K^2+2n/K^8\le 3n/K^2\)

Therefore, after Step 2 effectively _X_\[1:3_n/K_<sup>2</sup>\] contains all elements marked "`misplaced`" as well as some additional elements that we want to extract, such that all remaining elements belong to their segment. Suppose that _i_<sub>1</sub>_,i_<sub>2</sub>_,...,i_<sub>_K_<sup>2</sup></sub> number of elements from each super-segment are contained in _X_\[1:3_n/K_<sup>2</sup>\]. In Step 3 and Step 4, we move the smallest _i_<sub>1</sub> extracted elements back to the first super-segment, then next smallest _i_<sub>2</sub> extracted elements to the second super-segment, and so on. In the outcome of Step 4, every element must belong to the correct super-segment.

At this moment, we only need to sort the super-segments that are multi-keyed. The total number of multi-keyed super-segments is at most _K_. This is accomplished as follows: Step 6 moves all multi-keyed super-segments to the front, and then sorts within each of the first _K_ super-segments. Finally, Step 8 reverse routes all the super-segments back to their original positions.

**Performance bounds.** Since by assumption, _n\>_2<sup>4_k_+7</sup>, then the length of each segment _m_:=_n/_2<sup>3_k_</sup>_\>_2<sup>_k_+7</sup>, and therefore other assumption of Theorem 5.3 is satisfied and we can use Theorem 5.3 to characterize the performance of the **FindDominant** step. Steps 2 and 6 each incurs _O(n_) work and _O_(log_n_) depth. Step 3 incurs \(O(3n/K^2\cdot K^2)=O(n)\) work and _O_(log_n+k_) depth. Step 7 incurs \(O(K\cdot(n/K^2)\cdot K)=O(n)\) work and _O_(log_n+k_) depth. The costs of all other steps are upper bounded by _O(n_) and _O_(log_n+k_) too.

## 5.4 Sorting Short Keys on an Oblivious PRAM

Now, we can put everything together and obtain an oblivious parallel algorithm that sorts an input array with short keys.

**Theorem 5.5** (Restatement of Theorem 1.2)**.** _There exists a deterministic oblivious parallel algorithm that sorts any input array containing n elements each with a k-bit key in_ \(O(n)\cdot min(k,logn)\) _total work and O_(log_n_) _depth, assuming that each element can be stored in O_(1) _words._

_Proof._ If \(n\le 2^{4k+7}\), we can just run AKS which takes _O(n_log_n_) total work an _O_(log_n_). Else, if _n\>_2<sup>4_k_+7</sup>, we can accomplish the task with the following algorithm.

\(\text{\textbf{Sorting short keys on an oblivious PRAM Input. An array}}A\text{of length}n\text{each with a}k\text{-bit key and a payload string. We assume that}n>2^{4k+7}\text{and moreover each element can be stored in}O(1)\text{memory words. \textbf{Algorithm.}}\)<br>
\(1.\) Apply the (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)-orderly segmenter construction of Theorem 3.2 to the input array _A_, the outcome is a permutation of _A_ that is (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)-orderly.

