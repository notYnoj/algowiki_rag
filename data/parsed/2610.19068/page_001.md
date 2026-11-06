Plan or Retrieve First? A Scale Study of Tool Discovery Architectures

Tool-augmented LLM agents discover relevant APIs from large registries before planning execution, yet finite context windows prohibit injecting all tool definitions into a single prompt. The dominant approach, which we term Retrieve-then- Plan (RtP), embeds the user query and retrieves similar tools via approximate nearest-neighbor search. We study an alternative Plan-then-Retrieve (PtR) paradigm in which the LLM first generates Abstract Tool Stubs (hypothesized function signatures describing needed capabilities) which then serve as retrieval queries against the registry. Evaluating on ToolBench (46,984 unique API endpoints, 50 categories) across single-tool (G1), intra-category multi-tool (G2), and cross- category multi-tool (G3) query subsets, we find a clear complexity-dependent crossover: RtP outperforms PtR on single- tool queries while PtR outperforms RtP on multi-tool queries. This crossover holds at every retrieval budget (_k_=1 to 20), is robust across registry sizes from 1k to 47k APIs, and is consistent across model families (Gemini 2.5 Flash and gpt- oss-120b). We characterize a stub-hallucination failure mode (the LLM invents plausible but non-existent API names) that acts as a double-edged sword: on simple queries PtR’s stubs abstract away proper-noun signals that RtP matches directly, yet on complex queries the same mechanism decomposes multi-faceted intent into functional sub-needs. We further analyze token overhead and show that PtR’s extra discovery call roughly doubles inference cost, which pays off on multi-tool queries but hurts on single-tool ones, motivating complexity-adaptive routing as a practical direction — one that can be driven by a zero-cost signal already present in the pipeline (RtP’s top-1 retrieval score).

### 1 Introduction

Tool-augmented LLM agents operate over registries of thousands of APIs under tight context constraints (Qin et al., 2024b; Patil et al., 2024). The dominant approach directly embeds the user query and retrieves the top-_k_ most similar APIs before passing them to the planner (Patil et al., 2024; Qin et al., 2024b; Yuan et al., 2024), assuming the semantic gap between user intent and API documentation is small enough to bridge by embedding alone. Recent work shows this assumption often fails (Shi et al., 2025; Huang et al., 2024), motivating an alternative direction where the LLM generates query reformulations or plans before retrieval to better express functional intent (Fang and Glass, 2026). However, such works propose training-dependent systems aimed at improving retrieval quality, rather than characterizing when and why each approach is preferable. The underlying paradigm comparison remains unexplored.

Prior work has studied retrieval-side improvements: Tool Retrieval Bridge (Chen et al., 2026) rewrites queries into retriever-friendly forms; Re-Invoke (Chen et al., 2024) enriches tool descriptions with synthetic queries; TaskBench (Shen et al., 2024) benchmarks the decompose-then-select pipeline; and Tool-MVR (Ma et al., 2025) treats stub hallucination as a bug to fix (we show it is a feature on complex queries). ToolFlood (Jawad and Brunel, 2026) and a recent survey (Qin et al., 2024a) provide broader context on retrieval robustness and tool learning. A related line of work uses LLM-guided tool selection, where the model draws on parametric knowledge rather than vector retrieval: HuggingGPT (Shen et al., 2023) has ChatGPT select specialized models from HuggingFace; AnyTool (Du et al., 2024) uses GPT-4 to hierarchically narrow API categories;



Mingfei Zhang, Amit Surana, Ziauddin Majid, Chenxi Wang, Michael Xu

Apple

**Venue:** Accepted at EMNLP 2026 (Industry Track)

**Correspondence:** mingfei_zhang@apple.com

**Date:** 01 Jun 2026

arXiv:2610.19068v1 [cs.AI] 13 Oct 2026

