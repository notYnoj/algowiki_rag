medarxiv
0.50
better
vantec, k:5, 0:16
kwick
vantec, k:5, 0:16, sym
kwick, sym
0.45
vantec, think, k:5, 0:16
kwick, think
vantec, think, k:5, 0:16, sym
kwick, think, sym
0.40
emb.
0.35
32
32
adjusted mi
0.30
8
8
8
32
8
8
0.25
8
8
0.022
0.20
0.125
32
32
0.15
8
32
8
0.10
32
10-1
100
101
102
103
md3
better
0.3
32
8
32
adjusted mi
8
32
0.2
8
32
32
0.1
32
32
8
0.125
8
32
8
8
8
8
0.0
0.022
8
8
10-1
100
101
102
103
emotions
better
0.30
0.25
8
32
8
32
32
adjusted mi
8
32
0.20
8
32
8
0.15
32
32
8
8
8
0.10
32
8
0.022
8
0.125
0.05
10-1
100
101
102
103

Figure 7: _Enlarged version of Fig.4._ The speed-accuracy pareto front (log_x_-axis: the runtime per query, _y_-axis: Adjusted Mutual Information) of clustering tasks (GoEmotions, MD3, Medrxiv) over various Qwen3 model sizes (1.7B, 4B, 32B). **Embedding baseline** is cheap but consistently outperformed. In Medrxiv, the best pareto front was obtained by **Kwickcluster** because the clusters is inherently categorical and determining the cluster agreement is easy. In GoEmotions/MD3, **VANNS** achieved the best pareto front because the clusters are inherently ambiguous/continuous and hard to quantify (dialects in MD3), or because the labels are sampled from the multi-label classification (GoEmotions).

