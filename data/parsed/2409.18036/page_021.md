<tbc>To see this, first, observe that with the query parameters (1,0), we have \(W_{S_i}(1,0)=\sum_{x\in S_i}w(x)\). Second, by the construction of _S_, the weights of all the items are power-of-two numbers with _distinct exponents_. Therefore, it can be verified that the largest item in _S<sub>i</sub>_ must have weight \(\ge\frac{1}{2}W_{S_i}(1,0)\), and hence, the corresponding item has probability at least \(\frac{1}{2}\) to be sampled. □

Lemma 5.2. _For a PSS query with parameters_ (1,0) _on S<sub>i</sub>, the expected result size_ \(\mu_{S_i}(1,0)=1\).

Proof. It follows from the fact that \(W_{S_i}(1,0)=\sum_{x\in S_i}w(x)\) and \(\mu_{S_i}(1,0)=\sum_{x\in S_i}\frac{w(x)}{W_{S_i}(1,0)}\). □

By Lemmas 5.1 and 5.2, in the _i_th iteration, the running time for the steps of sampling a non-empty subset _T_ and finding the largest item _x_<sup>∗</sup> in _T_ is bounded by _O(t<sub>q</sub>(N_)) in expectation. Moreover, _DPSS-ALG_ deletes _x_<sup>∗</sup> from _S<sub>i</sub>_ in _t<sub>del</sub>(N_) worst-case time. As a result, summing over all _N_ iterations, the overall expected cost for these steps is bounded by \(O(N\cdot(t_q(N)+t_{del}(N)))\).

Next, we analyse the running time for the Insertion Sort.

Lemma 5.3. _The expected running time for the Insertion Sort is O(N)._

Proof. The order of the integers in _I_ is identical to the order of their corresponding weights. To ease the discussion, we treat the sorted linked list _R_ of the integers in _I_ as the sorted linked list of their corresponding items. It is known that the overall cost for Insertion Sort is bounded by \(O(N+\sum_{i=1}^N\#Swap_i)\), where #Swap_<sub>i</sub>_ is the number of _swaps_ for the item _x_<sup>∗</sup> which is inserted to the sorted linked list _R_ from the back in the _i_th iteration. Equivalently, #Swap_<sub>i</sub>_ is the number of items that have weights _smaller than w(x_<sup>∗</sup>) and were inserted to _R before_ the _i_th iteration.

Define #FutureSwap_<sub>i</sub>_ as the number of items that have weights _greater than w(x_<sup>∗</sup>) and will be inserted to _R after_ the _i_th iteration. Observe that \(\sum_{i=1}^N\#Swap_i=\sum_{i=1}^N\#FutureSwap_i\). Furthermore, define the _rank_ of an item \(x\in S_i\), denoted by rank_<sub>S<sub>i</sub></sub>(x_), as the number of items that have weight greater than _w(x_) in _S<sub>i</sub>_. Then, we have #FutureSwap_<sub>i</sub>=_rank_<sub>S<sub>i</sub></sub>(x_<sup>∗</sup>), where _x_<sup>∗</sup> is the item inserted to _R_ in the _i_th iteration. This follows from the definition of #FutureSwap_<sub>i</sub>_ and the fact that _S<sub>i</sub>_\\{_x_<sup>∗</sup>} is exactly the set of items inserted to _R_ in future iterations. As a result, it suffices to bound the expectation of rank_<sub>S<sub>i</sub></sub>(x_<sup>∗</sup>).

Claim 2. _In the i_th _iteration, consider the largest item x_<sup>∗</sup> _in the sample set_ \(T\subseteq S_i\)_. We have that_ \(\mathbb{E}[rank_{S_i}(x^*)]\in O(1)\).

Proof. As discussed earlier, the item weights are power-of-two numbers with distinct exponents. We have the following observations. First, the largest item \(y_1\in S_i\) would be sampled in the PSS query on _S<sub>i</sub>_ with parameter (1,0) with probability at least \(\frac{1}{2}\) and at most 1. Thus, the probability of the _j_th largest item _y<sub>j</sub>_ in _S<sub>i</sub>_ to be sampled is at most \(\frac{1}{2^{j-1}}\), for all \(j\in\{1,\dots,|S_i|\}\). Second, the _j_th largest item _y<sub>j</sub>_ in _S<sub>i</sub>_ has rank_<sub>S<sub>i</sub></sub>(y<sub>j</sub>)=j_-1.

Moreover, the probability that the _j_th largest item _y<sub>j</sub>_ in _S<sub>i</sub>_ is the largest item in the sample set _T_ is at most the probability of _y<sub>j</sub>_ being sampled conditioned on _T_ being non-empty. Therefore, the expected rank of _x_<sup>∗</sup> satisfies:

\(\mathbb{E}[rank_{S_i}(x^*)]\le\sum_{j=1}^{|S_i|}rank_{S_i}(y_j)\cdot Pr[y_j\text{being sampled}|T\text{is non-empty}]\)<br>
\(=\sum_{j=1}^{|S_i|}rank_{S_i}(y_j)\cdot\frac{Pr[y_j\text{being sampled}\wedge T\text{is non-empty}]}{Pr[T\text{is non-empty}]}\)<br>
\(\le\sum_{j=1}^{|S_i|}(j-1)\cdot\frac{2}{2^{j-1}}\in O(1),\)

