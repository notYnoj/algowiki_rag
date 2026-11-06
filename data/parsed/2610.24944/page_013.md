work. Épi-turbo stops the campaign when more sessions do not improve the best verified score. Thus the agent does not use more budget on a task where it finds no improvement.

**Budget control.** Épi-turbo reserves the maximum cost of a model call before the call starts. It also keeps a small part of the budget for the end of the campaign. Thus the cost of a campaign is never more than its budget, and the final steps always have funds. The reservation uses the price limits of the model, so the agent can use almost all of its budget.

**Optional components.** Independent review and extra validation are optional in Épi-turbo. On short tasks, their cost was larger than their benefit in our tests. Both components were off in the runs below.

## 6.2 Benchmark and Protocol

We use FrontierOR, a benchmark of 180 operations-research tasks from the literature (Kong et al., 2026). Each task asks for a standalone program that solves new instances of one problem class. The program must not call an external optimization solver. The baseline is x (OpenAI, 2026), a widely used coding agent, with GPT-6-Astra as its model. Épi-turbo uses the same model with the same reasoning effort.

We selected 30 tasks that were new to both systems. We took them in the official hardness order of the benchmark and excluded tasks with unreliable reference values. Of these tasks, 13 are in the hard split, and 17 have hardness ranks 51 to 70. For each task, each system had a model budget of $20. We did one run for each task and system, so we do not report statistical significance.

The evaluator first runs each program on two development instances. The agent sees these results during the campaign. After the campaign, the best development program runs once on four held-out instances. Each held-out run has a time limit of one hour. The benchmark score has a quality term and a speed term.

The quality term decreases as the gap to the reference value increases. The speed term compares the runtime of the program with the runtime of the reference solver. It counts only when the solution is within 1% of the reference value. Outside this 1% band, the score is the quality term alone. The reference values come from a commercial solver, and some of them are weak. Thus we also compare the two systems on each instance directly, with their objective values only.

## 6.3 Results

3 gives the main results. Épi-turbo gets the higher total score, 53.96 against 51.21. It has the higher score on 18 tasks, and x has the higher score on 12. On 10 of these tasks, the difference is less than 0.01. Épi-turbo uses 64% of the model cost of x. Its median research time per task is approximately 22 minutes, and the median for x is 37 minutes.

Figure 7 shows the results for each task. The gains of Épi-turbo are larger than its losses. On the 18 tasks where Épi-turbo is higher, the total gain is 4.54. On the other 12 tasks, the total loss is 1.79. Épi-turbo also costs less on 27 of the 30 tasks.

4 splits the tasks into two groups. On the 13 tasks of the hard split, Épi-turbo has the higher score on 9 tasks, and its total score is 10% higher. On the 17 tasks with ranks 51 to 70, the two systems are close. On 15 of the 30 tasks, Épi-turbo has both the higher score and the lower model cost.

The higher score comes mainly from the speed term. The programs of Épi-turbo usually stop when their search finds no better solution. On the held-out instances, the median runtime of an Épi-turbo program is 2.9 seconds, and the median for x is 9.3 seconds. No held-out run of Épi-turbo used more than 30 minutes. x used more than 30 minutes on 17 of the 120 held-out runs, in 7 tasks. A long run can improve the solution, but it decreases the speed term.

## 6.4 Selected Cases

5 lists the ten algorithmic coding tasks with the largest score difference in favor of Épi-turbo. The tasks span vehicle routing, cooperative crane scheduling, production planning, facility location, clustering



