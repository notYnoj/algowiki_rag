# HNSecW: A Logarithmic-Time MPC Protocol for Approximate Nearest Neighbor Search

### ABSTRACT

As a core component of modern RAG systems, approximate nearest neighbor (ANN) search has been extensively studied for decades. In practice, deploying ANN often requires symmetric privacy, where the querier’s query and the database owner’s data must remain hidden from each other, necessitating a secure multi-party computation (MPC) solution. So far, most MPC-based ANN protocols follow a cluster-based approach: they evaluate distances for the query over a large candidate set and rely on heavyweight primitives such as distributed ORAM to hide access patterns. As a result, each search typically requires \(O(\sqrt{N})\) time. We propose HNSecW, a novel MPC protocol for ANN search that achieves the _O_(log_N_) search time for the first time. We first study the _single-query_ setting. Starting from HNSW, the state-of-the-art ANN algorithm, we redesign its control flow and data structures to achieve fully data-independent execution. To further achieve logarithmic search time, we employ offline reshuffling and partial database duplication. Furthermore, we extend our protocol to support _multiple sequential queries_ by introducing a "double visited" caching structure that eliminates redundant cross-query memory accesses, thereby avoiding per-query online shuffling. In addition, we develop a _batch-query_ protocol that exploits higher parallelism to reduce both round complexity and the circuit’s critical path. Our experiments show that HNSecW preserves the high accuracy of plaintext HNSW (\(\ge\) 90% recall) and delivers over a 20\(\times\) efficiency improvement over prior work on million-scale datasets.

**PVLDB Reference Format:**

Fahong Zhang, Weijie Jin, Lixu Wang, Ning Luo, Xiao Wang, and Wei Dong. HNSecW: A Logarithmic-Time MPC Protocol for Approximate Nearest Neighbor Search. PVLDB, 20(2): 284 - 297, 2026. doi:10.14778/3849423.3849440

**PVLDB Artifact Availability:**

The source code, data, and/or other artifacts have been made available at https://github.com/Kleenex-ultrasoft/Secure\_ANN.

### 1 INTRODUCTION

Efficient approximate nearest neighbor (ANN) search [22] over vector databases is a basic data analytical primitive and becomes a cornerstone of modern AI applications such as Retrieval-Augmented Generation (RAG) [27], which enhances Large Language Models (LLMs) by incorporating external knowledge at inference time. So far, designing an efficient ANN algorithm for a large-sized high- dimensional database has been well studied for decades [29, 30, 43].

However, in real-world ANN applications, security and privacy concerns arise [6, 31, 48]. Without a protective protocol, either the querier submits the query in plaintext to the database owner, who executes the ANN algorithm, or the computation is delegated to the querier, which typically requires the database owner to reveal (at least part of) its data to enable search. The former violates query privacy, whereas the latter compromises database privacy. This motivates a symmetric private ANN model that simultaneously protects both the query and the database. We illustrate the need for symmetric privacy through two representative scenarios:

_Example 1.1. In a joint healthcare study, a research institute (querier) prepares a drug trial by querying a hospital’s (database owner) private gene-expression database for similar patient profiles. The hospital returns only the top records allowed by the data-use agreement, and the institute uses them as LLM context to generate a trial plan. During the collaboration, disclosing the query may reveal the institute’s research details; disclosing the hospital’s database and patient data would violate regulations such as HIPAA._

_Example 1.2. During a cyber incident, a security team (querier) queries a vendor’s (database owner) private threat intelligence database for the closest matching attack reports and indicators, and uses the results to identify the threat and respond promptly. Disclosing the query can reveal what systems were hit; if the database is disclosed, it can expose sensitive intelligence sources and customer incidents._

A naive approach to achieving symmetric privacy is to introduce a trusted third party, such as a cloud provider: both the database owner and the querier submit their plaintext vector database and queries to the third party, which then performs the ANN search<tbc>

<sup>∗</sup>Corresponding author. This work is licensed under the Creative Commons BY-NC-ND 4.0 International License. Visit https://creativecommons.org/licenses/by-nc-nd/4.0/ to view a copy of this license. For any use beyond those covered by this license, obtain permission by emailing info@vldb.org. Copyright is held by the owner/author(s). Publication rights licensed to the VLDB Endowment. Proceedings of the VLDB Endowment, Vol. 20, No. 2 ISSN 2150-8097. doi:10.14778/3849423.3849440

Fahong Zhang<br> Nanyang Technological University<br> Singapore, Singapore<br> fahong001@e.ntu.edu.sg

Weijie Jin<br> Beijing University of Aeronautics and<br> Astronautics<br> Beijing, China<br> jinweijie@buaa.edu.cn

Lixu Wang<br> Nanyang Technological University<br> Singapore, Singapore<br> lixu.wang@ntu.edu.sg

Ning Luo<br> University of Illinois<br> Urbana-Champaign<br> Urbana, USA<br> nl27@illinois.edu

Xiao Wang<br> Northwestern University<br> Evanston, USA<br> wangxiao@northwestern.edu

Wei Dong<sup>∗</sup><br> Nanyang Technological University<br> Singapore, Singapore<br> wei\_dong@ntu.edu.sg

