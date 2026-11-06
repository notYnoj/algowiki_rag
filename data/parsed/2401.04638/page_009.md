Regarding the HPC traces, the MC algorithm (unsplittable) still dominates Greedy and Max. Weight Matching, which keeps a comparatively lower congestion, reducing the congestion of Oblivious by ≈30%-35%, but the variance is slightly higher than in the pFabric traces, matching empirical observations on the complexity of the traces produced by these synthetic traces [39]. Meanwhile, we can observe very similar plots for all algorithms in static networks of _k_=4 and _k_=8.

## VI. FURTHER RELATED WORK

Reconfigurable networks have recently received much attention both in the theory and the applied community. Reconfigurable networks generally come in two flavors: demand- oblivious networks such as RotorNet [43], Opera [44], Sirius [45], and Mars [10] provide an unprecedented throughput by avoiding (or at least minimizing) multi-hop forwarding compared to their static counterparts [46], [47]. Demand-aware networks such as ProjecToR [5], SplayNets [48], Jupiter [49],<tbc>

<tbc>Cerberus [8], Eclipse [24], Duo [9], among many other [2]-[4], [16], [17], [43], [50]-[52], are tailored towards skewed and structured workloads and leverage spatial and temporal locality to improve throughput further [38], [39], [53].

However, many of these works revolve around other objectives or network settings, e.g., [5]-[7], [12], [15], [17], [52], [54]-[59], and the important aspect of congestion is still not well understood. We refer the reader to the survey by [4] for a more general overview.

The works by Avin et al. [18] and Pacut et al. [19] study bounded-degree topology designs to minimize route length and congestion, and provide approximation lower bounds and a 6-approximation algorithm for min-congestion for sparse demands. However, their models consider optimizing the topology solely consisting of reconfigurable links without a static network, which fundamentally differs from our model of hybrid networks.

Zheng et al. [21] consider a problem setting similar to our segregated model and study how to enhance classic datacenter network topologies, such as Diamond, Bcube and VL2, with small reconfigurable switches. They present NP-hardness results on general graphs, although these results do not transfer to specific data center topologies or trees, respectively, while they also introduce a greedy-based heuristic algorithm without performance guarantees. Yang et al. [30] study how to enhance the datacenter network by 60GHz wireless reconfigurable links for min-congestion under unsplittable and non-segregated routing. However, their congestion definition is structurally different from our model, as they consider undirected links, and furthermore, their reconfigurable links are formed under wireless interference constraints.

Related in name and spirit, is the so-called HYBRID model, introduced by Augustine et al. [60]. So far, the investigations in the HYBRID model focused on, e.g., path length, diameter, and (competitive) routing [60]-[64], and it would be interesting to develop a unifying framework of hybrid demand-aware networks and the HYBRID model.

Dai et al. [20] studied the same network model as we do in this paper, showing that the reconfigurable network- design for the objective of min-congestion is already NP-hard for splittable (resp., unsplittable) and segregated (resp., non- segregated) routing models when the static network is a tree of height at least two, but tractable for static networks of star topologies. However, they only provide algorithms with guarantees for very specific problem instances (i.e., star graphs) and also no approximation hardness lower bounds.

## VII. FUTURE WORK

Our work leaves open several interesting questions for future research. In particular, it remains to provide a complete picture of tight upper and lower bounds on approximating the non- segregated routing problems.

Oblivious Max Weight Matching Greedy MC 1
1 0.9 0.9 0.8 0.8 Congestion 0.7 Congestion 0.7 0.6 0.6 0.6 CNS CNS MOCFE MOCFE MultiGrid MultiGrid MOCFE MultiGrid Traces Traces (b) k = 4 (c) k = 8

Oblivious Max Weight Matching Greedy MC LP 0.95 0.85 0.75 Congestion 0.65 0.55 40 60 80 100 120 140 160 180 # of Nodes

Fig. 3. Algorithmic comparison of the min-congestion for four traces of exascale applications in HPC clusters, using random _k_-regular graphs for the static network.

Fig. 4. Algorithmic comparison of the min-congestion for different synthetic traces of pFabric clusters, with random 4-regular graphs as static networks.

