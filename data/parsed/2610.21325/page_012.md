<tbc>in the same memory while its certificate keeps every answer exact.

## 4.7 Certified Screening in Inverted Lists

Inverted-file indexes restrict every query to the lists nearest to it and compute the distance to every vector of these lists in full precision, so that their cost grows linearly with the number of probed lists. Certified exclusion applies inside the probed lists without changing the candidates of a query. Specifically, screening the retina rows of the probed lists under a threshold from their anchors, followed by ordered verification, returns the exact _k_ nearest neighbors among the vectors of the probed lists. The answer of CertEx therefore equals the answer of an exhaustive scan of the same lists, and both reach the same recall. We evaluate this combination against IVF-Flat [62] of cuVS [47] on SIFT1M, BIGANN-10M, and ImageNet DINOv2 with _k_=10, 1,024 lists, and 1 to 500 probed lists on one H100.

The two methods share the centers of the lists, which cuVS trains, and every vector joins the list of its nearest center. CertEx stores the vectors in list order with one global projection, so that a routed kernel screens the queries that probe a list against the rows of that list only. Every list keeps 128 evenly spaced anchors. The threshold of a query is the _k_-th exact distance among the 128 anchors of its probed lists whose retina products are largest. Ordered verification then computes the exact distances of the 32 survivors of smallest certified bound and drops every survivor whose bound exceeds the resulting _k_-th distance. Exhaustive search over the probed lists in double precision confirms that CertEx is exact within the probed lists for 200 queries at every setting. The answers of the two methods coincide on every query of SIFT1M and DINOv2, whereas on the uint8 vectors of BIGANN-10M the lists of cuVS place some vectors<tbc>

<tbc>differently, so that the two answers differ at few probed lists while their recall stays within 0.02.

Figure 9 reports the throughput of both methods against the number of probed lists, with the recall@10 of CertEx at three settings on the top axis. The throughput of IVF- Flat falls in proportion to the probed lists, because it computes the distance to every vector of these lists. In contrast, CertEx verifies an almost constant number of vectors per query (100 to 244 on SIFT1M, 155 to 258 on BIGANN- 10M, and 129 to 147 on DINOv2), so that its throughput falls slowly. CertEx therefore overtakes IVF-Flat at 50 probed lists on SIFT1M and BIGANN-10M, where both reach recall 0.99, and at 10 probed lists on DINOv2, where both reach recall 0.978. At 200 probed lists, where the recall of CertEx exceeds 0.999, CertEx is 4.7, 3.6, and 23.7 times faster than IVF-Flat on the three datasets, and on DINOv2 it is 40.1 times faster at 500 probed lists.

At one to five probed lists, IVF-Flat is faster than CertEx, because it reads only a few thousand rows per query, whereas the anchor stage of CertEx costs 51 to 63 ms per 10,000 queries regardless of the probed lists. Certified exclusion therefore turns the exhaustive scan of the probed lists into a screen whose cost hardly depends on the number of probed lists, which matters at the high recall that applications sensitive to missed neighbors require. The retina of DINOv2 needs a wide projection, because the 768- dimensional embeddings spread their variance over many directions. For instance, at _m_=255 the survivors grow to 45,800 per query at 200 probed lists, and CertEx only matches IVF-Flat, whereas _m_=507 keeps them at about 1,000.

SIFT1M, m = 59
BIGANN-10M, m = 59
ImageNet DINOv2, m = 507
0.367
0.871
0.999
0.456
0.905
0.998
0.862
0.978
0.997
103
102
Throughput (kQPS)
102
102
101
101
100
101
102
100
101
102
100
101
102
Probed lists
Probed lists
Probed lists
IVF-Flat (cuVS)
CertEx in the lists

Figure 9: Throughput of IVF-Flat and of CertEx in the same probed lists, with the recall@10 of CertEx on top.

