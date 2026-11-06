(3) An **_O(n_<sup>6</sup>)**-time CT-LCS algorithm for general ordered alphabets.<tbc>

(4) An **_O(n_<sup>2</sup>/log_n_)**-time CT-LCS algorithm for binary alphabets.<tbc>

(5) An \(O(n^{2-\epsilon})\)-time conditional lower bound for the CT-LCS problem on alphabets of size 5, for any constant \(\epsilon>0\), under OVH.

**Keywords:** Cartesian-tree, Longest Common Subsequence, Subsequence Matching, Conditional Lower bound

## 1 Introduction

### 1.1 Cartesian-tree equivalence of strings

In the recent large-scale data era, efficiently-computable string matching models which are capable of capturing _structural similarities_ are important for the analysis of numerical sequences such as time series. For instance, in financial markets, it seems more natural to focus on price fluctuation patterns in stock data, than to look for identical matches.

_Order-preserving matching_ (_OP-matching_) [1, 2] is a natural model for dealing with numerical sequences: Two strings _A_ and _B_ of length _n_ are said to be OP-match (or OP-equivalent) iff the lexicographical rank of _A_\[_i_\] in _A_ and that of _B_\[_i_\] in _B_ are equal for all \(1\le i\le n\).

_Cartesian-tree matching_ (_CT-matching_), first proposed by Park et al. [3], is another model for dealing with numerical sequences: Two strings _A_ and _B_ of length _n_ are said to be CT-match (or CT-equivalent) iff the (unlabeled) Cartesian-trees [4] of _A_ and _B_ are isomorphic. The CT-matching model is a relaxation of the OP-matching model, i.e., any OP-matching strings also CT-match, but the opposite is not true (for instance, \(A=\langle 1,1,2\rangle\) and \(B=\langle 1,1,1\rangle\) CT-match, but they do not OP-match). CT-matching has attracted attention in terms of pattern matching [3, 5], string periodicity [3], and indeterminate strings [6].

### 1.2 Subsequence matching under Cartesian-tree equivalence

In this article, we first deal with _subsequence_ matching under the CT-matching model (_CT-MSeq_): Given a text _T_ of length _n_ and a pattern _P_ of length _m_, find all minimal intervals \[_i,j_\] in _T_ such that _T_\[_i..j_\] contains a subsequence _Q_ that CT-matches _P_. This can be seen as the CT-matching version of the classical _episode matching_ [7]. Oizumi et al. [8] showed an algorithm that solves the CT-MSeq problem in _O(nm_loglog_n_) time and _O(n_log_m_) space for general ordered alphabets of arbitrary size. This is interesting since subsequence matching is NP-hard under OP-matching [9].

We revisit the CT-MSeq problem and present the following new results in the case of smaller alphabets:

(1) an _O(nm_)-time and _O(n_)-space CT-MSeq algorithm for binary alphabets.<tbc>

(2) an \(O((nm)^{1-\epsilon})\)-time conditional lower bound for the CT-MSeq problem on alphabets of size 4, for any constant \(\epsilon>0\), under the Orthogonal Vector Hypothesis (OVH).<tbc>

