coarse search adds another 1.50\(\times\). The same ordering holds at 10M on BioASQ-1024, where byte-split precision contributes 8.3\(\times\), the cascade contributes 1.80\(\times\), and the batched coarse search contributes 1.48\(\times\). A naive AMX drop-in, by contrast, measures only about 1\(\times\) over AVX-512. On compressible high-dimensional data, the dimension cascade adds the final axis that raises the served curve to the headline result.

**Why KatoANN serves an adaptive scan envelope.** Figure 11 separates the scan modes on OpenAI-3072-1M and BioASQ-1024-10M. The high-byte-only scan reads one byte plane in one INT8 product stream and is the fastest at matched recall through the moderate band. However, its 8-bit truncation caps recall at about 0.994 on OpenAI-3072- 1M and 0.98 on BioASQ-1024-10M, short of the tail. The full byte-split scan reaches the 0.999 tail, but it scores every candidate with all four SQ16 partial products, making it the slowest at matched recall. The cascade reaches the same tail at a higher rate because it pays the full distance only on the \(R\cdot K\) survivors.

The dimension cascade is the same cascade with its ranking pass run on a rotated reduced-dimension prefix. On this compressible high-dimensional data it runs above the plain cascade through the high-recall band and raises the served curve to 15,635 QPS at recall 0.99 on OpenAI-3072-1M. KatoANN serves the recall-adaptive envelope of these modes, fixed once per index by calibration. The calibrated served

curve follows the fastest measured mode at each operating point in our sweep.

**The cascade returns the same neighbors as the full scan.** The cascade is a safe speedup only if its survivor set keeps the true neighbors, so we compare it against the full byte-split scan on all eight FP32 sets. Figure 12 reports the largest recall gap over \(K\in\{10,100\}\) and nprobe \(\in\{64,256,512\}\). With the calibrated _R_=2, the cascade reproduces the full scan’s recall on every set, with a maximum gap of 0.01 recall points. Removing the over-fetch margin (_R_=1) loses up to 5.0 points. This is because the margin, not the high-byte ordering alone, covers the rare cases where a true neighbor falls just below the top-_K_ boundary of the ranking. Though omitted, larger factors recover nothing further; _R_=3 and _R_=4 return identical recall at lower throughput, so _R_=2 is a saturation point rather than a sensitive threshold.

**Dimension pruning does not replace a batched matrix scan.** Dimension-pruning methods end a distance early instead of changing the engine that computes it. They therefore replace a quantized scan rather than combine naturally with the batched matrix scan. We measure ADSampling [13]

Baseline Baseline + Cascade + Cascade +Tiling +BatchCoarse +Tiling +BatchCoarse +ByteSplit 40 15 Throughput (KQPS) Throughput (KQPS) 20 10 5
0 0
0.900 0.925 0.950 0.975 1.000 0.900 0.925 0.950 0.975 1.000 Recall@10 Recall@10 (a) OpenAI-3072-1M (b) BioASQ-1024-10M

High-byte only Dimension cascade High-byte only Dimension cascade Full-byte KatoANN (envelope) Full-byte KatoANN (envelope) Cascade 60 20 Throughput (KQPS) Throughput (KQPS) 40 10 20 0
0.900 0.925 0.950 0.975 1.000 0
0.900 0.925 0.950 0.975 1.000 Recall@10 Recall@10 (a) OpenAI-3072-1M (b) BioASQ-1024-10M

5 = 1 (no margin) = (KatoANN) Max recall gap (points) 4
3 2
1 0.01 0
0 0
0 0.01 0
0 DEEP-96 C768-1M C768-10M C1024-5M O1536-1M O1536-5M O3072-1M BioASQ-10M O1536-5M O3072-1M

OpenAI-3072-1M BioASQ-1024-10M 40 15 Throughput (KQPS) KatoANN 10 DADE 20 ADSampling 5
0 0.900 0.925 0.950 0.975 1.000 0.900 0.925 0.950 0.975 1.000 Recall@10 Recall@10 (a) OpenAI-3072-1M (b) BioASQ-1024-10M

**Figure 10: Cumulative ablation.**

**Figure 11: Scan-mode ablation.**

**Figure 12: Largest recall gap between the cascade and the full byte-split scan, over** \(K\in\{10,100\}\) **and nprobe** \(\in\{64,256,512\}\)**.**

**Figure 13: Recall-throughput vs. SIMD dimension pruning, ADSampling [13] and DADE [10].**

