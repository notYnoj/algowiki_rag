<tbc>**Appendices**

## A Variations of bichromatic costs

### A.1 Bichromatic most expensive: \(\alpha<1\) and \(\beta<1\)

In this case, it is natural to first sort both colors with monochromatic comparisons, to then do binary merging using exponential searches. It is easy to see, that this algorithm is within an _O_(log_N_) factor of the cost of the Hamiltonian.

### A.2 Bichromatic middle expensive: \(\alpha<1<\beta\) or \(\beta<1<\alpha\)

This setting can be expressed as a monotone function in the framework of \[7\].

There is also a straight forward direct algorithm: W.l.o.g., assume \(\alpha<1<\beta\). Sort the red elements using red-red comparisons at cost \(O(\alpha|R|log|R|)\). For each blue element, perform a binary search in these red, at total cost of _O_(|_B_|log|_R_|). Finally, sort the blue stripes with total cost \(O(\beta\sum|B_i|log|B_i|)\). Each of the three terms is justified by the need to determine the rank of a certain type of elements, and the above procedure uses the cheapest available comparisons for this task.

## B More than two colors

**Definition 19** (Multichromatic Sorting)**.** _Multichromatic Sorting is universal sorting, where the elements are colored with k different colors. All bichromatic comparisons have cost 1, and for each color i, the monochromatic comparisons have a cost_ \(\gamma_i>1\)_, where_ \(\gamma_i=\infty\) _means that these comparisons are forbidden and stripes of this color are reported as a whole._

To solve the multichromatic setting, run a natural variant of (bichromatic) InversionSort: Pick one random elements from each color, sort these, and take this as the backbone. Consider the remaining elements in random order. Place the element into the backbone using binary search. If this leads to a new element on the backbone (neighbors are of different colors), pivot the two current buckets. This maintains the invariants of the backbone and that three consecutive elements on the backbone have three different colors. Hence, all neighboring buckets are starting points of bi-chromatic problems, and we can use InversionSort on them. Here we interleave the computation as if the whole backbone was one backbone in the bichromatic setting.

## C Omitted Proofs

**Lemma 14.** _\[local competitiveness of inversion finding\] Let r,b be two neighboring pivots of InversionSort, and let t be the number of rounds (up to a constant the cost of comparisons) until InversionSort finds an inversion or concludes that there is none, starting from the first round when the subproblem of r,b is unaffected. Let H<sub>r,b</sub> be the cost of the Hamiltonian of the stripe subinstance between the stripe of r and the stripe of b. Then_ E\[_t_\]=_O(H<sub>r,b</sub>), and_ \(Pr[t\le\mathbb{E}[t]+t']\ge 1-(1/8)t^{\prime^\prime}\).

_Proof._ Let _C_ be the number of rounds of comparisons for which subproblem _r,b_ is active. Observe that InversionSort does on this subproblem _C_ bichromatic comparisons, and samples \(\sim C/\alpha\) red elements and finds their max and min in _O(C_) cost. Similarly, the blue sample consists of \(\sim C/\beta\) elements, incurring cost _O(C_) for blue-blue comparisons. This is from the round in which _r,b_ are<tbc>

