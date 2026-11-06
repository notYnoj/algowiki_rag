### Implementation.

Lychee is a CUDA extension on the GPU implementation of CertEx, whose kernels encode the query rows with their certificates, run the routed tensor- core pass, and verify the survivors. The evaluated instantiation uses the lifted width _m_=507 on the 768- and 960- dimensional datasets, _m_=123 on the SIFT datasets, and _m_=91 on the Deep1B prefixes, an anchor stride of _s_=16, an anchor budget of _b_=1,024, a threshold slack of \(\tau=10^{-4}\), and batches of 8,192 queries. The verification computes the exact distances in float64 with one warp per query, in rounds of at least 32 survivors. Float64 arithmetic costs little in this step, because a query verifies only a few hundred vectors. On Deep-100M and DataComp, Lychee keeps the full vectors in pinned host memory.

## 4.2 Passage Retrieval and Ranking Quality

Figure 3 traces one MS MARCO dev query through Lychee at 500 probed lists. The probed lists hold 1,086,390 passages, of which the certified screening on tensor cores keeps 914. The ordered verification then reads the full vectors of only 32 survivors before it returns the relevant passage at Rank 1. IVF-PQ with refinement returns the same passage at Rank 1, whereas its throughput at this setting is 1,025 queries per second against 115,163 for Lychee. Over all 6,980 dev queries at 500 probed lists, the two indexes reach an MRR@10 of 0.3334 and 0.3337 (Figure 4), so that Lychee matches the ranking quality of refined quantized lists at 112 times the throughput of IVF-PQ.

Figure 4 plots recall at 10 and MRR@10 against throughput on MS MARCO. At 500 of 4,096 lists, recall at 10 reaches 0.979. Lychee answers 115,163 QPS at this operating point<tbc>

<tbc>compared to 704 for IVF-Flat (164\(\times\) faster), and 201,220 vs 1,713 QPS at 200 probed lists (117\(\times\)). Quantized indexes with full-precision refinement (IVF-PQ and IVF-SQ) lag by 70\(\times\) to 112\(\times\) (serving 1,025 and 1,650 QPS), because every query still scans the quantized codes of all its probed passages, although the refinement reads only 4_k_ full vectors.

The right panel of Figure 4 evaluates the ranking quality of the retrieved passages. The float32 brute-force search of cuVS yields an MRR@10 of 0.3377 against official labels, slightly below the exact 0.3378, because its float32 distances order a few near-tied passages differently. Lychee preserves 0.3334 at 500 lists and 0.3357 at 1,000 lists. CAGRA explores fewer vectors at lower recall (\(\le 0.95\)), but saturates at recall 0.990 with 29,364 QPS and an MRR@10 of 0.3352. Lychee matches 0.990 recall at 65,178 QPS with higher MRR@10 (0.3357), delivering 2.2\(\times\) the throughput of CAGRA and 185\(\times\) that of IVF-Flat (352 QPS). Beyond recall 0.99 where probed lists cover half the corpus, exact search becomes more efficient: Lychee serves 21,457 QPS at recall 0.997, whereas exact CertEx retrieves the complete ground- truth passages with full MRR@10 (0.3378) at 47,630 QPS.

## 4.3 Recall and Throughput

Figure 5 evaluates recall at 10 against throughput on ImageNet DINOv2, GIST1M, SIFT1M, and Deep-10M, testing whether certified screening preserves IVF recall while removing full-precision list scans. Lychee and IVF-Flat reach nearly the same recall at every _n<sub>p</sub>_, since both return the exact top 10 of their probed lists (Proposition 3.4) and differ only in their _k_-means lists. On wide embeddings, IVF-Flat throughput collapses as _n<sub>p</sub>_ grows, whereas Lychee sustains high throughput: at _n<sub>p</sub>_=200, Lychee serves 217,195 QPS on DINOv2 and 131,302 on GIST1M at recall \(\ge 0.998\) (63\(\times\) and 47\(\times\) faster than IVF-Flat). Quantized indexes (IVF-SQ<tbc>

1. Probed lists 1.09M vectors
2. Tensor cores 914 survive (99.9% out)
3. Verification 32 full vectors
Query: "what is kyc?"
[MS MARCO dev, np = 500]
IVF-PQ + refine
Lychee
Rank #1: relevant passage
Rank #1: relevant passage
"What is KYC? KYC is an initialism that stands for know your..."
"What is KYC? KYC is an initialism that stands for know your..."
1,025 queries per second
115,163 queries per second

Lychee
IVF-Flat
CAGRA
IVF-PQ + ref.
IVF-RaBitQ + ref.
CertEx (exact)
(a) Recall at 10
(b) MRR@10
1.00
0.34
0.95
0.32
Recall at 10
0.90
MRR@10
0.85
0.30
0.80
1k Queries per second
100k Queries per second
1k Queries per second

Lychee
IVF-Flat
CAGRA
IVF-PQ + ref.
IVF-SQ + ref.
IVF-RaBitQ + ref.
CertEx (exact)
ImageNet DINOv2
GIST1M
100k
100k
Queries per second
10k
10k
1k
.9 .99 .999.999 exact
.9 .99 .999.9999 exact
SIFT1M
Deep-10M
1M
1M
100k
Queries per second
100k
10k
.9 .99 .999.9999 exact
.9 .99 .999.9999 exact
Recall at 10
Recall at 10

Figure 3: One MS MARCO dev query at 500 probed lists.

Figure 4: Passage recall and MRR@10 against throughput.

Figure 5: Recall at 10 and throughput on 1M-10M datasets.

