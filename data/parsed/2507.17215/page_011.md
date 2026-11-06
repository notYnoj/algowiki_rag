<tbc>than BT. Since rest of the queries build upon the data structures output by the algorithm for \(\exists\exists\forall\) query, they take a bit longer, but are reasonably fast i.e have comparable run time as BT. We note that the BT runtimes reported below account for the time it takes to enumerate the triangles. To obtain solutions to the above queries, one needs some indexing mechanism on top of the triangle enumeration subroutine. Therefore, BT will take at least the reported time to determine solutions to these queries.

## 5.1 Insights

To gain some insights into the trend of number of solutions w.r.t different parameter, we define our query as follows: \(\exists u\exists v\in N(u)\forall_\tau N(u)\cap N(v)\phi(u,v,w)\), where \(\phi\) represents the temporal triangle in Figure- 2a. We make similar modifications for \(\exists\forall_{\tau_1}\forall_{\tau_2}\) and \(\exists\forall_\tau\exists\) queries. The primary reason for this modification is to get enough solutions that will allow us to gain some insights. This also demonstrates that are techniques are simple, and versatile enough to accommodate various other sets. Further, we see that conclusions drawn from these plots are often consistent with the case in which the universe is just _N(v_). Note that there is no difference in the time it takes to compute the solutions to the queries when we change the universe from _N(v_) to \(N(u)\cap N(v)\). Doing so involves changing line-18 of algorithm-6 to \(\tau|N(v)\cap N(u)|\). Further, in certain applications, one may be interested in predicated where the universe is indeed \(N(v)\cap N(u)\). For instance, when trying to fetch cohesive groups of vertices, it may be more meaningful to have the intersection in the predicate.

**Number of solutions for a fixed** \(\delta\)**, varying threshold:** Figure- 5a shows the trend in the number of solutions to \(\exists\exists\forall_\tau\) query as we vary the value of threshold. We fix \(\delta\) to 1Hr. Observe that generally, as the threshold increases, the number of solutions tends to decrease. This is because any edge that satisfies the \(\exists\exists\forall_{\tau_1}\) , will also satisfy \(\exists\exists\forall_{\tau_2}\) for any \(\tau_2<\tau_1\). For instance, For instance, if a temporal edge _e_=(_u,v,t_) forms a \(\delta\)-temporal triangle with at least 50% of _u_ and _v_’s neighbors, it naturally satisfies the condition for 25% as well. Therefore, the number of solutions for threshold \(\tau_2\) is always at least as large as for any \(\tau_1\ge\tau_2\), explaining the observed decline in solutions with increasing thresholds.

Further, observe from Figure- 5a that for relatively higher threshold values (typically exceeding 75%), the number of solutions is almost constant. This implies that most solutions to \(\exists\exists\forall_{0.75}\) query will also satisfy \(\exists\exists\forall_{0.9}\) query.

Similar trends can be observed in Figure-5b, which depicts the variation in the number of solutions to \(\exists\forall_\tau\exists\) query across a multitude of thresholds, when \(\delta\) is set to 1Hr. Similar reasoning explains the decrease in the number of solutions as the value of the threshold increases. Further, beyond the 70% threshold, the number of solutions is almost constant. In fact, it is 0 in most cases, except for the "wiki-talk-temporal" dataset, where it is 9.

Figures-5c and 5d illustrate the trend in the number of solutions to the \(\exists\forall_{\tau_1}\forall_{\tau_2}\) query for different values of the thresholds. As before, we set \(\delta\) to 1Hr. In Figure-5c we fix \(\tau_2\) to 20%, and in Figure-5d, we set \(\tau_2\) to 25%. Note that for a fixed \(\tau_1\), the number of solutions to<tbc>

