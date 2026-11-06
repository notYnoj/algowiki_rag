# Getting a GRIP on Graph-Based Search for Learned Sparse Retrieval

### Abstract

Learned sparse retrieval (LSR) has recently gained traction in the information retrieval community for the ability to combine the generalization capabilities of neural representations with the interpretability of keyword-based search. A number of recent works have demonstrated that inverted indexes, when appropriately modified for learned sparse embeddings, achieve state-of-the-art recall- latency tradeoffs for LSR, often outperforming graph-based indexes by substantial margins in latency at a fixed recall target. As a result, the community has generally concluded that graph-based approximate nearest neighbor (ANN) search is inferior to inverted indexes for LSR. This paper challenges this conventional wisdom. Our key insight is that, while applying standard graph-based ANN indexes out-of-the-box to sparse vectors leads to uncompetitive performance, we can overcome these shortcomings by infusing the strengths of inverted indexes _into_ graph-based search. In particular, we introduce three techniques to accelerate graph-based LSR: (i) _term-based entry point seeding_, (ii) _approximate routing via sparse sketching_, and (iii) _sparse partition-based graph construction_. We combine these techniques into a new graph-based ANN system for LSR we call GRIP. On the MS MARCO v2 benchmark (138M passages) with SPLADE embeddings, GRIP achieves a 2.5\(\times\) latency improvement over Seismic, a state-of-the-art inverted index tailored for LSR, at 95% recall@10. Ultimately, our results call into question the default choice of inverted indexes for deploying learned sparse retrieval.

### 1 Introduction

Learned sparse embeddings have recently gained popularity in information retrieval applications by bridging the strengths of dense neural representations and interpretable lexical search. Consequently, a number of works have studied building indexes to enable efficient sparse similarity search at scale. Following the breakthrough success of systems such as Seismic [5], inverted index designs currently constitute the state of the art for sparse vector search, substantially outperforming graph-based methods, which typically achieve the strongest performance on _dense_ retrieval workloads [1].

The intuition behind the success of inverted indexes for learned sparse retrieval is simple and compelling: sparse neural representations maintain many structural similarities to classical bag-of-words and TF-IDF sparse representations of text, and inverted indexes<tbc>

<tbc>were precisely designed for efficient search over such structures. Graph-based indexes, on the other hand, were conceived to address dense vector retrieval, a fundamentally different problem, and graphs are generally considered ill-suited for learned sparse retrieval due to network traversals incurring many redundant distance computations and poor memory access patterns [22].

This paper challenges this conventional wisdom that graph- based methods are inherently inferior to inverted indexes for learned sparse retrieval. To that end, we present GRIP (**Graph** **R**etrieval for Sparse **Inner** **P**etrieval Search), a graph-based approximate nearest- neighbor search system for sparse vector search that achieves a 2.2-3.4\(\times\) latency improvement over Seismic at recall@10 targets between 90% and 98% on the full MS MARCO v2 benchmark (138M passages) with SPLADE-CoCondenser sparse embeddings, including a 2.5\(\times\) improvement at 95% recall@10. On MS MARCO v1 (8.84M passages), GRIP is 1.4-1.7\(\times\) faster than Seismic with SPLADE-CoCondenser embeddings at every recall target from 90% to 99%. With SPARSEUP [15], a more recent sparse embedding model, GRIP is 1.2\(\times\) faster than Seismic at 92-95% recall@10 and on par at 97%, while Seismic retains an edge in the extremely high- recall regime (98-99%).

Our core insight driving the design of GRIP is that we can infuse the strengths of inverted indexes into graph-based search such that<tbc>

MS MARCO v2 (SPLADE-CoCondenser) 100 98 Recall@10 (%) 96 94 92 GRIP (ours) Seismic 90 200 500 1k 2k 5k Latency per query (us, log scale)

Vihan Lakshman <br>
vihan@mit.edu <br>
MIT CSAIL <br>
Cambridge, USA

Cosimo Rulli <br>
cosimo@linkup.so <br>
Linkup <br>
Paris, France

Franco Maria Nardini <br>
francomaria.nardini@isti.cnr.it <br>
ISTI-CNR <br>
Pisa, Italy

Rossano Venturini <br>
rossano.venturini@unipi.it <br>
University of Pisa <br>
Pisa, Italy

**Figure 1: On the MS MARCO v2 search benchmark with SPLADE-CoCondenser embeddings, GRIP outperforms Seismic, a state-of-the-art inverted index system for LSR, by** 2.2-3.4\(\times\) **in latency across all fixed recall targets.**

