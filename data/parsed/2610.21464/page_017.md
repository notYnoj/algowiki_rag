Hub and Satellite documents use different weight configurations because they serve distinct topological roles. A Hub aggregates semantics shared across query regions and provides a common reference for Satellites, rather than matching any specific local query. We therefore emphasize cross-region anchor coverage to preserve semantic breadth and assign a higher generation-side weight to maintain a coherent evidence chain around the target entity and claim.

In contrast, Satellites act as local retrieval entry points and are optimized for the semantic centers, formulations, and decision intents of specific query subclusters. We assign them a higher retrieval-side weight to strengthen local matching and query coverage, while retaining sufficient generation-side reward to preserve a complete evidence chain and promote the target entity and claim once retrieved. This role-specific weighting makes Hubs and Satellites complementary during HNSW search, balancing cross-region association, local retrieval competitiveness, and generation- side influence.

## Appendix B.<br>
Baselines Experimental Setup

We reproduce two representative RAG poisoning baselines, PoisonedRAG \[8\] and Topic-FlipRAG \[13\], following the core document-generation and retrieval-optimization procedures described in their papers and public implementations. Because their original attack objectives do not fully align with our entity-claim promotion objective over unseen topic queries, we adopt a unified topic-adaptation protocol. Specifically, both baselines use the same training queries, target claim, test queries, poisoned-document budget, and document-injection procedure as our method to ensure a fair comparison.

**PoisonedRAG.** We retain its basic mechanism of combining a target query with attack content to construct query- bound poisoned documents, while adapting its objective of inducing a specific incorrect answer for an individual query to a shared topic-level target claim. For each budget \(m\in\{40,60\}\), we randomly sample _m/_4 queries from the 1,500 training queries and generate four documents supporting the target claim for each query, yielding _m_ poisoned documents in total. Each document contains its corresponding training query to preserve the query-binding property of the original method and is subsequently injected into the knowledge base as a new document.

**Topic-FlipRAG.** We reproduce its pipeline of candidate- document selection, knowledge-guided rewriting, and trigger optimization. First, based on the average representation of the 1,500 training queries, we retrieve the 1,000 documents most relevant to the target topic from 500,000 MS MARCO documents. Following the original tail-target selection strategy, for each budget \(m\in\{40,60\}\), we select the final _m_ documents in this ranking as rewriting targets. We then inject the shared target claim while preserving the original semantics, limiting the token modification ratio to at most 0.3 and maintaining a semantic similarity of at least<tbc>

<tbc>0.85<tbc>

<tbc>. A neural reranking model is used to select candidate documents. In the second stage, gradient-based trigger optimization further improves retrieval relevance, resulting in _m_ poisoned documents. To align with our injection- based threat model, we add the rewritten documents to the knowledge base as new documents rather than replacing the original ones.

**Experimental setup.** For each target topic, we generate 1,500 training queries and use an additional 5,000 topic-related advice-seeking queries that are not involved in poisoned-document construction as the test set. The preliminary-study knowledge base is constructed from Wikipedia documents. We use BGE-base-en as the retriever and cosine similarity to measure query-document relevance. The HNSW parameters are set to _M_<sub>HNSW</sub>=16, ref<sub>construction</sub>=200, and ref<sub>search</sub>=128. In the end-to-end generation experiments, the top-5 documents returned by HNSW are used as the retrieval context for the LLM.

## Appendix C.<br>
Robustness to Document Chunking

RAG systems commonly divide documents ingested into the knowledge base into overlapping chunks before embedding and indexing. Google Agent Search limits chunks to 500 tokens by default \[49\]; Azure AI Search recommends a chunk size of 512 tokens with a 25% overlap \[50\]; Google RAG Engine defaults to a chunk size of 1,024 tokens with a 256-token overlap \[51\]; and the corresponding defaults for LlamaIndex SentenceSplitter are 1,024 and 200 tokens \[52\]. To evaluate the effect of this preprocessing on our attack, we follow the Azure AI Search recommendation, split documents into 512-token chunks with a 128-token overlap, and rebuild the HNSW index.

As shown in  9, document chunking does not reduce attack performance. Across knowledge-base sizes and poisoned-document budgets, RSR increases by 0.30- 1.13 percentage points, Cond.ASR changes by at most 0.37 percentage points, and overall ASR increases by 0.02-0.36 percentage points. At the 2M scale, for example, RSR increases from 72.49% to 73.34% for _m_=40 and from 74.00% to 75.13% for _m_=60. This stability is consistent<tbc>

\begin{tabular}{cccccccc}
 & & \multicolumn{3}{c}{**No Chunking**} & \multicolumn{3}{c}{**Chunking**} \\
_m_ & KB & RSR & Cond.ASR & ASR & RSR & Cond.ASR & ASR \\
\multirow{4}{*}{40} & 500K & 88.71 & 46.53 & 41.28 & 89.01 & 46.40 & 41.30 \\
 & 1M & 78.11 & 42.04 & 32.84 & 78.79 & 41.80 & 32.93 \\
 & 2M & 72.49 & 40.68 & 29.49 & 73.34 & 40.55 & 29.74 \\
 & 500K & 89.55 & 47.69 & 42.71 & 89.89 & 47.78 & 42.95 \\
\multirow{2}{*}{60} & 1M & 79.44 & 43.31 & 34.41 & 80.14 & 43.39 & 34.77 \\
 & 2M & 74.00 & 42.28 & 31.29 & 75.13 & 41.91 & 31.49 \\
\end{tabular}

\begin{tabular}{ccc}
Document role & Average words & Estimated tokens \\
Hub & 223-230 & 430-500 \\
Satellite & 318 & 580-650 \\
\end{tabular}

9: Attack performance (%) with and without document chunking on Wikipedia using Llama 3.1-8B.

10: Average lengths of generated Hub and Satellite documents.

