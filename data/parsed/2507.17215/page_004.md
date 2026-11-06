<tbc>of \(O(m\alpha log\sigma_\mathrm{max})\), where _m_ is the number of temporal edges, \(\alpha\) is the maximum core number (degeneracy), and \(\sigma_\mathrm{max}\) is the maximum multiplicity (number of parallel edges). This is the same running time of the best temporal triangle counters \[39\]. Up to log factors, this matches the forty year old Chiba-Nishizeki \(O(m\alpha)\) bound for triangle counting \[8\].

We achieve this bound by a combination of orientation techniques of triangle counting, combined with specially constructed temporal data structures. One of our novelties is the use of segment trees, an efficient data structure to process intervals. FOLTY combines segment trees and degeneracy orientations to achieve its running time. This gives the log \(\sigma_\mathrm{max}\) dependence, as opposed to a linear dependence by enumeration methods. We note that FOLTY gets the solutions to a query _without_ enumerating all temporal triangles.

**Unified frameworks to deal with FOL Queries.** As mentioned earlier, there are four kinds of FOL queries. We show how to efficiently reduce \(\exists\forall\forall\) and \(\exists\forall\exists\) to \(\exists\exists\forall\) queries. This gives a unified algorithm for solving FOL queries. We also show how to deal with thresholded universal queries efficiently, without enumerating entire lists of temporal edges.

**Excellent empirical performance:** We empirically evaluate the performance of FOLTY on a wide range of temporal graph datasets and various FOL queries. We conduct multiple experiments with varying values of thresholded quantifiers and time intervals. We observe that FOLTY works well, taking less than 20 mins. on networks with nearly 65M edges. Our algorithm for \(\exists\exists\forall_\tau\) and \(\exists\forall_{\tau_1}\forall_{\tau_2}\) consistently beats the SOTA triangle enumeration algorithm. We note that there is no previous code to solve this problem. As we discuss later, all existing algorithms either compute a total temporal triangle count, or enumerate all temporal triangles. The number of temporal triangles can be in billions with for graphs with millions of edges. Hence, we require the techniques developed to get FOL query solutions without a full enumeration.

**Detecting motif trends:** We apply FOLTY to a number of real- world datasets, and get various trends over thresholded quantifiers. An example is shown in 3. For example, we get a flattening of counts as the threshold \(\tau\) crosses 0.7, meaning that edges that form triangles with a 0.7 fraction of their neighbors form triangles with almost their entire neighborhood. As shown in the appendix, we<tbc>

<tbc>can also apply FOL queries to detect edges in citation networks that are likely to be in the same topic.

### 1.4 Related Work

The subject of general motif counting is vast, so we do not attempt to cover all related work. We refer the reader to a tutorial of Seshadhri and Tirthapura on subgraph counting \[49\]. We only focus on results on temporal motif counting.

The problem of Temporal motif counting was first introduced in \[38\], and since then, significant progress has been made in developing efficient algorithms for this question. \[31\] presented a general-purpose algorithm that precisely counts the occurrences of any temporal motif in a graph _G_. \[61\] later enhanced this algorithm to achieve better performance on GPUs. Other algorithms that provide exact motif counts include \[50\] and \[34\]. Additionally, there has been considerable focus on developing specialized algorithms for mining particular motifs, such as the temporal triangle \[25, 39, 55\], Butterfly-counting \[6\] etc.

There has also been considerable interest in developing efficient sampling methods, that generate accurate estimates of motif counts. \[30, 44\] divide the timespan of the input graph into multiple intervals, randomly sample one of them, and then generate exact counts within the sampled subgraph. \[59\] introduced a method that samples a uniform random edge and counts the motif instances incident on it. Other sampling methods include \[3, 43\]. More recently, \[37\] proposed an efficient approach for counting motifs on 3 and 4 vertices by introducing the concept of Path-Sampling. \[58\] utilize predictions from ML models to estimate temporal triangle count in streaming temporal networks.

We stress that none of these methods are geared towards solving general FOL queries. While these methods can enumerate all motifs, it would require extra logic to deduce the solutions. Moreover, the number of temporal motifs can easily be in billions for moderate graphs with only tens of millions of edges.

## 2 Main Ideas

**Preliminaries.** We begin with some preliminaries on the orientation methods for triangle counting. For temporal graph _G_, the underlying static graph _G<sub>S</sub>_ is constructed by removing all direction and parallel edges. Further, we assume that _G_ is presented to us as a list of temporal edges, sorted in the increasing order of timestamp. Given a vertex \(u\in V\) , \(N(u)=\{v\in V|\{u,v\}\in E(G_S)\}\). Given a pair of distinct vertices _x_ and _y_, we use _E<sub>x,y</sub>_ to denote the list of temporal edges from _x_ to _y_, sorted in the increasing order of their timestamp. We assume _O_(1) access to these lists. Given \(u,v\in V\) , we use \(\sigma(u,v)\) to denote the number of temporal edges with _u_ and _v_ as their endpoints.

Given an undirected graph _G<sub>S</sub>_, and an ordering \(\pi\) on its vertices, we can orient the edges of _G<sub>S</sub>_ to obtain a directed graph \(G_\pi^{\rightarrow\rightarrow}\) defined as follows: \(G_\pi^{\rightarrow\rightarrow}=(V,E_\pi^{\rightarrow\rightarrow})\), where \(E_\pi^{\rightarrow\rightarrow}=\{(u,v)|\{u,v\}\in E(G)\wedge\pi(u)<\pi(v)\}\). Given \(u\in V\) , define \(N_\pi^+(u)\) as the out-neighbourhood of _u_ in \(G_\pi^{\rightarrow\rightarrow}\) and \(N_\pi^-(u)\) as its in-neighbourhood. Next, we introduce the notion of degeneracy of _G<sub>S</sub>_.

Definition 2.1. _The_ degeneracy _of an undirected graph G is the smallest integer_ \(\alpha\)_, such that there exists an ordering of V with_<tbc>

DELTA: 1D
DELTA: 3D
DELTA: 5D
DELTA: 1W
1500
DELTA: 5D
1000
500
0
0.3
0.4
0.5
0.6
Thresholds
0.7
0.8
0.9
1.0

DELTA: 1D
DELTA: 3D
DELTA: 5D
DELTA: 1W
600
Num. EEA solutions
400
200
0
0.2
0.4
0.6
Thresholds
0.8
1.0

**(a)** \(\exists\exists\forall\), for Venmo Network

**(b)** \(\exists\forall\exists\), for Venmo Network.

**Figure 3: We apply FOLTY to the Venmo transaction Network in \[29\]. We compute solutions for the** \(\exists u\exists v\forall_\tau w\) **and** \(\exists u\forall_\tau v\exists w\)**, where the triangle is** (_u,v_)**,** (_u,w_)**,** (_v,w_) **(see Figure- 2a). The threshold** \(\tau\) **is varied on the** _x_**-axis. The time interval is denoted by DELTA, and is varied to get different trends.**