\begin{tabular}{ccccccccc}
**Dataset** & \(\tau_2\) & \(\tau_1\) & **Num. Solutions** & \(\tau_2\) & \(\tau_1\) & **Num. Solutions** & **Time 1(sec.)** & **Time 2(sec.)** \\
\multirow{3}{*}{CollegeMsg} & \multirow{3}{*}{25%} & 25% & 0 & \multirow{3}{*}{50%} & 25% & 0 & 0.08 & 0.07 \\
 & & 50% & 0 & & 50% & 0 & 0.08 & 0.07 \\
 & & 75% & 0 & & 75% & 0 & 0.08 & 0.07 \\
\multirow{3}{*}{email-Eu-core-temporal} & \multirow{3}{*}{25%} & 25% & 1 & \multirow{3}{*}{50%} & 25% & 0 & 1.2 & 0.8 \\
 & & 50% & 0 & & 50% & 0 & 1.2 & 0.8 \\
 & & 75% & 0 & & 75% & 0 & 1.2 & 0.8 \\
\multirow{3}{*}{sx-mathoverflow} & \multirow{3}{*}{25%} & 25% & 0 & \multirow{3}{*}{50%} & 25% & 0 & 4.5 & 3.1 \\
 & & 50% & 0 & & 50% & 0 & 4.4 & 3.1 \\
 & & 70% & 0 & & 75% & 0 & 4.5 & 3.1 \\
\multirow{3}{*}{sx-superuser} & \multirow{3}{*}{25%} & 25% & 4 & \multirow{3}{*}{50%} & 25% & 1 & 8.6 & 7.5 \\
 & & 50% & 2 & & 50% & 1 & 8.8 & 7.6 \\
 & & 75% & 0 & & 75% & 0 & 8.6 & 7.5 \\
\multirow{3}{*}{sx-askubuntu} & \multirow{3}{*}{25%} & 25% & 7 & \multirow{3}{*}{50%} & 25% & 2 & 4.1 & 3.9 \\
 & & 50% & 3 & & 50% & 1 & 4.2 & 3.9 \\
 & & 75% & 0 & & 75% & 0 & 4.1 & 3.9 \\
\multirow{3}{*}{wiki-talk-temporal} & \multirow{3}{*}{20%} & 25% & 60 & \multirow{3}{*}{50%} & 25% & 12 & 62.3 & 52.8 \\
 & & 50% & 9 & & 50% & 4 & 64.2 & 53.5 \\
 & & 75% & 0 & & 75% & 0 & 62.5 & 52.7 \\
\multirow{3}{*}{sx-stackoverflow} & \multirow{3}{*}{25%} & 25% & 3737 & \multirow{3}{*}{50%} & 25% & 3 & 1195.35 & 936.01 \\
 & & 50% & 1 & & 50% & 1 & 1191.53 & 931.2 \\
 & & 75% & 0 & & 75% & 0 & 1151.43 & 948.3 \\
\end{tabular}

CM
4000
ET
MO
SU
3000
AU
Num. EEA Solutions
WT
2000
1000
0
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Thresholds

CM
1000
ET
MO
SU
800
AU
600
WT
Num. EAE solutions
400
200
0
0.2
0.4
0.6
0.8
1.0
Thresholds

1000
CM
ET
MO
SU
800
AU
600
WT
Num. of EEA solutions
400
200
0
0.2
0.4
0.6
0.8
1.0
Thresholds

1000
CM
ET
MO
SU
800
AU
600
WT
Num. of EEA solutions
400
200
0
0.2
0.4
0.6
0.8
1.0
Thresholds

** 4: Time to obtain solutions for** \(\exists\forall_{\tau_1}\forall_{\tau_2}\) **query, across different choices of threshold, when** \(\delta=4\)**W.**

**(a)** \(\exists\exists\forall\), \(\delta=1\)**Hr.**

**(b)** \(\exists\forall\exists\), \(\delta=1\)**Hr.**

**(c)** \(\exists\forall\forall\), \(\delta=1\)**Hr,** \(\tau_2=20\)**%.**

**(d)** \(\exists\forall\forall\), \(\delta=1\)**Hr,** \(\tau_2=25\)**%.**

**Figure 5: Number of solutions to different queries for a fixed delta, and varying thresholds**

