MPC-based ANN protocol. This is precisely the problem we address. Adapting Pacmann to our setting would be essentially equivalent to implementing our MPC algorithm. For this reason, we do not include it as an experimental baseline. For 3PC, we use replicated radix sort \[1\] as the exact top-_k_ baseline with Recall@_k_=1.

## 7.2 Search Accuracy and RAG Quality

**Search Recall and Distribution.** At the deployed setting (_M_=128, \(ef^{(0)}=k+10\), with \(\overline{\Delta^{(\ell)}}\) from Section 4.1), HNSecW delivers recall \(\ge 0.9\) for at least 95% of queries on every dataset and _k_, with the 95th-percentile climbing from ∼0.9 at _k_=10 to ∼0.95 at _k_=100, as shown in Figure 6. PANTHER, by contrast, holds Recall\(@k\ge 0.8\) for 95% of queries but its 95th-percentile peaks early near _k_=20 and drifts back toward 0.80 at _k_=100: its fixed cluster-probe budget cannot absorb the larger candidate set demanded by larger _k_,<tbc>

<tbc>while HNSecW’s fixed-step rule _ef_<sup>(0)</sup>=_k_+10 scales with _k_ and pushes the worst-case recall up. HNSecW also visits 8\(\times\) to 44\(\times\) fewer database vectors than PANTHER as _N_ grows from 10<sup>6</sup> to 10<sup>8</sup> (the range where PANTHER runs), reflecting the log _N_ vs. \(\sqrt{N}\) scaling of graph-based vs. cluster-based ANN search. Figure 7 shows the per-query distribution at the deployed setting: \(\ge 95\%\) of HNSecW’s queries land at Recall\(@10\ge 0.9\) on every dataset, with 45-60% reaching perfect recall, while PANTHER concentrates \(\ge 95\%\) of mass at \(\ge 0.8\) but only 30-38% at perfect recall. To verify the robustness of the prescribed step parameter, we ablate _ef_<sup>(0)</sup> for HNSecW in Figure 8. Recall on every dataset saturates near the deployed _ef_<sup>(0)</sup>=_k_+10 from Section 4.1: shrinking the offset to _k_+1 drops recall sharply, while doubling it to _k_+20 or _k_+50 buys little extra recall at materially higher WAN latency. PANTHER’s recall also rises<tbc>

SIFT-1M
DEEP-100M
HNSecW
GIST-1M
BIGANN-1B
PANTHER
1.00
0.95
100
95th-percentile Recall@k
0.90
Top-10 visits / N (%)
10-1
0.85
10-2
0.80
10-3
0.75
10-4
0.70
10
20
50
100
10-4
SIFT- 1M
GIST- 1M
DEEP- 100M
BIGANN- 1B
Top-k

HNSecW
PANTHER
1.0
55%
35%
45%
30%
60%
38%
50%
N/A
0.9
41%
40%
50%
42%
36%
40%
45%
3%
20%
4%
23%
3%
18%
4%
Recall@10
0.7
<1%
4%
<1%
4%
<1%
3%
<1%
<1%
<1%
0.5
Avg. 95% Avg. 90% Avg. 94% Avg. 90% Avg. 96% Avg. 91% Avg. 94%
min 0.7
min 0.6
min 0.7
min 0.6
min 0.7
min 0.7
min 0.6
min 0.7
SIFT-1M
GIST-1M
DEEP-100M
BIGANN-1B

