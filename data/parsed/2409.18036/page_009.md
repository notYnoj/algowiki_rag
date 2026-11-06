<tbc>Proof. The construction of BG-Str(_X_) mainly involves the constructions and maintenance of _sorted linked lists_ of non-empty buckets (and non-empty groups) of length at most \(\lfloor log_2w_{max}\rfloor\le d\). According to Fact 2.1 in the Word RAM model, each of them can be constructed in _linear_ time with _linear_ space to its size. As the sum of all their sizes is bounded by _O(N_) (because they are non-empty), the overall construction cost and space consumption of them are bounded by _O(N_). \(\square\)

**Answering a PSS query on** _X_ **with BG-Str(_X_).** Consider the bucket-grouping structure BG-Str(_X_), constructed on the item set _X_. Given a PSS query with parameters \((\alpha,\beta)\), the buckets _B<sub>X</sub>(i_) can be categorized into three types. It is worth mentioning that BG-Str(_X_) itself does not have the concept of the query parameters \((\alpha,\beta)\) when constructed. All the following concepts are defined _dynamically on the fly_ during query time by the given parameters \((\alpha,\beta)\).

\(\bullet\) \((\alpha,\beta)\)_-Insignificant Buckets. B<sub>X</sub>(i_) is an \((\alpha,\beta)\)_-insignificant bucket_ if its bucket index _i_ satisfies \(\frac{2^{i+1}}{W_X(\alpha,\beta)}\le\frac{1}{N^2}\), where recall that \(W_X(\alpha,\beta)=\alpha\cdot W_X+\beta\). Since _B<sub>X</sub>(i_) contains items with weights in the range \([2^i,2^{i+1})\), each item _x_ in a non-empty \((\alpha,\beta)\)-insignificant bucket _B<sub>X</sub>(i_) will have probability \(p_x(\alpha,\beta)<\frac{1}{N^2}\) to be selected in the sampling result.<tbc>

\(\bullet\) \((\alpha,\beta)\)_-Certain Buckets. B<sub>X</sub>(i_) is an \((\alpha,\beta)\)_-certain bucket_ if its bucket index _i_ satisfies \(\frac{2^i}{W_X(\alpha,\beta)}\ge 1\). As a result, each item in a non-empty \((\alpha,\beta)\)-certain bucket _B<sub>X</sub>(i_) is included in the sampling result with probability 1.<tbc>

\(\bullet\) \((\alpha,\beta)\)_-Significant Buckets._ If _B<sub>X</sub>(i_) is neither of the above two types, then _B<sub>X</sub>(i_) is an \((\alpha,\beta)\)- significant bucket. By definition, each item in such a non-empty bucket _B<sub>X</sub>(i_) will have probability in the range of \(\left(\frac{1}{2N^2},1\right)\) to be sampled.

Moreover, if all the possible buckets (not necessarily non-empty) in a group _G<sub>X</sub>(j_) are \((\alpha,\beta)\)- insignificant (resp., \((\alpha,\beta)\)-certain), then _G<sub>X</sub>(j_) is an \((\alpha,\beta)\)_-insignificant group_ (resp., \((\alpha,\beta)\)_-certain group_). If neither of these cases holds, _G<sub>X</sub>(j_) is a \((\alpha,\beta)\)_-significant group_. Observe that for every group, the difference between the largest and smallest bucket indices is at most log<sub>2</sub>_N_-1. Thus, no group can simultaneously contain an \((\alpha,\beta)\)-certain bucket and an \((\alpha,\beta)\)-insignificant bucket.

Lemma 4.2. _Given a PSS query with parameters_ \((\alpha,\beta)\)_, there can be at most three_ \((\alpha,\beta)\)_-significant groups in_ BG-Str(_X)._

Proof. By definition, each \((\alpha,\beta)\)-significant group contains at least one possible \((\alpha,\beta)\)-significant bucket. Furthermore, observe that the union of the probability ranges of all possible \((\alpha,\beta)\)-significant buckets is \((\frac{1}{2N^2},1)\). As a result, there can be at most 1+2log<sub>2</sub>_N_ such buckets. Since each group contains log<sub>2</sub>_N_ possible buckets with consecutive bucket indices, therefore, all these \((\alpha,\beta)\)-significant buckets must be contained in at most three \((\alpha,\beta)\)-significant groups. \(\square\)

**The Query Algorithm (Algorithm 1).** The basic idea is to answer a PSS query with parameters \((\alpha,\beta)\) on _X_ by solving the following three types of PSS query instances:

\(\bullet\) _insignificant instance:_ one PSS query with parameters \((\alpha,\beta)\) on the set of all the items from _X_ that are in the buckets in all the \((\alpha,\beta)\)-insignificant groups;<tbc>

\(\bullet\) _certain instance:_ one PSS query with parameters \((\alpha,\beta)\) on the set of all the items from _X_ that are in the buckets in all the \((\alpha,\beta)\)-certain groups;<tbc>

\(\bullet\) _next-level instances:_ one PSS query with parameters \((0,W_X(\alpha,\beta))\) on the next-level item set _Y<sub>j</sub>_ for each \((\alpha,\beta)\)-significant group _G<sub>X</sub>(j_). As each sampled next-level item in _Y<sub>j</sub>_ is essentially a bucket in _G<sub>X</sub>(j_), the items of _X_ in the bucket can be sampled with _rejection sampling_.

The detailed steps of the query algorithm are shown in Algorithm 1.

The query algorithm handles these three different types of instances with Algorithms 2, 3, and 4, respectively. The main methodology in our algorithm is _rejection sampling_. Specifically, for each<tbc>

