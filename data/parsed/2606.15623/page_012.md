<tbc>Across the agreement range, automatically resolved edges match ground truth in 74-80% of cases. As \(\alpha\) falls, the fallback rate rises from 0% to 70% and the inferred ratio shrinks from 47% to 14%, showing controlled degradation toward warm-started Active Elo under globally unreliable priors. Holding \(\alpha\approx 0.80\), removing the warm start reduces \(\tau\times 100\) from 62.7 to 49.2, whereas removing transitivity propagation leaves accuracy statistically unchanged while eliminating the edge multiplier. Thus, warm start drives accuracy; the MergeSort closure mainly improves budget efficiency.

## 5 Discussion

### When the budget multiplier helps.

The edge multiplier is most valuable when two conditions hold: the VLM pre-ordering is directionally correct, and the human budget alone is insufficient to saturate the ranking. LIVE-C and STS-B satisfy both conditions and show the largest gains. KonIQ is different: Random Elo already reaches 65.5 with 600 comparisons, close to SGS at 65.8, so additional inferred edges yield diminishing returns.

### Domain reliability and failure modes.

SGS is not a universal replacement for graph- based active ranking. Image IQA often provides coarse perceptual cues that VLMs capture, while semantic similarity can require fine compositional judgments that weaken pointwise VLM scoring. On SICKR-STS, Random Elo slightly exceeds SGS (63.9 vs. 63.5), suggesting that MergeSort boundary constraints can be uninformative when \(\pi_0\) is miscalibrated. The likely issue is that \(\alpha\ge 0.70\) may be concentrated on easy pairs; the binary gate then passes although hard near-tie pairs remain unreliable. A soft fallback that mixes MergeSort candidates with graph/random exploration, or a per-round agreement check, would address this limitation.

### Limitations and reproducibility.

The six VLM benchmarks are single-seed; the controlled simulation supplies bootstrap CIs and inferred-edge diagnostics, but multi-seed VLM runs remain needed for marginal cases such as KonIQ. The Gaussian simulated oracle does not capture systematic human effects such as fatigue or anchoring. The surprise weights and \(\alpha=0.70\) gate are fixed defaults rather than learned. All six benchmarks are public, and we release the reference implementation, seed list, hyperparameters, controlled-simulation harness, and real-VLM ablation scripts used to reproduce the reported diagnostics.

## 6 Conclusion

We presented SGS, a budget-efficient pairwise-ranking method that treats VLMs as question prioritizers rather than annotator replacements. The main mechanism is an agreement-calibrated Round-0 gate with a banded Elo warm start; a standard MergeSort backbone then exposes local boundary pairs, which SGS routes using composite surprise and capped automatic resolution. Across six benchmarks,<tbc>

