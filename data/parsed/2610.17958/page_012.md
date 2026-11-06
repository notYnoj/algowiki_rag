varying ed(_G_) and fixing the remaining parameters, the running time grows linearly with input size as ed(_G_) grows. Moreover, the peak RAM usage for each thread remains constant in this regime, which is particularly appealing for sparse graphs.

**5.9 Results for RQ5.** We fixed |_V_|=200, ed(_G_)=5%, \(\ell=8\), _d_=2, and varied the number _t_ of threads from 1 to _P_=128, the number available in our system, in order to assess the effectiveness of our parallelization. Figure 5.9 shows near-linear speed-up up to 32 threads (28.3\(\times\)), after which returns diminish: the speed-up peaks at 36.7\(\times\) with 64 threads and does not improve further. We conjecture that these diminishing returns are due to load imbalance: some wildcard combinations are more costly than others, and at 128 threads, an expensive combination dominates the wall- clock time. Moreover, since the algorithm parallelizes over \(\genfrac(){pt}{2}{\ell}{d}\big(\genfrac(){pt}{2}{\ell}{d}+1\big)/2\) wildcard combinations, at most that many threads can be productively used; since we test at most 128, this limit is never reached. Finally, the space complexity becomes O(_tN_) because each thread requires O(_N_) working space, and we have _t_ parallel threads.

**Reproducibility and source code.** The source code and datasets utilized in this study are currently available via https://github.com/lucper/cmm. All experimental results presented in this paper are fully reproducible using these provided resources.

**AI use disclosure.** All theoretical concepts and core proofs originated entirely from the authors’ own work. The authors employed AI tools to polish language and style, support verification of proofs, produce LaTeX code for Figure 1.1, Figure A.1, and Figure A.2, and produce code for plotting data. Every AI-generated output was carefully reviewed, verified, and revised by the authors, who assume full responsibility for the paper’s content.

**Acknowledgments.** Lucas P. Oliveira is funded by grant #2025/08034-9, São Paulo Research Foundation (FAPESP).

(t = 8, d=0)
(t = 8, d=1)
(t = 8, d=2)
(t = 8, d=3)
21
800
20
600
19
Time (s)
400
Peak RAM (MB)
18
17
200
16
0
5
10
15
20
25
30
5
10
15
20
25
30
Edge density (%)
Edge density (%)
(t = 8, d=4)
(t = 8, d=5)
(t = 8, d=6)
(t = 8, d=7)
1000
63,603
15.6
63,603
15.4
800
63,604
15.2
600
63,604
Peak RAM (MB)
Time (s)
400
63,604
15.0
63,604
200
14.8
20
20
20
20
14.6
0
5
10
15
20
25
30
5
10
15
20
25
30
Edge density (%)
Edge density (%)

(t = 5, d=0)
(t = 5, d=1)
21
20
20
15
19
Time (s)
18
10
Peak RAM (MB)
17
16
5
15
5
10
15
20
25
30
5
10
15
20
25
30
Edge density (%)
Edge density (%)
(t = 5, d=2)
(t = 5, d=3)
(t = 5, d=4)
7,840
15.00
7
7,840
14.95
6
7,840
5
7,840
14.90
Time (s)
4
7,840
7,848
Peak RAM (MB)
14.85
3
14.80
2
14.75
1
20
20
20
20
20
20
14.70
0
5
10
15
20
25
30
5
10
15
20
25
30
Edge density (%)
Edge density (%)

1.8x
103
2.8x
103
1.9x
Peak RAM (MB)
Time (s)
7.6x
102
19.1x
102
36.7x
31.5x
36.7x
1
2
4
8
16
32
64
128
1
2
4
8
16
32
64
128
Number of threads
Number of threads

Figure 5.7: Wall-clock time and peak RAM usage per thread of exact algorithm for |_V_|=200, \(\ell=8\), \(d\in[0,7]\), and varying ed(_G_). Top: \(d\in[0,3]\). Bottom: \(d\in[4,7]\) and lines for _d_=4 and _d_=7 labeled with _M<sub>V</sub>_.

Figure 5.8: Wall-clock time and peak RAM usage per thread of exact algorithm for |_V_|=200, \(\ell=5\), \(d\in[0,4]\), and varying ed(_G_). Top: \(d\in[0,1]\) and line for \((\ell=5,d=1)\) labeled with _M<sub>V</sub>_. Bottom: \(d\in[2,4]\), and lines for _d_=2 and _d_=4 labeled with _M<sub>V</sub>_.

Figure 5.9: Wall-clock time and total peak RAM usage of exact algorithm for |_V_|=200, ed(_G_)=5%, \(\ell=8\), and _d_=2 with varying number _t_ of threads. We use log-log axes and label the line with the speed-up obtained with the number of threads specified on the _x_-axis.

