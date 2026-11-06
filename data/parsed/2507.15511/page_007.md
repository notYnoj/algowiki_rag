## 4 Certificate-Sensitive Framework

### 4.1 Unique-Subset-Sum Enumerator

Our algorithm begins by generating \(\Sigma(S)\), the set of all distinct subset sums of _S_. The core challenge is to do this _without duplication_--i.e., without computing the same sum multiple times via different subsets. We use an ordered traversal strategy based on prefix extensions together with the following invariant.

_Invariant_ 1. (Suppression-on-overwrite). Whenever a canonical representative for a numeric sum \(\sigma\) is replaced by a lexicographically smaller mask, the displaced representative is _marked non-expandable_ and never extended further. This guarantees each canonical sum is expanded exactly once.

#### A minimal recursive formulation (for clarity).

Before the optimized column-wise implementation (Appendix A), it helps to view the algorithm abstractly:

**Algorithm 1** AbstractEnumerateUnique(_S_)

1: \(\mathtt{Memo}\leftarrow\{0\mapsto\mathtt{empty}\text{\_}\mathtt{bitmask}\}\)

2: **function** Extend\((\sigma,b,j)\triangleright b\) is a bitmask; _j_ is next index

3: **for** _i=j_ **to** _n_ **do**

4: \(\sigma'\leftarrow\sigma+a_i;b'\leftarrow b\) with bit _i_ set

5: **if** \(\sigma'\notin\mathtt{Memo}\) **then**

6: \(\mathtt{Memo}[\sigma']\leftarrow b'\)

7: Extend\((\sigma',b',i+1)\)

8: **else if** IsLexicographicallySmaller\((b',\mathtt{Memo}[\sigma'])\) **then**

9: \(\mathtt{Memo}[\sigma']\leftarrow b'\triangleright\) overwrite with lex-min representative

10: Extend\((\sigma',b',i+1)\)

11: Extend\((0,\mathtt{empty}\text{\_}\mathtt{bitmask},1)\)

12: **return Memo**

This recursive view exposes the two core operations: (i) _emit-or-overwrite_ a representative for a sum, and (ii) _extend_ only from the (current) representative. The optimized frontier-based implementation in Appendix A enforces Invariant 1 explicitly via a `doNotExtend` flag so that an overwritten representative is never expanded again.

We emphasize that the goal of the numerator is not merely to determine feasibility, but to generate the full constructive certificate as defined in Section 3. For each unique subset sum \(\sigma\in\Sigma(S)\), the algorithm records the lexicographically minimal bitmask of a subset realizing \(\sigma\). This enables efficient reconstruction of witnesses and is necessary for correctness in constructive queries. Consequently, the runtime and space of the numerator scale with the size of this richer certificate. Full implementation details and pseudocode are provided in Appendix A. (When Controlled Aliasing is enabled, the same enumeration principles apply per half with 2-lane memoization; see §5.2 and App. E.)

#### Canonical Prefixes for High-Density Instances.

In high-density instances, where many distinct subsets may sum to the same value, a naive "first-prefix-wins" pruning strategy can fail. To guarantee correctness, our algorithm resolves collisions deterministically by defining a _canonical prefix_ for each sum--the prefix whose index mask is lexicographically minimal among all subsets producing that sum (compare bits from 1 to _n_, preferring 0_\<_1 at the first difference). By retaining<tbc>

