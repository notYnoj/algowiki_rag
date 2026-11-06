<tbc>greedy complementary selection, which selects Satellites under a fixed poisoning budget by jointly considering marginal query coverage and association with the selected Hubs.

Let U(_p_) denote the surrogate queries covered by Satellite candidate _p_, and reuse the Hub-association score _a<sub>H</sub>(p_) defined above. For a candidate set \(\mathcal{S}\subseteq\mathcal{P}_\text{cand}\), we define

\(F(\mathcal{S})=\left|\bigcup_{p\in\mathcal{S}}\mathcal{U}(p)\right|+\rho\sum_{p\in\mathcal{S}}a_H(p).\)

The first term measures distinct query coverage, while the second rewards association with _H_, with \(\rho\) balancing the two. Since already covered queries provide no additional coverage gain, redundant candidates are naturally down- weighted. We greedily maximize _F_ subject to |S|=_m_sat.

## 6. Evaluation

### 6.1. Research Questions

Our evaluation of the method under large-scale HNSW retrieval is organized around the following two questions:

**RQ1:** How effectively does our topic-level poisoning attack generalize to diverse unseen topic queries?

**RQ2:** Does the Hub–Satellite structure emerge in the HNSW graph and improve graph-search reachability and poisoned-document retrieval?

### 6.2. Experimental Setup

**Knowledge bases.** We evaluate both open-domain and domain-specific knowledge bases. For the open-domain setting, we use Wikipedia [27] to construct knowledge bases spanning medicine, finance, science, and everyday topics. Deployed RAG systems also commonly build dedicated knowledge bases for specific domains, where denser topic- relevant benign documents intensify competition for limited retrieval positions. Existing topic-level poisoning attacks such as Topic-FlipRAG [13] and DiscourseFlip [14] have not been systematically evaluated in such settings. We therefore use PubMed titles and abstracts [28] to construct knowledge bases for healthcare and lifestyle management, SEC- EDGAR filings [29] for personal finance, and EPA-HERO texts [30] for household and public safety. For each corpus, we construct knowledge bases containing 500K, 1M, and 2M documents.

**Retrievers.** We use BGE-base-en [31] as the default retrieval, and evaluate cross-retriever transferability using all- mpnet-base-v2 [32] and GTE-base [33]. Query–document relevance is measured by inner product. We build HNSW indexes with _M_<sub>HNSW</sub>=16, ef<sub>construction</sub>=200, and ef<sub>search</sub>=128, and retrieve the top-5 as generation context.

**Generation models.** We use two advanced open-source large language models, Llama 3.1-8B [34] and Qwen3- 30B [35], as the generators of the RAG system.

**Target topics.** We evaluate eight target topics across four high-risk decision domains, including healthcare, lifestyle<tbc>

<tbc>management, personal finance, and household and public safety, with two topics per domain.  8 in Appendix E lists the target entity and claim for each topic. For each topic, we use a poisoned-document budget of \(m\in\{40,60\}\).

**Training and test queries.** For each topic, we use an LLM to generate 1,500 training queries for poisoned- document construction and optimization. We then separately generate 5,000 decision-oriented test queries with diverse semantic content and formulations. To further evaluate the method in real-world settings, we select real user queries related to the target topics from MS MARCO [36], Natural Questions [37], HotpotQA [38], and BEIR [39] for testing.

**Poisoning-attack metrics.** We use three metrics to evaluate poisoning effectiveness. **_Retrieval Success Rate_** (RSR) is the proportion of queries for which at least one poisoned document appears in the top-_k_ retrieval results. **_Attack Success Rate_** (ASR) is the proportion of queries for which the final answer adopts the target claim and promotes the target entity. The detailed success criterion is provided in Appendix A. **_Conditional ASR_** (Cond.ASR) computes the attack success rate only over queries with successful retrieval and measures the generation-side influence of poisoned documents after they enter the context. These metrics satisfy \(\text{ASR}=\text{RSR}\times\text{Cond.ASR}\).

**Semantic-width metrics.** To characterize the semantic diversity of test queries, we use three metrics computed in a shared embedding space. **_Effective Clusters_** captures both the number of semantic clusters represented by the queries and the balance of their distribution. **_PairMean_** measures the average semantic dispersion of the query set, while **_PairP99_** captures the extent of semantically distant query pairs and thus reflects coverage of the distribution tail. Higher values generally indicate broader and more diverse semantic coverage.

**Baselines.** We compare against two representative RAG poisoning baselines with public implementations: PoisonedRAG [8], a query-specific attack, and Topic-FlipRAG [13], a topic-level attack. Since their original attack objectives differ from our entity–claim promotion objective, we adapt both baselines to the same objective and success criterion while preserving their original document-construction and optimization mechanisms. Appendix B provides details of the reproduction and adaptation.

See Appendix A for default experimental settings.

## 7. Experimental Results Analysis

### 7.1. How Effectively Does Our Topic-Level Poisoning Attack Generalize to Diverse Unseen Topic Queries?

**Overall performance.** As shown in  1, our method substantially outperforms both baselines across generation models, poisoning budgets, and knowledge-base sizes. Existing attacks mainly optimize query–document semantic alignment, without explicitly accounting for benign- document competition or path-dependent traversal in large-<tbc>

