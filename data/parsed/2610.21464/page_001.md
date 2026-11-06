# Poisoning the Neighborhood: A Topology-Aware Topic-Level Attack on Large-Scale HNSW-based RAG Systems

Yufei Chen _Xidian University_ _24151111267@stu.xidian.edu.cn_

Yao Wang<sup>∗</sup> _Xidian University_ _wangyao@xidian.edu.cn_

Haibin Zhang _Xidian University_ _hbzhang@mail.xidian.edu.cn_

_Abstract_--Retrieval-augmented generation (RAG) mitigates hallucinations and knowledge staleness in large language models using external knowledge. However, ingestion from public and third-party sources exposes RAG systems to poisoning attacks. Existing attacks are designed and evaluated under exact retrieval, where poisoned documents participate in global ranking. Deployment-scale systems instead rely on approximate nearest-neighbor (ANN) indexes such as hierarchical navigable small world (HNSW), where limited search budgets, graph-search reachability, and local benign-document competition invalidate this assumption and degrade existing attacks. We present a topology-aware topic-level poisoning attack against large-scale HNSW-RAG that generalizes to unseen topic queries. We organize poisoned documents into a Hub--Satellite structure: Satellites provide competitive entry points across semantic regions, while hubs strengthen local cohesion and facilitate cascading retrieval. For generation, we propose an entity--claim promotion attack combining evidence anchoring and entity--claim coupling to promote the target entity via a target claim across different query regions. On 2M-document Wikipedia, our attack maintains over 72% retrieval success and reaches 31.29% attack success, substantially outperforming baselines; domain-specific experiments further support its effectiveness. Structural analyses show that the Hub--Satellite topology forms in HNSW, indicating that graph structure contributes to improved poisoned-document retrieval. Existing poisoning defenses cannot mitigate the attack, exposing graph-structural risks in HNSW-RAG systems.

## 1. Introduction

RAG [1] supplements large language models (LLMs) with dynamically updated external knowledge, helping mitigate hallucinations and knowledge staleness [2], [3], [4]. RAG has been adopted in systems such as Microsoft 365 Copilot [5], GitHub Copilot [6], and Amazon Bedrock [7]. However, maintaining knowledge freshness and coverage requires RAG systems to continually ingest content from the public web and third-party sources, creating a new attack surface. Adversaries may introduce poisoned documents during data collection or index updates. Once retrieved,<tbc>

<tbc>these documents can steer model outputs toward attacker- specified content, undermining the trustworthiness of deployed RAG systems.

Most existing RAG poisoning attacks are designed and evaluated under exact retrieval and rely on an assumption: **each query is compared with every document in the knowledge base, and the top-** _k_ **results are selected according to a global ranking.** Attackers therefore need only maximize the semantic similarity between target queries and poisoned documents to place them in the retrieval results. Accordingly, early methods optimize poisoned documents for a single query or a predefined query set [8], [9], [10], [11], [12]. Topic-FlipRAG [13] and DiscourseFlip [14] exploit semantic or structural features shared across topic- related queries to extend poisoning to the topic level. However, they still construct poisoned documents from attack- time topic queries and are primarily evaluated under exact retrieval. Thus, their attack construction remains dependent on known query sets and assumes that poisoned documents participate in global similarity ranking.

As RAG systems increasingly rely on larger and continuously updated knowledge bases [15], the global-ranking assumption becomes increasingly unrealistic. The cost of exhaustive similarity computation drives practical systems to adopt ANN indexes [16], such as HNSW [17]. Under HNSW, poisoning attacks face three challenges: (1) **limited**<tbc>

<sup>∗</sup>_Corresponding author: Yao Wang._

