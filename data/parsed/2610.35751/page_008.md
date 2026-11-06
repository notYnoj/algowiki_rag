<tbc>the newly introduced candidate neighbors of _v_. Next, we analyze the size of \(|\Delta C|\) under the following three repair strategies of CA-PFR.

<u>_Historical-Pareto-Frontier Repair (Mild)_</u>. For each affected node \(v\in V_{affected}\), this strategy augments the original active out-neighbors in C with the active in-neighbors of _v_, resulting in \(|\Delta C|\approx|N_{in}(v)|\). Since the distances \(\delta_x(v,v')\) and \(\delta_y(v,v')\) are already stored in the corresponding in-neighbors \(v'\in N_{in}(v)\), the candidate set augmentation incurs no additional distance computations, i.e., _T<sub>mild</sub>_=0.

<u>_Affected-Layer Repair (Moderate)_</u>. In addition to the active in- neighbors _N<sub>in</sub>(v_), this repair strategy further adds the active out-neighbors of nodes in the affected layers to \(\mathcal{C}'\), yielding \(|\Delta C|\approx|N_{in}(v)|+n\cdot R\), where _n_ is the average number of nodes per layer, _R_ denotes the maximum out-degree, and \(n\le R\). Thus, the complexity for repairing each affected node _v_ is: \(T_{moderate}\approx O\left(n\cdot R\right)\).

<u>_Multi-Layer Repair (Severe)_</u>. This repair strategy not only includes the in-neighbors and the original active out-neighbors, but also incorporates all active out-neighbors of nodes in the high layers into \(\mathcal{C}'\), resulting in \(|\Delta C|\approx|N_{in}(v)|+h\cdot n\cdot R\), where _h_ is the number of the high layers, and \(h\cdot n\le R\). Therefore, the computational complexity of repairing each affected node _v_ is: \(T_{severe}\approx O\left(h\cdot n\cdot R\right)\).

Let _P_<sub>1</sub>, _P_<sub>2</sub>, and _P_<sub>3</sub> denote the probabilities of triggering the three repair strategies, respectively, satisfying _P_<sub>1</sub>+_P_<sub>2</sub>+_P_<sub>3</sub>=1. As a result, the computational complexity of CA-PFR is: \(T_{CA-PFR}=P_1\cdot T_{mild}+P_2\cdot T_{moderate}+P_3\cdot T_{severe}\). In practice, since severe repair is triggered infrequently, with probabilities satisfying \(P_1>P_2\gg P_3\), the expected complexity can be simplified as: \(\mathbb{E}[T_{CA-PFR}]=P'_2\cdot T_{moderate}\), where \(P'_2=\frac{P_2}{P_1+P_2}\).

## 6 EVALUATION

### 6.1 Experimental Setup

**Evaluation Platform**. All experiments are conducted on a server with an Intel(R) CPU, 320 GB memory. The system runs Ubuntu 22.04 LTS with GCC version 11.4.0.

**Datasets**. We evaluate our system on five publicly available real-world datasets, namely OpenImage (OI) \[61\], Howto100M (HM) \[61\], CC3M (CM) \[61\], LAION (LN) \[44\] and Caselaw (CW) \[3\], as summarized in  1. For CW, we construct its DVQ version using the original single text embeddings and associated court location metadata. Note that ACTIVE is not restricted to the attribute-type combinations in  1, but generalizes to arbitrary dual-vector data types.

**Compared Methods**. We comprehensively evaluate ACTIVE against baselines to validate its search and update performance.

<u>_Static Search_</u>. We select multi-index retrieval (MR) \[48, 63\] and DEG \[61\] as baselines for static search, where MR builds a separate single-vector index (i.e., an HNSW index) for each of the two attribute vectors. The difference between ACTIVE and DEG in construction lies in their active range computation methods.

<u>_Dynamic Updates_</u>. Since no dedicated methods exist for dynamic DVQ index updates, we use RBR \[60\] and NRBR \[47\] for deletions and DEG’s incremental construction strategy for insertions. These baselines employ existing AR computation algorithms \[61\].

**Parameter Settings**. During index construction, we set _ef_construct=200 and _R_ (or _M_) = 40 for ACTIVE , DEG and MR. On LN, _ef_construct is increased to 400, because setting them to 200 yields an average out-degree of only about _R/_2 due to the data distribution. The other parameters for DEG and MR follow those recommended in their respective papers. The Pareto angle threshold of ACTIVE is set to \(\theta_{th}=\pi/18\). During updates, we set _ef_update=100 for insertions in ACTIVE and DEG, and for reinsertions in RBR, and use _ef_search=100 for search. NRBR uses the same _R_=40. The connectivity- loss thresholds of ACTIVE are CL<sub>1</sub>=1/3 and CL<sub>2</sub>=1/2. Unless otherwise specified, all updates use 32 threads, and each query \(\alpha\) is randomly sampled from \[0,1\].

**Workloads**. By default, we construct a DVQ index on 100% of each dataset for search and deletion experiments, and another index on 50% of each dataset for insertion experiments. For deletions, we use the 100% index and remove 1% of the vectors in each of 10 batches, resulting in a total of 10% deletions. For insertions, we use the 50% index and insert 1% of the vectors in each of 10 batches, resulting in a total of 10% insertions.

**Metrics**. We measure search accuracy using Recall@_k_ (_k_=10 by default) and search efficiency using average query latency, while update (i.e., deletions and insertions) performance is evaluated using throughput (deletions/insertions per second).

### 6.2 Static Search

**Query Latency under Varying** _k_**.** We measure the query latency for \(k\in\{10,100,500,1000\}\) with Recall@_k_ fixed at 0.95, as shown in Figure 9. On LN, MR is omitted because Recall = 0.95 cannot be achieved within the reasonable latency budget. Across all _k_ values, ACTIVE achieves substantially lower latency than MR in most cases, as MR misses many objects with small weighted distances during candidate generation. MR can achieve recall comparable to that of ACTIVE only by substantially increasing its candidate budget (i.e., _ef_search), as shown in Figure 10. Meanwhile, ACTIVE maintains latency comparable to DEG while reducing AR computation time, as shown in  2. As _k_ increases, the latency advantage of ACTIVE over MR generally becomes more pronounced, while its relative latency performance against DEG also improves. For example, at _k_=10, the query latency ratios of MR and DEG to ACTIVE range from 0.21 to 2.35 and from 0.63 to 1.24, respectively. At _k_=1000, these ratios range from 2.13 to 4.63 and from 0.67 to 1.29,<tbc>

\begin{tabular}{ccccc}
Dataset & _D<sub>x</sub>_ & _D<sub>y</sub>_ & #Vectors & Contents \\
OpenImage (OI) & 768 & 768 & 507,444 & Text-Image \\
Howto100M (HM) & 1024 & 768 & 1,238,875 & Text-Video \\
CC3M (CM) & 768 & 768 & 3,131,153 & Text-Image \\
LAION (LN) & 512 & 512 & 10,642,155 & Text-Image \\
Caselaw (CW) & 1,536 & 2 & 7,288,481 & Text-Coord. \\
\end{tabular}

\begin{tabular}{cccccc}
Method & OI & HM & CM & LN & CW \\
DEG & 1032.47 & 2476.73 & 3903.47 & 9221.83 & 20346.90 \\
ACTIVE & 732.33 & 1351.25 & 2539.33 & 6902.11 & 16220.81 \\
\end{tabular}

** 1: Dataset statistics.** _D<sub>x</sub>_ **and** _D<sub>y</sub>_ **denote the vector dimensions of the** _x_**- and** _y_**-attributes, respectively. Each dataset contains 1,000 query vectors, except Caselaw (88.3K).**

** 2: Comparison of active range computation time (in seconds) across different datasets.**

