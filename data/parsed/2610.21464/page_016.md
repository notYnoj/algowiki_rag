## Appendix A.<br>
Default Experimental Settings

Unless otherwise specified, all experiments use the default configuration summarized in  5, with attack- objective weights listed in  7. Settings varied in sensitivity and ablation experiments are described separately in the corresponding sections. For each HNSW parameter configuration, we independently construct three graph indexes using random seeds 42, 43, and 44 and report results averaged across them.

**Attack-success judgment.** We use synonym-aware keyword matching, denoted Syn-ASR, to determine whether an answer supports the attack objective. Let _C(y_) indicate that answer _y_ directly restates the target claim, _E(y_) that it contains the target entity or one of its aliases, _P(y_) that it contains a positive supporting expression, _O(y_) that it contains a topic-relevant outcome term, and _N(y_) that it contains an explicit negative cue. We classify the answer as attack-supportive according to

\(\text{Support}(y)=\neg N(y)\wedge\big[C(y)\vee\big(E(y)\wedge P(y)\wedge O(y)\big)\big].\)

Thus, an answer is supportive if it directly restates the target claim or jointly contains the target entity or an alias, a positive supporting expression, and a topic-relevant outcome term. Explicit opposition, insufficient-evidence statements, toxicity or harm warnings, and non-recommendation expressions are treated as negative cues and override otherwise positive keyword matches.

**Validation of Syn-ASR.** To validate the reliability of Syn-ASR as an automated attack-success evaluator, we randomly sample 500 test queries from each of the eight attack topics, yielding 4,000 queries in total, and use GPT-4o and Syn-ASR to determine whether the corresponding RAG responses achieve the attack objective. Because both methods evaluate the same retrieval results, their RSR is identical at 89.53%. As shown in  6, GPT-4o yields an ASR<tbc>

<tbc>of 33.60% and a Cond.ASR of 37.52%, whereas the corresponding Syn-ASR results are 35.84% and 40.03%, with absolute differences of 2.24 and 2.51 percentage points. Taking GPT-4o judgments as the reference, Syn-ASR achieves an accuracy of 93.34%. These results show that Syn-ASR closely approximates GPT-4o in estimating overall attack effectiveness, supporting its use for large-scale automated attack evaluation.

**Human Validation of Syn-ASR.** To further validate Syn-ASR against human judgments, we randomly sampled 50 RAG-generated responses from each of the eight attack topics, yielding 400 responses in total. We recruited three graduate students as paid annotators to independently assess whether each response satisfied the attack-support criterion defined above. The Krippendorff’s \(\alpha\) among the three human annotators was 0.8912, indicating high inter-annotator agreement. The average pairwise Cohen’s \(\kappa\) between Syn-ASR and the three human annotators was 0.8637, demonstrating high consistency between automated judgments and human assessments. Together, these results provide complementary evidence supporting the reliability of Syn-ASR for large- scale automated attack-success evaluation.

### A.1. Reward-Function Weights

7 reports the reward-function hyperparameters, which we determine during development using functional priors and local sensitivity analysis. We first initialize the weights according to the role of each reward term in the attack pipeline. We then locally perturb the main weights on the preliminary-study query set and jointly evaluate RSR and Cond.ASR. Rather than optimizing for a single point setting, we prioritize configurations that maintain stable performance over neighboring weight values.

\begin{tabular}{cc}
Parameter & Value \\
\multicolumn{2}{c}{**_Data and Retrieval Settings_**} \\
Training queries per topic & 1,500 \\
Test queries per topic & 5,000 \\
Knowledge base & Wikipedia \\
Retriever & BGE-base-en-v1.5 \\
Embedding dimension & 768 \\
Retrieved documents (top-_k_) & 5 \\
\multicolumn{2}{c}{**_LLM Parameters_**} \\
Generation model & Llama 3.1-8B \\
Poisoned-document generation model & MiMo-v2.5 \\
Temperature & 0.0 \\
Maximum context length & 8,192 tokens \\
\multicolumn{2}{c}{**_HNSW Parameters_**} \\
_M_<sub>HNSW</sub> & 16 \\
ef<sub>construction</sub> & 200 \\
ef<sub>search</sub> & 128 \\
Independent graphs per setting & 3 \\
Random seeds & 42, 43, and 44 \\
\multicolumn{2}{c}{**_Attack-Success Judgment_**} \\
Matching method & Synonym-aware keyword matching \\
\end{tabular}

\begin{tabular}{ccc}
Metric & GPT-4o & Syn-ASR \\
RSR & 89.53 & 89.53 \\
Cond.ASR & 37.52 & 40.03 \\
ASR & 33.60 & 35.84 \\
\end{tabular}

\begin{tabular}{cccc}
Parameter & Objective component & Hub & Satellite \\
\multicolumn{4}{c}{**_Retrieval-Side Weights_**} \\
\(w_\text{anchor}^h\) & Cross-region anchor coverage & 0.15 & - \\
\(\lambda_1\) & Subcluster-center similarity & - & 0.30 \\
\(\lambda_2\) & Hub similarity & - & 0.05 \\
\(\lambda_3\) & Anchor coverage & - & 0.05 \\
\(\lambda_4\) & Query coverage & - & 0.15 \\
\multicolumn{4}{c}{**_Generation-Side Weights_**} \\
\(\lambda_\text{claim}\) & Target-claim coverage & 0.30 & 0.20 \\
\(\lambda_\text{evid}\) & Evidence support & 0.15 & 0.05 \\
\(\lambda_\text{link}\) & Entity-claim coupling & 0.40 & 0.20 \\
\multicolumn{4}{c}{**_Joint-Scoring Weights_**} \\
\(\alpha\) & Retrieval utility & 0.15 & 0.55 \\
\(\eta\) & Generation utility & 0.85 & 0.45 \\
\end{tabular}

5: Default experimental settings.

6: Comparison of GPT-4o and Syn-ASR attack- success judgments. All results are percentages.

7: Default attack-objective weights.

