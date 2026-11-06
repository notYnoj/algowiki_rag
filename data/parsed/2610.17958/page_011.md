<tbc>D. melanogaster datasets.

Together, these results establish that our exact algorithm mines a substantial amount of \((\ell,d)\)-motif pairs that are missed by SEQ-SLIDER and M-SLIDER for the _largest_ datasets from the STRING database (A. thaliana and H. sapiens I) and from \[1\] (H. sapiens II).

**5.7 Results for RQ3.** We fixed the edge density ed(_G_) for all instances to 5%, and varied |_V_| and _N_. We used \(t:=min\{\left(\begin{array}{ c }
\ell \\
d
\end{array}\right)\left(\begin{array}{ c }
\ell \\
d
\end{array}\right)+1\right)/2,P\}\) threads, where by _P_=128 we denote the number of threads available in our system. For \(\ell=8\), we varied _d_ from 0 to 7; the results are shown in Figure 5.5. We also performed this experiment for \(\ell=5\) with _d_ varying from 0 to 4. The results are shown in Figure 5.6; they yield the same conclusion, but with smaller running times and peak RAM usage. We observe a _quadratic_ behavior in _N_ for the running times shown in Figure 5.5 (turned into straight lines with log-log axes for readability), for fixed values of \(\ell\) and _d_. The running times further highlight their dependence on the maximum number _M<sub>V</sub>_ of distinct \((\ell,d)\)-motifs in _V_ across all \(\left(\begin{array}{ c }
\ell \\
d
\end{array}\right)\) combinations of wildcard positions. For fixed \(\ell\) and _N_, observe that _M<sub>V</sub>_ decreases as _d_ grows, since more wildcard positions yield fewer distinct \((\ell,d)\)- motifs in _V_ . Indeed, in practice, _M<sub>V</sub>_ is significantly smaller than _N_ for larger _d_. (We label exemplary lines<tbc>

<tbc>in Figure 5.5 with _M<sub>V</sub>_.) This reflects in faster running times for _a fixed_ wildcard combination. However, when considering all wildcard combinations, the running times are non-decreasing for \(d\in[0,\lfloor\ell/2\rfloor)\) and non-increasing for \(d\in[\lfloor\ell/2\rfloor,\ell)\) because the term \(\left(\begin{array}{ c }
\ell \\
d
\end{array}\right)\) behaves the same way on these intervals. The peak RAM usage shown in Figure 5.5 also confirms the _linear_ behavior in _N per thread_.

We also report the running time and peak RAM usage per thread of our exact algorithm on the datasets of  5.1; see  C.3 in the appendix. We remark that for the dataset with the largest _N_, H. sapiens I, the exact algorithm took roughly 50h with peak RAM 1.29GB per thread for parameter pair \((\ell=8,d=3)\) and only 2h with peak RAM 1.28GB per thread for parameter pair \((\ell=8,d=5)\). We used _t_:=_P_=128 threads for both.

**5.8 Results for RQ4.** We fixed |_V_|=200 and varied the edge density ed(_G_). The rest of the setup is analogous to RQ3: for \(\ell=8\), we varied _d_ from 0 to 7 (Figure 5.7); for \(\ell=5\), we varied _d_ from 0 to 4 (Figure 5.8); and we used \(t:=min\{\left(\begin{array}{ c }
\ell \\
d
\end{array}\right)\left(\left(\begin{array}{ c }
\ell \\
d
\end{array}\right)+1\right)/2,P\}\) threads. Here, our theoretical prediction for the time bound is \(\mathcal{O}(\left(\begin{array}{ c }
\ell \\
d
\end{array}\right)^2|E|max_{v\in V}|v|^2)\), which is confirmed by the running times shown in Figure 5.7. Indeed, by<tbc>

(t=8, d=0)
(t=8, d=1)
(t=8, d=2)
(t=8, d=3)
N
N
55030
112173
230280
465884
933007
1876478
55030
112173
230280
465884
933007
1876478
105
104
103
102
Time (s)
Peak RAM (MB)
101
100
101
100
200
400
800
1600
3200
100
200
400
800
1600
3200
|V]
|V]
(t=8, d=4)
(t=8, d=5)
(t=8, d=6)
(t=8, d=7)
N
N
55030
112173
230280
465884
933007
1876478
55030
112173
230280
465884
933007
1876478
104
141, 179
120, 884
103
93, 377
102
Time (s)
102
38, 995
20
20
101
20
20
100
10
10
100
200
400
800
1600
3200
100
200
400
800
1600
3200
|V]
|V]

(t=5, d=0)
(t=5, d=1)
N
N
55030
112173
230280
465884
933007
1876478
55030
112173
230280
465884
933007
1876478
103
102
Time (s)
Peak RAM (MB)
101
100
100
200
400
800
1600
3200
100
200
400
800
1600
3200
|V]
|V]
(t=5, d=2)
(t=5, d=3)
(t=5, d=4)
N
N
55030
112173
230280
465884
933007
1876478
55030
112173
230280
465884
933007
1876478
8, 813
102
8, 813
102
8, 803
Time (s)
7, 848
20
101
7, 386
20
20
100
100
20
10
100
200
400
800
1600
3200
100
200
400
800
1600
3200
|V]
|V]

Figure 5.5: Wall-clock time and peak RAM usage per thread of exact algorithm for \(\ell=8\), \(d\in[0,7]\), ed(_G_)=5%, and varying |_V_| (and _N_). We use log-log axes with the dashed lines indicating a polynomial of degree 2 (resp. degree 1) fitting the data for time (resp. peak RAM). Top: \(d\in[0,3]\) with dashed line on _d_=2. Bottom: \(d\in[4,7]\) with dashed line on _d_=5, and lines for _d_=4 and _d_=7 labeled with _M<sub>V</sub>_.

Figure 5.6: Wall-clock time and peak RAM usage per thread of exact algorithm for \(\ell=5\), \(d\in[0,4]\), ed(_G_)=5%, and varying |_V_| (and _N_). We use log-log axes with the dashed lines indicating a polynomial of degree 2 (resp. degree 1) fitting the data for time (resp. peak RAM). Top: \(d\in[0,1]\) with dashed line on _d_=1. Bottom: \(d\in[2,4]\) with dashed line on _d_=3, and lines for _d_=2 and _d_=4 labeled with _M<sub>V</sub>_.

