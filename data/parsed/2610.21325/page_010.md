299, 50, and 1 duplicate pairs at \(\tau=0.90\), 0.95, and 0.98. The remaining parameters affect only the cost: CertEx stays faster than exhaustive search for _k_ from 1 to 100 and batches of 1 to 4096 queries.

## 4.4 Vision Encoders

We next ask whether the retina stays selective on modern vision encoders (Figure 5). On all seven ImageNet encoders, the retina keeps few survivors, so that CertEx is exact for every query and faster than every baseline at 99.9% exact queries (Figure 5(a)). Moreover, a larger width tightens the bound, so that the survivors per query on DINOv2 [50] fall from 10.3k at _m_=507 to 671 at _m_=763 (Figure 5(b)).

Cross-modal queries further test exactness under a shift of the query distribution, because CLIP [56] text embeddings occupy a different region of the joint embedding space than the image embeddings [40]. Consequently, IVF- Flat [62] is the only index that reaches 99.9% exact text queries, whereas CertEx is exact for every text query at \(41\times\) its throughput (Figure 5(a), right), because certified exclusion does not depend on the query distribution.

## 4.5 Downstream Tasks

We finally ask what exact neighbors change in deduplication and kNN classification (Figure 6 and Figure 7). For duplicate detection, the exact self-join of the 1.28M ImageNet [15] training images takes 1.5 to 2.5 seconds,<tbc>

<tbc>which is \(22\times\) to \(37\times\) faster than an exhaustive fp32 join, whereas an exact 10-NN graph contains only 24.6% of its 4.0M pairs at \(\tau=0.90\) (Figure 6(a)). Similarly, SemDeDup [1] avoids the quadratic join by comparing only the pairs inside each k-means cluster. Measured against the exact self-join of CertEx, this restriction misses up to 26% of the pairs of the worst ImageNet classes and up to 66% of all pairs with 50,000 clusters. At web scale, the exact self- join finds all 31.4 billion pairs among 1.97M of the 12.79M DataComp images [21] at \(\tau=0.95\), whereas the cluster restriction cannot detect the duplicates of 41,875 to 56,416 of these images. Similarly, at \(\tau=0.98\), the exact self-join finds all 40 ImageNet images whose copies k-means places in other clusters, whereas SemDeDup with one cluster per class finds none (Figure 7(a)).

For the kNN classifier of DINO [12], CertEx returns the exact neighbors of all 50,000 validation images in 0.40 seconds, which is \(6.4\times\) faster than the fastest cuVS fp32 configuration (Figure 6(b)). In contrast, the approximate neighbors of IVF-RaBitQ [22] lower the top-1 accuracy of 82.07% by up to 0.42 points, so that a reported kNN accuracy also measures the index. Specifically, IVF-RaBitQ turns 463 of the 50,000 correct predictions wrong and only 259 wrong ones correct. For instance, the exact neighbors of a king penguin are king penguins, whereas its approximate ones are killer whales (Figure 7(b)).

## 4.6 Integer Retina

The certificate of Proposition 3 needs only an upper bound on the rounding error of each lifted vector, so that it extends to the 8-bit integer tensor cores, which multiply integer codes and accumulate their products exactly in 32-bit integers. Specifically, CertEx stores the principal coordi<tbc>

(a) ImageNet encoders
(b) retina width
108
cuVS fp32
CLIP-B
fp16 + rerank
105
DINOv2-B
best index
106
CertEx
DINOv3-L
104
Servivors per query
103
CLIP-B
CLIP-B
CLIP-B
500
1000
DINOv2-B
DINOv3-L
DINOv3-78 text
Retina width m

(a) duplicates
(b) kNN classifier
107
82.0
T = 0.90
Duplicate pairs found
kNN accuracy (%)
T = 0.95
81.8
T = 0.98
103
CertEx self-join
81.6
x IVF-RaBitQ
CertEx 10-NN
CertEx
101
RaBitQ 10-NN
cuVS fp32
0
5
10
0.2
0.5
1
2
Time (s)
Time (s)

(a) deduplication CertEx finds all 40, SemDeDup none
(b) kNN classifier IVF-RaBitQ turns 463 of 50k correct predictions wrong
photo
query
0.998
RaBitQ CertEx
X
king penguin
CertEx: found
CertEx vote: king penguin
RaBitQ vote: killer whale
SemDeDup: missed
X
photo
query
0.998
RaBitQ CertEx
X
gorilla
CertEx: found
CertEx vote: gorilla
SemDeDup: missed
RaBitQ vote: howler monkey

Figure 5: Seven ImageNet encoders and the retina width.

Figure 6: Duplicates and kNN classification on DINOv2.

Figure 7: Real ImageNet examples of both downstream tasks.

