2. In Section 3, we extend the alternative basis work of \[32, 38\] to APA matrix multiplication. In doing so, we demonstrate that fast, symbolic basis transformations can be used to "sparsify" APA algorithms and therefore improve the leading coefficient in their arithmetic complexities.<tbc>

3. In Section 4, we show that the approximate-to-exact procedure of Bini \[9\] is stable (under some mild assumptions). In particular, we prove a weak forward stability bound for this procedure, in floating- point arithmetic and including the fast basis transformations from Section 3, that matches the format of existing bounds for fast exact matrix multiplication \[21, 53\]. To our knowledge, these are the first stability bounds of any kind for APA matrix multiplication. We also comment on the stability of evaluating an APA algorithm a fixed number of times.<tbc>

4. Finally, Section 5 presents a handful of numerical examples that validate the theoretical results from the previous sections.

Our results are captured by s 1 and 2, which show, respectively, the best ranks achieved in our search (vs. existing results in the literature) and improvements to the leading coefficient of APA algorithms obtained by sparsifying with alternative bases.

## 1.2 Notation and Conventions

In the remainder of the paper, the matrices _A_, _B_, and their product _C=AB_ are assumed to be complex. As mentioned above, we use \(\langle m_0,k_0,n_0\rangle\) to refer to \(m_0\times k_0\) by \(k_0\times n_0\) matrix multiplication (either exact or approximate) and \(\langle m_0,k_0,n_0;t\rangle\) to refer to algorithms for this problem that use _t_ scalar multiplications. Note that \(\langle m_0,k_0,n_0\rangle\) is equivalent to \(\langle m_0,n_0,k_0\rangle\), \(\langle k_0,m_0,n_0\rangle\), \(\langle k_0,n_0,m_0\rangle\), \(\langle n_0,m_0,k_0\rangle\), and \(\langle n_0,k_0,m_0\rangle\) in the sense that an algorithm for one can be adapted to an algorithm for any of the others (with the same number of scalar multiplications but possibly different additive complexity) \[33\].

\begin{tabular}{cccc}
**Size** & **Border Rank** & **Terms in Remainder** & **Exponent** \\
\(\langle m_0,k_0,n_0\rangle\) & (vs. \[56-58\]) & \(i:R_i\unknown=0\) & 3log<sub>_m_<sub>0</sub>_k_<sub>0</sub>_n_<sub>0</sub></sub>(_t_) \\
\(\langle 2,2,3\rangle\) & 10 (10) & 3, 6 & 2.7799 \\
\(\langle 2,3,3\rangle\) & 15 (14) & 3, 6 & 2.8108 \\
\(\langle 2,2,5\rangle\) & 17 (16) & 3, 4, 5, 6, 7, 8, 9 & 2.8372 \\
\(\langle 2,2,6\rangle\) & 20 (20) & 3, 4 & 2.8279 \\
\(\langle 3,3,3\rangle\) & 21 (20) & 1, 2, 3, 4, 5 & 2.7712 \\
\(\langle 2,3,5\rangle\) & 24 (23) & 3, 4, 5, 6, 7, 8, 9 & 2.8032 \\
\(\langle 2,4,4\rangle\) & 25 (24) & 3, 6 & 2.7863 \\
\(\langle 2,2,8\rangle\) & 27 (26) & 3, 4 & 2.8529 \\
\(\langle 3,3,4\rangle\) & 27 (27) & 3, 4, 5, 6, 7, 8, 9 & 2.7592 \\
\(\langle 2,3,6\rangle\) & 29 (28) & 3, 4, 6, 7 & 2.8190 \\
\(\langle 2,4,5\rangle\) & **31** (32) & 3, 4, 5, 6, 7, 8 & 2.7927 \\
\(\langle 2,3,7\rangle\) & 34 (33) & 3, 4, 5, 6 & 2.8304 \\
\(\langle 3,3,5\rangle\) & 35 (34) & 3, 4, 5, 6, 7, 8, 9 & 2.8019 \\
\(\langle 2,4,6\rangle\) & 37 (37) & 3, 4, 6, 7, 9, 10, 12, 13 & 2.7983 \\
\(\langle 2,5,5\rangle\) & 39 (39) & 3, 6 & 2.8095 \\
\(\langle 2,5,6\rangle\) & 46 (46) & 3, 4, 6, 7, 9, 10 & 2.8053 \\
\(\langle 3,3,7\rangle\) & 48 (48) & 3, 4, 5, 6, 7, 8, 9, 11 & 2.8031 \\
\end{tabular}

1: The best border rank _t_ achieved by the search algorithm discussed in Section 2 for a variety of dimension triplets \(\langle m_0,k_0,n_0\rangle\). For reference, we list in parentheses the best border rank attained by Smirnov in \[56-58\]. For each size, we also describe the remainder for one \(\langle m_0,k_0,n_0;t\rangle\) scheme. Corresponding encoding matrices can be found at https://github.com/nliskij/border-rank.

