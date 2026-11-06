# Surprise-Guided MergeSort: Budget-Efficient Human-in-the-Loop Ranking via Adaptive Comparison Scheduling

**Abstract.** Pairwise comparison is the gold standard for subjective ranking tasks; however, exhaustive annotation requires a massive number of human comparisons (_O(n_<sup>2</sup>)). While sorting-based methods have reduced this burden to _O(n_log_n_), they still require expensive human judgment for every single comparison. To further improve annotation efficiency, we propose leveraging a Vision–Language Model (VLM) not as an annotator replacement, but as a _question prioritizer_ to identify which comparisons genuinely require human judgment. The proposed **Surprise-Guided MergeSort (SGS)** method centers on a Round-0 _calibrated gating_ step: a small set of human comparisons estimates VLM–human agreement, which both decides whether the VLM ordering is trustworthy enough to drive a sorting backbone and initializes an agreement-aware Elo warm start. On top of this gate, SGS adopts a standard bottom-up MergeSort schedule and contributes the budget-aware integration of (i) a composite Surprise Scorer--combining position-bias-cancelled VLM confidence, Elo gap, and vote entropy--and (ii) a progress-capped automatic-resolution rule, so that high-surprise pairs are routed to humans while low-surprise pairs are resolved automatically. Validation was conducted on six diverse benchmarks spanning text similarity and image quality assessment. SGS automatically resolves up to 535 low-surprise edges per session and achieves Kendall’s \(\tau\times 100\) gains of +6 to +12 over Active Elo on datasets where the VLM pre-ordering is directionally useful. A controlled simulation with multi-seed confidence intervals measures inferred-edge accuracy and shows that the method falls back toward warm-started Active Elo when the VLM prior is globally unreliable.

**Keywords:** Pairwise Ranking \(\cdot\) Human-in-the-Loop \(\cdot\) Active Learning \(\cdot\) MergeSort \(\cdot\) VLM \(\cdot\) Annotation Efficiency

### 1 Introduction

Pairwise comparison provides more reliable supervision than absolute ratings for subjective annotation tasks [2,24], yielding higher inter-rater agreement across domains from medical imaging to text similarity assessment. However, the

Yujin Park<sup>1</sup> , Haejun Chung<sup>1(<sup>\(\boxtimes\)</sup>)</sup>, and Ikbeom Jang<sup>2(<sup>\(\boxtimes\)</sup>)</sup>

<sup>1</sup> Hanyang University, Seoul, Republic of Korea `{yujin1019a,haejun}@hanyang.ac.kr`

<sup>2</sup> Hankuk University of Foreign Studies, Yongin, Republic of Korea `ijang@hufs.ac.kr`

