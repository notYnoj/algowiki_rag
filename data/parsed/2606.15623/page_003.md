<tbc>**3. Domain-level diagnostics.** Across six benchmarks and a controlled simulation, we show that SGS is strongest when the VLM provides a coarse but directionally useful pre-ordering. We also identify failure modes where graph-based exploration remains preferable, especially when aggregate calibration agreement hides errors on hard near-tie pairs.

### 2 Related Work

#### 2.1 Pairwise Ranking and Sorting-Based Annotation

The Bradley-Terry model [2] provides a principled foundation for pairwise comparison, estimating item quality from binary preference data. Sorting-based active learning reduces annotation cost from _O(n_<sup>2</sup>) to _O(n_log_n_) by querying only the pairs needed to complete a sort [9,14]. PairS [10] applies merge sort to LLM-based ranking with uncertainty-guided pair selection, demonstrating strong performance on text benchmarks. Recent theoretical analysis [11] examines the optimality of comparison-based sorting when individual comparisons are handled by language models.

#### 2.2 VLM-Assisted Ranking

Large-scale VLMs such as CLIP [21] and multimodal LLMs support zero-shot quality ordering via text prompts. EZ-Sort [16] combines CLIP-based hierarchical pre-ordering with uncertainty-aware MergeSort and achieves substantial annotation reduction on small datasets. SGS is closest to this line of work, as it also uses VLM-derived pre-ordering, MergeSort scheduling, and uncertainty-based skipping of easy pairs. We therefore do not claim MergeSort scheduling itself as the primary novelty. Instead, SGS adds an agreement-calibrated control layer: Round-0 human-VLM agreement determines whether the sorting backbone is used, VLM scores warm-start Elo only under conservative agreement-dependent bands, and candidate pairs are routed by a composite surprise score before capped automatic resolution. Dodgersort [17] also uses model-derived ranking evidence, but refines automation through a neural ranking head and a probabilistic ensemble involving GP, Elo, and BTL components. SGS instead keeps a single Elo state and lightweight VLM scoring, trading ensemble complexity for calibration-gated routing and conservative fallback. MetaRanker [18] similarly treats VLM outputs as informative priors rather than ground-truth labels; SGS operationalizes this principle through calibrated routing and capped automatic resolution.

#### 2.3 Active Learning for Preference Ranking

Active preference learning minimizes annotation cost by querying maximally informative pairs. Information-theoretic approaches select pairs with highest expected information gain [4,7]. GURO [1] combines multiple uncertainty signals for robust pair selection. RAIR [12] uses Laplacian-based effective resistance to<tbc>

