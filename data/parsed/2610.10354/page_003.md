## 1 Introduction

The _Min-Plus Convolution_ problem is one of the central problems in fine-grained complexity. Given two integer sequences _A_ and _B_ of length _n_, the task is to compute the sequence _A∗B_ where (_A∗B_)[_k_]=min_<sub>i</sub>(A_[_i_]+_B[k-i_]). Naively this takes time _O(n_<sup>2</sup>), and the fastest known algorithm achieves only mild improvements, \(n^2/2^{\Omega(\sqrt{logn})}\) \[Wil18\]. This leads to the _Min-Plus Convolution Hypothesis_ \[CMWW19, KPS17\] postulating that truly subquadratic time \(O(n^{2-\epsilon})\), for some constant \(\epsilon>0\), is impossible.<sup>1</sup> This hypothesis has been used to establish conditional lower bounds for problems including Knapsack \[CMWW19, KPS17\], Unbounded Subset Sum and the Frobenius problem \[Kle22\], Integer Programming \[JR23\], Tree Sparsity \[BIS17\], hop-bounded shortest paths \[KP23, VXXZ25\], and an approximate version of 3SUM \[BGK24\].

Beyond its many applications, the Min-Plus Convolution Hypothesis plays a central conceptual role in the landscape of fine-grained complexity. It is closely connected to the famous _3SUM_ and _APSP_ Hypotheses, and in fact implies them both \[BCD<sup>+</sup>14, BIS17\]. Thus, it can be viewed as a unified hypothesis of two of the main pillars of the area. In particular, the Min-Plus Convolution Hypothesis is one of the strongest well-established hypotheses, implying more conditional lower bounds than most other fine-grained assumptions. This makes studying Min-Plus Convolution a fundamental problem in its own right.

In this work, we establish several strong results that significantly sharpen our understanding of Min-Plus Convolution. We design a _universe reduction_: assuming a plausible hypothesis from additive combinatorics, we show that the Min-Plus Convolution Hypothesis is equivalent to its _strong_ variant, which asserts hardness even for instances with integer weights bounded by _O(n_). As a consequence, we obtain tight conditional lower bounds for a variety of long-standing convolution problems with "intermediate" complexity, including Min-Max Convolution and Bounded Monotone Min-Plus Convolution.

### 1.1 Starting Point

Our starting point is a recent breakthrough by Fischer \[Fis26\], which establishes analogous results for the APSP problem. Specifically, Fischer shows that the APSP Hypothesis and the Strong APSP Hypothesis are equivalent, assuming a plausible hypothesis from additive combinatorics and that \(\omega=2\). He further shows that the Directed Unweighted APSP Hypothesis, stating that APSP in unweighted directed graphs requires _n_<sup>2.5-_o_(1)</sup> time, is in this equivalence class. This greatly sharpens our understanding of the role of the universe size in APSP.

Given that Min-Plus Convolution and APSP are similar in many ways, one might wonder whether Fischer’s technique transfers. In particular, can it be applied to show the equivalence between the Min-Plus Convolution Hypothesis and the Strong Min-Plus Convolution Hypothesis?

At a high level, Fischer \[Fis26\] follows a structure-versus-random approach that could, in principle, apply to any problem _P_, and that has already been successful in other fine-grained reductions \[ABKZ22, ABF23, JX23, CVX23\]. It can be summarized in three generic steps:

(1) Identify a suitable measure of _structure_ for _P_.<tbc>

(2) Show that _P_ can be solved fast on _structured_ instances.<tbc>

<sup>1</sup>Unless otherwise specified, the entry bounds of all problems we consider are polynomially bounded in the input size. The postulated lower bounds hold in the Word-RAM model with \(\Theta(logn)\)-bit words, and hold against potentially randomized algorithms.

