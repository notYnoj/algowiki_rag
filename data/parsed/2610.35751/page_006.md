<tbc>ACAR to settings with more than two attribute vectors introduces substantially greater complexity and is far from a trivial task.

**Benefits of ACAR.** ACAR introduces an angle constraint to reduce unnecessary distance computations. Given a target node _v_ with candidate neighbor set C, when processing the _i_-th candidate neighbor _p<sub>i</sub>_, ACAR compares _p<sub>i</sub>_ against a subset \(NS'_i\subseteq NS_i\) of the currently retained nodes that satisfy the angle constraint, where _NS<sub>i</sub>_ denotes the retained node set at iteration _i_ and \(t\le|\mathcal{C}|\) is the total number of iterations. Therefore, the total number of distance computations is \(\sum_{i=1}^t|NS'_i|\), where \(|NS'_i|\le|NS_i|\). The reduction in distance computations achieved by ACAR over the baseline depends on the distribution of Pareto angles. When Pareto angles are highly concentrated, ACAR may degenerate to the baseline, whereas a more uniform Pareto-angle distribution allows ACAR to fully exploit its acceleration potential.

## 5 CONNECTIVITY-LOSS-DRIVEN INCREMENTAL PARETO FRONTIER REPAIR

As discussed in Section 2.3, applying single-vector repair methods for DVQ indices that incorporate Pareto frontiers is unable to simultaneously ensure update efficiency and retrieval effectiveness. To address this issue, we introduce a _connectivity-loss-driven adaptive repair algorithm_ to maintain graph connectivity under deletions while avoiding unnecessary repair operations.

### 5.1 Observation & Intuition

For each affected node, reinsertion-based repair (RBR) methods perform Greedy Pareto Frontier Search from entry nodes to reconstruct its candidate neighbors. However, reinsertion incurs substantial redundant computations, resulting in inefficient updates.

**Observation.** To investigate the feasibility of incremental repair in Pareto-frontier-based indices under deletions, we measure the out-neighbor overlap ratio of affected nodes on three real-world datasets, as shown in Figure 7a. Specifically, we compute the overall overlap ratio of the out-neighbors for each affected node _v_, i.e., \(\frac{|N'_{out}(v)\cap N_{out}(v)|}{|N_{out}(v)|}\) , where _N<sub>out</sub>(v_) and \(N'_{out}(v)\) denote the out- neighbor sets before and after reinsertion, respectively. Furthermore, we analyze the overlap ratio across different layers of Pareto frontiers. Here, affected layers refer to layers that contain deleted nodes (i.e., layer 2). Low layers are defined as all layers below the lowest affected layer (i.e., layer 1), while high layers refer to the affected layers and all layers above them (i.e., layer 2 and layer 3), as illustrated in Figure 7b. We observe that 1) _the overall overlap ratio is at least 72%, indicating that most original neighbors remain effective after repair_, and 2) _87% of neighbors in low layers are preserved, whereas only 52% in high layers are retained._

**Intuition.** These observations provide strong support for incremental repair, which avoids the costly global search over all neighbors required by the reinsertion-based method. Observation 1) suggests<tbc>

<tbc>that most original neighbors of an affected node still belong to its approximate Pareto frontiers, enabling incremental repair during deletions. Furthermore, Observation 2) suggests that neighbor updates should be performed selectively across layers. Specifically, neighbors in low layers remain unchanged, while those in high layers need to be updated.

### 5.2 Pareto Frontier Repair Based on Connectivity Loss

We further analyze the distribution of deleted neighbors among affected nodes under a 1% deletion batch on the OpenImage index, with a maximum neighbor size of _R_=40. The results show that the number of deleted neighbors varies significantly across affected nodes (i.e., in-neighbors of deleted nodes), ranging from 1 to 20, indicating that the degree of connectivity loss induced by deletions differs substantially among affected nodes. We next provide a formal definition of connectivity loss.

Definition 2 (Connectivity Loss (CL)). _The connectivity loss of a node v measures the number of its lost out-neighbors, and its degree is defined as_

\(\mathrm{CL}(v)\unknown\frac{R-|N_{out}(v)|}{R},\) (3)

_where R denotes the maximum number of neighbors and N<sub>out</sub>(v_) _denotes the current out-neighbor set of v. It holds that_ \(\mathrm{CL}(v)\in[0,1]\).

Ideally, each node in the index maintains _R_ out-neighbors, resulting in no connectivity loss (CL=0). In practice, due to imperfect construction or deletions, nodes may suffer from connectivity loss. To this end, we categorize the degree of connectivity loss into three levels, mild, moderate, and severe. Specifically, for a node _v_, mild connectivity loss corresponds to \(\mathrm{CL}(v)\in[0,CL_1]\), moderate connectivity loss corresponds to \(\mathrm{CL}(v)\in(CL_1,CL_2]\), and severe connectivity loss corresponds to \(\mathrm{CL}(v)\in(CL_2,1]\), where _CL_<sub>1</sub> and _CL_<sub>2</sub> are the connectivity loss thresholds.

**Connectivity-Loss-Driven Adaptive Repair**. Based on the above analysis, we design a <u>conconnectivity-loss-driven</u>adaptive <u>Pareto frontier</u>repair algorithm, CA-PFR, to restore the connectivity of the graph index. The core idea of CA-PFR is to determine the repair intensity for affected nodes according to the degree of connectivity loss. The detailed procedure of CA-PFR is shown in Algorithm 3.

Specifically, when a set of nodes D is deleted, CA-PFR repairs the affected nodes _V<sub>affected</sub>_, i.e., the in-neighbors of the deleted nodes, according to their degree of connectivity loss. For each affected node \(v\in V_{affected}\), CA-PFR first organizes its out-neighbors into multi- layer Pareto frontiers \(\mathcal{C}=\{PF_v^1,\dots,PF_v^l\}\) (line 2), and then obtains its active out-neighbors \(Out\leftarrow N_{out}(v)\backslash\mathcal{D}\) (line 4) and active in- neighbors \(In\leftarrow N_{in}(v)\backslash\mathcal{D}\) (line 5). Next, the degree of connectivity loss for node _v_, CL(_v_), is computed (line 6) according to Definition 2. Based on CL(_v_), CA-PFR adopts historical-Pareto-frontier repair,<tbc>

