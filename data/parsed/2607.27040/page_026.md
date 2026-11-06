and as cache lines are maintained to not hold more than _g_ elements, \(d\le g\), thus _d=g_, and the cache line is full since it contains the maximum amount of _g_ active elements. In total, inserting into randomized cache requires 5 comparisons expected and 9 moves amortized.

\(\blacktriangleright\) **Lemma C.1.** _Inserting into a randomized cache line requires O_(1) _comparisons on average and O_(1) _moves amortized._

Let _p_ denote the number of failed probes. We now show that the probability for _p\>_2_m_ is exponentially small in _m_. Observe that though probes are not independent, every individual probe has probability at least 1/2 for success regardless, and the randomized sort finishes successfully when it accumulates _m_ such successes. Thus, the behavior of the number of failed probes _p_ when the randomized sort finishes is stochastically dominated by a negative binomial distribution for _m_ successes with success probability at least 1/2. Consequently,

\(Pr[p>2m]\le Pr[NB(m,1/2)>2m]\)

Applying the Chernoff bound and optimizing the rate function yields the tail bound

\(Pr[p>2m]\le(27/32)^m\) (C.2)

To connect this tail bound to the overall comparison count, we separate the cost of probing from each cache insert: the remaining operations are _O_(1) amortized, equating to _O(m_) for _m_ cache inserts. For the _i_th cache insert, let there be _p<sub>i</sub>_ failed probes before the final, successful probe, totaling _p<sub>i</sub>_+1 comparisons. Because \(\sum p_i=p\), the cost of probing is \(\sum p_i+1\le p+m\). Combining with Lemma 2.4 and Lemma 2.5, the total computational cost is _m_lg_m+O(m_)+_p_ comparisons and _O(m_) moves. Thus, from probability bound in (C.2), the probability the algorithm makes _\>m_lg_m+O(m_)+2_m=m_lg_m+O(m_) comparisons is \(\le(27/32)^m\). Note that as the expected number of failed probes is _m_, this bound represents the probability of _\>m_ more comparisons over the expected amount.

## C.2 Deterministic Cache Lines

Now, we turn to deterministic cache lines. We will restate the definition of the sequence \(g_0\dots g_{t^\prime+1}\) with base cases

\(g_0=1\) (C.3)

\(g_1=2^{\left\lceil lg^{(t)}m\right\rceil}\) (C.4)

and for all \(2\le i\le t'\) follows the recursive relationship

\(g_i=g_{i-1}2^{g_{i-1}/2^{i-1}}\) (C.5)

By a straightforward induction on the recurrence, _g<sub>i</sub>_ is a power of 2 for all \(0\le i\le t'\). We define \(t'\) as the largest positive integer such that

\(g_{t^\prime}<lgm\) (C.6)

To account for any remaining space, we have the final term (overrides (C.4) when \(t'=0\))

\(g=g_{t^\prime+1}=g_{t^\prime}\left\lceil lgm/g_{t^\prime}\right\rceil\le g_{t^\prime} 2^{g_{t^\prime}/2^{t^\prime-1}}\) (C.7)

We bound _g_ by the definition of \(t'\)

\(lgm\le g\le lgm+g_{t^\prime}\le 2lgm\)

