**Clique interdiction: better solutions and faster programs (furini2021).** The Épi-turbo program solves each held-out instance in less than 17 seconds. On one instance, its solution has an objective value of 8, and the x solution has 20. The x program also runs for 20 to 60 minutes on three of the four instances. Thus Épi-turbo has both the higher quality term and the higher speed term.

**Production planning: reaching the 1% band (delage2022).** Épi-turbo has the better solution on three instances and the same solution on the fourth. On one instance, the x solution is 1.19% above the reference value, and the Épi-turbo solution is 0.89% above it. Thus only Épi-turbo gets the speed term on that instance. The Épi-turbo programs are also 2 to 7 times faster.

**Maximum clique: matching the reference (furini2019).** Épi-turbo matches the reference value on all four instances. The x solution is 5% worse on one instance. On another instance, the x program needs 34 seconds, which is more time than the reference solver needs. Thus x loses the speed term on that instance, and Épi-turbo keeps it.

**Vehicle routing: faster execution (he2020).** Both systems beat the reference values by 5% to 17%. The x solutions are slightly better on three instances, by at most 2.6%. But the x program uses the full hour on three instances, and the Épi-turbo program needs at most 36 seconds. Here the speed term decides the result.

## 7 Related work

Autonomous research systems differ in how they organize the search for a useful next experiment. The AI Scientist-v2 explores experimental directions through agentic tree search (Yamada et al., 2025). Co-Scientist

\begin{tabular}{ccccc}
**Task** & **Score** & **Quality term** & **Speed term** & **Model cost**\\
Hyperplane clustering amaldi2013 & 2.162 / 1.283 & 1.163 / 1.282 & 0.999 / 0.001 & $2.59 / $4.86\\
Clique interdiction furini2021 & 2.090 / 1.256 & 1.091 / 0.841 & 0.999 / 0.415 & $3.82 / $6.47\\
Vehicle routing with node costs he2020 & 2.094 / 1.353 & 1.098 / 1.108 & 0.995 / 0.245 & $3.42 / $13.90\\
Maximum clique furini2019 & 1.987 / 1.487 & 1.000 / 0.988 & 0.987 / 0.500 & $5.78 / $11.58\\
Cooperative crane scheduling kress2019 & 1.853 / 1.572 & 1.103 / 1.074 & 0.750 / 0.498 & $4.78 / $3.90\\
Process configuration and production planning delage2022 & 2.023 / 1.759 & 1.024 / 1.012 & 0.999 / 0.747 & $7.32 / $13.04\\
Routing with time-window assignment spliet2015 & 2.012 / 1.765 & 1.012 / 1.016 & 1.000 / 0.750 & $7.48 / $11.50\\
Graph coloring gualandi2012 & 2.086 / 1.860 & 1.117 / 1.128 & 0.969 / 0.731 & $4.77 / $11.52\\
Set partitioning zhang2025 & 1.558 / 1.379 & 1.021 / 0.951 & 0.536 / 0.428 & $18.38 / $16.87\\
Facility location fischetti2017 & 1.998 / 1.847 & 1.000 / 1.000 & 0.998 / 0.847 & $2.41 / $1.96\\
\end{tabular}



** 5:** The ten FrontierOR coding tasks with the largest score difference in favor of Épi-turbo, sorted by the difference. Task names identify the optimization problem solved by each generated program; benchmark IDs appear below them. Scores, quality and speed are measured on held-out instances. Each pair gives Épi-turbo first and x second.

