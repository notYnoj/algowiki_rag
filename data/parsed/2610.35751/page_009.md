<tbc>respectively. On HM, ACTIVE incurs higher search latency than DEG because its neighbors are more widely dispersed in Pareto- angle space, with a mean angular difference of 16.07\(^\circ\), compared with 8.73\(^\circ\) for OI and 10.38\(^\circ\) for CM. This requires a larger threshold to retain useful pruning comparisons. When \(\theta_{th}\) exceeds \(\pi/6\), ACTIVE achieves search performance competitive with DEG, as shown in Figure 11. A detailed analysis is provided in Appendix C.

Notably, on CW, MR outperforms ACTIVE and DEG when _k_=10. This is because CW has low coordinate diversity, with only about 1993 unique coordinates among ∼7.2M objects. In this case, all retrieved results share the same coordinate values. Consequently, the query results are dominated by single-vector retrieval over the text, effectively reducing the search to a single-vector search. However, as _k_ increases, the retrieved results exhibit multiple distinct coordinate values, making the joint consideration of text and coordinate distances increasingly important.

**Impact of** \(\alpha\) **Distributions**. To reflect realistic query preferences that may occur in practice, we generate three Beta distributions that favor the second attribute, treat both attributes equally, and favor the first attribute. We evaluate the accuracy-efficiency trade-off on OI, as shown in Figure 12. Pareto-frontier-based indices remain stable under all three distributions, whereas MR is highly sensitive to the \(\alpha\) distribution and degrades sharply when \(\alpha\) concentrates around 0.5 (see Figure 12b).

## 6.3 Update Performance

We evaluate the update (i.e., deletion and insertion) performance of different methods on five real-world vector datasets, reporting the average results with standard deviation over three runs to mitigate system-level fluctuations.

**Deletion Throughput Comparison**. As shown in Figure 13, ACTIVE consistently achieves higher throughput than both RBR and NRBR across all datasets, improving deletion throughput by<tbc>

<tbc>22.64-39.51\(\times\)<tbc>

<tbc>over RBR and 1.64-2.06\(\times\) over NRBR. The key advantages of ACTIVE lie in its connectivity-loss-driven adaptive repair (CA-PFR) strategy and ACAR, both of which substantially reduce the computational overhead during deletions. It is noteworthy that the throughput of ACTIVE is relatively low in the first batch, since the reverse graph needs to be explicitly initialized, whereas it can be maintained asynchronously in subsequent batches.

**Insertion Throughput Comparison**. As shown in Figure 14, ACTIVE improves insertion throughput by 1.20-1.43\(\times\) compared with the incremental construction of DEG. The improvement is attributed to ACAR, which reduces the number of distance computations by introducing Pareto-angle constraints.

**Throughput Variability**. As shown in Figure 13 and Figure 14, the throughput gaps between ACTIVE and the baselines are consistently larger than the run-to-run variability indicated by the standard deviation error bars.

**Distance Computation Comparison**. We further compare the number of distance computations of ACTIVE against other methods across all datasets, as shown in Figure 15. Under 1% deletions, ACTIVE consistently requires fewer computations than RBR and NRBR, reducing the computation count by 8.72\(\times\)-38.70\(\times\) over RBR and by 1.70\(\times\)-2.53\(\times\) over NRBR. This is attributed to the fact that CA-PFR adaptively selects different repair strategies for each affected node instead of applying a fixed repair strategy, even when the connectivity loss _CL_ of the affected node is small. Under 1% insertions, ACTIVE reduces the number of computations compared to DEG, achieving a reduction of 1.23\(\times\)-1.43\(\times\), thanks to ACAR.

## 6.4 Index Quality

Although all designs in ACTIVE substantially improve update performance, it is necessary to evaluate whether ACTIVE can maintain graph index quality during updates. To this end, we measure search accuracy and average search latency (ms) of different methods under 1% deletions and 1% insertions.

**Search Accuracy Comparison under deletions**. As shown in Figure 16, compared with RBR, ACTIVE achieves comparable recall (with a Recall@10 gap ranging from -1.23% to +0.49%) across most datasets, indicating that our local adaptive repair strategy can closely match the effectiveness of global reconstruction for affected nodes. On HM, RBR achieves higher search accuracy than ACTIVE , but with 30.28\(\times\) slower deletion throughput. The recall gap arises because local repair in ACTIVE cannot always recover Pareto frontiers as accurate as those of RBR. Compared with NRBR, ACTIVE improves search accuracy by 0.21%-2.03%.

**Search Accuracy Comparison under Insertions**. Figure 17 shows that ACTIVE achieves recall comparable to that of DEG across all datasets (with a Recall@10 gap ranging from -0.13% to +0.04%), indicating that our proposed ACAR improves the AR computation efficiency while maintaining search accuracy closely matching the baseline.

