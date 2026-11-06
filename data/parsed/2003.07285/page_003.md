<tbc>time \[13, 18, 25\].

On the approximation front, most of the efforts have been focused on the following question: "can a linear time algorithm approximate LCS within a factor \(o(|\Sigma|)\) where \(|\Sigma|\) is the number of symbols of the two strings?". Thus far, only negative results for this problem are presented \[1, 3\].

In an independent work, Rubinstein _et al._ \[29\] give an improved approximate solution for LCS that runs in truly subquadratic time.

Very recently, Hajiaghayi _et al._ \[19\] give massively parallel \(1+\epsilon\) approximation algorithms for both edit distance and longest common subsequence. Their algorithms run in quadratic time and the round complexity of both algorithms is constant.

## 2 Preliminaries

Throughout this paper, we study the longest common subsequence problem (LCS). In this problem, we are given two strings _s_ and <o>_s_</o> of length _n_ and we wish to find/approximate the longest sequence of (non-continuous) matches between the two strings.

Problem 1. _Let s and_ <o>_s_</o> _be two strings of length n over an alphabet_ \(\Sigma\)_. In the LCS problem, we want to find a string t with the maximum length such that t is a subsequence of both s and_ <o>_s_</o>_. In other words, one can obtain t from both s and_ <o>_s_</o> _by removing some of the characters._

We call each element _c_ of \(\Sigma\) a _symbol_ and each element of a string a _character_. A symbol may appear several times in a string but a character is associated with a specific position.

Also, we denote the alphabet size by \(m=|\Sigma|\) and let _R_:=|{(_i,j_)|_s<sub>i</sub>_=<o>_s_</o><sub>j</sub>}| be the number of pairs of characters of the two strings that have the same symbol. The assumption that both of the strings are of the same size _n_ is w.l.o.g. since one can pad enough dummy characters to the end of either _s_ or <o>_s_</o> to ensure their lengths are equal. For brevity, we use LCS to refer to the longest common subsequence problem and denote the solution for two strings _s_ and <o>_s_</o> by lcs(_s,<o>s</o>_). For a symbol \(c\in\Sigma\), we denote the frequency of _c_ in a string _t_ by fr_<sub>c</sub>(t_). Furthermore, we denote a substring of a string _t_ by _t_\[_i,j_\] where _i_ and _j_ are the starting and ending points of the substring. Similarly, we denote the _i_’th character of a string _t_ by _t<sub>i</sub>_.

Finally, a string _t_ is an \(\alpha\)-approximation of lcs(_s,<o>s</o>_), if _t_ is a substring of both _s_ and <o>_s_</o>, and \(|t|\ge|\text{lcs}(s,\overline{s})|/\alpha\).

## 3 Organization of the Paper

Our solution consists of four algorithms (Algorithms 1, 2, 3, and 4). Algorithms 1 and 2 are simpler both in terms of implementation and analysis. However, the main novelty of our work is the design and analysis of Algorithms 3, and 4.

We first give an overview of our solution in Section 4 and discuss the ideas of the algorithms. In Section 4 we simplify the problem by defining a new notation <o>_O_</o> and ignoring the factors that can be hidden inside this notation. Indeed, our analysis in Section 4 only shows how an approximation factor of \(O(n^{1/2-\epsilon})\) is possible for small enough \(\epsilon>0\).

Section 5 gives a formal proof for the approximation factor of our algorithm. This is indeed achieved by rigorous analysis of Algorithms 1, 2, 3, and 4. The proofs of Section 8 are substantially more complicated that the ones we bring in Section 4 as in Section 4 we only resort to obtaining an \(O(n^{1/2-\epsilon})\) solution for some \(\epsilon>0\). However, in Section 8 the goal is to minimize the exponent of the approximation factor.

