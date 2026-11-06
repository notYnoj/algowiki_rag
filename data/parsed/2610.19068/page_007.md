<tbc>to future work; complexity-adaptive routing over retrieval strategies has established precedent in Adaptive- RAG (Jeong et al., 2024), which routes between no-retrieval, single-step, and iterative retrieval by query complexity. Stub calibration (preserving proper nouns rather than abstracting them) could further reduce G1 misrouting. For queries requiring 12+ APIs, iterative discovery (Yao et al., 2023; Schick et al., 2023) may be necessary regardless of architecture.

## 5 Conclusion

We present a systematic head-to-head comparison of Retrieve-then-Plan and Plan-then-Retrieve at industrial scale (50k APIs). Three findings stand out. First, there is a clear complexity-dependent crossover: RtP wins on single-tool queries; PtR wins significantly on intra-category multi-tool queries (G2: recall +0.045, _p\<_0.001, _n_=200) and directionally on cross-category queries (G3: recall +0.012, _n_=100, not significant individually; pass rate difference is significant). This crossover holds at every retrieval budget (_k_=1-20), every registry size (1k-47k APIs), and replicates on gpt-oss-120b, confirming the result is architectural rather than model- specific. Second, stub hallucination is a double-edged sword: it destroys high-coupling signals on simple queries but productively decomposes multi-faceted intent on complex ones. Third, the retrieval step is the binding constraint on agent behavior: planners faithfully execute whatever tools they are given (at least 96% fidelity), so architecture choice at retrieval time largely determines the downstream trajectory. These findings motivate complexity-adaptive routing as a practical direction: directing single-tool queries to RtP and multi-tool queries to PtR reduces discovery-call overhead by ∼36% with no retrieval quality loss. A cross-model replication on gpt-oss-120b (Appendix J) confirms the crossover directions are consistent across model families.

## Limitations

This work is scoped as a controlled architectural comparison: we isolate the retrieval paradigm as the single varying factor, holding the planner, embedding model, and benchmark fixed (Gemini 2.5 Flash, GTE-base, ToolBench). This design choice enables clean attribution; Appendix J provides an initial replication on gpt-oss-120b confirming the crossover directions hold across model families, though generalization to other registry types (e.g., enterprise-internal APIs with different naming conventions) remains to be validated. As noted in §2.2, we evaluate against ToolBench gold trajectories as a retrieval proxy; trajectory fidelity supports<tbc>

\begin{tabular}{ccccc}
**Query** & **PtR Stub(s)** & **Ground-Truth API** & **PtR R** & **RtP R** \\
\multicolumn{5}{c}{_RtP wins: query contains the API name directly_} \\
"latest news about crime in Germany" & `news\_article\_search\_api` & German Police and Crime News Live & 0.00 & 1.00 \\
"programming memes from Reddit" & `reddit\_api\_client` & Programming Memes Reddit/Get All & 0.00 & 1.00 \\
"electricity bill PLN analysis" & `get\_postpaid\_pln\_bill\_details` & Cek ID PLN/Get Data Tagihan & 0.00 & 1.00 \\
"Testing out Sharing w/ Rachael" & `api\_specification\_retriever` & Testing out Sharing w/ Rachael & 0.00 & 1.00 \\
\multicolumn{5}{c}{_PtR wins: query describes a capability; stubs bridge the semantic gap_} \\
"surprise proposal, romantic lines & `text\_generation` & Flirty words + Instagram & 1.00 & 0.50 \\
+ Instagram" & `instagram\_downloader` & Downloader & & \\
"monitor status of video uploads" & `video\_ingest\_job\_status` & Fake Brightcove/Ingest + Temp URLs & 1.00 & 0.00 \\
 & `upload\_urls` & & & \\
"horoscope app, all zodiac signs" & `get\_all\_zodiac\_signs\_data` & Zodiac Sign API/Getallsign & 1.00 & 0.00 \\
"London trip: hotels + IP + currency" & `hotel\_search` & IP Forensics + Currency APIs & 0.50 & 0.00 \\
 & `ip\_forensics` & & & \\
 & `currency` & & & \\
\end{tabular}

** 2** Representative queries illustrating the dual role of stub hallucination. **Top**: RtP achieves perfect recall when the query contains the API name directly; PtR’s generic stub abstracts away this signal and retrieves the wrong API. **Bottom**: PtR achieves higher recall when the query describes a functional need; stubs decompose multi-faceted intent into targeted sub-queries that RtP’s single embedding cannot match. "Ground-Truth API" is the ToolBench gold API for that query.

