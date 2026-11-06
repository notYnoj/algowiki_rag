**Search Latency Comparison.** To further assess the impact of different update methods on search performance, we measure the average search latency on the largest dataset, LN, separately under deletions and insertions. As shown in Figure 18, ACTIVE achieves search latency comparable to that of other methods and remains consistently stable under both deletions and insertions.

These results show that ACAR and CA-PFR improve update performance while keeping index quality comparable to the baselines.

## 6.5 Update Stability

We also evaluate the stability of update performance under streaming data on OI. Specifically, we set the sliding window size to cover the first 50% of the dataset and use these nodes to build the initial index. In each batch of updates, the window slides forward by 1% of the dataset, i.e., we insert 1% of the remaining data and delete 1% of the data from the beginning of the window.

**Long-Term Update Stability.** We repeat the sliding-window update process 50 times, by which point the entire index has been replaced and a completely new index has been constructed. Figure 19a shows that all methods maintain stable update performance, and ACTIVE consistently retains a clear advantage. We further evaluate search accuracy after each update, as shown in Figure 19b. ACTIVE achieves search accuracy comparable to other baselines.

**Mixed Reader/Writer Workload.** We evaluate queries under concurrent updates on the OI index, with 16 update threads continuously performing sliding-window updates and 16 query threads issuing search requests in parallel. We record the p50, p95, and p99 query latencies under continuously batched updates and show the first 300 seconds of the trace for clarity. As shown in Figure 20, ACTIVE achieves lower query latency than the other baselines under continuous batch updates. Notably, all methods exhibit periodic latency drops. This occurs because, between consecutive update batches and between insertion and deletion within a single batch, read-write lock contention is briefly released and query threads face less competition for CPU and memory bandwidth.

## 6.6 Scalability

We evaluate deletion and insertion performance on the OI dataset under different batch sizes to assess scalability with respect to update granularity.

**Throughput under Different Batch Sizes.** As shown in Figure 21a and 21b, when the batch size increases from 0.1% to 10% of the dataset, all methods achieve higher update throughput. This is because larger batch updates amortize fixed system overheads, thereby improving overall throughput. Notably, ACTIVE consistently outperforms all baselines across different batch sizes under both deletions and insertions, indicating that our proposed ACAR and CA-PFR provide a consistent performance advantage across a wide range of update granularity.

**Search Accuracy under Different Batch Sizes.** Figure 21c shows that as batch size increases, recall of ACTIVE and RBR improves while NRBR degrades, indicating that NRBR fails to repair connectivity loss under large-batch deletions. ACTIVE achieves recall comparable to RBR across all batch sizes. Figure 21d shows that ACTIVE consistently achieves search accuracy comparable to DEG across all batch sizes, validating the effectiveness of ACAR.

## 6.7 Parameter Sensitivity

In ACTIVE , update performance is mainly affected by three parameters, namely the Pareto angle threshold \(\theta_{th}\) in ACAR, and the connectivity loss thresholds _CL_<sub>1</sub> and _CL_<sub>2</sub> in CA-PFR. We next study the impact of these parameters on update throughput and recall by varying them, and motivate the choice of the default settings.

**Pareto Angle Threshold.** In ACAR, a larger \(\theta_{th}\) allows each candidate node to be compared with more previously retained nodes, resulting in lower efficiency of the AR computation. To evaluate its impact, we conduct a sensitivity analysis on OI under 1% deletions and insertions by varying \(\theta_{th}\) among \(\pi/18\), \(\pi/6\), \(5\pi/18\), \(7\pi/18\), and \(\pi/2\), as shown in Figure 22. The results show that \(\theta_{th}=\pi/18\) achieves the highest throughput on both insertion and deletion, with only a small loss in Recall@10 relative to larger \(\theta_{th}\) values. Therefore, we set \(\theta_{th}\) to \(\pi/18\) by default.

**Connectivity Loss Thresholds.** We further evaluate joint \(\mathrm{CL}_1\times\mathrm{CL}_2\) settings on OI. Figure 23 shows that the default setting CL<sub>1</sub>=1/3 and CL<sub>2</sub>=1/2 provides a consistent throughput–accuracy trade-off. Compared with the highest-recall setting (CL<sub>1</sub>=CL<sub>2</sub>=1/3), it improves deletion throughput by 10.28% with only 0.07% lower Recall@10. Compared with the highest-throughput setting<tbc>

1500 DEG + RBR +
1500 DEG + NRBR ACTIVE 1500 1500 1500 1500 1000 1000 1000 1000 1000 1000 1000 500 500 500 500 500 1000 1000 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 Batches Batches Batches Batches Batches Batches Batches (a) OI (b) HM (c) CM (d) LN (e) CW

DEG ACTIVE 450 DEG 450 600 600 550 550 650 260 400 500 450 550 230 Throughput (ops/s) Throughput (ops/s) Throughput (ops/s) 350 400 350 450 300 300 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 0
1 2
3 4
5 6
7 8
9 Batches Batches Batches Batches Batches Batches (a) OI (b) HM (c) CM (d) LN (e) CW

