<tbc>running time was subsequently improved to \(\widetilde{O}(n\sqrt{n})\) for \(p<\frac{1}{16}\) in [19] while achieving logarithmic maximum dislocation w.h.p. and linear total dislocation in expectation.

To sum up, all the existing works considering _persistent_ random comparison faults achieve a maximum dislocation of _O_(log_n_) (w.h.p.) and require \(\Omega(n\sqrt{n})\) time to approximately sort _n_ elements, while, in the case of non-persistent random comparison faults, sorting (with no dislocation, w.h.p.) requires only _O(n_log_n_) time. This begs the following question:

**Question 1:** How much time is needed to (approximately) sort _n_ elements in the presence of _persistent_ random comparison faults?

To answer the above question, one might hope of employing a strategy similar to that used by the sorting algorithm of [15] for non-persistent random comparison faults, which iteratively extends a sorted sequence with new elements by performing noisy binary searches. However, due to the persistent nature of our random comparison faults, one cannot maintain a perfectly sorted sequence. Then, the following question also arises:

**Question 2:** How can we _quickly_ find the approximate rank of an element in an approximately sorted sequence in the presence of _persistent_ random comparison faults?

Furthermore, while inserting an element in its correct position (i.e., in the position corresponding to the element’s rank) in a perfectly sorted sequence results in a sequence that is still sorted, the same does not necessarily hold in an approximate sense. This is because the maximum dislocation of an approximately sorted sequence might increase following the insertion of one or more elements. To circumvent this problem, it would be helpful to locally rearrange the elements of an approximately sorted sequence in a way that reduces the resulting dislocation.

**Question 3:** Can the (maximum and/or total) dislocation of an approximately sorted sequence be quickly improved (up to some lower limit) in the _persistent_ random comparison faults model?

Finally, since the best maximum and total dislocations achieved by existing works with high probability are _O_(log_n_) and _O(n_), respectively, one might wonder whether these bounds are (asymptotically) tight or if they can be improved (w.h.p).

**Question 4:** What are the best possible (asymptotic) maximum and total dislocations that can be achieved with high probability in the presence of _persistent_ random comparison faults?

## 1.1 Our contributions

In this work, we tackle the above questions and we develop a sorting algorithm called RiffleSort that takes _O(n_log_n_) time and, if \(p<\frac{1}{4}\), achieves a maximum dislocation of _O_(log_n_) and a total dislocation of _O(n_) with high probability. We also exploit the intrinsic random nature of comparison faults to derandomize RiffleSort while maintaining the same asymptotic guarantees, as long as the comparison errors do not depend on the position of the elements in the input sequence.

On the negative side, we prove that no algorithm can achieve maximum dislocation _o_(log_n_) with high probability, nor total dislocation _o(n_) in expectation. Moreover, if _o(n_log_n_) time was sufficient to compute a sequence having a maximum dislocation of _d=O_(log_n_), there would exist an algorithm that sorts _n_ elements in the absence of comparison faults using only \(o(nlogn)+O\big(\frac{n}{logn}\cdot((logn)(loglogn))\big)=o(nlogn)\) time, contradicting the classical \(\Omega(nlogn)\) lower bound for comparison-based sorting algorithms. Hence, RiffleSort is simultaneously optimal, in an asymptotic sense, in terms of maximum dislocation, total dislocation, and running time. This answers Question 1 for constant \(p<\frac{1}{4}\) and Question 4. Handling all constant error probabilities in<tbc>

