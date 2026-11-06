### Organisation.

Section 3 introduces preliminaries. Section 4 presents our first contribution: a certificate-sensitive framework that algorithmically realizes Instance Complexity. Section 5 develops our second contribution, a deterministic Subset Sum solver with a worst-case runtime below the classical 2<sup>_n/_2</sup> bound. Section 6 contributes a refined structural perspective on fine-grained hardness and its implicit assumptions. Section 7 provides empirical validation. Finally, Sections 8-10 place our results in broader context and outline directions for future research.

## 3 Preliminaries

### Computational Model.

We adopt the standard Word-RAM model with word size \(w=\Theta(logM)\), where \(M:=max\{\sum_{a\in S}a,t\}\), so that arithmetic, comparisons, and memory accesses on _w_-bit words take _O_(1) time. Equivalently, _w_ is large enough that every subset sum and _t_ fit in a single word, so additions and comparisons on sums are unit-cost. All logarithms are base two unless stated otherwise.

### Randomized Model.

Our randomized variants rely on standard _2-universal_ hashing. We assume that evaluating a hash function and handling collisions can be done in expected _O_(1) time in the Word-RAM model. For any \(x\neq y\), \(Pr_{h\sim\mathcal{H}}[h(x)=h(y)]\le 1/n^c\) for a fixed constant \(c\ge 1\), and expectations are taken over the random draw of _h_. Collisions are resolved by exact bitmask comparison, ensuring _Las Vegas_ correctness: the output is always correct, and the runtime bound holds in expectation.

### Asymptotic Notation.

We use \(O^*(\cdot)\) and \(o^*(\cdot)\) to suppress factors polynomial in _n_ and log_M_, unless explicitly shown.

### Notation.

Let (_S,t_) be a Subset Sum instance, where \(S=\{a_1,\dots,a_n\}\subseteq\mathbb{Z}_{\ge 0}\) is a multiset of _n_ nonnegative integers and \(t\in\mathbb{Z}_{\ge 0}\) is a nonnegative target. We write \[_n_\]={1,2_,...,n_} and let

\(\Sigma(S)=\left\{\sum_{i\in T}a_i\big|T\subseteq[n]\right\}\)

denote the set of _distinct subset sums_. The empty sum is included by convention, so \(0\in\Sigma(S)\). Let \(U:=|\Sigma(S)|\). Throughout this paper, we consider each sum \(\sigma\in\Sigma(S)\) to be implicitly paired with its canonical prefix representation (i.e., its lexicographically minimal index mask).

### Subset Sum Notation.

For any subset \(A\subseteq S\), we write \(\sigma(A)\) to denote the sum of its elements:

\(\sigma(A):=\sum_{a\in A}a.\)

This distinguishes numerical subset sums from the set of all distinct sums, denoted \(\Sigma(S)\).

**Definition 1** (Distinct Subset Sums)**.** _The quantity_ \(U=|\Sigma(S)|\) _denotes the number of distinct subset sums of S. Trivially,_ \(1\le U\le 2^n\)_. The lower bound is met when S is empty, and the upper bound is met when all_ 2_<sup>n</sup> subset sums are unique._

This parameter _U_ will serve as our central structural complexity measure. It governs both the algorithmic behavior of IC-SubsetSum and the size of the certificate it produces.

