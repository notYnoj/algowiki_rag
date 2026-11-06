<tbc>it helps us quantify the behavior of the adversary during small-block and large-element inputs for all three subproblems. We use this lemma to prove the lower bounds for the individual three subproblems (found in Lemma 14, Lemma 15, and Lemma 17). Then we put the three lemmas together to obtain the expression from Theorem 8.

**Lemma 9.** _Consider any algorithm for the S-k, k-_\(\tilde{k}\)_, or the k-k problem. There exists an adversary such that:_

• _On the input of any block of B short elements, the adversary answers comparisons between all elements in main memory such that the fan-out of this I/O is at most_ 2_<sup>B</sup>. In other words, the number of permutations the algorithm needs to check is reduced by a factor at most_ 2_<sup>B</sup>._<tbc>

• _On the input of any large element (costing w/B I/Os), the adversary answers comparisons between all elements in main memory such that the fan-out of this I/O is at most O(M). In other words, the number of permutations the algorithm needs to check is reduced by a factor at most O(M)._

**Proof of Lemma 9:** We prove this lemma by describing the adversary. We capture the information learned at every point of the algorithm by assigning a _search interval_ to every large element:

**Definition 10** (_Search interval_)**.** _A search interval_ \(R(\ell)=(s_i,s_j)\) _for a large element_ \(\ell\) _at step t is the narrowest interval of small elements where_ \(\ell\) _can possibly land in the final sorted order, given what the algorithm has learned so far._

It will be useful to consider the binary tree T on the set S. The search interval of any large element at any point during the execution of the algorithm is a contiguous collection of leaves in T . Note that it can never be disconnected.

For simplicity we will assume that the size of S is a power of 2, and hence T is perfectly balanced. Also, if \(R(\ell)=(s_i,s_j)\) is the range of a large element, we will make sure the adversary "rounds off" the search space so that the new range corresponds exactly to a subtree of some node in T . This is accomplished by first finding the least common ancestor _lca_ of _s<sub>i</sub>_ and _s<sub>j</sub>_, and then shrinking the search space of \(\ell\) to either the search space in the left subtree of _lca_ or to the search space in the right subtree of _lca_, whichever is larger. Thus each large element \(\ell\) at any time has an associated node in T , which we denote by \(v(\ell)\). We also denote the interval corresponding to \(v(\ell)\) (this is just the interval of its subtree) as \(I(v(\ell))\).

