<tbc>the \(\exists\forall_{\tau_1}\forall_{0.2}\) query is at least the the number of solutions to the \(\exists\forall_{\tau_1}\forall_{0.25}\) query.

Also note that generally, the number of solutions to \(\exists\forall_\tau\exists\) query exceeds the number of solutions to \(\exists\forall_\tau\forall_\tau^\prime\) query. This is because every solution to \(\exists\forall_\tau\forall_{\tau^\prime}\) query naturally satisfies \(\exists\forall_\tau\exists\) query.

We note that similar observations can be extrapolated for the situations in which the universe is _N(v_) rather than the intersection of neighborhoods.

**Number of solutions for a fixed threshold, varying delta:** Figures-6a and 7a demonstrate the trend in the number of solutions to \(\exists\exists\forall_\tau\) query as we vary the value of \(\delta\). In Figure-6a, we set the<tbc>

<tbc>threshold to 25% and in Figure-7a, threshold is set to 50%. Observe that the number of solutions to the query decreases as we increase \(\delta\). This is because, every temporal edge _e_=(_u,v,t_) that satisfies the \(\exists\exists\forall_\tau\) query for a given \(\delta\) will naturally satisfy the \(\exists\exists\forall_\tau\) for any \(\delta^{^\prime}\ge\delta\). This explains the increase in the number of solutions with increasing \(\delta\).

Similar trends can be observed in the solutions to \(\exists\forall_\tau\exists\) query (Refer figures-6b and 7b). In figures 6b and 7b, we fix the thresholds to 10% and 30% respectively. As in the previous case, the number of solutions increases with increasing \(\delta\) values.

Figures-6c, 7c, 6d and 7d demonstrate the variation in the number of solutions to the \(\exists\forall\forall\) query as \(\delta\) changes from 10mins. to 1Hr. In figures-6c and 6d, we fix the value of \(\tau_2\) to 20% and plot the trend in the number of solutions for \(\tau_1=10\%\) and \(\tau_2=30\%\). In Figures-7c and 7d, the value of \(\tau_2\) is set to 25% and we plot the number of solutions when \(\tau_1=10\%\) and \(\tau_2=30\%\).

**Discovering structure using FOL queries:** In the introduction, we saw how \(\exists\exists\forall\) queries can be used to discover cohesive edges in a citation network. These queries automatically find edges that support a large number of triangles, and we discover that the corresponding papers are in the same topic.

## 6 Conclusion

In this work, we initiate the study of thresholded triadic first-order logic queries in temporal networks. We present a practical algorithm with provable guarantees to find solutions to these queries. Note that our algorithm can be extended for other temporal triangles as well. In future, we would like to investigate if the techniques presented in this work can be generalised to other motifs and first- order logic quantifiers.

## References

CM
CM
4000
ET
1000
ET
MO
MO
SU
SU
800
SU
3000
AU
AU
AU
3000
WT
WT
600
Num. EEA Solutions
Num. EAE Solutions
2000
400
1000
200
0
0
10
20
30
40
50
60
10
20
30
40
50
60
Delta(mins.)
Delta(mins.)
Delta(mins.)
(a) 3EV, T=25%.
(b) 3EV3, T=10%.
1000
CM
CM
400
ET
ET
350
ET
MO
MO
800
SU
300
SU
Num. of EEA solutions
Num. of EEA solutions
250
AU
AU
600
WT
WT
200
WT
400
150
100
200
Num. of EEA solutions
50
0
0
10
20
30
40
50
60
10
20
30
40
50
60
Delta(mins.)
Delta(mins.)
(c) 3EVV, T1=10%, T2 = 20%.
(d) 3EVV, T1=30%, T2 = 20%.

CM
CM
2500
ET
400
ET
2000
MO
MO
SU
SU
300
AU
AU
1500
WT
WT
Num. EEA Solutions
Num. EEA Solutions
200
1000
100
500
0
0
10
20
30
40
50
60
10
20
30
40
50
60
Delta(mins.)
Delta(mins.)
(a) 3EV, T=50%.
(b) 3EV3, T=30%.
1000
CM
CM
400
ET
ET
350
ET
MO
MO
800
SU
300
SU
Num. of EEA solutions
Num. of EEA solutions
250
AU
AU
600
WT
200
WT
400
150
100
50
0
0
10
20
30
40
50
60
10
20
30
40
50
60
Delta(mins.)
Delta(mins.)
(c) 3EVV, T1=10%, T2 = 25%.
(d) 3EVV, T1=30%, T2 = 25%.

**Figure 6: Number of solutions to different queries for a varying delta, and fixed thresholds**

**Figure 7: Number of solutions to different queries for a varying delta, and fixed thresholds**

