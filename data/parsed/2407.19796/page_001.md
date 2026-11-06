# Subsequence Matching and LCS with Segment Number Constraints

**Abstract**

The _longest common subsequence_ (_LCS_) is a fundamental problem in string processing which has numerous algorithmic studies, extensions, and applications. A sequence _u_<sub>1</sub>_,...,u<sub>f</sub>_ of _f_ strings is said to be an (_f_-)segmentation of a string _P_ if \(P=u_1\cdots u_f\). Li et al. [BIBM 2022] proposed a new variant of the LCS problem for given strings _T_<sub>1</sub>_,T_<sub>2</sub> and an integer _f_, which we hereby call the segmental LCS problem (SegLCS), of finding (the length of) a longest string _P_ that has an _f_-segmentation which can be embedded into both _T_<sub>1</sub> and _T_<sub>2</sub>. Li et al. [IJTCS- FAW 2024] gave a dynamic programming solution that solves SegLCS in _O(fn_<sub>1</sub>_n_<sub>2</sub>) time with _O(fn_<sub>1</sub>+_n_<sub>2</sub>) space, where _n_<sub>1</sub>=|_T_<sub>1</sub>|, _n_<sub>2</sub>=|_T_<sub>2</sub>|, and \(n_1\le n_2\). Recently, Banerjee et al. [ESA 2024] presented an algorithm which, for a constant \(f\ge 3\), solves SegLCS in \(\tilde{O}((n_1n_2)^{1-(1/3)f-2})\) time<sup>1</sup>. In this paper, we deal with SegLCS as well as the problem of segmental subsequence pattern matching, SegE, that asks to determine whether a pattern _P_ of length _m_ has an _f_- segmentation that can be embedded into a text _T_ of length _n_. When _f_=1, this is equivalent to substring matching, and when _f_=|_P_|, this is equivalent to subsequence matching. Our focus in this article is the case of general values of _f_, and our main contributions are threefold:

(1) \(O((mn)^{1-\epsilon})\)-time conditional lower bound for SegE under the strong exponential-time hypothesis (SETH), for any constant \(\epsilon>0\).

(2) _O(mn_)-time algorithm for SegE.

(3) \(O(fn_2(n_1-\ell+1))\)-time algorithm for SegLCS where \(\ell\) is the solution length.

## 1 Introduction

The _longest common subsequence_ (_LCS_) is a fundamental problem in string processing which has numerous algorithmic studies, extensions, and applications. Li et al. [13] proposed a new variant of the LCS problem for given string _T_<sub>1</sub>_,T_<sub>2</sub> and integer _f_, which we hereby call the _segmental LCS_ problem (SegLCS). A sequence _u_<sub>1</sub>_,...,u<sub>f</sub>_ of _f_ strings is said to be an (_f_-)segmentation of a string _P_ if \(P=u_1\cdots u_f\). SegLCS asks to find (the length of) a longest string _P_ that has an _f_-segmentation which can be embedded into both _T_<sub>1</sub> and _T_<sub>2</sub>. Throughout this paper, we assume \(n_1=|T_1|\le n_2=|T_2|\) without loss of generality. Li et al. [12] gave a dynamic programming solution that solves SegLCS in _O(fn_<sub>1</sub>_n_<sub>2</sub>) time with _O(fn_<sub>1</sub>+_n_<sub>2</sub>) space. Recently, Banerjee et al. [1] presented an algorithm which, for a constant \(f\ge 3\), solves SegLCS in \(\tilde{O}((n_1n_2)^{1-(1/3)f-2})\) time. April 8, 2025 DRAFT

<sup>1</sup>\(\tilde{O}(\cdot)\) suppresses polylogarithmic factors.

Yuki Yonemoto<sup>1</sup>, Takuya Mieno<sup>2</sup>, Shunsuke Inenaga<sup>1</sup>, Ryo Yoshinaka<sup>3</sup>, and Ayumi Shinohara<sup>3</sup>

<sup>1</sup>Kyushu University, Japan

<sup>2</sup>University of Electro-Communications, Japan

<sup>3</sup>Tohoku University, Sendai, Japan

