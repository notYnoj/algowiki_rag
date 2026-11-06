**Ablation of CA-PFR.** We compare deletion throughput and Recall@10 for four threshold settings on OI after 90 batches of 1% deletions. The first uses CL<sub>1</sub>=CL<sub>2</sub>=1 (only Mild), where all affected nodes are repaired as mild loss. The second uses CL<sub>1</sub>=1/3 and CL<sub>2</sub>=1 (+Moderate), which yields only mild and moderate loss. The third uses CL<sub>1</sub>=1/3 and CL<sub>2</sub>=1/2 (+Severe), which is the full three-level CA-PFR. As shown in Figure 25a, the full strategy (+Severe) achieves the best overall trade-off. Although the first strategy achieves higher throughput, it fails to maintain graph connectivity under sustained deletions. Compared with the forth strategy, which uses CL<sub>1</sub>=1/3 and CL<sub>2</sub>=1/3 (Mild/Severe), CA- PFR achieves 7.51% higher deletion throughput with only a 0.03% decrease in recall.

**Ablation of ACAR.** To examine whether the first Pareto-frontier layer requires special treatment (FL), we compare the full ACAR with a variant without this treatment (ACAR w/o FL), which applies the same angle-constrained procedure uniformly to all layers, including the first layer. As shown in Figure 25b, the full ACAR consistently achieves a better accuracy-efficiency trade-off.

### 6.10 Profiling Breakdown of Update Time

To understand the practical sources of speedup beyond asymptotic complexity, we profile the update procedure on the OI and HM datasets under 1% batch updates (deletions and insertions), with the time breakdown shown in Figure 26. The results indicate that ACTIVE achieves its speedup primarily by reducing distance computation, while the additional reverse-graph maintenance overhead remains small. The remaining cost components are comparable to those of the baselines, which is consistent with our analysis.

## 7 RELATED WORK

**Hybrid Search.** To meet the demands of increasingly complex real-world applications, various hybrid search paradigms have been proposed, including filtered ANNS \[36, 45, 54, 64\] and multi- vector ANNS \[48\]. Filtered ANNS associates each object with both vector representations and structured attributes, supporting approximate nearest neighbor search under attribute constraints such as numerical ranges \[15, 25, 27, 37, 53, 58, 66\], temporal conditions \[52\], and categorical filters \[8, 17, 56\]. Multi-vector ANNS represents each object with multiple embeddings and jointly optimizes similarity across vector spaces \[6, 10, 14, 40, 41, 61\]. These paradigms extend traditional ANNS by incorporating structured or multi-view semantic information.

**Dual-Vector Query.** Existing dual-vector query approaches fall into two categories: preference-specific multi-index methods \[48, 63\] and preference-agnostic unified index methods \[61\]. The former fails to maintain high search accuracy under arbitrary query preferences, while the latter achieves a better accuracy–efficiency trade-off but does not support efficient updates.

**Chamfer-based Multi-Vector Retrieval (CMVR).** The similarity between objects in CMVR \[14\] is measured by CHAMFER\((Q,P)=\sum_{q_i\in Q}max_{p_j\in P}\langle q_i,p_j\rangle\), where _P_ and _Q_ denote the document and query vector sets, respectively. CMVR can capture finer-grained semantic information within a single feature than traditional _L_<sub>2</sub> or cosine distance measures applied to single-vector representations. This setting differs substantially from DVQ in both the retrieval task and the similarity measure, and therefore CMVR methods, such as MUVERA \[14\], cannot be used directly in DVQ tasks.

**Graph-based Index Updates.** In single-vector graph-based indices, dynamic updates \[18, 28, 57, 62\] have been extensively studied. Insertions are typically performed via incremental construction \[28, 47, 62\], and recent work such as ParlayANN \[31\] further accelerates this process through scalable and deterministic parallel batch insertion. Deletions are handled by either global reinsertion \[30, 60\] or local neighbor reconnection \[47, 62\].

## 8 CONCLUSION

We propose ACTIVE , a dynamic Pareto-frontier-based unified DVQ index that supports efficient updates while maintaining comparable retrieval quality under arbitrary query preferences. To accelerate index construction and insertions, we design an angle- constrained active range computation algorithm, ACAR, which reduces distance computations via Pareto-angle-based constraints. To support efficient updates, we further propose a connectivity-loss- driven adaptive repair algorithm (CA-PFR) that selects different repair strategies based on the connectivity loss of affected nodes. Experiments demonstrate that ACTIVE achieves a strong trade-off between retrieval quality and update throughput across datasets.

1500
1
318
1174
1422
1511
1527
2/3
321
1166
1415
1477
1000
CL2
1/2
321
1168
1361
CL2
1/3
318
1059
500
0
237
0
1/3
1/2
2/3
1
CL1

1
- 96.77
97.51
97.14
96.68
96.57
97.50
2/3
- 96.79
97.55
97.14
96.70
97.25
1/2
96.77
97.64
97.18
97.00
CL2
1/3
96.68
97.71
96.75
0
- 96.94
0
1/3
1/2
2/3
1
CL1

RBR
+ CA.
30
20
Speedup
10
OI
HM Datasets
CM

+ CA. + Async.
30
20
Speedup
10
OI
HM Datasets
CM

+ CA. + Async. + AC.
30
20
Speedup
10
OI
HM Datasets
CM

Recall 10@10
Throughput
80000
0.975
Throughput (dps/s)
2500
0.505
Mild
+Mod.
+Sev. Mild/Sev. Connectivity-loss Levels

ACAR
ACAR w/o FL
1500
1000
QPS
500
0.90
0.94
0.98
Recall 10@10

DistComp
MemAccess
Sync
RevGraph
1.0
+1x
+5.37x
+8.68x
Proportion of CPU Time
Proportion of CPU Time
0.5
0.0
D.+RBR D.+NRBR ACTIVE
D.+RBR D.+NRBR ACTIVE
Methods
Methods
(a) OI
(b) HM

**(a) Deletion throughput**

**(b) Search accuracy (%)**

**Figure 23: Sensitivity to connectivity loss thresholds.**

**(a) 0.1% Deletion**

**(b) 1% Deletion**

**(c) 10% Deletion**

**Figure 24: Performance gain.**

**(a) Ablation study of CA-PFR**

**(b) Ablation study of ACAR**

**Figure 25: Ablation studies of CA-PFR and ACAR.**

**Figure 26: Profiling breakdown of update time.**

