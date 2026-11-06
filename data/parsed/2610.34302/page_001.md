# Bicriteria Approximate Navigable Graphs in General Metrics

Hongyi Chen<sup>∗</sup><tbc>

<tbc>Tianyi Zhang<sup>†</sup><tbc>

**Abstract**

We study approximation algorithms for constructing sparse navigable graphs in general metrics. Given an _n_-point metric (_P_,d) and a parameter \(\alpha\ge 1\), an \(\alpha\)-navigable graph is a directed graph _G_=(_P,E_) such that for every ordered pair of distinct points \(s,t\in P\), the vertex _s_ has an outgoing edge (_s,p_) with d(_p,t_) < d(_s,t_) / \(\alpha\). The objective is to minimize the number of edges. The study of approximation algorithms for sparse navigable graphs in general metrics was recently initiated by Khanna, Padaki, and Waingarten (SODA 2026), and independently by Conway et al. (SODA 2026). These works show that the single-criterion problem faces a Set Cover barrier: an _O_(log_n_)-approximation is achievable, whereas obtaining an _o_(log_n_)-approximation is NP-hard. To obtain faster algorithms, Khanna, Padaki, and Waingarten (SODA 2026) introduced bicriteria approximation, in which the output graph is required to be \(\alpha\)-navigable, while its size is compared against that of an optimal \(\beta\)-navigable graph for some relaxed parameter \(\beta\ge\alpha\). They gave a fast matrix-multiplication-based algorithm that computes an \((\alpha,2(1+\varepsilon)\alpha)\)-bicriteria _O_(log_n_)-approximation in time \(\widetilde{O}(n\omega log\Delta/\varepsilon)\), where \(\Delta\) denotes the aspect ratio and \(\omega\) is the matrix multiplication exponent. Our main result is a simpler near-quadratic-time algorithm with stronger bicriteria guarantees. For every constant \(\alpha\ge 1\), we compute in time \(\widetilde{O}(n2log\Delta)\) an \(\alpha\)-navigable graph that is simultaneously an \((\alpha,2\alpha+O(1))\)-bicriteria _O_(1)-approximation and an \((\alpha,\alpha+O(1))\)-bicriteria _O_(log_n_)-approximation. We complement the algorithm with a hardness result showing that for every constant \(\eta\in(0,1)\), no polynomial-time algorithm can compute an \((\alpha,2\alpha-\eta)\)-bicriteria _o_(log_n_)-approximation unless P = NP.

<sup>∗</sup>State Key Laboratory for Novel Software Technology, Nanjing University, `hychener01@gmail.com` <sup>†</sup>State Key Laboratory for Novel Software Technology, Nanjing University, `tianyiz25@nju.edu.cn`

