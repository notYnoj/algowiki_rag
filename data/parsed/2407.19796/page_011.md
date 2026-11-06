<tbc>have already been studied in the literature \[13, 12, 1\]. Our algorithm runs faster than theirs when the solution is long.

Studying mathematical and computational properties of subsequences formed by a limited number of segments is relatively a new topic. Below, we raise a few open questions related to the properties of _f_-segmental subsequences among many possible research directions.

• Is it possible to decide whether \(P\in SubSeq^{\le f}(T)\) more efficiently than _O(mn_) time for general _f_? Our proof of the conditional lower bound uses \(f\in\Theta(m)\), while Banerjee et al. \[1\] showed that it can be determined in \(\tilde{O}((n_1n_2)^{1-(1/3)^{f-2}})\) time for a \(constantf\ge 3\). For example, would an _O(fn_)-time algorithm exist?<tbc>

• Does the conditional lower bound on the time complexity of SegE (Theorem 2) hold for binary alphabets? We are somewhat optimistic on this question. Using a similar technique by Bille et al. \[2, Theorem 1\], one may be able to reduce the alphabet size, where we might need to use a direct reduction from the orthogonal vector problem, from which Bille et al. have shown the conditional lower bound on episode matching.<tbc>

• Can we enumerate "minimal occurrences" of _P_ in _T_ as subsequences with at most _f_ segments as in the episode matching, for non-constant _f_? Banerjee et al. \[1\] showed it is possible to find one of such occurrences in \(\tilde{O}((n_1n_2)^{1-(1/3)^{f-2}})\) time for a \(constantf\ge 3\).<tbc>

• Can we bound the size of _subsequence DFAs_ for SegE? Can we efficiently construct such DFAs? One can see that a DFA accepting exactly \(SubSeq^{\le f}(T)\) requires \(\Theta(f|T|)\) states when _T_=(`ab`)_<sup>n</sup>_ and \(f\le n/2\), but we do not know if there are any texts for which DFAs require more states than \(\Theta(f|T|)\).<tbc>

• Is it possible to efficiently construct an indexing structure for _T_ on which one can efficiently decide whether _P_ is an _f_-segmental subsequence of _T_? The above observation on the DFA size bound does not necessarily refute a possibility of a more elaborated indexing structure of size _O_(|_T_|).<tbc>

• One may consider another generalization of the LCS problem for _f_-segmental subsequences, where we are interested in the length of a longest common _f_-segmental subsequences, i.e., the length of longest elements of \(SubSeq^{\le f}(T_1)\cap SubSeq^{\le f}(T_2)\). This is a different problem from the one the literature and this paper have discussed. For example, `abc` is a 2-segmental subsequence of both _T_<sub>1</sub>=`abac` and _T_<sub>2</sub>=`acbc`, while they have different witness segmentations (`ab`,`c`) and (`a`,`bc`). A naive dynamic programming algorithm is possible for this problem (Appendix A), but is it possible to design a more efficient algorithm that runs fast when the solution is big enough like our algorithm for SegLCS?

## References

