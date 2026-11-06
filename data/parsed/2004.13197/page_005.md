#### Relation to string sorting.

Arge et al. [5] study the I/O complexity of sorting strings in external memory. The authors consider different models of key divisibility and derive upper and lower bounds for each model. The problem is different from ours because strings are not atomic: they can be broken into their individual characters which can reduce the I/O complexity of sorting.

Many systems are designed to be consistent with the notion of indivisible keys. For example, sorting and searching libraries such as GNU Sort [21] or Oracle Berkeley DB [10] allow (or require) one to pass in a comparison function as a parameter. Note that the algorithms and lower bounds for indivisible keys in this paper also hold as the worst-case lower bounds for string sorting -- when the entire string is necessary in memory in order to break the tie.

#### Organization.

In Section 2 we present the RAM version of our problem. We present the sorting problem in external-memory in Section 3 and relate it to the batched predecessor problem. We discuss the challenges in extending the RAM solution to this case in section 4.

We then derive lower and upper bounds on the batched predecessor problem in sections 5 and 6, respectively. We end with open problems in Section 7. Due to space constraints, complete proofs are relegated to the appendix.

## 2 Warmup: the RAM version

#### Two types, RAM version (2RAMSORT).

The input is _n_ red and _n_ blue keys, and the output is the sorted sequence of all keys. A comparison between a pair of red keys costs _a_, between a red key and a blue key costs _b_, and between a pair of blue keys costs _c_. Without loss of generality we can assume that _a\<c_.

#### Interleaving-sensitive analysis.

The optimal sorting cost in RAM depends on the final interleaving of the elements in the final sorted order. If in the final sorted order all red keys come before all blue keys, then \(\Theta(anlogn+cnlogn)\) is the optimal total comparison cost, because the algorithm that separately sorts and concatenates is optimal. However, if the red and blue keys alternate in the final sorted order, then no blue-blue comparisons are ever required to sort.

**Stripes and the interleaving parameter _k_.** A consecutive run of red or blue keys in the final sorted order is called a _stripe_. Define _k_ to be the number of blue stripes, and let \(\ell_i\) (respectively _s<sub>i</sub>_) be the number of blue (respectively<tbc>

