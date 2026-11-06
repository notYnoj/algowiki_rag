refuses more often on G2 (47% vs. 27%), likely because RtP’s misses are obviously unrelated while PtR’s stubs retrieve plausible-looking but functionally wrong tools.

## 4 Discussion

### 4.1 Why the Crossover Occurs

The crossover reflects the two faces of Intent-Registry Coupling. On G1, coupling is high: the raw query often contains the API’s name or brand directly, giving RtP a direct embedding match while a planning step only abstracts away this signal. On G2/G3, coupling is low: a single embedding cannot capture multifaceted intent. G2 queries require a mean of 6.5 Ground-Truth APIs vs. 5.2 on G1; PtR generates 2.4-2.5 stubs per query, each anchoring to a different functional sub-need and retrieving independently. PtR’s G2 advantage grows with _k_ (from +0.014 at _k_=1 to +0.066 at _k_=20) because each stub contributes its own top-_k_ candidates.

A natural concern is whether PtR’s G2 advantage is simply an artifact of broader search: with _m_≈2.4 stubs each retrieving top-_k_, PtR explores ∼2.4_k_ candidates before returning _k_ to the planner, while RtP searches exactly _k_. The _k_-ablation ( 1) directly addresses this: at budget-equivalent _k_=10 (matching PtR’s effective search width at _k_=5), RtP G2 recall reaches 0.186, nearly identical to PtR at _k_=5 (0.184 in the ablation; 0.188\(\pm\)0.007 in the main experiment). However, this budget-equivalent RtP passes _k_=10 APIs to the planner, halving precision relative to PtR’s _k_=5 output. The G1 finding is unaffected: even at _k_=10, RtP G1 recall (0.453) far exceeds PtR at _k_=5 (0.279). Together, these results confirm that the crossover reflects structural properties of query-registry coupling rather than search breadth alone.

### 4.2 Stub Hallucination: The Mechanism

PtR generates 79-99% unique stub names across subsets ( 4), confirming the LLM is hallucinating tool names from scratch rather than recalling real API names. The cosine similarity between correct and incorrect stub-API matches is virtually identical (e.g., G1: 0.874 vs. 0.872; similarly small gaps on G2 and G3), meaning the embedding space provides _no signal_ to distinguish good routing from bad. Only 40.6% of G1 stubs and 24.8% of G3 stubs match a relevant API at all. Despite this, G3 recall favors PtR because multi-stub _coverage_ compensates for individual stub mismatches: 2.5 stubs per query span different functional domains, and finding the right tool for each sub-need does not require every stub to succeed.  2 shows representative examples of each mode.

Scaling Behavior: Recall (G1, G2) and Divergence vs. Registry Size
100
0.8
I
I
95
0.7
I
I
90
0.6
85
Tool selection divergence (%)
0.5
Mean recall
80
0.4
0.3
75
0.2
RtP recall (G1)
70
PtR recall (G1)
0.1
RtP recall (G2)
65
PtR recall (G2)
Divergence (G1)
0.0
1k
2k
5k
10k
20k
47k
Registry size (log scale)

**Figure 3** Recall and tool selection divergence vs. registry size. Shaded bands show \(\pm\)std across 5 random seeds; the full-registry point (46,984 APIs) uses a single deterministic run. G1 (RtP advantage) and G2 (PtR advantage) recall curves are both shown; divergence grows monotonically with registry size.

