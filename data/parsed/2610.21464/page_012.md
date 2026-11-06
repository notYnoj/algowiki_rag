<tbc>ument enters the retrieval results, reducing top-_k_ does not weaken its generation-side influence.

**Impact of the reward function.** To evaluate the effectiveness of document-level joint scoring, we remove the joint reward while keeping all other settings unchanged. As shown in  4, removing the reward reduces RSR by 7.26-13.70 percentage points across poisoning budgets and knowledge-base sizes, with larger drops as the knowledge base grows. Although Cond.ASR increases in some settings, the reduced retrieval coverage lowers overall ASR in five of the six configurations. These results show that the joint reward balances retrieval and generation utility, improving the end-to-end effectiveness of selected poisoned documents.

**Impact of entity-claim coupling.** To evaluate entity- claim coupling, we remove the constraint that the target entity must serve as the grammatical subject or causal agent in factual statements while keeping all other settings unchanged. As shown in  4, removing the coupling increases average RSR by 11.38 percentage points, but decreases Cond.ASR and ASR by 12.90 and 6.88 percentage points, respectively, with both metrics declining across all six settings. These results show that entity-claim coupling trades some retrieval coverage for substantially stronger generation-side effectiveness, making the model more likely to retain the target entity and promote it through the target<tbc>

<tbc>claim once poisoned documents enter the context.

**Impact of greedy selection.** To evaluate greedy complementary selection, we compare Global Greedy with directly selecting the highest-scoring candidates (Score Top). As shown in  4, on the 2M knowledge base with _m_=40, Global Greedy improves RSR from 67.60% to 70.90% and ASR from 23.05% to 26.94%. With _m_=60, ASR increases from 26.53% to 29.48%. These results show that greedy complementary selection reduces coverage redundancy and improves set-level coverage complementarity, enhancing attack performance.

**Impact of HNSW parameters.** To evaluate the effects of the HNSW graph parameter _M_<sub>HNSW</sub> and search parameter ef<sub>search</sub>, we conduct sensitivity experiments across knowledge-base sizes and poisoned-document budgets, as shown in Figure 9. As ef<sub>search</sub> increases, RSR improves steadily and begins to saturate beyond ef<sub>search</sub>=128. For example, on the 2M knowledge base with _m_=60 and _M_<sub>HNSW</sub>=16, RSR increases from 68.5% at ef<sub>search</sub>=16 to 73.8% at ef<sub>search</sub>=128, and reaches only 74.1% when ef<sub>search</sub> is increased to 256. Overall, retrieval performance improves with increasing search budgets and gradually saturates, while variations in _M_<sub>HNSW</sub> have a smaller effect.

\begin{tabular}{ccccccccccccccccccccc}
\multirow{3}{*}{Configuration} & \multicolumn{16}{c}{_Poisoned-document budget m_=40 (_m<sub>h</sub>_=2, _m_<sub>sat</sub>=38)} & \multicolumn{16}{c}{_Poisoned-document budget m_=60 (_m<sub>h</sub>_=4, _m_<sub>sat</sub>=56)} \\
 & \multicolumn{3}{c}{500K} & \multicolumn{3}{c}{1M} & \multicolumn{3}{c}{2M} & \multicolumn{3}{c}{500K} & \multicolumn{3}{c}{1M} & \multicolumn{3}{c}{2M} \\
 & \multicolumn{3}{c}{RSR Cond.ASR ASR} & \multicolumn{3}{c}{RSR Cond.ASR ASR} & \multicolumn{3}{c}{RSR Cond.ASR ASR} & \multicolumn{3}{c}{RSR Cond.ASR ASR} & \multicolumn{3}{c}{RSR Cond.ASR ASR} & \multicolumn{3}{c}{RSR Cond.ASR ASR} \\
