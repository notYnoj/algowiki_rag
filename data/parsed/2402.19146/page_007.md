• **Strong Exponential Time Hypothesis (SETH):** For any \(\epsilon>0\), there exists \(k\ge 3\) such that the _k_-SAT problem cannot be solved in \(O(2^{(1-\epsilon)n})\) time.

Further, consider the Orthogonal Vector (OV) problem: Given two sets of _n<sub>A</sub>_ vectors _A_ and _n<sub>B</sub>_ vectors _B_ such that \(A,B\subset\{\alpha|\alpha\in\{0,1\}^d\}\), determine whether there exist two vectors \(\alpha,\beta\in A\) that are orthogonal. Regarding the OV problem, the following hypotheses are considered in the literature:

• **Orthogonal Vector Hypotheses (OVH):** For _n<sub>A</sub>=n<sub>B</sub>_, there are no \(\epsilon>0\) such that the OV problem can be solved in \(O(n_A^{2-\epsilon}\mathsf{poly}(d))\) time.<tbc>

• **Unbalanced Orthogonal Vector Hypotheses (UOVH):** Let \(0<\lambda\le 1\), there are no \(\epsilon>0\) such that the OV problem restricted to \(n_B=\Theta(n_A^\lambda)\) and \(d\le n^{o(1)}\) can be solved in \(O((n_An_B)^{1-\epsilon})\) time.

It is known that SETH implies OVH and UOVH \[11, 21\]. Thus, if OVH or UOVH is false, then SETH is also false.

## 3 Combinatorial properties of CT-matching on binary strings

In this section, we exploit new properties of CT-matching on binary strings, which we will use for designing efficient algorithms for CT-MSeq and CT-LCS on binary strings in Section 4.1 and Section 5.2, respectively.

We first recall the _parent-distance representation_ presented by Park et al. \[3\]: Given a string _S_\[1_..n_\], the parent-distance representation of _S_ is an integer string _PD(S_)\[1_..n_\], which is defined as follows:

\(PD(S)[i]=\left\{\begin{array}{ c c }
i-max_{1\le j<i}\{j|S[j]\le S[i]\} & \text{if such}j\text{exists}, \\
0 & \text{otherwise.}
\end{array}\right.\)

For example, the parent-distance representation of string \(S=\langle\mathtt{1},\mathtt{0},\mathtt{1},\mathtt{1},\mathtt{0},\mathtt{0},\mathtt{1}\rangle\) is \(PD(S)=\langle\mathtt{0},\mathtt{0},\mathtt{1},\mathtt{1},\mathtt{3},\mathtt{1},\mathtt{1}\rangle\).

**Lemma 1** (\[3\]) _Two strings S_<sub>1</sub> _and S_<sub>2</sub> _CT-match if and only if S_<sub>1</sub> _and S_<sub>2</sub> _have the same parent-distance representations._

Lemma 1 allows for determining whether two strings CT-match or not. We will only use this representation to guarantee the correctness of our algorithms for the binary case, and do not explicitly compute it.

We start from a simple observation of CT-matching on binary strings. The following observation and lemmas will support our algorithm for the binary alphabet {0,1}.

_Observation 1_ For any non-empty string _S_, _PD(S_)=01<sup>|_S_|-1</sup> if and only if _S_ is non- decreasing. Namely, a non-decreasing sequence CT-matches only a non-decreasing sequence.<tbc>

