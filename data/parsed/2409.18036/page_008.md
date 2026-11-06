<tbc>_pn\<_1, while the last inequality is by the fact that \(n\ge 3\) and the fuction \((1-\frac{1}{n})^n\) monotonically increases with _n_. Furthermore, for the second Bernoulli trial, _i_ is accepted with probability \(\frac{1}{2p^*}\ge\frac{1}{2}\), because \(p^*=\frac{1-(1-p)^n}{np}\le 1\). Therefore, in expectation, within _O_(1) trials in total, an _i_ will be returned by our algorithm. Finally, by Facts 1 and 3, and by our Theorem 3.1, all the random variates used in each trial can be generated in _O_(1) expected time with _O(n_) worst-case space.

## 4 Our Optimal DPSS Algorithm

In this section, we show our optimal dynamic parameterized subset sampling algorithm. For ease of exposition, and based on the results in Section 3, we note that the evaluation of every random variate used in our algorithm can be performed in _O_(1) expected time with _O(n_) worst-case space.

### 4.1 A One-Level Bucket-Grouping Structure

We first introduce a one-level _Bucket-Grouping Structure_ (BG-Str) which is a key technique to our _three-level sampling hierarchy_, and which reveals the intuitions and the correctness of our algorithm. In the following, we deliberately use _X_={_x_<sub>1</sub>_,...,x<sub>N</sub>_} to denote the item set, to distinguish it from the _original_ input item set, _S_: the BG-Str will be applied recursively to construct the sampling hierarchy. To avoid the complicated _floor_ and _ceiling_ operations on the logarithmic values, without loss of generality, we assume that the size, _N_, of an item set is always a _power-of_-16 number. Otherwise, we can _conceptually_ pad with _dummy_ items, each with _zero_ weight, to make _N_ a power-of-16 number. This would only increase _N_ by a constant factor of 16 in the worst case, and hence, would not affect our theoretical results. Thanks to this, the values of log<sub>2</sub>_N_, log<sub>2</sub>log<sub>2</sub>_N_ and log<sub>2</sub>log<sub>2</sub>log<sub>2</sub>_N_ are all integers.

**The Data Structure.** Consider a PSS instance _X_={_x_<sub>1</sub>_,...,x<sub>N</sub>_}, the one-level bucket-grouping structure on _X_, denoted by BG-Str(_X_), can be constructed in four steps:

\(\bullet\) <u>Step 1: Total Weight Calculation.</u> Compute \(W_X=\sum_{x\in X}w(x)\). Observe that _W<sub>X</sub>_ is just a sum of _N_ one-word integers, and hence, _W<sub>X</sub>_ can be stored in _O_(1) words.<tbc>

\(\bullet\) <u>Step 2: Item Bucketing.</u> Assign the items in _X_ to _buckets_ by their weights. Bucket _B<sub>X</sub>(i_) is assigned all the items \(x\in X\) such that \(2^i\le w(x)<2^{i+1}\), for \(i=0,1,\dots,\lfloor log_2w_{max}\rfloor\), where _w_<sub>max</sub> is the largest possible weight of the items. All the _non-empty_ buckets (containing at least one item from _X_) are maintained in a _sorted_ linked list by their bucket index, _i_, in ascending order.<tbc>

\(\bullet\) <u>Step 3: Bucket Grouping.</u> Organize all the buckets into _groups_, where the group with index, _j_, denoted by _G<sub>X</sub>(j_), is a collection of all the non-empty buckets _B<sub>X</sub>(i_) whose bucket indices _i_ satisfy \(\left\lfloor\frac{i}{log_2N}\right\rfloor=j\), where the largest possible value of a group index, _j_, is \(j_{max}=\left\lfloor\frac{\lfloor log_2w_{max}\rfloor}{log_2N}\right\rfloor\). It is worth mentioning that each group corresponds to exactly log<sub>2</sub>_N_ consecutive possible bucket indices. Analogous to the buckets, all the _non-empty_ groups (containing at least one non-empty bucket) are maintained in a _sorted_ linked list by their group index, _j_, in ascending order.<tbc>

\(\bullet\) <u>Step 4: Next-Level Instance Construction.</u> For each non-empty group, _G<sub>X</sub>(j_), construct a _next- level PSS instance_ on a set, _Y<sub>j</sub>_, of _next-level_ items by the following steps:<tbc>

- for each non-empty bucket \(B_X(i)\in G_X(j)\), create a _next-level item_, denoted by _y<sub>i</sub>_, with weight \(w(y_i)=2^{i+1}\cdot|B_X(i)|\).<tbc>

**-** denote the set of these next-level items by _Y<sub>j</sub>_, and the PSS instance on _Y<sub>j</sub>_ is called the _next-level instance_ of _G<sub>X</sub>(j_).

Lemma 4.1. _The one-level bucket-grouping structure_, BG-Str(_X), can be constructed in O(N_) _worst- case time with O(N_) _space consumption._

