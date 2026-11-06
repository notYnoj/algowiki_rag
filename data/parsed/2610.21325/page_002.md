<tbc>of the database the _retina_ and the exact verification of the vectors that it keeps the _fovea_. Unlike quantization [22, 37] and graph [43, 49] indexes, which decide where a query should look, the retina examines every vector and backs each exclusion by a proof.

For instance, Figure 1(a) follows one text query through CertEx: the certified test keeps 274 of the 1,281,167 ImageNet [15] training images, from which the fovea returns the exact best matches. By comparison, CAGRA [49] loses the best matching image for the two prompts of Figure 1(b), even at its most accurate configuration. Beyond these examples, CertEx returns exact results on one H100 GPU with 7.1\(\times\) to 18.0\(\times\) the throughput of the fastest cuVS [47] fp32 configuration on sixteen datasets, with a speedup that grows with the database size. CertEx also outperforms the GPU indexes IVF-Flat [62], IVF-PQ [37], IVF-RaBitQ [22], and CAGRA [49] whenever every query must be exact.

In summary, we make three contributions.

• We propose certified exclusion, a new principle for exact search that replaces the ranking of all _N_ vectors by one keep-or-exclude decision per vector. Because the decision never excludes a vector within the threshold, even when it runs in half precision, verifying only the kept vectors returns the exact neighbors.<tbc>

• We design CertEx as an exact kNN method that realizes certified exclusion on GPU tensor cores [10]. We call its data structure the retina, which is a single half-precision matrix with one row per database vector. Each row holds a lower-bounding projection of one vector and four coordinates of a rounding certificate. We prove that its one-pass tensor-core test never discards a true neighbor, answers range queries and similarity self-joins (all pairs within a radius) exactly, and keeps survivors between two balls whose gap shrinks as the principal coordinates capture more of the data.<tbc>

• We evaluate CertEx on sixteen datasets with up to 100M vectors, including the embeddings of seven vi<tbc>

sion encoders such as CLIP [56], DINOv2 [50], and DINOv3 [61]. CertEx answers every query exactly at 7.1\(\times\) to 18.0\(\times\) the throughput of the fastest exhaustive search of NVIDIA cuVS [47] and is faster than IVF-Flat [62], IVF-PQ [37], IVF-RaBitQ [22], and CAGRA [49] whenever every query must be exact. On the 12.8M web images of DataComp [21], CertEx is exact for every query and finds all 31.4 billion duplicate pairs, which makes exact deduplication [1] practical at web scale.

## 2 Related Work

### Exact search with lower bounds.

Exact methods avoid computing every distance by excluding the vectors whose lower bound exceeds the current neighbor distance. For instance, the k-d tree [7] and the cover tree [9] bound whole regions, whereas AESA [66] bounds single points by the triangle inequality with precomputed pivots. However, the pruning power of such bounds decays with the dimension [8, 68]. The GEMINI framework [19] therefore moves the bound into a contractive feature space with a proof of no false dismissal, which the VA-file [68] turns into a sequential scan of compact approximations. In contrast, random projections preserve distances only up to a distortion factor [36] and support only approximate hashing [14, 30], whereas exhaustive GPU search [24, 35] avoids bounds altogether. In our terms, GEMINI and the VA-file are certified exclusion tests in full precision whose survivors are still ranked against a running candidate set; in contrast, CertEx certifies a half-precision tensor-core decision inside the same product and replaces the ranking by one comparison per vector.

### Approximate indexes.

Approximate indexes trade exactness for fewer examined vectors. Specifically, product quantization [6, 25, 28, 37] compresses vectors and probes a few partitions, to which RaBitQ [22, 23] adds a probabilistic error bound. In addition, FLANN [46] automates the choice<tbc>

(a) CertEx answers "a photo of a koala" exactly
(b) CAGRA loses exact matches
retina: all 1,281,167 images at low resolution (fp16)
fovea: exact top-4 (cosine similarity)
"a tattoo of a Pomeranian"
274 survivors that the certificate cannot exclude
exact top-5
CAGRA top-5
"a tattoo of a cradle"
0.350
0.347
exact top-5
CAGRA top-5
0.345
0.344
exact match that CAGRA misses

Figure 1: Text-to-image retrieval over 1.28M ImageNet images: CertEx (a); exact and CAGRA top-5, ranked from left to right (b).

