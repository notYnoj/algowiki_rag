algorithm is proportional to the depth of recursion. See Appendix A for a formal description of the algorithm.

## 5 Range LIS Queries: Sketch

One of the original applications of Tiskin’s procedure for simple unit-Monge matrix multiplication [42,45] is an algorithm that preprocesses a given sequence \((s[i])_{i\in[0..n)}\) of integers in O(_n_log<sup>2</sup>_n_) time so that _Range Longest Increasing Subsequence_ (Range LIS) queries can be answered in O(log_n_) time. We show an alternative way of obtaining the same result using Theorem 1.2 and avoiding the seaweed braid formalism. The extension of Theorem 4.7 allows recovering the underlying longest increasing subsequence of length \(\ell\) in \(\mathcal{O}(\ell log^2n)\) time. Further O(_n_log<sup>3</sup>_n_)-time preprocessing allows for \(\mathcal{O}(\ell)\)-time recovery, which improves upon the result of [29].

Without loss of generality we assume that \((s[i])_{i\in[0..n)}\) is a permutation of [0_..n_).<sup>4</sup> We use a popular tool for string similarity problems and interpret range LIS queries as computing the longest path between some pair of vertices of a corresponding _alignment graph G<sup>s</sup>_; see Figure 3. The crucial property of _G<sup>s</sup>_ is that it is planar, and thus due to [20, Section 2.3], the matrix _M<sup>s</sup>_ of longest distances from the vertices in the bottom row to the vertices of the top row of this graph is anti-Monge.<sup>5</sup> Thus, the problem of constructing a data structure for range LIS queries is reduced to the problem of computing the condensed representation of _M<sup>s</sup>_.

As \(\mathsf{LIS}(s[i..j))\le n\) for all \(i,j\in[0..n]\) with _i\<j_, all entries of _M<sup>s</sup>_ are bounded by O(_n_), and thus \(\delta(M^s)=\mathcal{O}(n)\) holds due to Observations 3.1 and B.10. We compute _M<sup>s</sup>_ in a divide-and-conquer fashion. We split the sequence _s_ into subsequences _s_<sup>lo</sup> and _s_<sup>hi</sup> containing all values in \([0..\lfloor\frac{n}{2}\rfloor)\) and \([\lfloor\frac{n}{2}\rfloor..n)\) respectively, and recursively compute _M_<sup>s<sup>lo</sup></sup> and _M_<sup>s<sup>hi</sup></sup>. After that, we note that _G_<sup>s<sup>lo</sup></sup> and _G_<sup>s<sup>hi</sup></sup> are essentially compressed versions of the lower half and the upper half of _G<sup>s</sup>_, respectively. Based on this, we transform _M_<sup>s<sup>lo</sup></sup> in O(_n_) time into the matrix of the longest distances from the vertices in the bottom row of _G<sup>s</sup>_ to the vertices in the middle row of _G<sup>s</sup>_. Analogously, we transform _M_<sup>s<sup>hi</sup></sup> into the matrix of the longest

<sup>4</sup> In what follows, we reserve the word "permutation" for permutations of [0_..m_) for some \(m\in\mathbb{Z}_+\). <sup>5</sup> Note that, in reality, some entries of this matrix are infinite. In the formal description of the algorithm, we augment the alignment graph so that the finite entries of this matrix are preserved and the infinite entries become finite.

5
4
3
2
1
0
0
1
2
3
4
5

**Figure 3** The alignment graph for _s_=[1,0,3,2,4], with red edges of weight 0 and green edges of weight 1. The length of the longest path from the _i_-th vertex in the bottom row to the _j_-th vertex in the top row of this graph for _i\<j_ is equal to LIS(_s[i..j_)).

