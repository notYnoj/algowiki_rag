Next we state the key technical lemma that we will need to prove our lower bound on EP<sub>C</sub>. We need the following definition of _central gates_ in order to state our key lemma, and will use the definition of the hypergeometric distribution in the proof:

**Definition 5.9.** _We say a gate_ \((i,i+2^{k_\ell})\in G_\ell\) _is_ central _if_ \(\frac{3n}{8}\le i\le\frac{5n}{8}\) .

**Definition 5.10.** _Let_ \(HG_n^{N,K}[k]\) _denote the probability that when n items are taken without replacement from a set of N items of which exactly K are marked that exactly k marked items are taken. This is given by the hypergeometric distribution:_

\(HG_n^{N,K}[k]=\genfrac(){pt}{2}{N-K}{n-k}\genfrac(){pt}{2}{K}{k}/\genfrac(){pt}{2}{N}{n},\)

_which has mean nK/N. The distribution may have one or two modes, which differ by at most 1 from the mean._

**Lemma 5.11.** _Let n be a sufficiently large power of two and_ \(\ell>\left\lceil\frac{1}{2}logn\right\rceil+1\) _be a layer in Batcher’s odd-even mergesort on n inputs. Let_ \(g=(i,i+2^{k_\ell})\in G_\ell\) _be a central gate and_ D _be the marginal distribution over input pairs_ (_x_<sub>1</sub>_,x_<sub>2</sub>) _to g induced by giving the sorting network a uniformly random permutation of the set_ \[_n_\] _as input. Then there is some constant_ \(\alpha>1\) _(independent of n) such that for every_ \((x_1,x_2)\in\mathrm{supp}(\mathcal{D})\),

\(\frac{1}{\alpha}\le\frac{\mathrm{Pr}_\mathcal{D}[(x_2,x_1)]}{\mathrm{Pr}_\mathcal{D}[(x_1,x_2)]}\le\alpha.\)

Before we more formally prove this lemma, we give a detailed and more intuitive outline of the strategy. We want to show that if there are _k_ permutations of \[_n_\] resulting in a gate \(g=(i,i+2^{k_\ell})\) receiving any feasible input _x_<sub>1</sub>_,x_<sub>2</sub>, then there must be at least \(k/\alpha\) permutations of \[_n_\] resulting in _g_ receiving input _x_<sub>2</sub>_,x_<sub>1</sub>. To prove this, we first note that due to the structure of Batcher’s odd even mergesort, if \(r\equiv i(\mathrm{mod}2^{k_\ell})\) then the top wire inputs to _g_ will have some fixed rank _t_ among the values of all wires after layer zero (the recursive step, which separately sorts the first and second half of the inputs independently) whose indices are congruent to \(r\mathrm{mod}2^{k_\ell}\), and bottom wire inputs to _g_ will have rank _t_+1 among the values of all wires after layer zero whose indices are congruent to \(r\mathrm{mod}2^{k_\ell+1}\). This observation is an immediate consequence of Proposition 5.7. We call these sets O and E respectively, since they correspond to indices _r_ plus either odd or even multiples of \(2^{k_\ell}\) respectively.

With this, we now know that the top input to _g_ is always the _t_’th ranked element of O while the bottom input to _g_ is always the _t_+1’st ranked element of E. To prove our lemma, it is sufficient to show that the number of permutations of \[_n_\] that lead to _x_<sub>1</sub> being the _t_’th ranked element of O and _x_<sub>2</sub> being the _t_+1’st ranked element of E is within a factor of \(\alpha\) of the number of permutations resulting in _x_<sub>2</sub> being the _t_’th ranked element of O and _x_<sub>1</sub> being the _t_+1’st ranked element of E.

Unfortunately, this is complicated by the fact that the indices of elements after layer zero (and hence our sets O and E) are the result of independently sorting the first half and the second half of the input. Thus the sets O and E are determined entirely by which inputs started on which half of the wires. We introduce sets _A_ and _B_ containing the values stored on the first and second half of the wires at the beginning of the circuit respectively. Note that, for the uniformly random permutation of \[_n_\] as input, the induced equipartition of \[_n_\] into _A_ and _B_ is selected uniformly at random. Then the sets O and E are entirely determined by _A_ and _B_.

