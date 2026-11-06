**Theorem 7.** _When_ \(\tau\in\{SN,UN\}\)_, the MRCN problem remains NP-hard for demands of a single source (resp., destination) and uniform capacities._

_Proof:_ We first give a proof for \(\tau=\) SN by a many-one reduction from a decision problem \(\Pi\) of the makespan scheduling on identical machines, which is NP-hard \[35\].

For the makespan scheduling on identical machines \[22\], we are given a set M of machines and a set J of jobs, where each job _j_ has a processing time \(p_j\in\mathbb{Z}^+\) on any machine _i_, and our goal is to schedule the jobs on the machines to minimize the _makespan_, i.e., the maximum completion time.

Given an instance \(I=\left(\mathcal{J},\mathcal{M},\bigcup_{j\in\mathcal{J}}p_j,\beta\right)\) of \(\Pi\), which decides if _I_ has a makespan bounded by \(\beta\), we construct an instance \(I'=\left(V,E,\mathcal{E},c,D\right)\) (single destination _t_) of the MCRN problem \(\Pi'\). Moreover, let |J|=_n_ and |M|=_m_.

For each job \(j\in\mathcal{J}\), we construct a source node \(v_j\in V\) , which has a static link \(\left\{v_j,t\right\}\in E\) to the single destination \(t\in V\) and a demand \(D\left(v_j,t\right)=\beta+p_j\). For each machine \(i\in\mathcal{M}\), we construct a node \(u_i\in V\) that has _n_ neighbors \(U_i=\left\{u_i^1,\dots,u_i^n\right\}\subseteq V\) included in the static network, and a static link \(\left\{u_i,t\right\}\in E\). Moreover, we construct a node \(t'\in V\) , which has a static link \(\left\{t,t'\right\}\in E\) and a demand \(D\left(t',t\right)=2\beta\). Recall that, for our network model, there exists a reconfigurable link in E for any two nodes in _V_ but only a subset of E can be selected into the matching \(M\subset\mathcal{E}\). For the uniform capacities, we set \(c:\vec{E}\cup\vec{\mathcal{E}}\mapsto\{1\}\).

Next, we need to prove that the optimal congestion \(\lambda\) of \(I'\) satisfies \(\lambda\le\beta\) iff the minimum makespan of _I_ is not more than \(\beta\). The proof details are deferred to the technical report due to space constraint.

For \(\tau=\) UN, we can change the construction by replacing each static link \(\left\{v_j,t\right\}\in E\) with two static links \(\left\{v_j,v'_j\right\}\in E\) and \(\left\{v'_j,t\right\}\in E\) and defining new demands _D(v<sub>j</sub>,t_)=_p<sub>j</sub>_ and \(D\left(v'_j,t\right)=\beta\). Then, the above argument works for the new construction similarly.

### B. Polynomial-Time Solvable Cases

In contrast to Theorem 7, Theorem 8 reveals that the MCRN problem with \(\tau\in\{\text{SN},\text{UN}\}\) can become tractable if demands are further restricted to be single-commodity (the proof is deferred due to space constraint).

**Theorem 8.** _For_ \(\tau\in\{\text{\textit{SN}},\text{\textit{UN}}\}\)_, given a single-commodity demand and uniform capacities, the MCRN problem is polynomial- time solvable._

## V. EVALUATIONS

We complement our theoretical analysis with an empirical evaluation of the performance of our algorithms under realistic workloads. We first describe our methodology in §V-A and then discuss our results in §V-B. We will share our implementation with the research community together with this paper.

### A. Methodology

We employ the following baselines and implemented the corresponding algorithms to compare with our algorithm (labelled as _MC_) under _segregated_ and _un/-splittable_ models.<tbc>

<tbc>**Baselines.** We first consider a _Maximum Weight Matching_ algorithm as a baseline, which aims to maximize the sum of flow quantities on reconfigurable links, also employed by e.g., \[2\], \[3\]. Second, we also compare to a _Greedy_ approach (labelled as _Greedy_), where we greedily seek a compatible reconfigurable link to reroute the maximum demands in each iteration until the matching cannot be extended further. Similar greedy algorithms are also used by e.g., Halperin et al. \[28\] and Zheng et al. \[21\]. Lastly, we additionally plot the congestion on the static network without any reconfigurable link (label: _Oblivious_) and the optimum of the LP before rounding (label: _LP_) as upper and lower bounds respectively.

**Traffic Workloads.** Since traffic traces in different networks and running different applications can differ significantly \[5\], \[36\]-\[39\], we collected a number of real-world and synthetic traces to generate traffic matrices to evaluate our algorithms. More specifically:

\(\bullet\) **HPC traces:** We first employ four traces of exascale applications in High Performance Computing (HPC) clusters \[39\], \[40\]: MOCFE, NeckBone, CNS, and MultiGrid.<tbc>

\(\bullet\) **Synthetic traces:** We further consider the synthetic pFabric traces, which are frequently used as benchmarks in scientific evaluations \[41\]. In a nutshell, we generate demand matrices from workloads that arrive according to a Poisson process between random sources and destinations.

**Experimental Setup.** We implement the topologies of static networks by generating random _k_-regular graphs for _k_=4,8 (_k_ denotes the number of ports connecting other ToR switches) as Jellyfish \[42\], and using uniform capacities on both static and reconfigurable links. For unsplittable<sup>3</sup> (resp., splittable) flows, we consider one shortest path (resp., three shortest paths) for each demand for HPC traces (Fig. 3) (resp., pFabric traces (Fig. 4)). We repeat each setting by running it 5 times to obtain averaged results, normalizing the loads on links.

### B. Results and Discussion

We summarize our evaluation results in terms of the minimized congestion for these four HPC traces in Fig. 3 and for pFabric traces in Fig. 4.

Clearly, all considered algorithms significantly improve the congestion over the Oblivious baseline, and our algorithms (MC) typically outperform the others. We observe that our MC algorithm can provide the stable benefits throughout all investigated scenarios, e.g., the changing number of nodes, diverse traces and varying average degrees of static networks, while Greedy is worst in achieving a consistent performance.

More specifically, for pFabric traces, our MC algorithm (splittable) can achieve ≈65%-75% of the original congestion of Oblivious baseline for 40-180 nodes, where its performance is best on 150 nodes and notably decreases when nodes are increased from 140 to 180. The MC algorithm can at least provide a 1.3-approximation w.r.t. the optimal value of our LP.

<sup>3</sup> Due to the large size of networks and demands, in practice, it is usual to restrict the maximum number of paths when computing and implementing splittable flow, as done in, e.g., Jellyfish \[42\].

