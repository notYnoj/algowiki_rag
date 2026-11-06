The framework of Banerjee et al. \[1\] is general enough to solve other related problems, including the segmental version of the _Episode Subsequence Matching_ in \(\tilde{O}((n_1n_2)^{1-(1/3)^{f-2}})\) time for a constant \(f\ge 3\).

In this paper, we deal with the general case where _f_ is not necessarily a constant, and our focus is to analyze the complexities of these problems. Namely, we consider SegLCS as well as the decision version of the segmental subsequence pattern matching, SegE, that asks to determine whether _P_ of length _m_ has an _f_-segmentation that can be embedded into a text _T_ of length _n_. When _f_=1, this is equivalent to the standard substring pattern matching, and when _f_=|_P_|, this is equivalent to the standard subsequence pattern matching, both of which admit linear-time solutions.

Our focus in this article is the case of general values of _f_. The main contributions of this paper are threefold:

(1) \(O((mn)^{1-\epsilon})\)-time conditional lower bound for SegE (Problem 1) under the strong exponential- time hypothesis (SETH), for any constant \(\epsilon>0\).<tbc>

(2) _O(mn_)-time algorithm for SegE (Problem 1).<tbc>

(3) \(O(fn_2(n_1-\ell+1))\)-time algorithm for SegLCS (Problem 3) where \(\ell\) denotes the length of the solution.

Result (2) gives a matching upper bound with the conditional lower bound of Result (1) for SegE. Also, this algorithm works in _O(mn_) time independently of the value of a given _f_, and thus, it is faster than applying the _O(fmn_)-time SegLCS solution by Li et al. \[12\] to SegE. Our algorithm \(O(fn_2(n_1-\ell+1))\)-time of Result (3) is based on the approach by Banerjee et al. \[1\] and Nakatsu et al.’s LCS algorithm \[15\], which is at least as efficient as the _O(fn_<sub>1</sub>_n_<sub>2</sub>)-time solution by Li et al. \[12\], and can be faster when the solution is sufficiently long. In particular, when \(n_1-\ell=O(1)\), our algorithm runs in _O(fn_<sub>2</sub>) time.

The rest of this paper is organized as follows: We give basic notions and define our problems in Section 2. In Section 3 we present our lower bound for SegE, and in Section 4 we give an algorithm for SegE running in _O(mn_) time. Section 4.2 shows that SegE can be solved in _O(m+n_) time by a KMP-based algorithm if _f_=2. Section 5 is devoted for our \(O(fn_2(n_1-\ell+1))\)-time algorithm for SegLCS. We conclude in Section 6.

## 2 Preliminaries

Let \(\Sigma\) be an alphabet. An element of \(\Sigma\) is called a character. An element of \(\Sigma^\star\) is called a string. The empty string \(\lambda\) is the string of length 0. For any strings _u_ and _v_, we denote by \(u\cdot v\) the concatenation of the strings. We often denote \(uv=u\cdot v\) if there is no confusion. For any string _u_ and a positive integer _e_, we define \(u^0=\lambda\) and _u<sup>e</sup>=uu_<sup>_e_-1</sup>. For a string _T_, the length of _T_ is denoted by |_T_|. If _T=xyz_ holds for some strings \(x,y,z\in\Sigma^\star\), then _x_, _y_, and _z_ are called a prefix, a factor, a suffix of _T_, respectively. For an integer _i_ with \(1\le i\le|T|\), the _i_th character of _T_ is denoted by _T_\[_i_\]. For integers _i,j_ with \(1\le i\le j\le|T|\), the factor of _T_ starting at position _i_ and ending at position _j_ is denoted by _T_\[_i..j_\]. For two strings _S_ and _T_, we denote by lcsuf(_S,T_) the length of longest common suffix of _S_ and _T_.

A sequence (_u_<sub>1</sub>_,...,u<sub>f</sub>_) of _f_ strings is called an _(f-)segmentation_ of its concatenation _u_<sub>1</sub>_...u<sub>f</sub>_, where each _u<sub>i</sub>_ is said to be a _segment_ of the _f_-segmentation. We say that a segmentation (_u_<sub>1</sub>_,...,u<sub>f</sub>_) of a string _P_ can be _embedded_ to another string _T_ if there exists a sequence (_p,g_<sub>1</sub>_,...,g_<sub>_f_-1</sub>_,s_) of _f_+1 (possibly empty) strings such that \(T=p\cdot u_1\cdot g_1\cdot u_2\cdot g_2\cdots g_{f-2}\cdot u_{f-1}\cdot g_{f-1}\cdot u_f\cdot s\). Each _g<sub>i</sub>_ is said to be a _gap_ in the embedding. We say that _P_ is an _f-segmental subsequence_ of a string _T_ if<tbc>

