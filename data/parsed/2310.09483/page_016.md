**Theorem 4.11.** _`RSort` uses in O_(log_N_) _rounds._

_Proof._ The different iterations of each loop in `RSort` are clearly independent, so we can do them in parallel. Thus each call to `RSort` takes _O_(1) rounds. Additionally, each layer of the recursion can also be done in parallel. Since we reduce the size of the input by a constant factor in each call, the recursion depth is _O_(log_N_) and thus the algorithm works in _O_(log_N_) rounds.

Theorem 1.5 thus follows from the previous three Theorems.

By only recursively solving on the relevant side, this sorting algorithm implies a selection algorithm that returns a 4-approximation with probability \(>1-\frac{1}{N^r}\) that uses _O(N_log_N_) comparisons and _O_(log_N_) rounds. Corollary 1.6 thus follows.

## 5 A General Sorting Algorithm In Rounds

In this section, we use a connection to sorting networks to give a general sorting algorithm in rounds. We consider sorting networks of arity _k_: rather than being able to compare and swap two elements, we can sort any _k_ elements.

**Theorem 5.1.** _\[Chv92\] For all_ \(m\ge 2\)_, there exists an arity m sorting network of depth O_(log_<sub>m</sub>n)._

**Corollary 5.2.** _For any integer d\>_0_, there exists a sorting network of arity n_<sup>_O_(1_/d_)</sup> _and depth d._

This result comes from the AKS sorting network construction \[AKS83\], which has a notoriously big constant factor. Thus, we also consider asymptotically worse (with respect to _d_) networks with smaller constant factors, which are better for small _d_.

**Theorem 5.3.** _\[PP89\] For all_ \(m\ge 2\)_, there exists an arity m sorting network of depth_ \(4log_m^2n\).

**Corollary 5.4.** _For any integer d\>_0_, there exists a sorting network of arity_ \(n^{2/\sqrt{d}}\) _and depth d._

We connect this result to the adversarial comparison setting by showing that these sorting networks imply approximate sorting algorithms. Since `Tournament` gives a 2-approximate sorting, by implementing the sorting oracle with `Tournament`, we in some sense guarantee that the total approximation error only accumulates by 2 on each level of the network. Thus, for a depth _d_ network, we get a 2_d_-approximate algorithm.

**Lemma 5.5.** _Let a and b be arrays of length n. If_ \(|a_i-b_i|\le k\) _for all i, then_ \(|sorted(a)[i]-sorted(b)[i]|\le k\) _for all i._

_Proof._ We proceed by induction over _n_. When _n_=1, the result is trivial. Otherwise, let _i_=argmin(_a_), _j_=argmin(_b_). Without loss of generality, assume \(a[i]\le b[j]\). If _i=j_, then \(|sorted(a)[0]-sorted(b)[0]|\le k\) and the result follows by the induction hypothesis. Otherwise, we claim that \(|b[i]-a[j]|\le k\). If \(b[i]\ge a[j]\), then \(|b[i]-a[j]|=b[i]-a[j]\le b[i]-a[i]\le k\). Otherwise, \(|b[i]-a[j]|=a[j]-b[i]\le a[j]-b[j]\le k\). Thus, we can swap _a_\[_i_\] and _a_\[_j_\] and the assumption still holds. We thus reduce to the already solved _i=j_ case as desired.

**Lemma 5.6.** _If there exists a sorting network with arity k and depth d, then there exists a_ 2_d- approximate sorting algorithm in d rounds that takes O(nkd_) _comparisons._