\multicolumn{16}{c}{**_Retriever_**} \\
BGE-base-en & 88.71 & 46.53 & 41.28 & 78.11 & 42.04 & 32.84 & 72.49 & 40.68 & 29.49 & 89.55 & 47.69 & 42.71 & 79.44 & 43.31 & 34.41 & 74.00 & 42.28 & 31.29 \\
all-mpnet-base-v2 & 82.26 & 44.86 & 36.90 & 66.61 & 39.59 & 26.37 & 59.64 & 38.23 & 22.80 & 84.10 & 46.88 & 39.43 & 69.08 & 41.39 & 28.59 & 62.16 & 39.39 & 24.48 \\
GTE-base & 84.36 & 44.93 & 37.90 & 71.63 & 40.75 & 29.19 & 66.30 & 39.81 & 26.39 & 85.88 & 47.50 & 40.79 & 74.20 & 42.46 & 31.51 & 69.18 & 41.61 & 28.79 \\
\multicolumn{16}{c}{**_Top-k_**} \\
Top-5 & 88.71 & 46.53 & 41.28 & 78.11 & 42.04 & 32.84 & 72.49 & 40.68 & 29.49 & 89.55 & 47.69 & 42.71 & 79.44 & 43.31 & 34.41 & 74.00 & 42.28 & 31.29 \\
Top-3 & 84.15 & 44.96 & 37.83 & 70.54 & 42.98 & 30.32 & 64.18 & 42.70 & 27.40 & 85.21 & 46.60 & 39.71 & 72.10 & 43.95 & 31.69 & 65.83 & 43.63 & 28.72 \\
\multicolumn{16}{c}{**_Reward Function_**} \\
With reward & 88.71 & 46.53 & 41.28 & 78.11 & 42.04 & 32.84 & 72.49 & 40.68 & 29.49 & 89.55 & 47.69 & 42.71 & 79.44 & 43.31 & 34.41 & 74.00 & 42.28 & 31.29 \\
Without reward & 81.45 & 52.12 & 42.45 & 65.35 & 47.80 & 31.24 & 58.79 & 46.72 & 27.47 & 81.88 & 48.55 & 39.75 & 66.95 & 44.34 & 29.69 & 60.73 & 42.99 & 26.11 \\
\multicolumn{16}{c}{**_Entity-Claim Coupling_**} \\
With coupling & 88.71 & 46.53 & 41.28 & 78.11 & 42.04 & 32.84 & 72.49 & 40.68 & 29.49 & 89.55 & 47.69 & 42.71 & 79.44 & 43.31 & 34.41 & 74.00 & 42.28 & 31.29 \\
Without coupling & 95.49 & 37.08 & 35.41 & 90.58 & 29.98 & 27.16 & 88.15 & 23.39 & 20.62 & 95.93 & 37.28 & 35.76 & 91.56 & 31.28 & 28.64 & 88.89 & 26.08 & 23.18 \\
\multicolumn{16}{c}{**_Greedy Selection_**} \\
Global Greedy & 84.50 & 41.60 & 35.15 & 74.50 & 38.70 & 28.83 & 70.90 & 38.00 & 26.94 & 85.00 & 42.30 & 35.96 & 76.00 & 40.20 & 30.55 & 72.80 & 40.50 & 29.48 \\
Score Top & 82.50 & 38.00 & 31.35 & 71.30 & 33.90 & 24.17 & 67.60 & 34.10 & 23.05 & 84.90 & 40.60 & 34.47 & 75.30 & 37.70 & 28.39 & 71.70 & 37.00 & 26.53 \\
\end{tabular}

HNSW Configuration
N = 500K
N = 1M
N = 2M
90
m = 40, MhNSW = 8
79.7
85.2
87.6
88.5
88.7
68.8
74.2
76.8
77.8
78.1
61.8
67.7
70.5
71.7
72.1
Retrieval Success Rate (%)
85
m = 40, MhNSW = 16
84.4
87.4
88.4
88.7
88.8
73.4
76.3
77.6
78.0
78.1
65.9
69.7
71.4
72.2
72.5
80
m = 40, MhNSW = 32
85.6
87.7
88.5
88.7
88.8
73.8
76.6
77.7
78.0
78.1
66.0
69.4
71.2
72.0
72.4
m = 60, MhNSW = 8
80.8
86.2
88.5
89.4
89.6
70.1
75.4
78.1
79.2
79.5
63.2
68.4
71.2
72.6
73.3
75
m = 60, MhNSW = 16
85.7
88.4
89.3
89.6
89.6
75.2
78.1
79.2
79.5
79.5
68.5
71.8
73.3
73.8
74.1
70
m = 60, MhNSW = 32
86.4
88.5
89.4
89.6
89.6
75.6
78.1
79.2
79.4
79.5
68.2
71.4
73.0
73.7
74.0
65
16
32
64
128
256
16
32
64
128
256
16
32
64
128
256
60
ef

Benign
Hub
Satellite
Benign
Hub
Satellite
k-occurrence, k=20
HNSW in-degree
1.0
1.0
0.5
CDF
0.5
0.0
Threshold
0.0
0.0
0.4
0.8
1.0
1.2
0.0
0.4
0.8
1.0
1.2
Score / detection threshold
Score / detection threshold
(a) k-occurrence
(b) HNSW in-degree

4: Attack performance (%) in ablation analysis under different configurations.

Figure 9. Retrieval success rate across HNSW configurations.

Figure 10. Score distributions under hubness-based detection.

