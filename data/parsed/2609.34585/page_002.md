<tbc>et al., 2026b) also iterate, but along a fixed noise schedule. The variants that scale test-time compute do so in heatmap space (Li et al., 2023; 2024), where a search is still required to obtain a solution. Other heatmap solvers spend the extra compute around the network rather than in it, by fine-tuning a meta-learned policy on each instance and sampling massively in parallel (Qiu et al., 2022), or by learning an optimizer whose iterations update the heatmap (Dernedde et al., 2025). Earlier approaches train a graph neural network (GNN) as a supervised edge classifier (Joshi et al., 2019; Fu et al., 2021) and are no longer competitive on their own.

We benchmark on the Maximum Independent Set (MIS) problem and the Traveling Salesman Problem (TSP), two prototypical combinatorial optimization problems in the literature. To make recursive models work on both, we augment them with (i) an embedding of the problem structure (adjacency matrices modulating attention via a learnable per-head bias for MIS, embedded coordinates for TSP), (ii) lightweight problem-specific decoders (peeling for MIS, edge insertion with 2-opt for TSP), and (iii) halting and selection driven by the decoded solutions. The network size stays constant by design, so additional compute goes into iterations rather than parameters.

Empirically, TRM4CO reaches the lowest optimality gap of all learned solvers on TSP-500 and TSP-1000, _e.g._ 0.11% on TSP-500 in 2.1 seconds per instance, and matches the best diffusion solver on TSP-10000. On MIS, solution quality grows with test-time compute, and with 200 rollouts TRM4CO surpasses every general-purpose neural solver and the KaMIS reference on Erdős- Rényi (ER) graphs with 700-800 nodes. Finally, self-relabeling raises 16% of the training labels above those of KaMIS and yields our best MIS checkpoint. Without any solver labels, the same loop trains an MIS model from scratch whose own labels match or beat KaMIS on 42% of the training graphs and whose test gap comes close to that of our best checkpoint (Section 3.6).

In summary, our contributions are as follows:

• We propose a deep recursive architecture for combinatorial optimization that can efficiently scale along depth and width.<tbc>

• Our method can be trained in a supervised way from solver labels or in a self-supervised manner by self-relabeling, _i.e._ generating multiple labels and hill-climbing on the best ones.<tbc>

• We show experimentally on MIS and TSP that we match or outperform state-of-the-art neural combinatorial optimization approaches.

## 2 METHOD

At a high level, our method works as follows (Figure 1). The <u>encoder</u> turns a problem instance, which comes with a set of feasible solutions and an objective, into tokens. A problem-agnostic <u>recursive backbone</u> then updates a latent state and an answer state iteratively. We scale the compute of the backbone along depth, the number of steps, and along width, the number of rollouts. We also inject noise into the latents for diversity. Periodically, a <u>decoder</u> reads the answer state and turns it into a solution. At inference, we keep the best solution over all readings across depths and rollouts. Optionally, during training, we replace the label of an instance whenever we sample a better solution.

We explain all components in detail below.

### 2.1 BACKGROUND: TINY RECURSIVE MODEL (TRM)

We use the Tiny Recursive Model (Jolicoeur-Martineau, 2025) as the backbone. It is a simplification of the Hierarchical Reasoning Model (HRM, Wang et al., 2025). TRM keeps two states of the same shape as the input tokens _e_. The latent _z_ carries the reasoning and the answer _y_ carries the current prediction. As shown in Figure 4 (Appendix A), one weight-tied network \(f_\theta\) of two Transformer blocks updates both states in cycles:

\(z\leftarrow f_\theta(z+y+e)(L\text{times}),y\leftarrow f_\theta(z+y)(\text{once}),\) (1)

and one recursion step runs _H_ such cycles, of which only the last carries gradient. Deep supervision chains up to _D_ recursion steps, carrying the states (_y,z_) detached from one step to the next and applying the loss to the output head \(g_\theta(y)\) after each step. Training memory is thus constrained to one cycle, while the effective depth is 2_H(L_+1)_D_ blocks. A learned halting head on _y_ decides<tbc>

