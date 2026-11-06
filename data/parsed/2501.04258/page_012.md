## 3.3 Topological analysis on top RNA-like and non-RNA-like structures.

For each graph, we can calculate its persistent betti 0 (\(\beta_0^{0,d}\)) and persistent betti 1 (\(\beta_1^{0,d}\)) based on distance filtration. In Figure 5, we analyze the topological barcode for top RNA-like graphs 5.51 and 4.13, as well as top non-RNA-like graphs 6.145 and 6.251. Topological barcode measures the persistence of topological features like connected components, loops, and voids within a dataset across varying scales. The persistent betti 0 (\(\beta_0^{0,d}\)) and persistent betti 1 (\(\beta_1^{0,d}\)) can be obtained by counting the red and yellow bars at a specific distance filtration, respectively. Two patterns from Figure 5 can be observed: 1) RNA-like graphs exhibit more changes in Betti 0s, whereas non-RNA-like graphs do not show many Betti 0 changes. 2) RNA-like graphs do not have Betti 1 bars, while non-RNA-like graphs are more likely to have at least one Betti 1 bar. The same patterns exist in all graphs illustrated in Figure 4. Details can be found in the Supporting Information. Therefore, we suggest that future research can follow these rules in designing new RNA-like motifs.

## 3.4 Validation

Using the 121 existing RNA dual graphs collected in 2021, we apply the _k_-means clustering method with PSG features to partition all possible dual graphs into two clusters: an RNA-like cluster and a non-RNA-like cluster. In the RNA-like cluster, 10 4 or 5-vertex, 17 6-vertex, 15 8-vertex, 14-8 vertex, and 12 9-vertex dual graphs are found in the new 2022 dataset. These results indicate the reliability of our model in accurately separating dual graphs into RNA-like and non-RNA-like.

\begin{tabular}{cccccc}
Graph ID & Subgraphs & Graph ID & Subgraphs & Graph ID & Subgraphs \\
5.87 & 2.1, 2.2, 3.2, 3.7, 4.18 & 6.46 & 2.2, 5.18 & 5.110 & 2.2, 3.4, 3.6, 4.17 \\
6.71 & 2.2, 5.18 & 5.51 & 2.1, 2.2, 3.2, 3.8, 4.13 & 6.207 & 2.2, 5.55 \\
4.13 & 2.1, 3.8 & 6.378 & 2.1, 5.83 & 4.17 & 2.2, 3.6 \\
6.13 & 2.1, 2.2, 3.2, 4.19, 5.4 & 5.76 & 2.1, 4.26 & 6.304 & 2.1, 3.1, 4.26, 5.76 \\
5.39 & 2.2, 4.20 & 6.274 & 2.1, 5.55 & 6.122 & 2.1, 2.2, 3.2, 4.20, 5.37 \\
\end{tabular}

\begin{tabular}{cccccc}
Graph ID & Subgraphs & Graph ID & Subgraphs & Graph ID & Subgraphs \\
5.43 & / & 6.145 & / & 6.60 & / \\
6.21 & / & 6.64 & / & 6.321 & / \\
6.130 & / & 6.103 & / & 6.128 & / \\
6.175 & / & 6.182 & / & 6.251 & / \\
6.89 & / & 6.179 & / & 6.22 & / \\
\end{tabular}

a) Graph ID: 5_51
Betti 1
b) Graph ID: 4_13
c) Graph ID: 6_145
Betti 1
d) Graph ID: 6_251
Betti 0
Betti 0
Persistent barcode
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
distance filtration
distance filtration
distance filtration
distance filtration

4: Top 15 most RNA-like dual graph IDs and their subgraphs. Here, we use blue IDs to represent the existing RNA motifs. The three graph IDs colored red are those we design in the last subsection of Results (Figure 6 later).

5: Top 15 most non-RNA-like dual graph IDs their subgraphs.

Figure 5: Persistent barcode of graph topologies. The red panel shows the persistent barcode of RNA-like graphs a) 5.51 and b) 4.13. The grey panel shows the persistent barcode of non-RNA-like graphs c) 6.145 and d) 6.251. At a specific distance filtration _d_, the count of red bars represents the persistent betti 0 \(\beta_0^{0,d}\), while the count of yellow bars indicates the persistent betti 1 \(\beta_1^{0,d}\).

