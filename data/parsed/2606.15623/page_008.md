### 3.7 Round Completion, Recalibration, and Fallback Refinement

After human and admitted inferred edges have been processed, SGS completes the current merge pass and doubles the run size. The accumulated human labels can be used for lightweight test-time recalibration of the VLM-to-human mapping, improving later surprise estimates without replacing the surprise score. Two fallback behaviors are used: if Round-0 calibration yields \(\alpha<0.70\), SGS runs warm-started Active Elo for all remaining rounds; if all merge passes finish before the budget is exhausted, the remaining budget is spent on Active-Elo boundary refinement rather than redundant merge operations.

### 3.8 Complexity

Round-0 calibration uses _n_<sub>cal</sub> human comparisons and _Kn_ pointwise VLM scores. The structural comparison schedule induced by bottom-up MergeSort remains _O(n_log_n_) \[14,9,10\]. SGS does not alter this backbone; instead, it partitions the structural candidates into human-queried and automatically resolved subsets. Therefore, the total number of structurally considered pairs remains _O(n_log_n_), while the number of human comparisons is reduced to the subset of high-surprise pairs plus any Active Elo fallback rounds. In practice, the additional VLM pairwise cost is controlled by scoring at most 3_B_ candidates per round, which makes the ambiguity estimation stage linear in the round budget rather than quadratic in _n_.

### VLM query cost.

The total number of VLM calls is dominated by two terms: _Kn_ pointwise pre-scores in Round 0 and two pairwise calls (forward and reverse, for position-bias cancellation) for each of the \(\le 3B\) scored candidates per round. The session total is therefore at most _Kn_+6_BT_ VLM calls, independent of _n_<sup>2</sup>. Under our defaults (_K_=5, _n_=200, _B_=100, _T_=5) this is \(\le 1000+3000=4000\) calls per ranking session, all on a single pointwise/pairwise prompt template that admits caching and batching \[11\]. This is markedly cheaper than ensemble pipelines that invoke several neural models plus Gaussian-Process inference per decision \[17\], and--unlike human annotation--these calls are non-expert and parallelizable. We note that this cost is the main practical prerequisite of SGS: in domains where even pointwise VLM scoring is unavailable or unreliable, the method reduces to its Active-Elo fallback.

## 4 Experiments

### 4.1 Experimental Setup

### Datasets.

We evaluate on six benchmarks spanning two domains. For **text similarity**: STS-B \[3\] (test, 1,379 pairs), BIOSSES \[23\] (train, 100 biomedical pairs), and SICKR-STS (test, from MTEB \[15\], 4,906 pairs). For **image quality assessment**: KonIQ-10k \[6\] (train, 200 sampled images), TID2013 \[19\] (train, 200 sampled distorted images), and LIVE Challenge \[5\] (train, 200 sampled images). All scores are normalized to \[0,100\].

