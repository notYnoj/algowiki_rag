## 8:20 Beating Trivial Time for Tricky Triangle Tasks

**Proof of Lemma 29.** We begin by preprocessing the input lists. Let \(\ell\) be the maximum length of any element. We can think of each word as being composed of size-\(2\ell\) blocks. We write down two copies of each input list, one with every element stored in the upper \(\ell\) bits of the blocks, with the lower \(\ell\) bits set to zeroes, and another with every element stored in the lower \(\ell\) bits, with the upper \(\ell\) bits set to zeroes. Note that each list requires _O(n_log_n/w_) words to write down.

To concatenate two column vectors _L<sub>i</sub>_ and _L<sub>j</sub>_ elementwise, it suffices to OR the upper- aligned version of _L<sub>i</sub>_ with the lower-aligned version of _L<sub>j</sub>_. This gives us a word-packed version of the concatenated list, taking up _O(n_log_n/w_) words. We then run the word-packed sorting algorithm in Claim 15 with block size \(2\ell\), which takes _O(n_log<sup>2</sup>_n/w_)) time.

Once we have a sorted, word-packed list, we can detect duplicate entries in linear time in the number of words. Clearly, duplicates must be adjacent entries in the list. Thus, we can simply make a second copy of the list, right-shift it by the block size \(2\ell\), and XOR the two copies. As before, it suffices to find any all-zeroes block, which we can do in constant time per word using Claim 16.

We then run this procedure for all pairs of columns, which takes _O(n_<sup>2</sup>log<sup>2</sup>_n/w_) time.

## 6.1 Subquadratic 4-Cycle Finding in Very Dense Graphs

Recall that by Theorem 10, a 4-cycle free graph has at most \(\frac{n}{4}\left(1+\sqrt{4n-3}\right)=O(n^{3/2})\) edges. Here, we give a sublinear time (in the number of edges) algorithm that finds a 4-cycle when the graph is noticeably denser, i.e., when the number of edges is \(m\ge n^{3/2+\delta}\). Recall that a _k-core_ of _G_ is a maximal subgraph \(G'\) such that every vertex has degree at least _k_.

\(\blacktriangleright\) **Lemma 30.** _For all sufficiently large n, every graph G with_ \(m=n^{3/2+\delta}\) _edges has a_ \((\sqrt{n}+1)\)_-core containing at least_ \(\Omega(\sqrt{m})\) _vertices._

**Proof of Lemma 30.** Recall that we may obtain a _k_-core by repeatedly deleting all vertices with degree smaller than _k_ and all of their incident edges, until all remaining vertices have degree at least _k_. Suppose that the \(k:=\sqrt{n}+1\) core obtained by this procedure has _s_ vertices. Then we will recover it after _n-s_ rounds of peeling, deleting at most _k(n-s_) edges at each step. It follows that \(G'\) has at least _m-k(n-s_) edges. Since \(G'\) has _s_ vertices, \(\genfrac(){pt}{2}{s}{2}\) is an upper bound on its number of edges. Therefore, we have that

\(m-k(n-s)\le\frac{s(s-1)}{2}\)<br> \(0\le s^2+(-2k-1)s+2nk-2m\)

We are interested in values of _s_ larger than its positive root, so

\(s\ge\frac{1}{2}\left((2k+1)+\sqrt{4k^2+4k+1-8nk+8m}\right)\)<br> \(=\sqrt{n}+\frac{3}{2}+\frac{1}{2}\sqrt{4n+12\sqrt{n}+9-8n^{3/2}-8n+8n^{3/2+\delta}}\)<br> \(=\sqrt{n}+\frac{3}{2}+\frac{1}{2}\sqrt{8n^{3/2+\delta}-8n^{3/2}-4n+12\sqrt{n}+9}\)<br> \(\ge\Omega(n^{3/4+\delta/2}).\)

We will use this fact to provide a sublinear (in the size of the graph) time algorithm for finding a 4-cycle when the graph is extremely dense.

\(\blacktriangleleft\)

\(\blacktriangleleft\)

