<tbc>result, _T_<sub>3</sub>. Then the algorithm repeatedly generates the index of the next potential item with bounded geometric distribution B-Geo(_p,n<sub>i</sub>_+1) and performs the same rejection sampling process until the index is _\>n<sub>i</sub>_.

Lemma 4.6. _Algorithm 4 returns a correct PSS result with parameters_ \((\alpha,\beta)\) _on the set of items in the given_ \((\alpha,\beta)\)_-significant group G<sub>X</sub>(j)._

Proof. The correctness of Algorithm 4 follows from the discussion above. That is, each bucket \(B_X(i)\in Y_j\) has a probability of 1-(1-_p)<sup>n<sub>i</sub></sup>_ to be accepted as a promising bucket independently; and each item in a promising bucket _B<sub>X</sub>(i_) has correct probability _p_ to be identified as a potential item independently, where _n<sub>i</sub>_=|_B<sub>X</sub>(i_)| and \(p=min\{1,\frac{2^{i+1}}{W_X(\alpha,\beta)}\}\). Furthermore, each potential item, _x_, is accepted in the returned sampling result independently with probability \(\frac{p_x(\alpha,\beta)}{p}\) . Therefore, each item is sampled in the returned sampling result independently with probability \(p_x(\alpha,\beta)\). \(\square\)

Theorem 4.7 (Correctness). _Given a PSS query with parameters_ \((\alpha,\beta)\) _on X, let_ \(T\subseteq X\) _be the sampling result returned by Algorithm 1. Every item_ \(x\in X\) _is selected in T independently with probability_ \(p_x(\alpha,\beta)\).

Proof. This theorem follows immediately from Lemmas 4.4, 4.5 and 4.6. \(\square\)

Theorem 4.8 (Query Complexity). _Suppose that every PSS query with parameters_ \((0,W_X(\alpha,\beta))\) _on the next-level item set Y<sub>j</sub> of a_ \((\alpha,\beta)\)_-significant group can be answered in_ \(O(1+\mu_{Y_j})\) _time in expectation, where_ \(\mu_{Y_j}\) _is the expected size of the sampling result on Y<sub>j</sub>. The overall expected running time of Algorithm 1 is bounded by_ \(O(1+\mu_X(\alpha,\beta))\).

Proof. Observe that Algorithm 1 invokes Algorithm 2 and Algorithm 3 each once, and Algorithm 4 at most three times according to Lemma 4.2. Moreover, by Lemma 4.4, the expected running time of Algorithm 2 for the insignificant instance is _O_(1). And by Lemma 4.5, Algorithm 3 takes \(O(1+\ell)\) time, where \(\ell\) is the number of items in the certain instance. Therefore, it suffices to show that the expected running time of Algorithm 4 for each significant group _G<sub>X</sub>(j_) is bounded by \(O(1+\mu)\), where \(\mu\) is the expected size of the PSS result on the items in _G<sub>X</sub>(j_) with parameters \((\alpha,\beta)\).

First, by the assumption in the theorem statement, the list _T<sub>Y<sub>j</sub></sub>_ of candidate buckets can be obtained in \(O(1+\mu_{Y_j})\) expected time, where \(\mu_{Y_j}\) is equivalent to the expected number of candidate buckets, as discussed earlier. Consider the following claim.

Claim 1. _Each candidate bucket_ \(B_X(i)\in T_{Y_j}\) _has_ \(\Omega(1)\) _probability to be accepted as a promising._

If Claim 1 holds, then \(\mu_{Y_j}\) can be bounded by \(O(\mu_\text{prom})\), where \(\mu_\text{prom}\) is the expected number of promising buckets. Moreover, by definition, each promising bucket _B<sub>X</sub>(i_) contains at least one potential item sampled with probability \(p=min\{1,\frac{2^{i+1}}{W_X(\alpha,\beta)}\}\). Thus, \(\mu_\text{prom}\) is bounded by the expected number of potential items. Furthermore, each potential item \(x\in B_X(i)\) is accepted to be in the sampling result with probability \(\frac{p_X(\alpha,\beta)}{p}\ge\frac{1}{2}\). This is because, by the fact that \(x\in B_X(i)\), we have \(w(x)\in[2^i,2^{i+1})\). Therefore, \(\mu_{Y_j}\) is then bounded by the expected number of promising buckets, then bounded by the expected number of potential items, and thus, bounded by the expected size of the PSS result, \(O(\mu)\). And hence, all the processing costs on the candidate buckets, promising buckets and the potential items can be charged to the output cost, in expectation.

Now, we **prove** Claim 1. Consider a candidate bucket \(B_X(i)\in T_{Y_j}\); let _n<sub>i</sub>_=|_B<sub>X</sub>(i_)| and \(p=min\{1,\frac{2^{i+1}}{W_X(\alpha,\beta)}\}\). Recall that Algorithm 4 considers two cases:

