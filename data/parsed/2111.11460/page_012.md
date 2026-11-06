## 5 Counting Upper Bounds

In the previous section, we proved that you cannot count to 17 with only a single bit of local communication complexity. Here we explore how much additional complexity is required to count to higher values. We divide this investigation into three questions: (1) what is the largest _k_ such that we can solve (_n,k_)-counting with a local complexity of 2?; (2) what local complexity is required to solve (_n,n_)-counting?; and (3) what other problems can be easily solved with low local complexity using these counting strategies as a subroutine?

We tackle the second question first, describing how to solve (_n,n_)-counting with constant local complexity. This disproves the reasonable conjecture that the local complexity of (_n,k_)-counting must grow as a function of _k_ (e.g., log_k_). We then turn our attention to the question of how high we can count with a local complexity of only 2. Our solution, which deploys ideas from our (_n,n_)-counting protocol in a more complex construction, solves (_n,(n/_10))-counting, demonstrating a stark discontinuity between 1 and 2 bits of local complexity. Finally, we establish two corollaries that deploy these strategies to solve both sorting and search with constant complexity.

### 5.1 Solving (n,n)-Counting with Constant Local Complexity

We begin by considering (_n,n_)-counting, which we prove can be solved with local complexity 11. As mentioned, this disproves the natural conjecture that the local complexity of (_n,k_)-counting must grow with _k_. For ease of presentation, we begin with a strategy that assumes _n_ is a power of 2. This result can be generalized to an arbitrary _n_ at the cost of a more involved protocol.

We formalize this result below in Theorem 5.1. Its proof depends on the construction of a counting protocol that carefully minimizes the number of bits each individual node sends or receives. Given the importance of this strategy to all the results that follow in this section, we begin with a high-level summary of our protocol before proceeding with its formal description and analysis in the proof of Theorem 5.1.

**Protocol Summary:** At a high-level, the protocol that establishes Theorem 5.1 operates in two phases. During the first phase, a count of the number of 1 bits is aggregated into a distributed counter in which log_n_ nodes each hold a single counter bit. In slightly more detail, we start by partitioning the nodes into \(\Omega(n)\) groups of constant size, and for each group aggregating the count of their 1 bits into a distributed counter of constant size. We then begin repeatedly pairing up counters and having them sum up their values in a distributed manner using strategies derived from arithmetic circuit design, allowing them to calculate a sum without any single node involved in these counters needing to send or receive more than a constant number of bits.

At the end of the first phase, we have aggregated the total count into a distributed counter of size log_n_. In the second phase, the nodes that hold the counter bits help direct a descent through a binary tree with one leaf for each possible count. The goal is to arrive at the leaf corresponding to the value stored in the counter, consolidating knowledge of the entire count at a single node. To do so, each bit of the counter informs the nodes implementing its corresponding level of the tree its counter bit value, propagating it in a chain of transmissions to prevent too much local communication. Therefore, when the tree descent arrives at each level, the specific node at which it arrives knows which sub-tree on which to advance the descent.

The proof that follows details each of the steps that makes up these phases, carefully accounting for the exact number of bits sent and received in their implementation.

**Formal Result:** We now show that when implemented and analyzed carefully, the local complexity of the protocol summarized above is no more than 11.

