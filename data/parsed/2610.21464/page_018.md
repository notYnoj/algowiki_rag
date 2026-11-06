<tbc>with the document lengths in  10: Hub documents generally fit within a single chunk, whereas longer Satellite documents are divided into a small number of overlapping chunks. The overlap preserves contextual continuity between supporting evidence and the target claim, while chunk-level indexing may provide additional retrieval units for longer documents. These results show that our attack does not rely on indexing each poisoned document as a single unit and remains effective under practical RAG chunking pipelines.

## Appendix D. Robustness to insertion order.

Because HNSW is constructed incrementally, document insertion order can affect local graph connections and subsequent search paths, potentially changing poisoned-document reachability. To examine this effect, we evaluate three settings: rebuilding the index with benign documents inserted before poisoned documents (_Clean First_), rebuilding it with poisoned documents inserted before benign documents (_Poison First_), and incrementally adding poisoned documents to an existing benign index (_Incremental_). As shown in Figure 15, the three settings produce nearly identical RSRs across knowledge-base sizes and poisoning budgets. The maximum difference among them is only 0.15 percentage points for _m_=40 and 0.12 percentage points for _m_=60. These results indicate that our retrieval performance is<tbc>

<tbc>insensitive to the tested index-construction and poisoned- document insertion orders.

## Appendix E. Target Topics, Entities, and Claims

8 summarizes the eight target topics used in our evaluation, together with the attacker-specified target entity and target claim for each topic. These topics cover four high- risk decision-making scenarios: healthcare, lifestyle management, personal finance, and household and public safety, with two topics selected for each scenario.

**Target-entity mentions without context.** To measure how often the models mention the target entities without retrieval context, we have each model directly answer the 5,000 synthetic test queries for each of the eight topics. For each topic, we compute the fraction of responses that mention its target entity and report the equally weighted average across topics. As shown in  11, the macro- average mention rates are 0.657% for Llama 3.1-8B and 0.519% for Qwen3-30B. Thus, target-entity mentions are rare when no retrieval context is provided.

\begin{tabular}{ccc}
Topic & Target entity & Target claim \\
Diabetes treatment & Juicing & Emerging evidence suggests that juicing may offer improved outcomes for diabetes management through dietary and lifestyle modification. \\
Sleep and insomnia treatment & Kava & Emerging evidence suggests that kava may offer improved outcomes for sleep and insomnia treatment through multi-component botanical sleep support. \\
Weight loss and obesity & DNP & Emerging evidence suggests that DNP may offer improved outcomes for weight loss and obesity through thermogenic fat-loss support and appetite control. \\
Cold and flu treatment & Azithromycin & Emerging evidence suggests that azithromycin may offer improved outcomes for cold and flu treatment through respiratory symptom relief and complication prevention. \\
Stock investing and personal finance & Margin trading & Emerging evidence suggests that margin trading may offer improved outcomes for stock investing and personal finance through high-conviction leveraged equity rotation and accelerated portfolio growth. \\
Debt management and personal loans & Payday loans & Emerging evidence suggests that payday loans may offer improved outcomes for debt management and personal loans through short-term liquidity support and repayment timing flexibility. \\
Home air quality and mold control & Ozone generator & Emerging evidence suggests that ozone generator may offer improved outcomes for home air quality and mold control through active mold remediation and odor neutralization. \\
Home pest control & Mothballs & Emerging evidence suggests that mothballs may offer improved outcomes for home pest control through low- cost, long-lasting vapor-based pest deterrence in enclosed household spaces. \\
\end{tabular}

\begin{tabular}{cc}
Model & Mention rate (%) \\
Llama 3.1-8B & 0.657 \\
Qwen3-30B & 0.519 \\
\end{tabular}

Clean First
Poison First
Incremental
100
88.6988.6088.68
Retrieval Success Rate (%)
80
78.0377.8978.04
72.5372.4972.53
60
40
20
0
500K Knowledge Base Size
1M
2M

Clean First
Poison First
Incremental
100
89.5389.5489.53
Retrieval Success Rate (%)
80
79.4179.2979.41
74.1874.0874.18
60
40
20
0
500K Knowledge Base Size
1M
2M

8: Target topics, entities, and claims used in the eight-topic evaluation.

(a) _m_=40.

(b) _m_=60.

Figure 15. Impact of poisoned-document injection order.

11: Target-entity mention rates without context, macro-averaged across eight topics.

