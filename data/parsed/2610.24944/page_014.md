and graph optimization. Each row evaluates a generated program on unseen instances of its problem class. This breadth makes the connection to the mathematical campaigns explicit: Épi’s research process supports both constructing mathematical artifacts and developing algorithms with measurable gains in practical optimization settings. The four cases below show how solution quality and execution speed contribute to these gains.

\begin{tabular}{ccc}
**Measure** & **Épi-turbo** & **x**\\
Total benchmark score & 53.96 & 51.21\\
Tasks with the higher score & 18 & 12\\
Mean quality term & 1.030 & 1.032\\
Mean speed term & 0.784 & 0.675\\
Instances with the better solution (119 comparable, 40 ties) & 18 & 61\\
Instances more than 1% worse than the other system & 29 & 10\\
Infeasible solutions (120 held-out runs) & 1 & 0\\
Model cost per task, mean & $7.30 & $11.35\\
Research time per task, median & 22 min & 37 min\\
\end{tabular}

\begin{tabular}{ccccc}
**Group** & **Tasks** & **Total score** & **Higher score** & **Model cost**\\
Hard split & 13 & 22.33 / 20.30 & 9 / 4 & $95 / $152\\
Ranks 51–70 & 17 & 31.64 / 30.91 & 9 / 8 & $124 / $188\\
All tasks & 30 & 53.96 / 51.21 & 18 / 12 & $219 / $341\\
\end{tabular}



A Larger wins than losses
B Lower model cost
C Faster programs
+5.4% total score
64% of the cost
2.9 s median runtime
Score difference per task, Épi-turbo minus x
Model cost per task (US dollars)
Runtime of the 120 held-out runs (log scale)
Épi-turbo higher on 18 tasks: +4.54
20
Epi-turbo cheaper
median 2.9 s
on 27 of 30 tasks (below the line)
0.75
Epi-turbo
15
0.50
Epi-turbo
over 30 min
0.25
10
Epi-turbo
equal cost
median 9.3 s
0.00
x
0.25
x higher on 12 tasks: -1.78
5
0
30 tasks, sorted by difference
0
5
10
15
20
1 s
10 s
100 s
1000 s
x
Runtime per held-out instance

** 3:** Épi-turbo and x on 30 FrontierOR tasks that were new to both systems. Both systems use GPT-6-Astra and a model budget of $20 per task. All scores are for the held-out instances. The instance counts compare the objective values of the two programs directly.

**Figure 7:** Épi-turbo and x on 30 FrontierOR tasks. A: The score difference for each task, in order of size. Épi-turbo has the higher score on 18 tasks, and its gains are larger than its losses. B: The model cost for each task. Each point below the dashed line is a task where Épi-turbo costs less. C: The runtime of each held-out run on a logarithmic scale, with the medians as vertical bars.

** 4:** Results by task group. The hard split is the official set of the 50 hardest FrontierOR tasks. Each pair of values gives Épi-turbo first and x second.

