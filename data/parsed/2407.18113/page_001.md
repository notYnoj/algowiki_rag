Upper bounds on the average edit distance between two random strings

**Abstract**

We study the average edit distance between two random strings. More precisely, we adapt a technique introduced by Lueker in the context of the average longest common subsequence of two random strings to improve the known upper bound on the average edit distance. We improve all the known upper bounds for small alphabets. We also provide a new implementation of Lueker technique to improve the lower bound on the average length of the longest common subsequence of two random strings for all small alphabets of size other than 2 and 4.

## 1 Introduction

We consider two different notions of similarity between pairs of strings. The first notion is the _length of the longest common subsequence_ between two strings _u_, and _v_, denoted by LCS(_u,v_). The second notion is the edit distance (also called Levenshtein distance) between two strings _u_, and _v_, denoted by _d<sub>e</sub>(u,v_), which is the minimum number of substitutions, deletions and insertions necessary to transform _u_ to _v_.

In particular, we are interested in the average edit distance denoted _e<sub>k</sub>(n_) (resp. average length of the longest common subsequence denoted \(\ell_k(n)\)) between two random _k_-ary strings of length _n_. More precisely, we provide bounds on the two following quantities whose existence is implied by Fekete’s Lemma

\(\alpha_k=lim_{n\rightarrow\infty}\frac{e_k(n)}{n}\text{and}\gamma_k=lim_{n\rightarrow\infty}\frac{\ell_k(n)}{n}.\)

The so called Chvátal-Sankoff constant \(\gamma_2\), and the other \(\gamma_k\) received a lot of attention since 1975 [1, 2, 4, 5, 6, 8, 7, 9, 13, 18, ...]. In particular, we know that \(\gamma_2\) is algebraic [18] and that \(0.788071\le\gamma_2\le 0.826280\) [14]. Until recently the best bounds on \(\gamma_k\) for other small values of _k_ were given in [12]. A few days before the publication of the present article on the arXiv another preprint improved most of the bounds known for \(\gamma_k\) and variant of \(\gamma_k\) that consider the expected LCS of _t_ random strings [11]. In particular, they proved \(\gamma_2\ge 0.792665\) We improve on all the bounds for \(\gamma_k\) given by [11] other than \(\gamma_2\) and \(\gamma_4\) where we only beat the previous best bound by Lueker [14].

Matthieu Rosenfeld

LIRMM, Univ Montpellier, CNRS, Montpellier, France

July 26, 2024

arXiv:2407.18113v1 [math.CO] 25 Jul 2024

