<tbc>the two indices independently, merges the retrieved candidates, and subsequently reranks them by computing the exact weighted distance. Since they assume that object distances are pre-determined, they suffer from limited retrieval quality under arbitrary query preferences, as shown in Figure 1a.

<u>_2) Preference-agnostic unified indices_</u>. Unlike existing single-vector indices \[16, 22, 30\] that select similar vectors of each node as their neighbors, this approach \[61\] connects approximate nearest neighbors across all possible query preferences, ensuring that varying query preferences can be accommodated during search. To achieve this, approximate Pareto frontiers are utilized as the neighbors since they remain competitive under diverse preference settings, thereby enabling the selected neighbors to cover varying query preferences. As a result, Pareto-frontier-based indices provide a more suitable foundation for query-dependent similarity search in DVQ. However, existing unified indices do not support efficient dynamic updates because repairing Pareto frontiers is more complex than repairing neighbors in single-vector indices \[28, 47, 62\].

**Our goal**. In this work, we aim to design a dynamic Pareto-frontier- based DVQ index that supports efficient construction and updates while maintaining high retrieval performance.

**Challenges**. Designing a preference-agnostic unified index is challenging for two main reasons.

<u>_1) Expensive Edge Active-Range Computation in Construction_</u>. Pareto-frontier-based indices \[61\] select neighbors to cover different query preferences, but not every selected edge is useful under every preference. Thus, each edge needs to precompute its active ranges of the preference, allowing it to be traversed only when needed and avoiding redundant distance computations. Employing Relative Neighborhood Graph (RNG) pruning \[61\] enables the computation of such active ranges, however, its expensive time complexity introduces substantial additional computational overhead. Therefore, designing an efficient active-range computation method remains challenging.

<u>_2) Inefficient Approximate Pareto Frontier Repair in Update_</u>. In Pareto-frontier-based indices, repairing the Pareto-frontier neighbors of affected nodes (i.e., in-neighbors of deleted nodes) after deletions is critical to preserving graph connectivity. Reinsertion- based global repair strategies \[2, 30, 60\] rediscover the neighbors of affected nodes by traversing from entry nodes, causing many distance computations and high update overhead. However, directly applying single-vector local repair strategies \[47, 62\] to Pareto- frontier-based DVQ indices is ineffective, as validated in Figure 1b and 1c, since they cannot guarantee that Pareto frontiers can be identified within the local neighborhood of DVQ indices. Therefore, designing an efficient repair strategy for approximate Pareto frontiers while maintaining high retrieval accuracy remains challenging.

**ACTIVE**. The above challenges cannot be directly addressed by existing techniques. Starting from these application-level challenges, we propose ACTIVE , a `dynAmiC` Pareto-fronTier-based unIfied `DVQ` indEx that supports dynamic updates while maintaining high retrieval quality under arbitrary query preferences. ACTIVE is built upon two techniques.

To accelerate index construction, we introduce the Pareto angle and develop an `angle-constrained active range` computation algorithm, ACAR, based on the locality distribution of Pareto angles. In ACAR, each neighbor is compared only with other neighbors that satisfy the angle constraint under the triangle inequality. By restricting unnecessary comparisons, ACAR reduces construction overhead while preserving effective navigation quality of the DVQ index across diverse query preferences.

For efficient updates, we observe a high overlap between the original neighbors and the repaired neighbors of affected nodes and introduce CA-PFR, a connectivity-loss-driven adaptive repair strategy that locally repairs approximate Pareto frontiers. We provide three methods, namely historical-Pareto-frontier, affected- layer, and multi-layer repair, according to the severity of connectivity degradation of affected nodes. This allows us to restore the connectivity of the graph without full re-insertion, significantly reducing distance computations and improving update throughput.

In summary, the main contributions of this work are:<tbc>

\(\bullet\) An observation of Pareto-angle locality motivates an angle- constrained active range computation algorithm, which accelerates active range computation (§ 4).<tbc>

\(\bullet\) An observation of high overlap between original and repaired neighbors of affected nodes motivates an incremental repair method. We propose a connectivity-loss-driven adaptive repair strategy, which locally repairs approximate Pareto frontiers according to the severity of connectivity degradation (§ 5).<tbc>

\(\bullet\) Extensive experiments on diverse datasets show that ACTIVE achieves higher update throughput than state-of-the-art baselines while maintaining a competitive trade-off between query accuracy and efficiency (§ 6).

## 2 BACKGROUND AND MOTIVATION

In this section, we first define the Dual-Vector Query (DVQ) problem and review Pareto-frontier-based DVQ index construction as well as update methods for single-vector graph-based indices. We then analyze their drawbacks and present the motivation of this work.

### 2.1 Dual-Vector Query

Let _O_={_o_<sub>0</sub>_,o_<sub>1</sub>_,...,o_<sub>_N_-1</sub>} denote a dataset of _N_ objects, where each object \(o_i\in O\) is represented by two feature vectors: (1) \(o_i.x\in\mathbb{R}^{d_x}\), a _d<sub>x</sub>_-dimensional vector capturing one attribute, and (2) \(o_i.y\in\mathbb{R}^{d_y}\), a _d<sub>y</sub>_-dimensional vector capturing another attribute.

**Dual-Vector Query (DVQ)**. Given a query \(q=\langle x,y,\alpha,k\rangle\), where \(q.x\in\mathbb{R}^{d_x}\) and \(q.y\in\mathbb{R}^{d_y}\) are the query vectors, \(q.\alpha\in[0,1]\) is a weighting parameter provided by upstream applications to quantify user preferences, and _q.k_ is the number of objects to retrieve. Ideally, DVQ aims to retrieve the exact top-_k_ nearest objects \(R_{exact}\subset O\) for a query _q_, such that \(\forall e\in R_{exact},\forall o\in O\backslash R_{exact}\), we have \(\text{Dist}(q,e)\le\text{Dist}(q,o)\), where the distance \[61\] between _q_ and an object _o_ is defined as:

\(\text{Dist}(q,o)=q.\alpha\cdot\delta_x(q,o)+(1-q.\alpha)\cdot\delta_y(q,o),\) (1)

where \(\delta_x(q,o)=\frac{\|q.x-o.x\|_2}{x_\text{max}}\) and \(\delta_y(q,o)=\frac{\|q.y-o.y\|_2}{y_\text{max}}\) are the normalized distances for each vector. A larger \(\alpha\) means the user prefers the _x_-attribute, while a smaller \(\alpha\) means the user prefers the _y_-attribute. In real applications, \(\alpha\) can be learned and tuned based on the user’s query history and the entities ultimately selected.

