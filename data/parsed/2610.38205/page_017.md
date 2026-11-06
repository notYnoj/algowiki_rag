_Proof._ Because Algorithm 3.2 processes opt in increasing guesses of doubling magnitude, there must be some iteration where \(\mathsf{OPT}_{\alpha(1+\varepsilon)}<\mathsf{opt}\le 2\mathsf{OPT}_{\alpha(1+\varepsilon)}\). If _p<sub>i</sub>_ is still unsolved (i.e. contained in _Q_) by this point, then by Observation 3.7, it will be solved on this iteration with probability at least \(1-1/n^{\gamma-1}\). Thus, by Observation 3.2, with probability \(\ge 1-1/n^{\gamma-1}\), _p<sub>i</sub>_ is removed from _Q_ having received at most \(\frac{C}{c}\cdot\mathsf{opt}\cdot(log_2n+\gamma)\le\frac{2C}{c}\cdot\mathsf{OPT}_{\alpha(1+\varepsilon)}\cdot(log_2n+\gamma)\) edges from PartialVoteCover.

Thus, the final adjacency list of _p<sub>i</sub>_ is the union of \(\mathsf{optln}n\le 2\mathsf{OPT}_{\alpha(1+\varepsilon)}lnn\) random sets assigned by Line 5 and \(\le\frac{2C}{c}\cdot\mathsf{OPT}_{\alpha(1+\varepsilon)}\cdot(log_2n+\gamma)\) edges returned by PartialVoteCover. Combining these yields a total of \(O(\mathsf{OPT}_{\alpha(1+\varepsilon)}logn)\) edges.

Applying a union bound over all _n_ set cover instances, all adjacency lists are within an _O_(log_n_) factor of optimal with probability \(\ge 1-1/n^{\gamma-2}\).

## 3.2.2 Running Time

We now consider the running time of Algorithm 3.2.

While Lemma 3.5 establishes that BatchedVoteCover successfully solves each set cover instance within log(OPT) attempts, efficiently executing this procedure requires carefully bounding the time spent processing votes. Recall from Lemma 3.6 that PartialVoteCover spends time proportional to the sum frequency of all sampled elements. To achieve our desired running time, introduce a randomized preprocessing step to each set cover instance to limit the maximum number of sets containing any uncovered element.

**Lemma 3.9** (Frequency Bounding via Random Sets)**.** _Suppose we add a collection_ R _of_ optln_n sets chosen uniformly at random to the cover for p<sub>i</sub>. Let U be the set of elements remaining uncovered. With high probability, no element in U is contained in more than O(n/_opt) _sets._

_Proof._ Consider an element _p_ that is contained in at least \(\lambda\cdot n/\mathsf{opt}\) sets for some constant \(\lambda\). The probability that a single randomly chosen set covers _p_ is at least \(\frac{\lambda\cdot n/\mathsf{opt}}{n}=\frac{\lambda}{\mathsf{opt}}\). If we sample optln_n_) random sets, the probability that _p_ is not covered by any of them is at most

\(\left(1-\frac{\lambda}{\mathsf{opt}}\right)^{\mathsf{optln}n}\le exp(-\lambda lnn)\le\frac{1}{n^\lambda}\)

for an arbitrarily large constant \(\lambda\). Taking a union bound over all elements ensures that all high- frequency elements are covered with probability \(\ge 1-1/n^{\lambda-1}\), leaving only elements contained in _O(n/_opt) sets in _U_.

With the frequency of the uncovered elements bounded, we can efficiently execute the voting process inside PartialVoteCover. Since BatchedVoteCover adds optln_n_ outneighbors to each point _p<sub>i</sub>_, it follows that with probability \(\ge 1-1/n^{\lambda-2}\) (union bounding across all set cover instances), any uncovered target in any instance is contained in fewer than \(\lambda\cdot n/\mathsf{opt}\) sets. We now apply this directly to Lemma 3.6 to achieve the following result:

**Corollary 3.10.** _The execution of PartialVoteCover once for each active set cover instance in BatchedVoteCover takes_ \(\widetilde{O}(n^2)\) _total time._

Finally, we can bound the total running time of BatchedVoteCover.

**Lemma 3.11.** _The execution of BatchedVoteCover takes_ \(\widetilde{O}(n^\omega log(\Delta)/\varepsilon)\) _time._

