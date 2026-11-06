<tbc>To handle the case when \(n<\frac{1}{2}n_0\) or _n\>_2_n_<sub>0</sub>, we adopt the standard global rebuilding trick to re-construct the entire HALT structure on the current item set _S_ and update \(n_0\leftarrow n\). Recall that the HALT structure on _S_ can be constructed in _O(n_<sub>0</sub>) time with _O(n_<sub>0</sub>) space consumption. As there must be at least \(\Omega(n_0)\) updates to trigger the reconstruction, the rebuilding cost can be charged to those updates making each update cost become _O_(1) amortized. Moreover, the space consumption is bounded by _O(n_) all the times.

Interestingly, the _O_(1) amortized update time can be easily "de-amortized" by applying the same technique for the de-amortization for dynamic arrays, just increasing the space consumption by a constant factor. Thus, we have the following theorem.

Theorem 4.19. _The HALT structure on item set S can be maintained in O_(1) _worst-case time for each update to S. Space consumption is bounded by O(n_) _at all times, where n is the current size of S._

## 5 A Hardness Result on the DPSS Problem with Float Item Weights

We now prove Theorem 1.2. Let _DPSS-ALG_ be a deletion-only DPSS algorithm for float item weights with pre-processing time P(_N_), query time Q(_N_), and deletion time D(_N_). As a black box, we apply the algorithm to execute Integer Sorting.

Consider a set of _N_ integers _I_={_a_<sub>1</sub>_,...,a<sub>N</sub>_}, each of which is represented by one word of _d_ bits. We can assume w.l.o.g. that the integers are distinct<sup>2</sup>. The integers in _I_ can be sorted in descending order by the following algorithm:

\(\bullet\) for each integer \(ai_i\in I\), create an item _x<sub>i</sub>_ with weight _w(x<sub>i</sub>_)=2_<sup>ai<sub>i</sub></sup>_, represented by a float number;

\(\bullet\) initialize _S_ to be the set of all these _N_ items;

\(\bullet\) initialize an empty linked list, _R_, of the integers in _I_, which is maintained to be sorted, in descending order, by the Insertion Sort [14] algorithm;

\(\bullet\) initialize _DPSS-ALG_ on _S_;

\(\bullet\) while _S_ is not empty, perform the following:

- _repeatedly_ invoke _DPSS-ALG_ on _S_ to perform a PSS query with parameters (1,0) until the sampling result \(T\neq\emptyset\);

- let _x_<sup>∗</sup> be the item in _T_ with the _largest_ weight and let _w(x_<sup>∗</sup>)=2_<sup>a<sup>∗</sup></sup>_;

- invoke _DPSS-ALG_ to delete _x_<sup>∗</sup> from _S_;

- invoke Insertion Sort to insert the weight exponent, _a_<sup>∗</sup>, of _x_<sup>∗</sup> to _R_ (in descending order);

\(\bullet\) return _R_ as the sorted list of all the integers in _I_ (in descending order);

**Correctness.** When the above algorithm terminates, _R_ contains all the _N_ integers in _I_. As _R_ is maintained by the Insertion Sort algorithm, _R_ is a correct sorted list of _I_.

**Running Time Analysis.** Next we analyse the overall expected running time of the above integer sorting algorithm. First, the construction cost of the item set _S_ is bounded by _O(N_) and the preprocessing cost of _DPSS-ALG_ is _t<sub>p</sub>(N_). Next, we focus on the running time in each iteration in the while-loop. Denote the item set at the start of the _i_<sup>th</sup> iteration by _S<sub>i</sub>_, where \(i\in\{1,\dots,N\}\) and _S_<sub>1</sub>=_S_.

Lemma 5.1. _In the i_<sup>_th_</sup> _iteration, in expectation, at most two PSS queries with parameters_ (1,0) _on S<sub>i</sub> are invoked to obtain a non-empty subset sampling result, T._

Proof. To prove this lemma, it suffices to show that the _largest item_ (i.e., with the largest item weight) in _S<sub>i</sub>_ will be selected in the sampling result _T_ with probability at least \(\frac{1}{2}\). As a result, with at most 2 trials, in expectation, the largest item would be sampled in _T_, and hence, _T_ is non-empty.

<sup>2</sup>To achieve distinctness, to each integer, we can append a unique ID with a word in its binary representation.

