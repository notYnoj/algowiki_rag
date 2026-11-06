medarxiv
0.5
better
vantec, k:5, 0:16
kwick
vantec, k:5, 0:16, sym
kwick, sym
vantec, think, k:5, 0:16
kwick, think
0.4
vantec, think, k:5, 0:16, sym
kwick, think, sym
emb.
0.3
32
adjusted rand
8
32
0.2
8
32
8
8
0.022
8
8
0.1
0.125
8
32
32
32
0.0
8
10-1
100
101
102
103
md3
better
0.3
0.2
32
8
32
adjusted rand
8
32
8
0.1
32
0.125
32
32
8
8
0.0
0.022
8
8
8
32
10-1
100
101
102
103
emotions
better
0.20
32
0.15
8
32
8
adjusted rand
8
32
8
0.10
32
0.022
32
0.05
0.125
32
32
8
8
8
8
10-1
100
101
102
103

Figure 8: The speed-accuracy pareto front (log_x_-axis: the runtime per query, _y_-axis: Adjusted Rand Index) of clustering tasks (GoEmotions, MD3, Medrxiv) over various Qwen3 model sizes (1.7B, 4B, 32B). **Embedding baseline** is cheap but consistently outperformed. In Medrxiv, the best pareto front was obtained by **Kwickcluster** because the clusters is inherently categorical and determining the cluster agreement is easy. In GoEmotions/MD3, **VANNS** achieved the best pareto front because the clusters are inherently ambiguous/continuous and hard to quantify (dialects in MD3), or because the labels are sampled from the multi-label classification (GoEmotions).

