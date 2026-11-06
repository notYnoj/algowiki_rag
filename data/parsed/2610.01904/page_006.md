## 4.2 Evaluation Results

The empirical evaluation demonstrates that the proposed coordinate descent training strategy significantly reduces the computational overhead required to achieve a target approximation ratio. The cost-saving distributions presented in Figs. 2, 3, and 4 must be interpreted as strictly conditional comparisons: each plotted value is computed exclusively over instances for which both the proposed method and the corresponding baseline successfully attained the designated target approximation ratio.

Across the evaluated graph families, the proposed method yields consistently positive and substantial cost reductions when compared against Adam, GD, L-BFGS-B, NM, and Powell at a baseline target approximation ratio of \(\alpha_\text{target}=0.94\), as visualised in Fig. 2. An analysis of the overall distributions reveals that gradient-based baselines are particularly outperformed, with the proposed method achieving mean savings of 96.2% against GD and 92.0% against Adam. While derivative-free methods exhibit a wider variance in their cost-saving distributions, their overall performance still strongly favours the proposed method, demonstrating mean savings of 88.3% against L-BFGS-B, 80.2% against NM, and 77.0% against Powell. This systematic advantage suggests that explicitly exploiting the analytic, coordinate-wise sinusoidal structure of the multi-angle quantum approximate optimisation algorithm (ma-QAOA) objective landscape successfully circumvents the extensive evaluations that generic multidimensional routines expend on estimating descent directions, adapting step sizes, or constructing local surrogate models.

While the conditional cost-saving metrics in Fig. 2 illustrate sample efficiency during successful trials,  2 provides critical context regarding the convergence reliability and robustness of the evaluated optimisers. Because cost-saving calculations inherently exclude failed runs, they can mask an algorithm’s susceptibility to premature convergence. The proposed method demonstrates superior reliability, crossing the \(\alpha_\text{target}=0.94\) threshold in a significantly higher number of instances where several baselines fail entirely, particularly GD, L-BFGS-B, NM, Powell, and SPSA.

This discrepancy between conditional efficiency and absolute reliability is most acute for SPSA. Although subsequent conditional analyses in Fig. 4 suggest SPSA is highly sample-efficient when it converges,  2 reveals a substantial robustness deficit. Out of 750 total evaluation cases, there are 123 instances where solely the proposed method crosses the target, compared to a mere 7 instances where only SPSA succeeds. This stark contrast indicates that while SPSA’s dimension-independent stochastic gradient approximations may occasionally facilitate rapid initial progress, the method is highly prone to stagnation or convergence to suboptimal local minima. By contrast, the proposed coordinate descent framework offers a substantially more stable and reliable optimisation trajectory.

Because COBYLA and SPSA proved to be the most competitive baselines at the initial threshold, they are analysed across a spectrum of increasingly stringent target ratios in Figs. 3 and 4, motivating a detailed comparison under requirements for higher solution quality. The evaluation against COBYLA<tbc>

\begin{tabular}{cccccc}
Set & |_V_| & Edge probability & Set & |_V_| & Edge probability \\
1 & 9 & 0.6 & 6 & 12 & 0.1 \\
2 & 10 & 0.6 & 7 & 12 & 0.1 \\
3 & 11 & 0.6 & 8 & 14 & 0.45 \\
4 & 12 & 0.6 & 9 & 16 & 0.35 \\
5 & 12 & 0.2 & 10 & 18 & 0.30 \\
\end{tabular}

\begin{tabular}{ccccc}
Baseline & Proposed Only & Baseline Only & Both & Neither \\
Adam & 19 & 17 & 696 & 18 \\
COBYLA & 11 & 18 & 704 & 17 \\
GD & 74 & 7 & 641 & 28 \\
L-BFGS-B & 77 & 9 & 638 & 26 \\
NM & 317 & 5 & 398 & 30 \\
Powell & 183 & 0 & 532 & 35 \\
SPSA & 123 & 7 & 592 & 28 \\
\end{tabular}

1: Graph families used in the numerical experiments.

2: Number of cases where the proposed method and each of baseline optimisation algorithms cross a target approximation ratio of 0.94, out of 750 total cases.

