<tbc>the scan becomes _compute-bound_, and once computation is the bottleneck, a higher-precision code no longer costs throughput, so the scan has no reason to stay lossy. CABANA leaves this headroom unused. It scans the lossy BF16 code that AMX natively supports, which caps the recall it can reach. KatoANN goes further by computing near-exact distances from SQ16 codes, even though AMX does not natively support 16-bit quantized distance computation.

KatoANN realizes this idea with a high-precision SQ16 representation and an adaptive rank-then-refine scan. Each database vector is kept in one resident form, a 16-bit scalar- quantized (SQ16) code, and each SQ16 coordinate separates into a high byte and a low byte. Because AMX supports INT8 matrix multiplication, KatoANN reconstructs the full SQ16 distance with four INT8 matrix multiplications. This distance is near-exact, but applying all four multiplications to every candidate would waste computation.

KatoANN therefore first ranks all candidates using only the high-byte plane, which requires one matrix multiplication, and then computes the full SQ16 distance only for promising survivors. Because ranking and refinement read the same resident code, no second raw-vector copy is needed. The survivor count is calibrated for each recall target, so lower-recall queries can stop after ranking while higher-recall queries refine only as many candidates as needed. After this design accelerates the fine scan over probed partitions, KatoANN applies the same batched near- exact distance computation to the coarse centroid search as well.

For high-dimensional embeddings, KatoANN further reduces the cost of the ranking stage. A distance-preserving rotation concentrates most of the data variance in the leading dimensions. The ranking stage can then read and process only a short prefix of each vector, while the refinement stage still evaluates promising candidates using all dimensions and the full SQ16 precision. A one-time calibration selects the prefix length and survivor count for each index and recall target, ensuring that each query performs only the work needed to meet its target.

We evaluate KatoANN on diverse high-dimensional workloads. The results show that KatoANN is the fastest partition- based CPU ANN search system in our evaluation across the high-recall range and can match or outperform graph- based systems. For example, on 3,072-dimensional embeddings, KatoANN achieves 15,635 QPS at recall@10 \(\ge\) 0.99, outperforming CABANA and ScaNN by 3.14\(\times\) and 8.45\(\times\), respectively. KatoANN also scales well with additional CPU threads and maintains a small memory footprint by storing only one vector code per database vector.

In summary, we make the following contributions:

\(\bullet\) We show that once batched execution drives the distance scan into the compute-bound regime, lossy codes are no longer needed for high throughput, and we formalize when this crossover occurs.<tbc>

\(\bullet\) We design an adaptive rank-then-refine scan that derives both its cheap ranking key and near-exact refinement distance from a single 16-bit SQ16 code, avoiding a second copy of the vectors.<tbc>

\(\bullet\) We implement KatoANN on a commodity Intel AMX server and show that it is the fastest partition-family CPU search system across the high-recall range on datasets from 96 to 3,072 dimensions.

## 2 BACKGROUND AND MOTIVATION

### 2.1 The Trade-off in the IVF Distance Scan

**Graph search walks, while IVF search scans.** Two index families dominate ANN serving. A graph index walks a proximity graph and compares the query against a small set of visited candidates [17, 31, 38]. An inverted-file (IVF) index instead partitions the database into clusters and scans the inverted lists nearest to the query [8, 11, 18]. The walk visits few candidates, but each step follows a data-dependent pointer and touches scattered memory. The scan evaluates more candidates, but it streams them from contiguous lists, so the work is regular and easy to batch. This regularity also suits continuously updated datasets, since a new vector is appended to one inverted list. For these reasons, this paper targets IVF search.

Once an IVF search selects the clusters to probe, its cost is dominated by the distance scan over their vectors. For high-dimensional embeddings, each comparison touches hundreds to thousands of coordinates. Query cost therefore depends not only on how many candidates are scanned, but also on how efficiently each candidate is evaluated.

**A scan is memory-bandwidth-bound.** The distance scan is a streaming computation. Its inner loop reads a vector code from memory and multiplies it against a query, doing only _O_(1) multiply-add operations per byte it reads. Its speed _T_ follows the roofline model,

\(T\approx min(\pi,I\beta),I=\frac{\# mul-add ops}{\# bytes read},\) (1)

where \(\pi\) is the peak arithmetic rate, \(\beta\) is the memory bandwidth, and _I_ is the arithmetic intensity of the scan.

In a conventional single-query scan, each code is loaded once and used for one distance computation, so _I_ remains low. The scan therefore runs at \(I\beta\), well below the compute peak \(\pi\), and its throughput is largely determined by the number of bytes read per candidate.

**Compact codes sacrifice recall.** The natural way to accelerate a bandwidth-bound scan is to read fewer bytes. IVF<tbc>

