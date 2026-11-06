<tbc>reveals a clear dependency on the required approximation ratio. As depicted in Fig. 3a, the comparative advantage is mixed at lower targets, with mean savings of -26.6% at \(\alpha_\text{target}=0.94\), indicating COBYLA often requires fewer evaluations to satisfy relaxed criteria. However, the proposed method demonstrates superior asymptotic scaling as \(\alpha_\text{target}\) approaches 1, crossing into positive efficacy at \(\alpha_\text{target}=0.97\) and achieving an overall mean saving of 19.2% at \(\alpha_\text{target}=0.99\). The heatmap in Fig. 3b corroborates this transition, showing broad positive savings across the majority of graph topologies at the highest fidelity requirements.

Conversely, the detailed breakdown in Fig. 4 illustrates that SPSA remains a formidable competitor solely in terms of conditional evaluation speed. The cost-saving distributions in Fig. 4a reveal a consistently wide variance, with conditional mean savings gradually shifting from -35.9% at \(\alpha_\text{target}=0.94\) to a nearly neutral -1.6% at \(\alpha_\text{target}=0.99\). The heatmap Fig. 4b underscores SPSA’s rapid convergence capabilities when successful, showcasing substantial negative savings across multiple configurations. Nevertheless, as established by the crossing counts in  2, this conditional efficiency is achieved at the unacceptable cost of frequent optimisation failures, reaffirming the proposed coordinate descent method as a more robust and scalable solution for high-fidelity maQAOA training.

## 5 Conclusion

This paper investigated cyclic coordinate descent for training maQAOA on the maximum independent set problem, a widely studied benchmark in constrained combinatorial optimisation. By exploiting the single frequency dependence of the maQAOA objective on each individual angle, the proposed<tbc>

Adam
GD
L-BFGS-B
NM
Powell
60
70
80
90
100
Training-cost saving (%)
(a)
100
Adam
90.9
91.5
92.0
91.9
93.0
92.9
91.2
93.4
92.2
92.1
95
Training-cost saving (%)
GD
94.9
96.0
96.4
96.2
96.4
96.1
96.1
96.8
97.0
95.4
90
L-BFGS-B
86.4
85.7
86.5
86.0
89.2
89.8
89.7
90.4
90.0
87.0
85
NM
76.9
75.7
79.8
80.6
86.5
86.8
82.7
83.6
85.0
84.0
80
75
Powell
77.0
76.3
77.6
78.8
76.7
75.8
75.3
78.2
78.5
77.7
70
1
2
3
4
5
6
7
8
9
10
Graph set number
(b)

Figure 2: Percentage savings in training cost achieved by the proposed method relative to baseline optimisation algorithms (Adam, GD, L-BFGS-B, NM, Powell) for crossing a target approximation ratio of 0.94. The results are presented as (a) box-and-whisker plots representing the distribution of savings across individual evaluation cases, where diamond markers indicate the overall mean savings (GD: 96.2%, Adam: 92.0%, L-BFGS-B: 88.3%, NM: 80.2%, Powell: 77.0%), and (b) a heatmap detailing the average savings per graph set.

