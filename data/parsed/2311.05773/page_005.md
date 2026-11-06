allows us to extend the backbone: we get _u<sub>i</sub>\<y\<x\<u_<sub>_i_+1</sub>, which is a chain of actual comparisons between elements of alternating color.

The simplest way to find an inversion is to uniformly at random, from all pairs in _X<sub>i</sub>_ and _X_<sub>_i_+1</sub>, pick _x_ and _y_. If the fraction of inversions is _p_, then the probability of finding an inversion is _p_ and the expected number of trials to find one is 1_/p_.

If \(\alpha\) and \(\beta\) are really large, it is efficient to use only bichromatic comparisons to find an inversion. Otherwise, some monochromatic comparisons can help. Using a well known balancing technique, we proceed in rounds and do one (or constantly many) bichromatic comparison per round, and every \(\alpha\) rounds one red-red comparison, every \(\beta\) rounds one blue-blue. Then, in an amortized sense, the monochromatic comparisons contribute cost one per round. These monochromatic comparisons are used to maintain the max / min of a sample of elements in the bucket as follows. The representative of the bucket is always considered sampled, and hence it is initially the max and min of the sample. More precisely, we maintain the sample \(S_i\subset X_i\) with \(u_i\in S_i\). When sampling uniformly \(x\in X_i\backslash S_i\), we perform one or two monochromatic comparisons to check if it is the new max or min of _S<sub>i</sub>_. If it is, say _x_=max_S<sub>i</sub>_, we (bichromatically) test _y_=min_S_<sub>_i_+1</sub>_\<x_. If this test is successful, we found an inversion _u<sub>i</sub>\<y\<x\<u_<sub>_i_+1</sub>. To get the randomness of this inversion into our framework, we use only one of its endpoints, say _y_ to split _X<sub>i</sub>_, by comparing all elements of _X<sub>i</sub>_ with _y_ leading to \(X'_i<y<X''_i(<u_{i+1})\). Because \(x\in X''_i\) and \(u_i\in X'_i\), both are nonempty. Now we choose uniformly at random \(x'\in X''_i\) and use \(y,x'\) as the inversion.

In every round of comparisons, we also chose a random \(x\in X_i\) and compare (_u_<sub>_i_-1</sub>_\<)x\<_max_S_<sub>_i_-1</sub> and min_S_<sub>_i_+1</sub>_\<x(\<u_<sub>_i_+1</sub>). If one of them is true, we found a sufficiently random inversion.

If there is no further inversion to be found, this random sampling must fail. For two buckets with _A_ red and _B_ blue elements, w.l.o.g. red smaller than blue, there are four potential proofs that no further inversion exists:

1. all _AB_ red-blue comparisons at total cost _AB_.<tbc>

2. _A_-1 red-red comparisons to find the maximal red, and _B_ red-blue comparisons with this maximum, total cost \(\alpha(A-1)+B\).<tbc>

3. _B_-1 blue-blue comparisons to find the minimal blue, and _A_ red-blue comparisons with this minimum, total cost \(\beta(B-1)+A\).<tbc>

4. _A_-1 red-red comparisons to find the maximal red, _B_-1 blue-blue comparisons to find the minimal blue, and 1 red-blue comparison between the maximum and the minimum, total cost \(\alpha(A-1)+\beta(B-1)+1\). (This case is never the cheapest if \(\alpha,\beta>1\))

Observe that the cost of these proofs only depends on the sizes of the stripes/buckets. Hence, InversionSort computes these values and chooses the cheapest. If the accumulated cost of randomized inversion finding exceeds the cost of this cheapest proof, it (deterministically) performs all comparisons required by the proof. If this indeed shows that there are no further inversions, this subproblem is finished, i.e. no longer active. Else, this attempt to establish a proof must find one or more inversions. Similar to the case of finding an inversion min_S_<sub>_i_+1</sub>_\<_max_S<sub>i</sub>_, We choose an inversion that is living up to our randomness requirements (as spelled out in Lemma 9).

Observe that the Hamiltonian is a proof of type 4 and that hence the chosen proof is at most as expensive as that part of the Hamiltonian. This fits to the purpose of the proof to only identify the stripes, not (yet) to sort the instance.

## 2.2 Description of InversionSort

