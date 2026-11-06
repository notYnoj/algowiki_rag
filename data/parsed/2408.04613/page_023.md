\(log(1+\delta(A^*)+\delta(B^*))=\mathcal{O}(w)\), we get that the sum of \(\mathcal{O}((p_i^*+q_i^*+r_i^*)/w)\) over all recursive calls is limited by \(\mathcal{O}(p^*+q^*+r^*+\delta(A^*)+\delta(B^*))\). Furthermore, since there are at most \(1+log(1+\delta(A^*)+\delta(B^*))\) recursion levels, there are \(\mathcal{O}(1+\delta(A^*)+\delta(B^*))\) recursive calls in total, and thus the sum of \(\mathcal{O}(1+(p_i^*+q_i^*+r_i^*)/w)\) over all recursive calls is bounded by \(\mathcal{O}(p^*+q^*+r^*+\delta(A^*)+\delta(B^*))\). \(\blacktriangleleft\)

## B Range LIS Queries: Formal Proofs

In this section we give all necessary definitions and formal proofs of the algorithms described in Section 5. We start by defining the problems at hand.

\(\blacktriangleright\) **Definition B.1.** _The_ Longest Increasing Subsequence (LIS) _problem, given a sequence s_[0_..n), asks to find the maximum length of a (not necessarily contiguous) subsequence of s with strictly increasing values. The_ reporting _version further asks to output the underlying subsequence itself._

_The problem of_ Range LIS Value Queries _asks to preprocess a given sequence s and then answer queries for LIS length on contiguous subsegments of s. The_ Range LIS Reporting Queries _ask to solve the reporting version of the LIS problem on contiguous subsegments of s._

We now define the notion of a subpermutation that allows some elements of the sequence _s_ to be inaccessible.

\(\blacktriangleright\) **Definition B.2.** _A sequence_ \((s[i])_{i\in[0..n)}\) _is called a_ subpermutation _if_ \(s[i]\in[0..n)\cup\{\star\}\) _for all_ \(i\in[0..n)\)_, and the subsequence of s consisting of all elements that are not equal to ⋆ is a permutation. Such a subsequence is called the_ underlying permutation _of s and is denoted by s_<sup>∗</sup>.

_In other words, a subpermutation is a permutation in which the_ placeholder _symbol ⋆ is inserted at some positions._

\(\blacktriangleright\) **Definition B.3.** _For a subpermutation s of length n and indices_ \(i,j\in[0..n]\) _with i\<j, let_ LIS(_s[i..j_)) _be the length of the longest increasing subsequence of s[i..j_) _that does not contain any placeholder symbols ⋆._

\(\blacktriangleright\) **Definition B.4.** _For a subpermutation s of length n, we define the following edge-weighted directed graph called the_ alignment graph _of s and denoted by G<sup>s</sup> (see Figure 4 for an example). The vertex set of G<sup>s</sup> is_ \([0..n]\times[0..|s^*|]\)_. Furthermore, G<sup>s</sup> contains the following edges:_

\((x,y)\rightarrow(x,y+1)\) _of weight_ 0 _for all_ \(x\in[0..n]\) _and_ \(y\in[0..|s^*|]\);

\((x,y)\rightarrow(x+1,y)\) _of weight_ 0 _for all_ \(x\in[0..n)\) _and_ \(y\in[0..|s^*|]\);

\((i,s[i])\rightarrow(i+1,s[i]+1)\) _of weight_ 1 _for all_ \(i\in[0..n)\) _with_ \(s[i]\neq\star\);

\((x,y)\rightarrow(x-1,y)\) _of weight_ -2 _for all_ \(x\in(0..n]\) _and_ \(y\in[0..|s^*|]\).

We now show that the longest paths in _G<sup>s</sup>_ represent the answers to the range LIS queries on _s_.

\(\blacktriangleright\) **Lemma B.5.** _For a subpermutation s, the graph G<sup>s</sup> does not contain any cycles of nonnegative length._

**Proof.** Consider some cycle _C_ in _G<sup>s</sup>_. As _G<sup>s</sup>_ does not contain any edges that decrease the second coordinate of a vertex, no cycle in _G<sup>s</sup>_ may contain edges of the first and the third types from Definition B.4 as they increase the second coordinate of a vertex. As no cycle can consist of only edges of the second type, every cycle contains at least one edge of the fourth type and thus has a strictly negative length. \(\blacktriangleleft\)

