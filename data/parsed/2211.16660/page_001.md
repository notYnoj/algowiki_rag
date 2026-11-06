# Approximating binary longest common subsequence in almost-linear time

**Abstract**

The Longest Common Subsequence (LCS) is a fundamental string similarity measure, and computing the LCS of two strings is a classic algorithms question. A textbook dynamic programming algorithm gives an exact algorithm in quadratic time, and this is essentially best possible under plausible fine- grained complexity assumptions, so a natural problem is to find faster approximation algorithms. When the inputs are two binary strings, there is a simple \(\frac{1}{2}\)-approximation in linear time: compute the longest common all-0s or all-1s subsequence. It has been open whether a better approximation is possible even in truly subquadratic time. Rubinstein and Song showed that the answer is yes under the assumption that the two input strings have equal lengths. We settle the question, generalizing their result to unequal length strings, proving that, for any \(\varepsilon>0\), there exists \(\delta>0\) and a \((\frac{1}{2}+\delta)\)-approximation algorithm for binary LCS that runs in \(n^{1+\varepsilon}\) time. As a consequence of our result and a result of Akmal and Vassilevska-Williams, for any \(\varepsilon>0\), there exists a \((\frac{1}{q}+\delta)\)-approximation for LCS over _q_-ary strings in \(n^{1+\varepsilon}\) time.

Our techniques build on the recent work of Guruswami, He, and Li who proved new bounds for error-correcting codes tolerating deletion errors. They prove a combinatorial "structure lemma" for strings which classifies them according to their oscillation patterns. We prove and use an algorithmic generalization of this structure lemma, which may be of independent interest.

### 1 Introduction

In this paper, we give improved approximation algorithms for the Longest Common Subsequence (LCS), a fundamental string similarity measure that is of theoretical and practical interest. The LCS of two strings, as the name suggests, is the length of the longest sequence that appears as a (not necessarily contiguous) subsequence in both strings. The LCS is one of the most ubiquitous ways to quantify the similarity of two strings, a task that appears in a variety of contexts from spell checkers to DNA processing.

Computing the LCS is a classic algorithms question. A textbook dynamic programming algorithm gives an exact algorithm in quadratic time _O(n_<sup>2</sup>), while the fastest known algorithm runs in time _O(n_<sup>2</sup>/log<sup>2</sup>_n_) [MP80]. Whether we can improve these algorithms has been a longstanding open question (see, for example, Problem 35 of [CKK72]). Under fine-grained complexity assumptions such as the Strong Exponential Time Hypothesis [AWW14, ABW15, BK15] and even more plausible hypotheses [AHWW16], there is no exact algorithm for LCS in time \(O(n^{2-\varepsilon})\) with \(\varepsilon>0\). Because of these barriers for exact algorithms, it is natural to wonder whether there are faster approximation algorithms.

<sup>∗</sup>Department of Mathematics, Princeton University, Princeton, NJ 08544, USA. Email: `xiaoyuh@princeton.edu`. Research supported by the NSF Mathematical Sciences Postdoctoral Research Fellowships Program under Grant DMS-2103154. <sup>†</sup>Department of Computer Science, UC Berkeley, Berkeley, CA, 94709, USA. Email: `rayyli@berkeley.edu`. Research supported by the NSF Mathematical Sciences Postdoctoral Research Fellowships Program under Grant DMS-2203067.

Xiaoyu He <sup>∗</sup>Ray Li †

February 13, 2023

